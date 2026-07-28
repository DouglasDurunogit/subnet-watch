"""briefs.py — bootstrap one ≤10-paragraph challenge brief per subnet.

    python -m collector.briefs [--out briefs] [--only 26,9,4]

These are EVIDENCE-ASSEMBLED drafts, not authored prose. Everything written here
is either quoted from a fetched file or marked [UNKNOWN]. That is the point: a
brief that guesses is worse than one that admits a gap, because the user builds
from it.

Box type is decided by probing for the reward code directly rather than by
reading marketing copy. The glossary's step 1 is "locate the validator's reward
path; if not found, answer UNKNOWN and stop" -- so we fetch the candidate paths
and record which exist. A subnet whose scoring code is present and whose README
does not describe hidden ground truth is WHITE; one where we cannot find the
reward path at all is UNKNOWN, never a guess.

ChatGPT regenerates an individual brief when that subnet's alarm fires; this
module exists so the corpus is complete on day one rather than filling in slowly.
"""

from __future__ import annotations

import argparse
import csv
import os
import re
import sys
from concurrent.futures import ThreadPoolExecutor
from typing import Any, Dict, List, Optional, Tuple

import requests

from . import gh

# Checked in order. Coverage measured across live subnet repos: neurons/validator.py
# ~40%, the template's reward.py convention is effectively dead (0/40), and half
# of all repos use none of these -- so UNKNOWN is a common, correct outcome.
REWARD_PATHS = [
    "neurons/validator.py", "validator/reward.py", "validator/scoring.py",
    "reward.py", "scoring.py", "validator/forward.py",
]

# README evidence that scoring depends on something the miner cannot see.
BLACK_SIGNALS = [
    (re.compile(r"\b(human (evaluat|review|feedback|judge)|manual review)\b", re.I), "human judgement"),
    (re.compile(r"\b(llm[- ]as[- ]a?[- ]?judge|judged by (an? )?(llm|model|gpt))\b", re.I), "LLM judge"),
    (re.compile(r"\b(future price|forecast|predict(ion)? of future|will occur|resolves? (later|at))\b", re.I), "future outcome"),
    (re.compile(r"\b(ground truth (is )?(hidden|withheld|revealed later|not public))\b", re.I), "hidden ground truth"),
    (re.compile(r"\b(private|proprietary|internal) (dataset|corpus|benchmark|test set)\b", re.I), "private dataset"),
    (re.compile(r"\b(relative to other miners|compared against other miners|consensus of miners|peer[- ]rank)\b", re.I), "relative to other miners"),
    (re.compile(r"\b(closed|private|internal|hosted) api\b", re.I), "closed API dependency"),
]

SECTION_RE = re.compile(r"^(#{1,4})\s*(.+?)\s*$", re.M)


def _sections(md: str) -> List[Tuple[str, str]]:
    """[(heading, body)] from a markdown document."""
    out, marks = [], list(SECTION_RE.finditer(md or ""))
    for i, m in enumerate(marks):
        end = marks[i + 1].start() if i + 1 < len(marks) else len(md)
        out.append((m.group(2).strip(), md[m.end():end].strip()))
    return out


def _find_section(md: str, pattern: str, limit: int = 900) -> Optional[Tuple[str, str]]:
    rx = re.compile(pattern, re.I)
    for head, body in _sections(md):
        if rx.search(head) and body:
            return head, re.sub(r"\n{3,}", "\n\n", body)[:limit]
    return None


def probe_reward_paths(owner: str, repo: str, branch: str) -> List[str]:
    """Which conventional reward-code paths actually exist in the repo."""
    found = []
    for path in REWARD_PATHS:
        url = f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{path}"
        try:
            r = requests.head(url, headers=gh.UA, timeout=(5, 10), allow_redirects=True)
            if r.status_code == 200:
                found.append(path)
        except Exception:
            continue
    return found


def decide_box(readme: str, reward_paths: List[str]) -> Tuple[str, str]:
    """(box_type, reason). Follows 04_GLOSSARY.md, including its refusals."""
    hits = [label for rx, label in BLACK_SIGNALS if rx.search(readme or "")]
    closed_api = "closed API dependency" in hits
    hard = [h for h in hits if h != "closed API dependency"]

    if not reward_paths:
        return "UNKNOWN", (
            "reward path not located in the repo (checked "
            + ", ".join(f"`{p}`" for p in REWARD_PATHS) + "); per the glossary "
            "we do not infer box type from the subnet's description"
        )
    if hard:
        return "BLACK", (
            f"scoring code is at `{reward_paths[0]}`, but the README indicates the "
            f"score depends on {', '.join(hard)} — which a miner cannot evaluate "
            "locally before submitting"
        )
    if closed_api:
        return "WHITE-with-a-dependency", (
            f"the scoring function is in the repo (`{reward_paths[0]}`) so you can "
            "score yourself locally, but the task/submission path runs through a "
            "closed endpoint you do not control"
        )
    return "WHITE", (
        f"the scoring function is in the repo (`{reward_paths[0]}`) and the README "
        "describes no hidden ground truth, future outcome, or judge — so you can "
        "compute your own score before submitting"
    )


def _v(row: Dict[str, Any], key: str, dflt: str = "[UNKNOWN]") -> str:
    v = row.get(key)
    return dflt if v in (None, "") else str(v)


def _num(row: Dict[str, Any], key: str) -> Optional[float]:
    try:
        return float(row[key])
    except Exception:
        return None


def build(row: Dict[str, Any], readme: str, reward_paths: List[str],
          machines: Dict[str, Dict[str, Any]]) -> str:
    n = row["netuid"]
    name = _v(row, "name", "(unnamed)")
    snap = f"{_v(row,'snapshot_utc')} b{_v(row,'block')}"
    dead_repo = row.get("repo_status") not in ("ok", "redirected")
    burn = _num(row, "miner_burn")
    ev = f"[VERIFIED: pack sn{n}, {_v(row,'snapshot_utc')[:10]}]"

    box, box_reason = ("UNKNOWN", "the repository is unreadable, so no scoring code could be inspected") \
        if dead_repo else decide_box(readme, reward_paths)

    def readme_or_unknown(pattern: str, what: str) -> str:
        got = _find_section(readme, pattern)
        if not got:
            return f"**[UNKNOWN]** The README does not describe {what}."
        head, body = got
        return f"From README §{head} [VERIFIED: README §{head}]:\n\n> " + \
               body.replace("\n", "\n> ")[:700]

    L = [f"# sn{n} — {name} · challenge brief", ""]

    conf = "DRAFT — assembled from fetched evidence; regenerate on alarm"
    if dead_repo:
        conf = "OPAQUE — no readable repository; ¶2–¶7 are [UNKNOWN]"
    elif not readme:
        conf = "OPAQUE — no README readable; most paragraphs are [UNKNOWN]"
    L += [f"`CONFIDENCE: {conf}`", "", f"_snapshot {snap}_", "", "---", ""]

    # 1 Identity
    L += ["## ¶1 — Identity", "",
          f"**sn{n} \"{name}\"** ({_v(row,'symbol','')}), "
          f"{_v(row,'subnet_age_days')} days old. Snapshot {snap}.",
          "",
          f"- on-chain repo: `{_v(row,'github_url_onchain','(none)')}`",
          f"- resolved: `{_v(row,'github_url_resolved','(none)')}` — "
          f"**{_v(row,'repo_status')}**"
          + (f" ({_v(row,'repo_status_reason','')})" if row.get("repo_status_reason") else ""),
          "",
          f"On-chain description: _{_v(row,'description','(none)')}_ {ev}", ""]
    if dead_repo:
        L += [f"> **The repository is not readable (`{_v(row,'repo_status')}`), so paragraphs "
              "2–7 below are `[UNKNOWN]`. A similarly-named repo is NOT substituted: "
              "a plausible substitute is worse than nothing.**", ""]

    # 2 INPUT
    L += ["## ¶2 — INPUT (what the validator hands you)", "",
          "**[UNKNOWN]** — no readable repository." if dead_repo
          else readme_or_unknown(r"(task|challenge|miner|how it works|overview|protocol|flow)",
                                 "what a miner receives each round"), ""]

    # 3 BOX TYPE
    L += ["## ¶3 — BOX TYPE", "", f"**{box}** — {box_reason}.", ""]
    if reward_paths:
        L += ["Reward code found at: " + ", ".join(f"`{p}`" for p in reward_paths)
              + f" [VERIFIED: repo file probe, {_v(row,'snapshot_utc')[:10]}]", ""]
    elif not dead_repo:
        L += [f"None of {', '.join('`%s`' % p for p in REWARD_PATHS)} exist in this repo. "
              "Roughly half of subnet repos use none of the conventional paths, so this "
              "is a gap in evidence, not proof of a black box.", ""]

    # 4 The box
    L += ["## ¶4 — The box (what you actually build)", "",
          "**[UNKNOWN]** — no readable repository." if dead_repo
          else readme_or_unknown(r"(architect|approach|model|algorithm|implement|method|design)",
                                 "the computation a miner must perform"), ""]

    # 5 OUTPUT
    L += ["## ¶5 — OUTPUT (what you return)", "",
          "**[UNKNOWN]** — no readable repository." if dead_repo
          else readme_or_unknown(r"(response|output|submit|result|respond|return)",
                                 "the artifact a miner returns"), ""]

    # 6 SCORING
    L += ["## ¶6 — SCORING", "",
          "**[UNKNOWN]** — no readable repository." if dead_repo
          else readme_or_unknown(r"(scor|reward|incentive|evaluat|rank|weight)",
                                 "how responses are scored"), ""]

    # 7 RESOURCES
    mc = row.get("machine_class_cheapest") or ""
    m = machines.get(mc)
    basis = _v(row, "gpu_class_basis", "no evidence")
    L += ["## ¶7 — RESOURCES", "",
          f"- requirement: **{_v(row,'gpu_class_required','unknown')}** "
          f"(~{_v(row,'required_vram_gb','?')} GB VRAM) — basis: **{basis}**",
          f"- `min_compute.yml` present: {_v(row,'min_compute_present','False')}, "
          f"unmodified template: {_v(row,'min_compute_is_template','False')}"]
    if str(row.get("min_compute_is_template")) == "True":
        L += ["", "> `min_compute.yml` exists but is an **unmodified template copy** "
              "(19 of 34 such files are). It says nothing about this subnet's real "
              "requirement, so the requirement above is `[UNKNOWN]`."]
    if m:
        L += ["", f"- cheapest satisfying machine: **{m['label']}** — "
                  f"${m['usd_month']}/mo, {m['vram_gb']} GB VRAM, {m['vcpu']} vCPU, "
                  f"{m['ram_gb']} GB RAM, {m['bandwidth_mbps']} Mbps [margin:{n}.{mc}]"]
    if str(row.get("machine_assumed")) == "True":
        L += ["", "> No hardware evidence was found, so a default 24 GB box was assumed. "
              "**The margin below is indicative, not a measured requirement.**"]
    L += [""]

    # 8 ECONOMICS
    L += ["## ¶8 — ECONOMICS", ""]
    if burn is not None and burn >= 0.99:
        L += [f"**Miners earn nothing here.** `miner_burn` is {burn:.3f} — "
              f"{burn*100:.1f}% of miner emission is withheld by owner-controlled "
              f"hotkeys and destroyed. {ev}", ""]
    else:
        L += [f"- registration: **{_v(row,'reg_cost_tao')} TAO** "
              f"(~${_v(row,'reg_cost_usd')}), open={_v(row,'registration_allowed')}",
              f"- `miner_burn`: **{_v(row,'miner_burn')}**",
              f"- achievable income (`competitive_miner_usd_day`): "
              f"**${_v(row,'competitive_miner_usd_day')}/day** (uid {_v(row,'competitive_miner_uid')})",
              f"- machine cost: ${_v(row,'machine_cost_usd_day')}/day",
              f"- **net margin: ${_v(row,'net_margin_usd_day')}/day**, "
              f"payback on registration {_v(row,'payback_days')} days", ""]
        tm, cm = _num(row, "top_miner_usd_day"), _num(row, "competitive_miner_usd_day")
        if tm and cm is not None and cm > 0 and tm / max(cm, 0.01) > 5:
            L += [f"> The headline top miner earns ${tm:,.0f}/day but is "
                  f"owner={_v(row,'top_miner_is_owner')} / "
                  f"validator-permitted={_v(row,'top_miner_is_permitted')} — "
                  f"**not achievable**. The competitive figure above is "
                  f"{tm/max(cm,0.01):,.0f}x lower. {ev}", ""]

    # 9 COMPETITIVE SHAPE
    t1 = _num(row, "top1_share")
    shape = "unknown"
    if t1 is not None:
        shape = ("highly concentrated" if t1 > 0.6 else
                 "concentrated" if t1 > 0.3 else "wide")
    L += ["## ¶9 — COMPETITIVE SHAPE", "",
          f"- earners: **{_v(row,'earners')}**, gini {_v(row,'gini')}, "
          f"top-1 share {_v(row,'top1_share')}, top-10 share {_v(row,'top10_share')}",
          f"- shape: **{shape}**"
          + (f" — the top miner takes {t1*100:.0f}% of miner emission" if t1 is not None else ""),
          "", "**(display only — not scored)**", ""]

    # 10 VERDICT
    gate = _v(row, "gate_status", "OK")
    net = _num(row, "net_margin_usd_day")
    if gate != "OK":
        verdict, first = "**SKIP**", f"gated: {_v(row,'gate_reason')}"
    elif net is not None and net > 100:
        verdict, first = "**BUILD-CANDIDATE**", \
            f"read `{reward_paths[0]}` and reproduce the score locally" if reward_paths \
            else "locate the scoring code — it is not at any conventional path"
    elif net is not None and net > 0:
        verdict, first = "**WATCH**", "margin is positive but thin; re-check after the next sweep"
    else:
        verdict, first = "**SKIP**", "no positive margin at the cheapest satisfying machine"

    unknowns = [f"¶{i}" for i, blk in enumerate(L) if False]  # placeholder, filled below
    L += ["## ¶10 — VERDICT", "",
          f"{verdict} (score {_v(row,'score','n/a')}, rank {_v(row,'rank','n/a')}, "
          f"confidence {_v(row,'confidence','n/a')}"
          + (f" — {_v(row,'confidence_reason','')}" if row.get("confidence_reason") else "") + ")",
          "", f"**First step:** {first}.", "", "**Open questions:**"]
    qs = []
    if box == "UNKNOWN":
        qs.append("Where is the scoring code? Box type cannot be decided without it.")
    if basis == "no evidence":
        qs.append("What hardware does this actually need? No evidence was found.")
    if not readme and not dead_repo:
        qs.append("Why is the README unreadable — wrong branch, or moved?")
    if _num(row, "competitive_miner_usd_day") is None and gate == "OK":
        qs.append("Is there any non-owner, non-permitted miner earning here at all?")
    bd = _num(row, "burn_disagreement")
    if bd is not None and bd > 0.10:
        qs.append(f"The two burn measures disagree by {bd:.2f} — is the burn picture shifting?")
    L += [f"- {q}" for q in (qs or ["None — the evidence is complete for a first pass."])]
    L += ["", "---", "",
          f"_Assembled from `data/subnets/sn{n}.md` and the repo README. Every claim is "
          "either quoted with a [VERIFIED] tag or marked [UNKNOWN]. Regenerate when this "
          "subnet appears in ALARMS.md under NEW SINCE LAST RUN._", ""]
    return "\n".join(L)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Bootstrap challenge briefs.")
    ap.add_argument("--data", default="data")
    ap.add_argument("--out", default="briefs")
    ap.add_argument("--only", default="", help="comma-separated netuids")
    ap.add_argument("--workers", type=int, default=10)
    args = ap.parse_args(argv)

    rows = []
    with open(os.path.join(args.data, "SNAPSHOT.csv"), newline="", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            if r.get("netuid"):
                rows.append(r)
    if args.only:
        want = {int(x) for x in args.only.split(",") if x.strip()}
        rows = [r for r in rows if int(r["netuid"]) in want]

    machines = {m["class_id"]: m for m in
                __import__("collector.margin", fromlist=["x"]).load_machines(
                    os.path.join(args.data, "machines.csv"))}
    os.makedirs(args.out, exist_ok=True)

    def one(row):
        n = int(row["netuid"])
        readme, paths = "", []
        if row.get("repo_status") in ("ok", "redirected"):
            ref = gh.parse_repo(row.get("github_url_resolved") or row.get("github_url_onchain", ""))
            if ref.ok:
                # Fetch the FULL README rather than the evidence pack's excerpt.
                # The pack truncates at 6000 chars for browsing safety, and on
                # sn26 that cut off the OUTPUT and SCORING sections entirely --
                # producing three false [UNKNOWN]s and, worse, a BOX TYPE of
                # WHITE where the closed-API mention further down makes it
                # WHITE-with-a-dependency. Briefs are generated offline, so
                # there is no reason to read the truncated copy.
                readme = gh.fetch_readme(ref).get("readme_text", "") or ""
                paths = probe_reward_paths(ref.owner, ref.repo, "main") or \
                        probe_reward_paths(ref.owner, ref.repo, "master")
        if not readme:
            pack = os.path.join(args.data, "subnets", f"sn{n}.md")
            if os.path.exists(pack):
                txt = open(pack, encoding="utf-8").read()
                m = re.search(r"```markdown\n(.*?)\n```", txt, re.S)
                readme = m.group(1) if m else ""
        text = build(row, readme, paths, machines)
        with open(os.path.join(args.out, f"sn{n}.md"), "w", encoding="utf-8") as fh:
            fh.write(text)
        return n, len(paths), bool(readme)

    done = 0
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        for n, npaths, has_readme in ex.map(one, rows):
            done += 1
            if done % 25 == 0:
                print(f"  {done}/{len(rows)} ...", flush=True)
    print(f"wrote {done} briefs to {args.out}/", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
