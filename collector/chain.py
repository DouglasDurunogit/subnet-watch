"""chain.py — read-only access layer to the Bittensor (finney) chain + price feed.

Ported from research-subnet/scout/chain.py, which is proven against finney, plus
three raw storage reads scout does not have and which this project depends on:

    miner_burned_map(st)      -> {netuid: 0..1}   THE burn metric (protocol-level)
    weights_version_map(st)   -> {netuid: int}    the "everyone must upgrade" lever
    subnet_owner_map(st)      -> {netuid: ss58}   owner COLDKEY, for owner detection

Nothing here spends TAO. `recycle_cost` reads the registration cost but never
registers.

Two decoding traps, both load-bearing:
  * `MinerBurned` is a U96F32 fixed-point — the raw value arrives as {'bits': N}
    and must be divided by 2**32. Reading it raw yields ~1e9 instead of ~0.5.
  * `query_map` omits keys that were never explicitly set, because these are
    ValueQuery maps that fall through to a default. An absent netuid is NOT
    missing data — it is the default. Callers must backfill.
"""

from __future__ import annotations

import time
from typing import Any, Dict, List, Optional

import requests

try:
    import bittensor as bt
except Exception as e:  # pragma: no cover
    raise RuntimeError(
        "bittensor package not installed. Run: pip install -U bittensor"
    ) from e


# --- low-level value coercion (Balance / tensor / numpy -> python) -----------

def safe_float(x: Any) -> Optional[float]:
    """Convert Balance/tensor/numpy/python values into a float, or None."""
    if x is None:
        return None
    for getter in (
        lambda v: float(v.tao),      # bittensor Balance -> TAO units
        lambda v: float(v.rao) / 1e9,
        lambda v: float(v.item()),   # 0-d tensor / numpy scalar
        lambda v: float(v),
    ):
        try:
            return getter(x)
        except Exception:
            continue
    return None


def to_list(x: Any) -> List[Any]:
    """Convert torch/numpy/list-like to a plain python list."""
    if x is None:
        return []
    for getter in (
        lambda v: v.detach().cpu().numpy().tolist(),
        lambda v: v.cpu().numpy().tolist(),
        lambda v: v.numpy().tolist(),
        lambda v: list(v),
    ):
        try:
            return getter(x)
        except Exception:
            continue
    return []


def get_attr_any(obj: Any, names: List[str], default=None):
    for name in names:
        if hasattr(obj, name):
            return getattr(obj, name)
    return default


def _call_first(obj: Any, names: List[str], *args):
    for name in names:
        fn = getattr(obj, name, None)
        if callable(fn):
            try:
                return fn(*args)
            except Exception:
                continue
    return None


# --- connection --------------------------------------------------------------

def connect(network: str = "finney"):
    """Return a Subtensor, compatible across new/old SDK casing."""
    if hasattr(bt, "Subtensor"):
        return bt.Subtensor(network=network)
    if hasattr(bt, "subtensor"):
        return bt.subtensor(network=network)
    raise RuntimeError("No bt.Subtensor / bt.subtensor in installed bittensor.")


def current_block(st: Any) -> Optional[int]:
    try:
        return int(st.get_current_block())
    except Exception:
        return None


def list_netuids(st: Any) -> List[int]:
    """Active subnet netuids (excludes root/0)."""
    for name in ("get_all_subnet_netuids", "get_subnets"):
        res = _call_first(st, [name])
        if res is not None:
            try:
                return sorted(int(x) for x in res if int(x) != 0)
            except Exception:
                pass
    total = safe_float(_call_first(st, ["get_total_subnets"]))
    if total:
        return list(range(1, int(total) + 1))
    raise RuntimeError("Could not enumerate subnets from subtensor.")


# --- per-subnet reads --------------------------------------------------------

def subnet_info(st: Any, netuid: int) -> Any:
    """On-chain DynamicInfo: authoritative identity + dTAO economics."""
    return _call_first(st, ["subnet"], netuid)


def all_subnet_info(st: Any) -> Dict[int, Any]:
    """All subnets' DynamicInfo in a single batch RPC ({netuid: info}).

    ~1.5s for the whole network vs ~1s/subnet one-by-one. Excludes root (0).
    """
    res = _call_first(st, ["all_subnets"])
    out: Dict[int, Any] = {}
    if res:
        for info in res:
            nid = get_attr_any(info, ["netuid"], None)
            if nid is not None and int(nid) != 0:
                out[int(nid)] = info
    return out


def metagraph(st: Any, netuid: int, lite: bool = True) -> Any:
    """Per-UID metagraph. `lite=True` skips weights/bonds for speed."""
    fn = getattr(st, "metagraph", None)
    if callable(fn):
        try:
            return fn(netuid=netuid, lite=lite)
        except TypeError:
            return fn(netuid)
    for ctor in ("metagraph", "Metagraph"):
        maker = getattr(bt, ctor, None)
        if callable(maker):
            return maker(netuid=netuid, network="finney", lite=lite, sync=True)
    raise RuntimeError(f"Could not load metagraph for netuid {netuid}")


def recycle_cost(st: Any, netuid: int) -> Optional[float]:
    """Per-UID registration burn ("recycle") in TAO. Read-only.

    Deliberately NOT get_subnet_burn_cost() (the global new-SUBNET creation cost)
    and NOT burned_register() (which actually spends TAO).
    """
    val = safe_float(_call_first(st, ["recycle", "get_burned_register_cost"], netuid))
    if val is not None:
        return val
    try:
        from bittensor.extras.subtensor_api.subnets import Subnets

        api = Subnets(st)
        return safe_float(_call_first(api, ["recycle", "get_burned_register_cost"], netuid))
    except Exception:
        return None


def hyperparams(st: Any, netuid: int) -> Dict[str, Any]:
    """Selected subnet hyperparameters relevant to registration status."""
    hp = _call_first(st, ["get_subnet_hyperparameters"], netuid)
    out: Dict[str, Any] = {}
    if hp is None:
        return out
    out["max_uids"] = int(safe_float(get_attr_any(hp, ["max_n", "max_allowed_uids", "max_uids"], 256)) or 256)
    out["immunity_period"] = safe_float(get_attr_any(hp, ["immunity_period"], None))
    out["tempo"] = safe_float(get_attr_any(hp, ["tempo"], None))
    ra = get_attr_any(hp, ["registration_allowed"], None)
    out["registration_allowed"] = bool(ra) if ra is not None else None
    out["weights_version"] = safe_float(get_attr_any(hp, ["weights_version"], None))
    return out


# --- raw storage maps (not exposed by the SDK) --------------------------------
#
# One query_map per storage item, never a per-netuid loop: 128 sequential
# single-key query() calls reliably trips a keepalive ping timeout and drops the
# websocket, while the equivalent query_map is one round trip in ~1.4s.

def _substrate(st: Any):
    return get_attr_any(st, ["substrate"], None)


def _query_map(st: Any, module: str, item: str, attempts: int = 2) -> Optional[Dict[int, Any]]:
    """{netuid: raw_value} for a storage map keyed by netuid.

    Returns **None on failure**, which is NOT the same as an empty map. These are
    ValueQuery maps: an absent key legitimately means "the default applies", so a
    caller must be able to tell "the chain says nothing about netuid 5" from "the
    query did not run".

    Conflating those two caused a real false alarm. A transient failure returned
    {}, every subnet fell back to the MechanismCount default of 1, and the next
    successful sweep read 2 again — firing MECHANISM_ADDED "1->2" for all six
    multi-mechanism subnets in the same second, when nothing had changed on
    chain. The MinerBurned version of this bug would be far worse: its default is
    0.0, so one failed query would make every dead subnet look alive and fire a
    P0 BURN_DROP for each.
    """
    sub = _substrate(st)
    if sub is None:
        return None
    last: Optional[Exception] = None
    for _ in range(max(1, attempts)):
        try:
            res = sub.query_map(module, item)
        except Exception as e:      # public finney does drop connections
            last = e
            continue
        out: Dict[int, Any] = {}
        for key, val in res:
            try:
                nid = int(getattr(key, "value", key))
            except Exception:
                continue
            out[nid] = getattr(val, "value", val)
        return out
    print(f"  chain: query_map({module}.{item}) FAILED "
          f"({type(last).__name__ if last else 'no substrate'}) - "
          f"values will be reported MISSING, not defaulted", flush=True)
    return None


def _defix(raw: Any, frac_bits: int) -> Optional[float]:
    """Decode a substrate fixed-point value ({'bits': N} or a bare int)."""
    if raw is None:
        return None
    bits = raw.get("bits") if isinstance(raw, dict) else raw
    try:
        return float(bits) / float(2 ** frac_bits)
    except Exception:
        return None


def miner_burned_map(st: Any, netuids: List[int]) -> Dict[int, Optional[float]]:
    """{netuid: 0..1} — the fraction of miner (incentive) emission withheld.

    This is THE burn metric. It is the proportion of each tempo's incentive
    emission that landed on an owner-controlled hotkey and was therefore
    recycled or burned instead of paid. A value >= 0.99 means miners earn
    nothing on that subnet no matter what any income column says.

    U96F32 fixed-point: divide by 2**32. Absent netuids default to 0.0.
    """
    raw = _query_map(st, "SubtensorModule", "MinerBurned")
    if raw is None:
        return {n: None for n in netuids}      # missing, NOT 0.0 ("everyone alive")
    return {n: (_defix(raw[n], 32) if n in raw else 0.0) for n in netuids}


def weights_version_map(st: Any, netuids: List[int]) -> Dict[int, Optional[int]]:
    """{netuid: weights_version_key} — 0 means the version gate is disabled.

    Only the subnet owner can raise this, and raising it hard-rejects weight
    submissions from validators still running old code. A bump is therefore a
    near-certain "breaking scoring change" signal. Treat the value as an opaque
    monotonic counter, NOT semver: observed values range from 1 to 1000910.
    """
    raw = _query_map(st, "SubtensorModule", "WeightsVersionKey")
    if raw is None:
        return {n: None for n in netuids}      # missing, NOT 0 ("gate disabled")
    out: Dict[int, Optional[int]] = {}
    for n in netuids:
        try:
            out[n] = int(raw.get(n, 0) or 0)
        except Exception:
            out[n] = 0
    return out


def mechanism_count_map(st: Any, netuids: List[int]) -> Dict[int, Optional[int]]:
    """{netuid: mechanism count} — a 1 -> 2 transition means a second, distinct
    incentive mechanism (a whole new challenge) was added under one netuid.
    Absent netuids default to 1."""
    raw = _query_map(st, "SubtensorModule", "MechanismCountCurrent")
    if raw is None:
        return {n: None for n in netuids}      # missing, NOT 1 ("one mechanism")
    out: Dict[int, Optional[int]] = {}
    for n in netuids:
        try:
            out[n] = int(raw.get(n, 1) or 1)
        except Exception:
            out[n] = 1
    return out


def subnet_owner_map(st: Any, netuids: List[int]) -> Dict[int, str]:
    """{netuid: owner coldkey ss58}. Owner detection by coldkey catches an owner
    mining under a fresh hotkey, which hotkey-only matching misses."""
    raw = _query_map(st, "SubtensorModule", "SubnetOwner")
    if raw is None:
        return {n: "" for n in netuids}
    return {n: str(raw.get(n, "") or "") for n in netuids}


# --- price feed --------------------------------------------------------------

_TAO_USD_CACHE: Dict[str, Any] = {"ts": 0.0, "value": None}


def tao_usd(ttl_seconds: float = 300.0) -> Optional[float]:
    """Spot TAO/USD from CoinGecko (free, no key). Cached for `ttl_seconds`.

    Returns None on failure; callers must keep working in TAO-only terms rather
    than substituting a stale or invented rate.
    """
    now = time.monotonic()
    if _TAO_USD_CACHE["value"] is not None and now - _TAO_USD_CACHE["ts"] < ttl_seconds:
        return _TAO_USD_CACHE["value"]
    try:
        r = requests.get(
            "https://api.coingecko.com/api/v3/simple/price",
            params={"ids": "bittensor", "vs_currencies": "usd"},
            timeout=15,
        )
        r.raise_for_status()
        val = float(r.json()["bittensor"]["usd"])
        _TAO_USD_CACHE.update(ts=now, value=val)
        return val
    except Exception:
        return _TAO_USD_CACHE["value"]
