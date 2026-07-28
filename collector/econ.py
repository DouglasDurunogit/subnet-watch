"""econ.py — dTAO income, distribution, and burn math (all read-only).

Ported from research-subnet/scout/econ.py, whose derivation is confirmed against
chain (sum(emission) = alpha_out_emission * tempo * 0.82, i.e. an ~18% owner cut
that we DERIVE rather than hardcode).

    per-UID daily alpha = metagraph.emission[uid] * tempos_per_day
    per-UID daily TAO   = daily_alpha * DynamicInfo.price
    per-UID daily USD   = daily_TAO  * TAO/USD spot

The one thing added here, and the reason this module exists rather than a plain
import: COMPETITIVE income.

`metagraph.emission[uid]` is a PRE-BURN accounting figure — it includes emission
that is withheld and destroyed. And the highest-earning miner is, on ~94 of 127
subnets, either the subnet owner or a validator-permitted UID. Quoting that
number as "what you could earn" is the single most misleading thing this
pipeline could do: on Zipcode the headline top miner earns ~$4.5k/day while the
best a permit-less newcomer achieves is ~$1/day.

So `competitive_*` deliberately excludes owner UIDs (by hotkey AND by coldkey,
which catches an owner mining under a fresh hotkey) and validator-permitted
UIDs. That is the only income figure allowed downstream of here to be presented
as achievable.
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from . import chain

BLOCK_TIME_SECONDS = 12
SECONDS_PER_DAY = 86_400
BLOCKS_PER_DAY = SECONDS_PER_DAY // BLOCK_TIME_SECONDS  # 7200


def _identity_field(info: Any, names: List[str]) -> str:
    sid = chain.get_attr_any(info, ["subnet_identity"], None)
    if sid is None:
        return ""
    return str(chain.get_attr_any(sid, names, "") or "")


def tempos_per_day(tempo: Optional[float]) -> float:
    """Reward epochs per day. Tempo is NOT uniform (sn1 is 99, most are 360),
    so this must never be hardcoded to 20."""
    if not tempo or tempo <= 0:
        return 0.0
    return SECONDS_PER_DAY / (float(tempo) * BLOCK_TIME_SECONDS)


def quick_metrics(info: Any, *, tao_usd: Optional[float], recycle_tao: Optional[float] = None) -> Dict[str, Any]:
    """Subnet-level economics from DynamicInfo alone — no metagraph sync."""
    price = chain.safe_float(chain.get_attr_any(info, ["price"], None)) or 0.0
    alpha_out = chain.safe_float(chain.get_attr_any(info, ["alpha_out"], None)) or 0.0
    alpha_out_em = chain.safe_float(chain.get_attr_any(info, ["alpha_out_emission"], None)) or 0.0
    volume_alpha = chain.safe_float(chain.get_attr_any(info, ["subnet_volume"], None)) or 0.0

    market_cap_tao = alpha_out * price
    emission_tao_day = alpha_out_em * BLOCKS_PER_DAY * price

    def usd(t):
        return (t * tao_usd) if tao_usd else None

    return {
        "netuid": int(chain.get_attr_any(info, ["netuid"], -1) or -1),
        "name": str(chain.get_attr_any(info, ["subnet_name"], "") or ""),
        "symbol": str(chain.get_attr_any(info, ["symbol"], "") or ""),
        "price_tao": price,
        "market_cap_tao": market_cap_tao,
        "emission_tao_day": emission_tao_day,
        "emission_usd_day": usd(emission_tao_day),
        "volume_tao": volume_alpha * price,
        "tempo": chain.safe_float(chain.get_attr_any(info, ["tempo"], None)),
        "registered_at": chain.safe_float(chain.get_attr_any(info, ["network_registered_at"], None)),
        "moving_price": chain.safe_float(chain.get_attr_any(info, ["moving_price"], None)),
        "owner_hotkey": str(chain.get_attr_any(info, ["owner_hotkey"], "") or ""),
        "recycle_tao": recycle_tao,
        "recycle_usd": (recycle_tao * tao_usd) if (recycle_tao is not None and tao_usd) else None,
        "github": _identity_field(info, ["github_repo", "github"]),
        "website": _identity_field(info, ["subnet_url", "url", "website"]),
        "description": _identity_field(info, ["description"]),
    }


def gini(values: List[float]) -> Optional[float]:
    """Gini over non-negative values. 0 = perfectly equal, 1 = one UID takes all."""
    vals = sorted(v for v in values if v is not None and v > 0)
    n = len(vals)
    if n == 0:
        return None
    if n == 1:
        return 0.0
    total = sum(vals)
    if total <= 0:
        return None
    cum = sum(i * v for i, v in enumerate(vals, start=1))
    return (2.0 * cum) / (n * total) - (n + 1.0) / n


def _share(values: List[float], k: int) -> Optional[float]:
    total = sum(values)
    if total <= 0:
        return None
    return sum(sorted(values, reverse=True)[:k]) / total


def _percentile(sorted_vals: List[float], q: float) -> Optional[float]:
    if not sorted_vals:
        return None
    idx = q * (len(sorted_vals) - 1)
    lo = int(idx)
    hi = min(lo + 1, len(sorted_vals) - 1)
    frac = idx - lo
    return sorted_vals[lo] * (1 - frac) + sorted_vals[hi] * frac


def analyze(
    info: Any,
    mg: Any,
    *,
    tao_usd: Optional[float],
    recycle_tao: Optional[float] = None,
    owner_coldkey: str = "",
    miner_burn: Optional[float] = None,
    eps: float = 1e-12,
) -> Dict[str, Any]:
    """Income, distribution and burn for one subnet.

    `miner_burn` comes from the chain's MinerBurned map, not from a heuristic —
    pass it through so the caller can cross-check it against the owner-hotkey
    incentive share computed here.
    """
    tempo = chain.safe_float(chain.get_attr_any(info, ["tempo"], None))
    tpd = tempos_per_day(tempo)
    price_tao = chain.safe_float(chain.get_attr_any(info, ["price"], None)) or 0.0

    # MetagraphInfo (bulk API) names these `incentives`/`dividends`; bt.Metagraph
    # uses singular `incentive`. Accept both so either source works.
    emission = [float(chain.safe_float(x) or 0.0) for x in chain.to_list(chain.get_attr_any(mg, ["emission"], []))]
    incentive = [float(chain.safe_float(x) or 0.0) for x in chain.to_list(chain.get_attr_any(mg, ["incentives", "incentive"], []))]
    dividends = [float(chain.safe_float(x) or 0.0) for x in chain.to_list(chain.get_attr_any(mg, ["dividends", "dividend"], []))]
    vpermit = [bool(x) for x in chain.to_list(chain.get_attr_any(mg, ["validator_permit"], []))]
    hotkeys = [str(x) for x in chain.to_list(chain.get_attr_any(mg, ["hotkeys"], []))]
    coldkeys = [str(x) for x in chain.to_list(chain.get_attr_any(mg, ["coldkeys"], []))]

    n = len(emission)

    def pad(lst, fill):
        return lst + [fill] * (n - len(lst)) if len(lst) < n else lst

    incentive, dividends = pad(incentive, 0.0), pad(dividends, 0.0)
    vpermit = pad(vpermit, False)
    hotkeys, coldkeys = pad(hotkeys, ""), pad(coldkeys, "")

    owner_hotkey = str(chain.get_attr_any(info, ["owner_hotkey"], "") or "")
    owner_coldkey = owner_coldkey or str(chain.get_attr_any(info, ["owner_coldkey"], "") or "")

    players: List[Dict[str, Any]] = []
    for uid in range(n):
        alpha_day = emission[uid] * tpd
        tao_day = alpha_day * price_tao
        is_val = vpermit[uid] or dividends[uid] > eps
        is_miner = incentive[uid] > eps
        role = "both" if (is_miner and is_val) else "validator" if is_val else "miner" if is_miner else "idle"
        players.append({
            "uid": uid,
            "role": role,
            "alpha_day": alpha_day,
            "tao_day": tao_day,
            "usd_day": tao_day * tao_usd if tao_usd else None,
            "incentive": incentive[uid],
            "dividend": dividends[uid],
            "validator_permit": vpermit[uid],
            "hotkey": hotkeys[uid],
            "coldkey": coldkeys[uid],
            "is_owner": (bool(owner_hotkey) and hotkeys[uid] == owner_hotkey)
                        or (bool(owner_coldkey) and coldkeys[uid] == owner_coldkey),
        })
    players.sort(key=lambda p: p["alpha_day"], reverse=True)

    def to_usd(alpha):
        t = alpha * price_tao
        return (t * tao_usd) if tao_usd else None

    # --- MINER-side income only -------------------------------------------
    # Split each UID's emission into its miner and validator components rather
    # than using total emission: a UID can legitimately earn both streams, and
    # only the incentive half is what a miner competes for.
    alpha_out_per_block = chain.safe_float(chain.get_attr_any(info, ["alpha_out_emission"], None)) or 0.0
    minted_per_tempo = alpha_out_per_block * (tempo or 0.0)
    to_uids_per_tempo = sum(emission)
    owner_cut_frac = (
        max(0.0, minted_per_tempo - to_uids_per_tempo) / minted_per_tempo
        if minted_per_tempo > 0 else None
    )
    # The miner pool per tempo: total distributable, split evenly between the
    # incentive and dividend streams (41/41 of the 18/41/41 protocol split).
    miner_pool_per_tempo = to_uids_per_tempo / 2.0
    for p in players:
        p["miner_alpha_day"] = p["incentive"] * miner_pool_per_tempo * tpd
        p["miner_usd_day"] = to_usd(p["miner_alpha_day"])

    miners = [p for p in players if p["incentive"] > eps]
    miners.sort(key=lambda p: p["miner_alpha_day"], reverse=True)

    top_miner = miners[0] if miners else None
    # THE achievable figure: exclude owner-controlled and validator-permitted UIDs.
    competitive = next(
        (p for p in miners if not p["is_owner"] and not p["validator_permit"]),
        None,
    )

    earner_alpha = [p["miner_alpha_day"] for p in miners]
    earner_sorted = sorted(earner_alpha)

    # Owner-captured share of incentive — an independent reconstruction of
    # MinerBurned from the metagraph, used to sanity-check the chain value.
    total_incentive = sum(incentive)
    owner_incentive_share = (
        sum(p["incentive"] for p in players if p["is_owner"]) / total_incentive
        if total_incentive > eps else None
    )

    distribution = {
        "earners": len(miners),
        "validators": sum(1 for p in players if p["role"] in ("validator", "both")),
        "gini": gini(earner_alpha),
        "top1_share": _share(earner_alpha, 1),
        "top10_share": _share(earner_alpha, 10),
        "median_miner_usd_day": to_usd(_percentile(earner_sorted, 0.5)) if earner_alpha else None,
    }

    return {
        "netuid": int(chain.get_attr_any(info, ["netuid"], -1) or -1),
        "name": str(chain.get_attr_any(info, ["subnet_name"], "") or ""),
        "symbol": str(chain.get_attr_any(info, ["symbol"], "") or ""),
        "price_tao": price_tao,
        "tempo": tempo,
        "n_uids": n,
        "active_uids": sum(1 for p in players if p["role"] != "idle"),
        "distribution": distribution,
        "owner_cut_frac": owner_cut_frac,
        "miner_burn": miner_burn,
        "owner_incentive_share": owner_incentive_share,
        "top_miner_usd_day": top_miner["miner_usd_day"] if top_miner else None,
        "top_miner_uid": top_miner["uid"] if top_miner else None,
        "top_miner_is_owner": bool(top_miner["is_owner"]) if top_miner else None,
        "top_miner_is_permitted": bool(top_miner["validator_permit"]) if top_miner else None,
        "competitive_miner_usd_day": competitive["miner_usd_day"] if competitive else None,
        "competitive_miner_alpha_day": competitive["miner_alpha_day"] if competitive else None,
        "competitive_miner_uid": competitive["uid"] if competitive else None,
        "players": players,
    }
