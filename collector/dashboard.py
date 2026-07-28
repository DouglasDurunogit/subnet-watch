"""dashboard.py — the at-a-glance view: DASHBOARD.md + SVG charts.

    python -m collector.dashboard [--data data]

Two audiences, two media, one source:

  * DASHBOARD.md  — hero figure, KPI row, text bars, tables. Renders in ChatGPT,
    in a terminal, and on GitHub. This is what ChatGPT quotes.
  * charts/*.svg  — hand-written SVG. GitHub renders it natively, it stays sharp,
    it carries its own dark-mode styles, and it needs no plotting library. That
    last point is load-bearing: the Action installs only bittensor + requests.

FORM CHOICES (decided before colour, per the data's job):

  * "How many subnets are worth your attention" is ONE number → a hero figure and
    a KPI row, not a chart. A one-bar bar chart of a single value is noise.
  * The burn distribution is the headline finding and it is BIMODAL — subnets sit
    at ~0 or at ~1, almost nothing between. That is an EMPHASIS chart: the dead
    bucket in status-critical, everything else in one blue. Not a categorical
    palette; there is one thing to look at.
  * The top-20 is magnitude, one series → sequential blue, no legend (the title
    names it), values direct-labelled.
  * Viability is stage-to-stage attrition → a funnel of nested bars.

COLOUR: validated with the skill's own validator rather than by eye —
`#2a78d6` (blue) vs `#d03b3b` (critical) passes every gate on the light surface
(CVD ΔE 23.8 protan, normal-vision 31.6, both ≥3:1 contrast). The de-emphasis
grey carries no identity, so it is chrome, not a series.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import sys
from collections import Counter
from typing import Any, Dict, List, Optional

# --- palette (light / dark), from the validated reference instance -----------
LIGHT = {
    "surface": "#fcfcfb", "ink": "#0b0b0b", "ink2": "#52514e", "muted": "#898781",
    "grid": "#e1e0d9", "axis": "#c3c2b7", "accent": "#2a78d6", "critical": "#d03b3b",
    "deemph": "#d8d7d0",
}
DARK = {
    "surface": "#1a1a19", "ink": "#ffffff", "ink2": "#c3c2b7", "muted": "#898781",
    "grid": "#2c2c2a", "axis": "#383835", "accent": "#3987e5", "critical": "#d03b3b",
    "deemph": "#3a3a37",
}

BURN_DEAD = 0.99


def _f(row: Dict[str, Any], key: str) -> Optional[float]:
    v = row.get(key)
    if v in (None, ""):
        return None
    try:
        return float(v)
    except Exception:
        return None


def _esc(s: Any) -> str:
    return (str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            .replace('"', "&quot;"))


# --- SVG scaffolding ---------------------------------------------------------

def _svg_open(w: int, h: int, title: str, subtitle: str = "") -> List[str]:
    """Root element + the theme stylesheet. Dark mode is a selected set of steps
    from the same ramps, not an inversion."""
    css = []
    for sel, p in ((":root", LIGHT),):
        css.append(f"""
    .surface {{ fill: {p['surface']}; }}
    .ink {{ fill: {p['ink']}; }}
    .ink2 {{ fill: {p['ink2']}; }}
    .muted {{ fill: {p['muted']}; }}
    .grid {{ stroke: {p['grid']}; }}
    .axis {{ stroke: {p['axis']}; }}
    .accent {{ fill: {p['accent']}; }}
    .critical {{ fill: {p['critical']}; }}
    .deemph {{ fill: {p['deemph']}; }}""")
    dark = f"""
    @media (prefers-color-scheme: dark) {{
      .surface {{ fill: {DARK['surface']}; }}
      .ink {{ fill: {DARK['ink']}; }}
      .ink2 {{ fill: {DARK['ink2']}; }}
      .muted {{ fill: {DARK['muted']}; }}
      .grid {{ stroke: {DARK['grid']}; }}
      .axis {{ stroke: {DARK['axis']}; }}
      .accent {{ fill: {DARK['accent']}; }}
      .deemph {{ fill: {DARK['deemph']}; }}
    }}"""
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
        f'viewBox="0 0 {w} {h}" role="img" aria-label="{_esc(title)}">',
        "<style>",
        "    text { font-family: system-ui, -apple-system, 'Segoe UI', sans-serif; }",
        "    .t-title { font-size: 15px; font-weight: 600; }",
        "    .t-sub { font-size: 11.5px; }",
        "    .t-lab { font-size: 11px; }",
        "    .t-val { font-size: 11px; font-weight: 600; font-variant-numeric: tabular-nums; }",
        "    .t-tick { font-size: 10.5px; font-variant-numeric: tabular-nums; }",
        "".join(css), dark, "</style>",
        f'<rect class="surface" width="{w}" height="{h}" rx="8"/>',
        f'<text class="ink t-title" x="20" y="28">{_esc(title)}</text>',
    ]
    if subtitle:
        out.append(f'<text class="muted t-sub" x="20" y="46">{_esc(subtitle)}</text>')
    return out


def _write(path: str, lines: List[str]) -> None:
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")
    os.replace(tmp, path)


def _bar(x: float, y: float, w: float, h: float, cls: str, r: float = 4.0) -> str:
    """A bar with rounded ends only on the VALUE end, anchored square to the
    baseline. w may be 0-width, in which case nothing is drawn."""
    if w <= 0.5:
        return ""
    r = min(r, w / 2.0, h / 2.0)
    return (f'<path class="{cls}" d="M{x:.1f},{y:.1f} H{x+w-r:.1f} '
            f'a{r:.1f},{r:.1f} 0 0 1 {r:.1f},{r:.1f} V{y+h-r:.1f} '
            f'a{r:.1f},{r:.1f} 0 0 1 -{r:.1f},{r:.1f} H{x:.1f} Z"/>')


# --- chart 1: burn distribution (emphasis) -----------------------------------

def chart_burn(rows: List[Dict[str, Any]], path: str) -> Dict[str, int]:
    edges = [0.0, 0.001, 0.2, 0.4, 0.6, 0.8, 0.99, 1.0001]
    labels = ["0 (none)", "0–0.2", "0.2–0.4", "0.4–0.6", "0.6–0.8", "0.8–0.99", "≥0.99 dead"]
    counts = [0] * len(labels)
    for r in rows:
        b = _f(r, "miner_burn")
        if b is None:
            continue
        for i in range(len(labels)):
            if edges[i] <= b < edges[i + 1]:
                counts[i] += 1
                break
    W, H = 760, 300
    L, T, BH, GAP = 128, 74, 24, 8
    maxc = max(counts) or 1
    plot_w = W - L - 90
    out = _svg_open(W, H, "Where miner emission actually goes",
                    f"{len(rows)} subnets. The two ends are what matter: "
                    f"{counts[0]} burn nothing, {counts[-1]} burn everything.")
    for i, (lab, c) in enumerate(zip(labels, counts)):
        y = T + i * (BH + GAP)
        dead = (i == len(labels) - 1)
        out.append(f'<text class="ink2 t-lab" x="{L-10}" y="{y+16}" text-anchor="end">{_esc(lab)}</text>')
        w = plot_w * c / maxc
        out.append(_bar(L, y, w, BH, "critical" if dead else "accent"))
        out.append(f'<text class="{"ink" if dead else "ink2"} t-val" x="{L+w+8:.1f}" y="{y+16}">{c}</text>')
    out.append(f'<line class="axis" x1="{L}" y1="{T-6}" x2="{L}" y2="{T+len(labels)*(BH+GAP)-GAP+2}" stroke-width="1"/>')
    out.append(f'<text class="muted t-tick" x="20" y="{H-14}">'
               f'A subnet at ≥0.99 pays miners nothing, whatever its headline income says.</text>')
    out.append("</svg>")
    _write(path, out)
    return dict(zip(labels, counts))


# --- chart 2: top 20 by score ------------------------------------------------

def chart_top(ranked: List[Dict[str, Any]], path: str, n: int = 20) -> None:
    top = ranked[:n]
    W = 760
    T, BH, GAP, L = 74, 20, 7, 168
    H = T + len(top) * (BH + GAP) + 42
    # Reserve enough right-hand room that the score label sitting at the end of a
    # full-width bar cannot run into the right-aligned "$N/day" label.
    plot_w = W - L - 150
    maxs = max((_f(r, "score") or 0) for r in top) or 1
    out = _svg_open(W, H, f"Top {len(top)} subnets by score",
                    "Bar = score. Number at right = net margin per day for a "
                    "non-owner miner, after machine cost.")
    for i, r in enumerate(top):
        y = T + i * (BH + GAP)
        s = _f(r, "score") or 0
        nm = _f(r, "net_margin_usd_day")
        name = f"{r['rank']}. sn{r['netuid']} {str(r.get('name',''))[:13]}"
        out.append(f'<text class="ink2 t-lab" x="{L-10}" y="{y+14}" text-anchor="end">{_esc(name)}</text>')
        w = plot_w * s / maxs
        out.append(_bar(L, y, w, BH, "accent"))
        out.append(f'<text class="ink t-val" x="{L+w+8:.1f}" y="{y+14}">{s:.0f}</text>')
        if nm is not None:
            out.append(f'<text class="muted t-tick" x="{W-20}" y="{y+14}" text-anchor="end">'
                       f'${nm:,.0f}/day</text>')
    out.append(f'<line class="axis" x1="{L}" y1="{T-6}" x2="{L}" y2="{T+len(top)*(BH+GAP)-GAP+2}" stroke-width="1"/>')
    out.append(f'<text class="muted t-tick" x="20" y="{H-14}">'
               f'Income is the best NON-owner, NON-validator miner - not the headline top earner.</text>')
    out.append("</svg>")
    _write(path, out)


# --- chart 3: viability funnel -----------------------------------------------

def chart_funnel(rows: List[Dict[str, Any]], path: str) -> List[tuple]:
    total = len(rows)
    alive = [r for r in rows if (_f(r, "miner_burn") or 0) < BURN_DEAD]
    open_reg = [r for r in alive if str(r.get("registration_allowed")) != "False"]
    profitable = [r for r in open_reg if (_f(r, "net_margin_usd_day") or -1) > 0]
    evidenced = [r for r in profitable if r.get("gpu_class_basis") not in ("no evidence", "", None)]
    stages = [
        ("All subnets", total),
        ("Not 100% burned", len(alive)),
        ("Registration open", len(open_reg)),
        ("Positive margin", len(profitable)),
        ("+ hardware evidence", len(evidenced)),
    ]
    W, H = 760, 268
    L, T, BH, GAP = 176, 74, 26, 10
    plot_w = W - L - 96
    out = _svg_open(W, H, "How many subnets survive each filter",
                    f"Of {total} subnets, {len(evidenced)} clear every gate with "
                    f"hardware evidence to back the margin.")
    for i, (lab, c) in enumerate(stages):
        y = T + i * (BH + GAP)
        out.append(f'<text class="ink2 t-lab" x="{L-10}" y="{y+17}" text-anchor="end">{_esc(lab)}</text>')
        out.append(_bar(L, y, plot_w, BH, "deemph"))
        out.append(_bar(L, y, plot_w * c / max(total, 1), BH, "accent"))
        out.append(f'<text class="ink t-val" x="{L+plot_w+10}" y="{y+17}">{c}</text>')
    out.append(f'<text class="muted t-tick" x="20" y="{H-14}">'
               f'"Positive margin" already nets off the cheapest machine that meets the requirement.</text>')
    out.append("</svg>")
    _write(path, out)
    return stages


# --- the markdown dashboard --------------------------------------------------

def _textbar(v: float, vmax: float, width: int = 28, ch: str = "█") -> str:
    n = 0 if vmax <= 0 else int(round(width * max(0.0, v) / vmax))
    return ch * n


def write_dashboard(path: str, rows: List[Dict[str, Any]], manifest: Dict[str, Any],
                    burn_hist: Dict[str, int], stages: List[tuple],
                    events: List[Dict[str, Any]]) -> None:
    ranked = sorted([r for r in rows if r.get("rank")], key=lambda r: int(r["rank"]))
    alive = [r for r in rows if (_f(r, "miner_burn") or 0) < BURN_DEAD]
    profitable = [r for r in ranked if (_f(r, "net_margin_usd_day") or -1) > 0]
    gen = manifest.get("generated_utc", "?")
    blk = manifest.get("block", "?")

    L = [
        "# Subnet watch — dashboard",
        "",
        f"_snapshot {gen} · block {blk} · run_status **{manifest.get('run_status','?')}**_",
        "",
        "> Numbers here are quotable. Income is always `competitive_miner_usd_day` —",
        "> the best miner that is neither the owner nor validator-permitted.",
        "",
        "## The one number",
        "",
        f"# {len(profitable)} of {len(rows)}",
        "",
        f"subnets are worth looking at: not 100% burned, registration open, and the",
        f"competitive miner out-earns the cheapest machine that meets the requirement.",
        "",
        "| | count | meaning |",
        "|---|---:|---|",
        f"| Total subnets | {len(rows)} | everything on chain |",
        f"| Pays miners at all | {len(alive)} | `miner_burn` < 0.99 |",
        f"| Ranked | {len(ranked)} | passed every gate |",
        f"| **Positive margin** | **{len(profitable)}** | income beats machine cost |",
        f"| New events this window | {manifest.get('events_new', 0)} | see ALARMS.md |",
        "",
        "![viability funnel](charts/funnel.svg)",
        "",
        "## Where miner emission goes",
        "",
        "The distribution is bimodal — subnets either burn nothing or burn everything.",
        "There is very little middle ground, which is why burn is a gate and not a score.",
        "",
        "| miner_burn | subnets | |",
        "|---|---:|---|",
    ]
    hmax = max(burn_hist.values()) if burn_hist else 1
    for lab, c in burn_hist.items():
        L.append(f"| {lab} | {c} | `{_textbar(c, hmax)}` |")
    L += [
        "",
        "![burn distribution](charts/burn.svg)",
        "",
        "## Top 20",
        "",
        "| # | subnet | score | net $/day | machine | burn | earners | top-1 share |",
        "|---:|---|---:|---:|---|---:|---:|---:|",
    ]
    for r in ranked[:20]:
        nm, b, t1 = _f(r, "net_margin_usd_day"), _f(r, "miner_burn"), _f(r, "top1_share")
        asm = "*" if str(r.get("machine_assumed")) == "True" else ""
        L.append(
            f"| {r['rank']} | sn{r['netuid']} {str(r.get('name',''))[:16]} | {r.get('score','')} "
            f"| {('%.2f' % nm) if nm is not None else 'n/a'} "
            f"| {r.get('machine_class_cheapest','n/a')}{asm} "
            f"| {('%.2f' % b) if b is not None else 'n/a'} | {r.get('earners','')} "
            f"| {('%.0f%%' % (t1*100)) if t1 is not None else 'n/a'} |"
        )
    L += [
        "",
        "`*` = machine is an assumed default; no hardware evidence was found for that subnet.",
        "",
        "![top 20 by score](charts/top20.svg)",
        "",
        "## Concentration — reported, never scored",
        "",
        "A low top-1 share means many miners share the emission. A high one means a",
        "single UID takes almost everything, so the headline income is not reachable.",
        "**This is deliberately excluded from the score** — judge the shape yourself.",
        "",
        "| top-1 share | subnets (of those that pay) |",
        "|---|---:|",
    ]
    conc = Counter()
    for r in alive:
        t1 = _f(r, "top1_share")
        if t1 is None:
            continue
        conc["wide (<30%)" if t1 < 0.3 else
             "concentrated (30–60%)" if t1 < 0.6 else
             "dominated (60–90%)" if t1 < 0.9 else "captured (>90%)"] += 1
    for k in ("wide (<30%)", "concentrated (30–60%)", "dominated (60–90%)", "captured (>90%)"):
        L.append(f"| {k} | {conc.get(k, 0)} |")

    L += ["", "## Hardware evidence quality", "",
          "Most subnets do not state a requirement anywhere machine-readable, so their",
          "margin assumes a default box. Treat those as indicative.", "",
          "| basis | subnets |", "|---|---:|"]
    for k, v in Counter(r.get("gpu_class_basis", "?") for r in rows).most_common():
        L.append(f"| {k} | {v} |")

    if events:
        L += ["", "## Recent changes (last 7 days)", "",
              "| when | subnet | class | what |", "|---|---|---|---|"]
        for e in events[:15]:
            L.append(f"| {e.get('first_seen_utc','')[:16]} | sn{e.get('netuid')} "
                     f"| {e.get('class')} | {str(e.get('one_line',''))[:70]} |")

    L += ["", "---", "",
          "_Regenerated every sweep. Charts are SVG and follow the same numbers._", ""]
    _write(path, L)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Build DASHBOARD.md and the SVG charts.")
    ap.add_argument("--data", default="data")
    args = ap.parse_args(argv)

    with open(os.path.join(args.data, "SNAPSHOT.csv"), newline="", encoding="utf-8") as fh:
        rows = [r for r in csv.DictReader(fh) if r.get("netuid")]
    manifest = {}
    mpath = os.path.join(args.data, "MANIFEST.json")
    if os.path.exists(mpath):
        manifest = json.load(open(mpath, encoding="utf-8"))

    events = []
    epath = os.path.join(args.data, "EVENTS.jsonl")
    if os.path.exists(epath):
        for line in open(epath, encoding="utf-8"):
            try:
                rec = json.loads(line)
            except Exception:
                continue
            if not rec.get("seeded"):
                events.append(rec)
        events.sort(key=lambda e: e.get("first_seen_utc", ""), reverse=True)

    ranked = sorted([r for r in rows if r.get("rank")], key=lambda r: int(r["rank"]))
    charts = os.path.join(args.data, "charts")
    burn_hist = chart_burn(rows, os.path.join(charts, "burn.svg"))
    chart_top(ranked, os.path.join(charts, "top20.svg"))
    stages = chart_funnel(rows, os.path.join(charts, "funnel.svg"))
    write_dashboard(os.path.join(args.data, "DASHBOARD.md"), rows, manifest,
                    burn_hist, stages, events)
    print(f"  dashboard: {len(rows)} rows, {len(ranked)} ranked, 3 charts", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
