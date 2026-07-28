"""events.py — the new-challenge detector and its alarm window.

WHAT THIS REPLACES. scout's change detection diffed `last_step`, the on-chain
scoring epoch. That advances several times an hour on every subnet, so shipping
it as "new challenge" would produce ~3000 alarms a day, the user would stop
reading, and the highest-priority requirement would be defeated by its own
noise. `last_step` is deliberately, permanently excluded here.

WHAT COUNTS. Only a change to what miners are asked to do, or how they are
scored, in descending confidence:

  NEW_SUBNET            a netuid that did not exist before
  WEIGHTS_VERSION_BUMP  owner raised WeightsVersionKey; the chain now REJECTS
                        weight submissions from un-upgraded validators, so this
                        is as close to a guaranteed breaking change as exists
  MECHANISM_ADDED       mechanism count rose; a second distinct challenge now
                        runs under one netuid
  BURN_DROP             miner_burn fell out of >=0.99; a subnet where miners
                        earned nothing now pays (the user's "unseen subnet")
  RELEASE               a new entry in releases.atom
  SCORING_COMMIT        a commit whose message matches the scoring vocabulary
  README_TASK_DIFF      the README's task/scoring sections changed
  REGISTRATION_OPENED   registration went closed -> open, or slots freed

DEDUP WITHOUT MEMORY. ChatGPT Tasks are stateless and cannot write back to the
repo, so "have I already reported this?" cannot be answered by recall. Instead
every event carries an immutable `first_seen_utc` assigned once, and window
membership is a pure function of (first_seen_utc, now, declared interval). An
event is NEW for exactly one window, then STILL_OPEN until it ages out. A missed
run therefore delays a report but can never lose one.
"""

from __future__ import annotations

import json
import os
from datetime import datetime, timedelta, timezone
from typing import Any, Dict, List, Optional

# severity drives ordering in ALARMS.md, not whether something is reported.
SEVERITY = {
    "NEW_SUBNET": "P0",
    "WEIGHTS_VERSION_BUMP": "P0",
    "MECHANISM_ADDED": "P0",
    "BURN_DROP": "P0",
    "RELEASE": "P1",
    "SCORING_COMMIT": "P1",
    "README_TASK_DIFF": "P2",
    "REGISTRATION_OPENED": "P2",
}
_SEV_ORDER = {"P0": 0, "P1": 1, "P2": 2}

BURN_DEAD = 0.99      # at or above this, miners earn nothing
OPEN_TTL_HOURS = 168  # an unresolved event stays listed for 7 days


def _now() -> datetime:
    return datetime.now(timezone.utc)


def iso(dt: datetime) -> str:
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")


def _parse(ts: str) -> Optional[datetime]:
    if not ts:
        return None
    try:
        return datetime.fromisoformat(ts.replace("Z", "+00:00")).astimezone(timezone.utc)
    except Exception:
        return None


def _f(row: Dict[str, Any], key: str) -> Optional[float]:
    v = row.get(key)
    if v is None or v == "":
        return None
    try:
        return float(v)
    except Exception:
        return None


def detect(prev: Optional[Dict[str, Any]], cur: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Events implied by prev -> cur for ONE subnet.

    `prev` is None the first time a subnet is seen. Returns event dicts without
    first_seen_utc; the log assigns that once, on first sighting.
    """
    n = int(cur["netuid"])
    out: List[Dict[str, Any]] = []

    def add(cls: str, disc: str, one_line: str, detail: str = ""):
        out.append({
            "event_id": f"sn{n}:{cls.lower()}:{disc}",
            "netuid": n,
            "name": cur.get("name", ""),
            "class": cls,
            "severity": SEVERITY[cls],
            "one_line": one_line,
            "detail": detail,
        })

    if prev is None:
        # A subnet absent from the previous snapshot. On the very first run every
        # subnet is "new", which would be 128 false alarms -- the caller
        # suppresses this by seeding the log without emitting (see load_and_merge).
        add("NEW_SUBNET", f"b{cur.get('block', '0')}",
            f"NEW SUBNET sn{n} \"{cur.get('name', '')}\" first seen",
            f"burn={cur.get('miner_burn')} reg={cur.get('reg_cost_tao')} TAO "
            f"repo={cur.get('github_url_resolved') or 'NONE'}")
        return out

    # --- chain-side signals (high confidence: the protocol enforces these) ---
    pw, cw = _f(prev, "weights_version"), _f(cur, "weights_version")
    if pw is not None and cw is not None and cw > pw:
        add("WEIGHTS_VERSION_BUMP", str(int(cw)),
            f"sn{n} weights_version {int(pw)} -> {int(cw)}",
            "Owner raised the version gate; the chain now rejects weights from "
            "un-upgraded validators. Near-certain breaking scoring change.")

    pm, cm = _f(prev, "mechanism_count"), _f(cur, "mechanism_count")
    if pm is not None and cm is not None and cm > pm:
        add("MECHANISM_ADDED", f"{int(pm)}to{int(cm)}",
            f"sn{n} now runs {int(cm)} incentive mechanisms (was {int(pm)})",
            "A second distinct challenge now runs under this netuid.")

    pb, cb = _f(prev, "miner_burn"), _f(cur, "miner_burn")
    if pb is not None and cb is not None and pb >= BURN_DEAD and cb < BURN_DEAD:
        add("BURN_DROP", f"{cb:.3f}",
            f"sn{n} burn fell {pb:.3f} -> {cb:.3f} - miners can earn again",
            "This subnet paid miners nothing and now pays. Worth a look before "
            "the field fills up.")

    pr, cr = prev.get("registration_allowed"), cur.get("registration_allowed")
    if str(pr) == "False" and str(cr) == "True":
        add("REGISTRATION_OPENED", "open",
            f"sn{n} registration reopened",
            f"reg cost {cur.get('reg_cost_tao')} TAO")

    # --- GitHub-side signals ------------------------------------------------
    # Each requires the PREVIOUS value to be non-empty. Populating a field for
    # the first time is not a change, and treating it as one produces a false
    # alarm for every repo the moment GitHub probing is enabled, or whenever a
    # repo 404s transiently and comes back. The cost is that a genuine release
    # on a newly-readable repo waits one cycle, which is the right trade: we
    # cannot distinguish "new release" from "first time we looked".
    if (cur.get("latest_release") and prev.get("latest_release")
            and cur["latest_release"] != prev["latest_release"]):
        add("RELEASE", str(cur["latest_release"])[:40],
            f"sn{n} released {cur['latest_release']}",
            f"published {cur.get('latest_release_utc', '')} "
            f"(was {prev.get('latest_release')})")

    if (cur.get("scoring_commit_utc") and prev.get("scoring_commit_utc")
            and cur["scoring_commit_utc"] != prev["scoring_commit_utc"]):
        add("SCORING_COMMIT", str(cur["scoring_commit_utc"])[:20],
            f"sn{n} commit touches scoring: {str(cur.get('scoring_commit_title', ''))[:70]}",
            "Matched on the commit MESSAGE, not a file diff - weaker evidence "
            "than a release; confirm before acting.")

    ps, cs = prev.get("readme_task_sections"), cur.get("readme_task_sections")
    if cs and ps and cs != ps:
        add("README_TASK_DIFF", str(cs)[:16],
            f"sn{n} README task/scoring sections changed",
            "Only the task-describing headings are hashed, so badge and typo "
            "edits do not trigger this.")

    return out


# --- the append-only log -----------------------------------------------------

def load_log(path: str) -> Dict[str, Dict[str, Any]]:
    """{event_id: record}. Missing or corrupt lines are skipped, not fatal."""
    out: Dict[str, Dict[str, Any]] = {}
    if not os.path.exists(path):
        return out
    with open(path, "r", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                rec = json.loads(line)
                out[rec["event_id"]] = rec
            except Exception:
                continue
    return out


def merge(log: Dict[str, Dict[str, Any]], fresh: List[Dict[str, Any]],
          *, now: Optional[datetime] = None, seed_only: bool = False) -> List[Dict[str, Any]]:
    """Assign first_seen_utc to genuinely new events; return the added records.

    `seed_only` records the events without making them alarm-visible. That is
    what the first-ever run uses: with no previous snapshot every subnet looks
    new, and 128 NEW_SUBNET alarms on day one would train the user to ignore the
    feed before it has said anything true.
    """
    now = now or _now()
    added: List[Dict[str, Any]] = []
    for ev in fresh:
        if ev["event_id"] in log:
            continue
        rec = dict(ev)
        rec["first_seen_utc"] = iso(now)
        rec["resolved_utc"] = ""
        rec["seeded"] = bool(seed_only)
        log[rec["event_id"]] = rec
        added.append(rec)
    return added


def append_log(path: str, records: List[Dict[str, Any]]) -> None:
    if not records:
        return
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "a", encoding="utf-8") as fh:
        for rec in records:
            fh.write(json.dumps(rec, sort_keys=True) + "\n")


def window(log: Dict[str, Dict[str, Any]], *, interval_minutes: int,
           overlap_minutes: int, now: Optional[datetime] = None) -> Dict[str, List[Dict[str, Any]]]:
    """Split the log into NEW / STILL_OPEN / RESOLVED for this run.

    Membership keys on the immutable first_seen_utc, never on "did I notice it
    this run", which is what makes the result identical for any observer and
    reproducible after the fact.
    """
    now = now or _now()
    start = now - timedelta(minutes=interval_minutes + overlap_minutes)
    ttl = now - timedelta(hours=OPEN_TTL_HOURS)

    new, still, resolved = [], [], []
    for rec in log.values():
        if rec.get("seeded"):
            continue
        seen = _parse(rec.get("first_seen_utc", ""))
        if seen is None:
            continue
        if rec.get("resolved_utc"):
            if (_parse(rec["resolved_utc"]) or now) >= start:
                resolved.append(rec)
            continue
        if seen >= start:
            new.append(rec)
        elif seen >= ttl:
            still.append(rec)

    def order(rows):
        return sorted(rows, key=lambda r: (_SEV_ORDER.get(r.get("severity", "P2"), 9),
                                           r.get("first_seen_utc", "")), reverse=False)

    return {
        "new": order(new),
        "still_open": order(still),
        "resolved": order(resolved),
        "window_start": iso(start),
        "window_end": iso(now),
    }
