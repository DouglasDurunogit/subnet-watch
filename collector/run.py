"""run.py — one sweep: chain + GitHub -> events -> score -> published files.

    python -m collector.run [--out DIR] [--skip-github] [--seed]

Runs read-only. Never registers, stakes, or spends TAO.

Ordering matters in one place: events are detected against the PREVIOUS
SNAPSHOT.csv before the new one is written, so a crash mid-run leaves the old
snapshot intact and the next run re-detects rather than silently skipping a
change.

--seed records events without making them alarm-visible. The first ever run has
no previous snapshot, so every subnet looks new; 128 NEW_SUBNET alarms on day
one would train the reader to ignore the feed before it has said anything true.
"""

from __future__ import annotations

import argparse
import csv
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional

from . import chain, econ, events, gh, margin, render, score

DEFAULT_CONFIG = {"watch_interval_minutes": 60, "window_overlap_minutes": 15}
BLOCK_TIME_SECONDS = 12


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def load_prev(path: str) -> Dict[int, Dict[str, Any]]:
    if not os.path.exists(path):
        return {}
    out: Dict[int, Dict[str, Any]] = {}
    with open(path, newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            try:
                out[int(row["netuid"])] = row
            except Exception:
                continue
    return out


def load_config(path: str) -> Dict[str, Any]:
    import json
    if os.path.exists(path):
        try:
            with open(path, encoding="utf-8") as fh:
                cfg = json.load(fh)
            return {**DEFAULT_CONFIG, **cfg}
        except Exception:
            pass
    return dict(DEFAULT_CONFIG)


def sweep_chain(st) -> Dict[str, Any]:
    """All chain reads. Bulk calls only - a per-netuid loop drops the socket."""
    t0 = time.time()
    netuids = chain.list_netuids(st)
    block = chain.current_block(st)

    metas = {}
    fn = getattr(st, "get_all_metagraphs_info", None)
    if callable(fn):
        for m in (fn() or []):
            try:
                nid = int(getattr(m, "netuid"))
            except Exception:
                continue
            if nid != 0:
                metas[nid] = m
    infos = chain.all_subnet_info(st)

    out = {
        "netuids": [n for n in netuids if n in metas or n in infos],
        "block": block,
        "metas": metas,
        "infos": infos,
        "miner_burn": chain.miner_burned_map(st, netuids),
        "weights_version": chain.weights_version_map(st, netuids),
        "mechanism_count": chain.mechanism_count_map(st, netuids),
        "tao_usd": chain.tao_usd(),
        "seconds": time.time() - t0,
    }
    return out


def build_row(nid: int, sw: Dict[str, Any], now_iso: str) -> Dict[str, Any]:
    """One subnet's chain-derived row. Marks row_status on partial failure."""
    info = sw["infos"].get(nid)
    meta = sw["metas"].get(nid)
    row: Dict[str, Any] = {
        "netuid": nid,
        "snapshot_utc": now_iso,
        "block": sw["block"],
        "row_status": "ok",
        "tao_usd": sw["tao_usd"],
        "miner_burn": sw["miner_burn"].get(nid),
        "weights_version": sw["weights_version"].get(nid),
        "mechanism_count": sw["mechanism_count"].get(nid),
    }
    if info is None or meta is None:
        row["row_status"] = "failed"
        row["gate_reason"] = "no chain data returned for this netuid"
        return row

    try:
        owner_ck = str(chain.get_attr_any(meta, ["owner_coldkey"], "") or "")
        a = econ.analyze(info, meta, tao_usd=sw["tao_usd"], owner_coldkey=owner_ck,
                         miner_burn=sw["miner_burn"].get(nid))
        d = a["distribution"]

        ident = chain.get_attr_any(meta, ["identity"], None) or {}
        if isinstance(ident, dict):
            gh_url = ident.get("github_repo", "") or ""
            desc = ident.get("description", "") or ""
            site = ident.get("subnet_url", "") or ""
        else:
            gh_url = str(chain.get_attr_any(ident, ["github_repo"], "") or "")
            desc = str(chain.get_attr_any(ident, ["description"], "") or "")
            site = str(chain.get_attr_any(ident, ["subnet_url"], "") or "")

        reg_tao = chain.safe_float(chain.get_attr_any(meta, ["burn"], None))
        max_uids = int(chain.safe_float(chain.get_attr_any(meta, ["max_uids"], 256)) or 256)
        num_uids = int(chain.safe_float(chain.get_attr_any(meta, ["num_uids"], 0)) or 0)
        reg_at = chain.safe_float(chain.get_attr_any(meta, ["network_registered_at"], None))
        age_days = (
            ((sw["block"] - reg_at) * BLOCK_TIME_SECONDS / 86400.0)
            if (reg_at and sw["block"]) else None
        )

        row.update({
            "name": a["name"], "symbol": a["symbol"],
            "tempo": a["tempo"], "price_tao": a["price_tao"],
            "max_uids": max_uids, "active_uids": a["active_uids"],
            "free_uids": max(0, max_uids - num_uids),
            "immunity_period": chain.safe_float(chain.get_attr_any(meta, ["immunity_period"], None)),
            "registration_allowed": bool(chain.get_attr_any(meta, ["registration_allowed"], True)),
            "reg_cost_tao": reg_tao,
            "reg_cost_usd": (reg_tao * sw["tao_usd"]) if (reg_tao is not None and sw["tao_usd"]) else None,
            "registered_block": int(reg_at) if reg_at else None,
            "subnet_age_days": round(age_days, 1) if age_days is not None else None,
            "competitive_miner_usd_day": a["competitive_miner_usd_day"],
            "competitive_miner_alpha_day": a["competitive_miner_alpha_day"],
            "competitive_miner_uid": a["competitive_miner_uid"],
            "median_miner_usd_day": d["median_miner_usd_day"],
            "top_miner_usd_day": a["top_miner_usd_day"],
            "top_miner_uid": a["top_miner_uid"],
            "top_miner_is_owner": a["top_miner_is_owner"],
            "top_miner_is_permitted": a["top_miner_is_permitted"],
            "top1_share": d["top1_share"], "top10_share": d["top10_share"],
            "gini": d["gini"], "earners": d["earners"],
            "owner_cut_frac": a["owner_cut_frac"],
            "owner_incentive_share": a["owner_incentive_share"],
            # Two independent measures of the same thing: MinerBurned is what the
            # chain recorded at the last distribution, owner_incentive_share is
            # what the current incentive vector implies. They agree to ~1e-4 on a
            # settled subnet. A gap means the burn picture is actively shifting,
            # which is information, not an error - so flag it rather than
            # silently preferring one.
            "burn_disagreement": (
                round(abs(sw["miner_burn"][nid] - a["owner_incentive_share"]), 4)
                if (sw["miner_burn"].get(nid) is not None
                    and a["owner_incentive_share"] is not None) else None
            ),
            "description": desc.replace("\n", " ")[:300],
            "website": site,
            "github_url_onchain": gh_url,
        })
    except Exception as e:
        row["row_status"] = "partial"
        row["gate_reason"] = f"{type(e).__name__}: {e}"
    return row


def probe_github(rows: List[Dict[str, Any]], *, workers: int = 12) -> Dict[int, Dict[str, Any]]:
    """Parallel GitHub evidence for every row that has a repo URL."""
    def one(row):
        ref = gh.resolve(gh.parse_repo(row.get("github_url_onchain", "")))
        try:
            return int(row["netuid"]), gh.probe(ref)
        except Exception:
            return int(row["netuid"]), dict(ref.as_dict())

    out: Dict[int, Dict[str, Any]] = {}
    with ThreadPoolExecutor(max_workers=workers) as ex:
        for nid, data in ex.map(one, rows):
            out[nid] = data
    return out


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="One read-only Bittensor subnet sweep.")
    ap.add_argument("--out", default="data", help="output directory (default: data)")
    ap.add_argument("--skip-github", action="store_true",
                    help="chain only; leaves GitHub columns from the previous snapshot")
    ap.add_argument("--seed", action="store_true",
                    help="record events without alarming (use for the first ever run)")
    ap.add_argument("--network", default="finney")
    args = ap.parse_args(argv)

    t_start = time.time()
    out = args.out
    os.makedirs(os.path.join(out, "subnets"), exist_ok=True)
    snapshot_path = os.path.join(out, "SNAPSHOT.csv")
    config = load_config(os.path.join(out, "config.json"))
    prev = load_prev(snapshot_path)
    now_iso = _now_iso()

    print(f"[{now_iso}] connecting to {args.network} ...", flush=True)
    st = chain.connect(args.network)
    sw = sweep_chain(st)
    print(f"  chain sweep: {len(sw['netuids'])} subnets, block {sw['block']}, "
          f"{sw['seconds']:.1f}s, TAO/USD={sw['tao_usd']}", flush=True)

    rows = [build_row(n, sw, now_iso) for n in sw["netuids"]]
    failed = [int(r["netuid"]) for r in rows if r["row_status"] == "failed"]

    readme_texts: Dict[int, str] = {}
    if args.skip_github:
        print("  github: SKIPPED (--skip-github); carrying previous columns", flush=True)
        for r in rows:
            p = prev.get(int(r["netuid"]))
            if p:
                for k in ("github_url_resolved", "repo_status", "repo_status_reason",
                          "readme_sha", "readme_bytes", "readme_task_sections",
                          "last_commit_utc", "latest_release", "latest_release_utc",
                          "scoring_commit_utc", "scoring_commit_title",
                          "min_compute_present", "min_compute_is_template"):
                    r[k] = p.get(k)
    else:
        t0 = time.time()
        probes = probe_github(rows)
        for r in rows:
            data = probes.get(int(r["netuid"]), {})
            readme_texts[int(r["netuid"])] = data.pop("readme_text", "") or ""
            r.update({k: v for k, v in data.items() if k != "min_compute_text"})
            r["_min_compute_text"] = data.get("min_compute_text", "")
        ok = sum(1 for r in rows if r.get("repo_status") in ("ok", "redirected"))
        print(f"  github: {ok}/{len(rows)} repos reachable, {time.time()-t0:.1f}s", flush=True)

    # --- resources + margin --------------------------------------------------
    machines = margin.load_machines(os.path.join(out, "machines.csv"))
    tier_by_class = {m["class_id"]: m["tier"] for m in machines}
    for r in rows:
        r["readme_text"] = readme_texts.get(int(r["netuid"]), "")
        r["min_compute_text"] = r.pop("_min_compute_text", "")
        r.update(margin.compute(r, machines))
        r["machine_tier"] = tier_by_class.get(r.get("machine_class_cheapest"))
        r.pop("readme_text", None)
        r.pop("min_compute_text", None)

    # --- events (against the PREVIOUS snapshot, before overwriting it) -------
    log_path = os.path.join(out, "EVENTS.jsonl")
    log = events.load_log(log_path)
    first_run = not prev
    fresh: List[Dict[str, Any]] = []
    for r in rows:
        fresh.extend(events.detect(prev.get(int(r["netuid"])), r))
    added = events.merge(log, fresh, seed_only=(args.seed or first_run))
    events.append_log(log_path, added)
    if first_run or args.seed:
        print(f"  events: {len(added)} SEEDED (not alarmed) - first run has no baseline",
              flush=True)
    else:
        print(f"  events: {len(added)} new", flush=True)

    win = events.window(log, interval_minutes=config["watch_interval_minutes"],
                        overlap_minutes=config["window_overlap_minutes"])

    # Seeded records are excluded from freshness as well as from alarms. The
    # baseline run writes one NEW_SUBNET per subnet; counting those would give
    # all 128 a perfect freshness score dated to the day the monitor was
    # installed, which is an artefact of when we started looking, not a fact
    # about any subnet.
    ev_by_net: Dict[int, List[Dict[str, Any]]] = {}
    for rec in log.values():
        if rec.get("seeded"):
            continue
        ev_by_net.setdefault(int(rec["netuid"]), []).append(rec)

    # --- score + rank --------------------------------------------------------
    for r in rows:
        r.update(score.score_row(r, ev_by_net))
    ranked = score.rank(rows)

    # --- publish -------------------------------------------------------------
    render.write_snapshot(snapshot_path, rows)
    render.write_margin(os.path.join(out, "MARGIN.csv"), rows)
    render.write_alarms(os.path.join(out, "ALARMS.md"), win,
                        generated_utc=now_iso, block=sw["block"], config=config)
    render.write_ranking(os.path.join(out, "RANKING.md"), ranked, rows,
                         generated_utc=now_iso, block=sw["block"])

    run_status = "ok" if not failed else ("partial" if len(failed) < len(rows) else "failed")
    render.write_manifest(
        os.path.join(out, "MANIFEST.json"), generated_utc=now_iso, block=sw["block"],
        run_status=run_status, rows=rows, failed=failed, tao_usd=sw["tao_usd"],
        window=win, config=config, duration_s=time.time() - t_start,
    )
    for r in rows:
        render.write_evidence_pack(
            os.path.join(out, "subnets", f"sn{int(r['netuid'])}.md"), r,
            generated_utc=now_iso, block=sw["block"],
            readme_text=readme_texts.get(int(r["netuid"]), ""),
        )

    gated = sum(1 for r in rows if r.get("gate_status", "OK") != "OK")
    print(f"  published: {len(rows)} rows, {len(ranked)} ranked, {gated} gated, "
          f"status={run_status}, {time.time()-t_start:.1f}s total", flush=True)
    if ranked:
        print("  top 5: " + ", ".join(
            f"sn{r['netuid']}({r['name']}) {r['score']}" for r in ranked[:5]), flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
