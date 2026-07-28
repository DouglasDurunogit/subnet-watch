"""render.py — write the files ChatGPT reads.

Everything ChatGPT is allowed to state must be quotable from one of these. The
column list in COLUMNS is a CONTRACT: chatgpt/00_INSTRUCTIONS.md cites these
names literally, so renaming one silently breaks the citation rule.

Note `row_status`. A 0.0 in a row whose row_status is not "ok" means the sweep
failed, NOT that the value is zero. This is the same failure that makes
taomarketcap dangerous (it serves placeholder zeros that read as data), and the
column exists so the pipeline cannot reintroduce it from the inside.
"""

from __future__ import annotations

import csv
import json
import os
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional

COLUMNS = [
    "netuid", "name", "symbol", "snapshot_utc", "block", "row_status",
    "miner_burn", "reg_cost_tao", "reg_cost_usd", "registration_allowed",
    "max_uids", "active_uids", "free_uids", "immunity_period", "tempo",
    "price_tao", "tao_usd", "subnet_age_days", "registered_block",
    "weights_version", "mechanism_count",
    "competitive_miner_alpha_day", "competitive_miner_usd_day", "competitive_miner_uid",
    "competitive_median_usd_day", "competitive_earners",
    "median_miner_usd_day", "top_miner_usd_day", "top_miner_uid",
    "top_miner_is_owner", "top_miner_is_permitted",
    "top1_share", "top10_share", "gini", "earners",
    "owner_cut_frac", "owner_incentive_share", "burn_disagreement",
    "github_url_onchain", "github_url_resolved", "repo_status", "repo_status_reason",
    "readme_sha", "readme_bytes", "readme_task_sections",
    "last_commit_utc", "latest_release", "latest_release_utc",
    "scoring_commit_utc", "scoring_commit_title",
    "min_compute_present", "min_compute_is_template",
    "required_vram_gb", "gpu_class_required", "gpu_class_basis",
    "machine_class_cheapest", "machine_cost_usd_day", "machine_tier", "machine_assumed",
    "net_margin_usd_day", "net_margin_top_usd_day", "payback_days",
    "gate_status", "gate_reason",
    "income_pts", "freshness_pts", "resource_pts", "registration_pts",
    "freshness_reason", "confidence", "confidence_reason", "score", "rank",
    "description", "website",
]


def _atomic(path: str, text: str) -> None:
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8", newline="") as fh:
        fh.write(text)
    os.replace(tmp, path)


def _money(v: Optional[float]) -> str:
    """Shared precision for median and ceiling. Rendering them differently made
    the same number look like a ceiling below its own median."""
    if v is None:
        return "n/a"
    return f"{v:,.0f}" if abs(v) >= 100 else f"{v:,.2f}"


def _fmt(v: Any) -> str:
    if v is None:
        return ""
    if isinstance(v, bool):
        return "True" if v else "False"
    if isinstance(v, float):
        return f"{v:.6g}"
    return str(v)


def write_snapshot(path: str, rows: List[Dict[str, Any]]) -> None:
    lines = [",".join(COLUMNS)]
    buf = []
    for r in sorted(rows, key=lambda x: int(x["netuid"])):
        buf.append([_fmt(r.get(c)) for c in COLUMNS])
    out = [COLUMNS] + buf
    tmp = path + ".tmp"
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(tmp, "w", encoding="utf-8", newline="") as fh:
        csv.writer(fh, lineterminator="\n").writerows(out)
    os.replace(tmp, path)


def write_manifest(path: str, *, generated_utc: str, block: Optional[int],
                   run_status: str, rows: List[Dict[str, Any]],
                   failed: List[int], tao_usd: Optional[float],
                   window: Dict[str, Any], config: Dict[str, Any],
                   duration_s: float) -> None:
    gated = {}
    for r in rows:
        g = r.get("gate_status", "")
        if g and g != "OK":
            gated[g] = gated.get(g, 0) + 1
    payload = {
        "generated_utc": generated_utc,
        "block": block,
        "run_status": run_status,
        "duration_seconds": round(duration_s, 1),
        "subnets_total": len(rows),
        "subnets_failed": len(failed),
        "failed_netuids": sorted(failed),
        "tao_usd": tao_usd,
        "ranked": sum(1 for r in rows if r.get("rank")),
        "gated": gated,
        "events_new": len(window.get("new", [])),
        "events_still_open": len(window.get("still_open", [])),
        "window_start": window.get("window_start", ""),
        "window_end": window.get("window_end", ""),
        "config": config,
        "files": {
            "snapshot": "data/SNAPSHOT.csv",
            "alarms": "data/ALARMS.md",
            "ranking": "data/RANKING.md",
            "margin": "data/MARGIN.csv",
            "machines": "data/machines.csv",
            "events": "data/EVENTS.jsonl",
            "evidence_packs": "data/subnets/sn<NN>.md",
            "briefs": "briefs/sn<NN>.md",
        },
    }
    _atomic(path, json.dumps(payload, indent=2, sort_keys=True) + "\n")


def write_alarms(path: str, window: Dict[str, Any], *, generated_utc: str,
                 block: Optional[int], config: Dict[str, Any]) -> None:
    iv, ov = config["watch_interval_minutes"], config["window_overlap_minutes"]
    L = [
        f"# ALARMS - generated {generated_utc}, block {block}",
        "",
        f"window: first_seen in [{window['window_start']}, {window['window_end']})  "
        f"({iv} min interval + {ov} min overlap)",
        "",
        "Report ONLY the rows under NEW SINCE LAST RUN. Rows under STILL OPEN were",
        "already reported in an earlier window and must not be re-alarmed.",
        "",
        "## NEW SINCE LAST RUN",
        "",
    ]
    if not window["new"]:
        L += ["_none_", ""]
    else:
        L += ["| event_id | netuid | class | severity | first_seen_utc | one_line |",
              "|---|---|---|---|---|---|"]
        for e in window["new"]:
            L.append(f"| `{e['event_id']}` | {e['netuid']} | {e['class']} | {e['severity']} "
                     f"| {e['first_seen_utc']} | {e['one_line']} |")
        L.append("")
        L.append("### detail")
        L.append("")
        for e in window["new"]:
            L.append(f"- **`{e['event_id']}`** - {e['one_line']}")
            if e.get("detail"):
                L.append(f"  - {e['detail']}")
        L.append("")

    L += ["## STILL OPEN (already reported - do not re-alarm)", ""]
    if not window["still_open"]:
        L += ["_none_", ""]
    else:
        L += ["| event_id | netuid | class | first_seen_utc | one_line |",
              "|---|---|---|---|---|"]
        for e in window["still_open"]:
            L.append(f"| `{e['event_id']}` | {e['netuid']} | {e['class']} "
                     f"| {e['first_seen_utc']} | {e['one_line']} |")
        L.append("")

    L += ["## RESOLVED IN THIS WINDOW", ""]
    L += ["_none_", ""] if not window["resolved"] else \
         [f"- `{e['event_id']}` resolved {e.get('resolved_utc','')}" for e in window["resolved"]] + [""]

    _atomic(path, "\n".join(L))


def write_ranking(path: str, ranked: List[Dict[str, Any]], all_rows: List[Dict[str, Any]],
                  *, generated_utc: str, block: Optional[int], top: int = 25) -> None:
    L = [
        f"# RANKING - generated {generated_utc}, block {block}",
        "",
        "Weights: income 40 / new-challenge freshness 35 / resource cost 15 / registration 10.",
        "Incentive structure is weight ZERO by explicit decision - it is reported per subnet",
        "but never scored, and no incentive-structure subscore is published to re-weight.",
        "",
        "Income is the MEDIAN non-owner, non-validator-permitted miner - what a newcomer",
        "should actually expect. The best competitive miner is shown separately as the",
        "ceiling: on a winner-take-all subnet the two differ by orders of magnitude (sn15",
        "ORO's best clears $10k/day while its median earner makes $10.20), and scoring the",
        "ceiling ranked winner-take-all subnets above genuinely open ones.",
        "",
        f"## TOP {top}",
        "",
        "| # | netuid | name | score | conf | net $/day (median) | ceiling $/day | machine | burn | earners | top1% | freshness |",
        "|---|---|---|---|---|---|---|---|---|---|---|---|",
    ]

    def g(r, k, dflt=""):
        v = r.get(k)
        return dflt if v in (None, "") else v

    for r in ranked[:top]:
        net = r.get("net_margin_usd_day")
        t1 = r.get("top1_share")
        L.append(
            f"| {r['rank']} | {r['netuid']} | {g(r,'name')} | {g(r,'score')} | {g(r,'confidence')} "
            f"| {_money(net)} "
            f"| {_money(float(r['net_margin_top_usd_day']) if g(r,'net_margin_top_usd_day')!='' else None)} "
            f"| {g(r,'machine_class_cheapest','n/a')} "
            f"| {('%.3f' % float(r['miner_burn'])) if g(r,'miner_burn')!='' else 'n/a'} "
            f"| {g(r,'earners','n/a')} "
            f"| {('%.0f%%' % (float(t1)*100)) if t1 not in (None,'') else 'n/a'} "
            f"| {g(r,'freshness_reason','-')} |"
        )

    below = [r for r in ranked if (r.get("net_margin_usd_day") is not None
                                   and float(r["net_margin_usd_day"]) < 0)]
    L += ["", "## BELOW COST (ranked, but the cheapest satisfying machine costs more than the",
          "competitive miner earns - listed so the information is not destroyed)", ""]
    if not below:
        L += ["_none_", ""]
    else:
        L += ["| netuid | name | net $/day | machine | competitive $/day |", "|---|---|---|---|---|"]
        for r in below[:20]:
            L.append(f"| {r['netuid']} | {g(r,'name')} | {float(r['net_margin_usd_day']):.2f} "
                     f"| {g(r,'machine_class_cheapest')} | {g(r,'competitive_miner_usd_day','n/a')} |")
        L.append("")

    gates: Dict[str, List[int]] = {}
    for r in all_rows:
        gs = r.get("gate_status", "")
        if gs and gs != "OK":
            gates.setdefault(gs, []).append(int(r["netuid"]))
    L += ["## GATED (excluded from the ranking)", ""]
    for gs, nets in sorted(gates.items()):
        L.append(f"- **{gs}** - {len(nets)} subnets: {', '.join('sn%d' % n for n in sorted(nets))}")
    L.append("")

    L += ["## COMPONENT POINTS (for re-weighting without re-deriving)", "",
          "| netuid | income_pts | freshness_pts | resource_pts | registration_pts | confidence |",
          "|---|---|---|---|---|---|"]
    for r in ranked[:top]:
        L.append(f"| {r['netuid']} | {g(r,'income_pts')} | {g(r,'freshness_pts')} "
                 f"| {g(r,'resource_pts')} | {g(r,'registration_pts')} | {g(r,'confidence')} |")
    L.append("")
    _atomic(path, "\n".join(L))


def write_margin(path: str, rows: List[Dict[str, Any]]) -> None:
    cols = ["netuid", "name", "required_vram_gb", "gpu_class_required", "gpu_class_basis",
            "machine_class_cheapest", "machine_vram_gb", "machine_bandwidth_mbps",
            "machine_cost_usd_day", "competitive_miner_usd_day", "net_margin_usd_day",
            "payback_days", "gate_status"]
    out = [cols] + [[_fmt(r.get(c)) for c in cols]
                    for r in sorted(rows, key=lambda x: int(x["netuid"]))]
    tmp = path + ".tmp"
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(tmp, "w", encoding="utf-8", newline="") as fh:
        csv.writer(fh, lineterminator="\n").writerows(out)
    os.replace(tmp, path)


def write_evidence_pack(path: str, row: Dict[str, Any], *, generated_utc: str,
                        block: Optional[int], readme_text: str = "") -> None:
    """One subnet's evidence, small enough to fetch whole.

    SNAPSHOT.csv at ~70 columns can truncate mid-file in a browsing fetch, and a
    plausible partial table is the worst possible failure. A 2 KB pack either
    arrives or does not.
    """
    n = row["netuid"]

    def g(k, dflt="[UNKNOWN]"):
        v = row.get(k)
        return dflt if v in (None, "") else v

    L = [
        f"# sn{n} - {g('name','(unnamed)')} ({g('symbol','')})",
        "",
        f"snapshot_utc: {generated_utc}  |  block: {block}  |  row_status: {g('row_status')}",
        "",
        "## Chain row",
        "",
        f"- miner_burn: **{g('miner_burn')}**"
        + ("  <- 100% burn: miners earn NOTHING here" if _isnum(row.get('miner_burn')) and float(row['miner_burn']) >= 0.99 else ""),
        f"- registration cost: {g('reg_cost_tao')} TAO ({g('reg_cost_usd')} USD), open={g('registration_allowed')}",
        f"- tempo: {g('tempo')}  |  max_uids: {g('max_uids')}  |  active: {g('active_uids')}  |  free: {g('free_uids')}",
        f"- subnet age: {g('subnet_age_days')} days  |  registered at block {g('registered_block')}",
        f"- weights_version: {g('weights_version')}  |  mechanisms: {g('mechanism_count')}",
        "",
        "## Income (miner side)",
        "",
        f"- **competitive_miner_usd_day: {g('competitive_miner_usd_day')}** (uid {g('competitive_miner_uid')}) "
        "<- the only figure quotable as achievable",
        f"- median_miner_usd_day: {g('median_miner_usd_day')}",
        f"- top_miner_usd_day: {g('top_miner_usd_day')} (uid {g('top_miner_uid')}, "
        f"owner={g('top_miner_is_owner')}, validator_permitted={g('top_miner_is_permitted')}) "
        "<- NOT achievable if owner or permitted",
        "",
        "## Incentive structure (display only - never scored)",
        "",
        f"- earners: {g('earners')}  |  gini: {g('gini')}  |  top1_share: {g('top1_share')}  "
        f"|  top10_share: {g('top10_share')}",
        f"- owner_incentive_share: {g('owner_incentive_share')} (independent check on miner_burn; "
        f"disagreement {g('burn_disagreement','n/a')})"
        + ("  <- the two burn measures DISAGREE; the burn picture is shifting, treat both as provisional"
           if _isnum(row.get("burn_disagreement")) and float(row["burn_disagreement"]) > 0.10 else ""),
        "",
        "## Repository",
        "",
        f"- on-chain URL: `{g('github_url_onchain','(none)')}`",
        f"- resolved URL: `{g('github_url_resolved','(none)')}`",
        f"- status: **{g('repo_status')}** {('- ' + str(row.get('repo_status_reason'))) if row.get('repo_status_reason') else ''}",
        f"- README: {g('readme_bytes','0')} bytes, sha {g('readme_sha','(none)')}",
        f"- latest release: {g('latest_release','(none)')} {g('latest_release_utc','')}",
        f"- last commit: {g('last_commit_utc','(unknown)')}",
        f"- scoring-related commit: {g('scoring_commit_title','(none)')} {g('scoring_commit_utc','')}",
        "",
        "## Resources",
        "",
        f"- min_compute.yml present: {g('min_compute_present')}  |  "
        f"unmodified template: {g('min_compute_is_template')}",
        f"- required: {g('gpu_class_required')} (~{g('required_vram_gb')} GB VRAM)  "
        f"|  basis: **{g('gpu_class_basis')}**",
        f"- cheapest satisfying machine: {g('machine_class_cheapest')} at "
        f"{g('machine_cost_usd_day')} USD/day"
        + ("  <- ASSUMED default box; no hardware evidence was found, so the margin "
           "below is indicative only" if str(row.get("machine_assumed")) == "True" else ""),
        f"- net margin: {g('net_margin_usd_day')} USD/day  |  payback on registration: "
        f"{g('payback_days')} days",
        "",
        "## Score",
        "",
        f"- gate: **{g('gate_status')}** {('- ' + str(row.get('gate_reason'))) if row.get('gate_reason') else ''}",
        f"- score: {g('score')} (rank {g('rank','-')}), confidence {g('confidence')} "
        f"{('- ' + str(row.get('confidence_reason'))) if row.get('confidence_reason') else ''}",
        f"- components: income {g('income_pts')} / freshness {g('freshness_pts')} "
        f"/ resource {g('resource_pts')} / registration {g('registration_pts')}",
        f"- freshness basis: {g('freshness_reason','-')}",
        "",
        "## On-chain description",
        "",
        f"> {g('description','(none)')}",
        "",
    ]
    if readme_text:
        excerpt = readme_text[:6000]
        L += ["## README excerpt (evidence for the brief)", "",
              "```markdown", excerpt, "```", ""]
        if len(readme_text) > 6000:
            L.append(f"_(truncated at 6000 of {len(readme_text)} chars - "
                     f"read the full file at {row.get('github_url_resolved','')})_\n")
    _atomic(path, "\n".join(L))


def _isnum(v) -> bool:
    try:
        float(v)
        return True
    except Exception:
        return False
