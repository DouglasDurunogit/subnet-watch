"""score.py — gates, weights, and the deterministic ranking.

The ranking is computed HERE, in Python, and never by the model reading the
table. Weighted ranking of 128 rows across five criteria is arithmetic; an LLM
asked to do it produces a different order each run, and rank churn that is not a
real change destroys the whole point of a monitor.

WEIGHTS (from the user's stated priorities):
    income (net margin)      40   "income is important"
    new-challenge freshness  35   "must be big weight so I know instantly"
    resource cost / entry    15   "affects whether I enter or not"
    registration cost        10   soft; small next to monthly machine cost
    incentive structure       0   EXPLICIT: display only, "I should see the
                                  problem itself" -- so it is never scored

The zero is enforced structurally, not by politeness: no incentive-structure
subscore is ever published, so there is nothing for a later conversation to
re-weight. Asking to weight it requires changing this file.

GATES run first and remove a subnet from the ranking entirely, because a score
implies "you could earn this" and a gated subnet cannot pay.
"""

from __future__ import annotations

import math
from datetime import datetime, timedelta, timezone
from typing import Any, Dict, List, Optional

WEIGHTS = {"income": 40.0, "freshness": 35.0, "resource": 15.0, "registration": 10.0}

BURN_DEAD = 0.99
# The log scale saturates here. Set from the observed top competitive margin
# (~$24k/day on sn107), not a round guess: at the original $500 the top eight
# ranked subnets all pinned to full marks despite spanning $3.2k to $10k/day,
# which is a 3x income difference the score reported as a dead heat.
INCOME_CEILING_USD_DAY = 25_000.0
PAYBACK_HORIZON_DAYS = 30.0

FRESH_EVENT_CLASSES = {
    "NEW_SUBNET", "RELEASE", "SCORING_COMMIT",
    "README_TASK_DIFF", "WEIGHTS_VERSION_BUMP", "MECHANISM_ADDED",
}

_TIER_MAX = 4.0


def _f(row: Dict[str, Any], key: str) -> Optional[float]:
    v = row.get(key)
    if v is None or v == "":
        return None
    try:
        return float(v)
    except Exception:
        return None


def clamp01(x: float) -> float:
    return max(0.0, min(1.0, x))


def gate(row: Dict[str, Any]) -> tuple:
    """(gate_status, gate_reason). 'OK' means the subnet enters the ranking."""
    if row.get("row_status") == "failed":
        return "BLOCKED:no-data", "the sweep failed for this subnet; values are missing, not zero"

    burn = _f(row, "miner_burn")
    if burn is not None and burn >= BURN_DEAD:
        return "BLOCKED:burn", (
            f"miner_burn={burn:.3f} - {burn * 100:.1f}% of miner emission is withheld "
            "by owner-controlled hotkeys, so miners earn nothing here"
        )

    if str(row.get("registration_allowed")) == "False":
        return "BLOCKED:closed", "registration is closed; you cannot get a UID"

    if row.get("machine_class_cheapest") in (None, "") and row.get("required_vram_gb") not in (None, ""):
        return "BLOCKED:no-machine", (
            f"requires ~{row.get('required_vram_gb')} GB VRAM; no class in machines.csv satisfies it"
        )

    return "OK", ""


def _freshness(row: Dict[str, Any], events_by_netuid: Dict[int, List[Dict[str, Any]]],
               now: datetime) -> tuple:
    """(decay 0..1, reason). Newest qualifying event wins; a young subnet is
    itself fresh even with no event yet."""
    best_age_days: Optional[float] = None
    best_cls = ""
    for ev in events_by_netuid.get(int(row["netuid"]), []):
        if ev.get("class") not in FRESH_EVENT_CLASSES:
            continue
        try:
            seen = datetime.fromisoformat(ev["first_seen_utc"].replace("Z", "+00:00"))
        except Exception:
            continue
        age = (now - seen.astimezone(timezone.utc)).total_seconds() / 86400.0
        if best_age_days is None or age < best_age_days:
            best_age_days, best_cls = age, ev.get("class", "")

    age_days = _f(row, "subnet_age_days")
    if age_days is not None and age_days <= 30:
        if best_age_days is None or best_age_days > 0:
            return 1.0, f"subnet is {age_days:.0f} days old"

    if best_age_days is None:
        return 0.0, "no challenge change on record"
    if best_age_days <= 7:
        return 1.00, f"{best_cls} {best_age_days:.1f}d ago"
    if best_age_days <= 30:
        return 0.60, f"{best_cls} {best_age_days:.0f}d ago"
    if best_age_days <= 90:
        return 0.30, f"{best_cls} {best_age_days:.0f}d ago"
    return 0.0, f"{best_cls} {best_age_days:.0f}d ago (stale)"


def _confidence(row: Dict[str, Any]) -> tuple:
    """Multiplier + reason. Unknowns cost confidence rather than inventing data."""
    reasons = []
    if row.get("gpu_class_basis") in ("no evidence", None, ""):
        reasons.append("hardware requirement unknown")
    elif str(row.get("gpu_class_basis", "")).endswith("(GUESS)"):
        reasons.append("hardware from README keywords, not curated")
    if not row.get("readme_sha"):
        reasons.append("no README readable")
    if row.get("repo_status") not in ("ok", "redirected"):
        reasons.append(f"repo {row.get('repo_status')}")

    # A median over one or two samples is not an estimate. Scoring the median
    # instead of the ceiling fixed the winner-take-all bias, but on a subnet with
    # a single competitive miner the two are the same number by definition, so
    # the fix buys nothing there and the figure deserves the same scepticism as
    # missing data. 31 ranked subnets are in this position, 6 of them in the top
    # 8 - so this is the difference between a supported ranking and a confident
    # one built on n=1.
    ce = _f(row, "competitive_earners")
    if ce is not None and ce <= 2 and _f(row, "net_margin_usd_day") is not None:
        reasons.append(f"income rests on {int(ce)} competitive miner"
                       f"{'s' if ce != 1 else ''} (n<=2: not a distribution)")

    if not reasons:
        return 1.00, ""
    if len(reasons) == 1:
        return 0.85, "; ".join(reasons)
    return 0.60, "; ".join(reasons)


def score_row(row: Dict[str, Any], events_by_netuid: Dict[int, List[Dict[str, Any]]],
              now: Optional[datetime] = None) -> Dict[str, Any]:
    """Attach gate, component points, confidence and score to one row."""
    now = now or datetime.now(timezone.utc)
    status, reason = gate(row)
    out: Dict[str, Any] = {"gate_status": status, "gate_reason": reason}

    if status != "OK":
        out.update(income_pts=None, freshness_pts=None, resource_pts=None,
                   registration_pts=None, confidence=None, confidence_reason="",
                   freshness_reason="", score=None)
        return out

    # Income: log-scaled. Margins span $0.10 to $5000/day, so a linear scale
    # makes the ranking a pure sort by the single largest subnet.
    net = _f(row, "net_margin_usd_day")
    if net is None:
        income_pts = 0.0
        out["income_flag"] = "NO-INCOME-DATA"
    else:
        income_pts = WEIGHTS["income"] * clamp01(
            math.log10(1.0 + max(0.0, net)) / math.log10(1.0 + INCOME_CEILING_USD_DAY)
        )

    decay, fresh_reason = _freshness(row, events_by_netuid, now)
    freshness_pts = WEIGHTS["freshness"] * decay

    tier = _f(row, "machine_tier")
    if tier is None:
        resource_pts = WEIGHTS["resource"] / 2.0   # half, and confidence pays for it
    else:
        resource_pts = WEIGHTS["resource"] * (1.0 - min(tier, _TIER_MAX) / _TIER_MAX)

    payback = _f(row, "payback_days")
    registration_pts = (
        WEIGHTS["registration"] * clamp01(1.0 - payback / PAYBACK_HORIZON_DAYS)
        if payback is not None else 0.0
    )

    conf, conf_reason = _confidence(row)
    raw = income_pts + freshness_pts + resource_pts + registration_pts

    out.update(
        income_pts=round(income_pts, 2),
        freshness_pts=round(freshness_pts, 2),
        resource_pts=round(resource_pts, 2),
        registration_pts=round(registration_pts, 2),
        freshness_reason=fresh_reason,
        confidence=conf,
        confidence_reason=conf_reason,
        score=round(raw * conf, 1),
    )
    return out


def rank(rows: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Sort scored rows. Ties break deterministically so that any rank change
    between runs is a real change and never sort instability."""
    scored = [r for r in rows if r.get("score") is not None]
    scored.sort(
        key=lambda r: (
            -(r.get("score") or 0.0),
            -(_f(r, "net_margin_usd_day") or -1e9),
            (_f(r, "reg_cost_tao") if _f(r, "reg_cost_tao") is not None else 1e9),
            -(_f(r, "earners") or 0.0),
            int(r["netuid"]),
        )
    )
    for i, r in enumerate(scored, start=1):
        r["rank"] = i
    return scored
