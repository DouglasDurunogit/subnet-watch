"""margin.py — hardware requirement -> cheapest satisfying machine -> net margin.

The user's requirement 7 is not "does this fit MY box" but "what would it cost to
run this, and does the income beat that". So we map each subnet's requirement to
the cheapest class in data/machines.csv that satisfies it, and report

    net_margin_usd_day = competitive_miner_usd_day - machine_cost_usd_day

using the COMPETITIVE income figure (see econ.py) rather than the headline top
miner, because the headline is owner- or validator-captured on most subnets.

On requirement evidence quality. min_compute.yml is present in only ~31 of 100
live subnet repos and roughly 23 of those are unmodified template copies that
carry the template's own default numbers. Quoting those as a subnet's
requirement would be fabrication wearing a citation. So a template copy is
treated as NO evidence, and the requirement falls through to README keywords,
which is explicitly labelled as a guess. `gpu_class_basis` records which rung
the answer came from so nothing downstream can present a keyword guess as a
measured requirement.
"""

from __future__ import annotations

import csv
import os
import re
from typing import Any, Dict, List, Optional

# Ordered strongest-evidence-first. The label lands in `gpu_class_basis`.
BASIS_MIN_COMPUTE = "min_compute.yml (curated)"
BASIS_README_STATED = "README stated VRAM (explicit)"
BASIS_SUBMISSION = "code-submission (validator runs it)"
BASIS_README = "README keywords (GUESS)"
BASIS_NONE = "no evidence"

# Some subnets do not ask miners to RUN anything. The miner writes code and
# submits it; the validator executes it in its own sandbox. sn15 ORO is the clear
# case: "Miners submit Python agents that define an agent_main() function.
# Validators run each agent in an isolated Docker sandbox." There is no
# persistent miner process, so charging rented-GPU rates against that subnet's
# income is simply the wrong cost model — it was pricing an RTX 4090 at
# $8.22/day against a $10.54/day median and calling the subnet marginal.
#
# Both halves are required. "Miners submit X" alone is far too common, and
# validator-side execution alone does not mean the miner is idle.
_SUBMITS = re.compile(
    r"(miners?\s+(submit|upload|push)|submit\s+(your|an?|the)\s+(agent|model|solution|code)"
    r"|agent_main)", re.I)
_VALIDATOR_EXECUTES = re.compile(
    r"(validators?\s+(run|execute|evaluate)s?[^.]{0,60}(agent|submission|sandbox|container)"
    r"|docker\s+sandbox|isolated\s+sandbox)", re.I)
# ...unless the miner still has to TRAIN the thing before submitting it, which is
# a large GPU bill even though the validator does the serving.
_TRAINS = re.compile(r"\b(train|fine-?tun|checkpoint|pretrain|gradient)\w*", re.I)

# Two orderings, both requiring the word VRAM/GPU explicitly.
#
# The obvious regex is wrong twice over, and both errors were observed on sn26:
#   * `v?ram` also matches bare "RAM", so "16 GB RAM" (system memory) was read
#     as a 16 GB VRAM requirement.
#   * "8+ GB VRAM" did not match at all, because `\s*` cannot cross the "+".
# Between them the pipeline read sn26 as needing 16 GB when its README says 8.
_VRAM_RE = re.compile(
    r"(\d{1,3})\s*\+?\s*(?:gb|gib)\s*(?:of\s+)?(?:v-?ram|gpu(?:\s+memory)?|graphics\s+memory)",
    re.I,
)
# Reversed phrasing ("VRAM: 48 GB"). The separator must NOT cross a comma or
# newline: on sn26 a permissive `\W{0,12}` turned "...8+ GB VRAM, 100+ GB SSD"
# into a claimed 100 GB VRAM requirement by reaching past the comma to the disk
# size. Only spaces, colons and dashes may sit between the word and its number.
_VRAM_RE_REVERSED = re.compile(
    r"(?:v-?ram|gpu\s+memory)[ :=-]{0,4}(\d{1,3})\s*\+?\s*(?:gb|gib)", re.I,
)
_MIN_VRAM_RE = re.compile(r"min_vram\s*:\s*(\d+)", re.I)
_GPU_REQUIRED_RE = re.compile(r"required\s*:\s*(true|false)", re.I)

# Model/hardware names that imply a VRAM floor when stated in a README.
_HINTS: List[tuple] = [
    (re.compile(r"\b(8\s*x\s*h100|8xh100|multi-?gpu|distributed training)\b", re.I), 640),
    (re.compile(r"\b(h200)\b", re.I), 141),
    (re.compile(r"\b(h100|a100\s*80)\b", re.I), 80),
    (re.compile(r"\b(a100|a6000|48\s*gb)\b", re.I), 48),
    (re.compile(r"\b(70b|72b|llama-?3[.-]?\d*-?70)\b", re.I), 80),
    (re.compile(r"\b(30b|32b|34b)\b", re.I), 48),
    (re.compile(r"\b(4090|5090|3090|24\s*gb|13b|14b)\b", re.I), 24),
    (re.compile(r"\b(7b|8b|stable diffusion|sdxl|whisper|yolo|efficientnet|resnet)\b", re.I), 24),
    (re.compile(r"\b(cpu[- ]only|no gpu required|does not require a gpu)\b", re.I), 0),
]


def load_machines(path: str) -> List[Dict[str, Any]]:
    with open(path, newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    for r in rows:
        for k in ("gpu_count", "vram_gb", "vcpu", "ram_gb", "disk_gb", "bandwidth_mbps", "tier"):
            r[k] = int(float(r[k]))
        for k in ("usd_hour", "usd_month"):
            r[k] = float(r[k])
    return sorted(rows, key=lambda r: r["usd_month"])


def infer_requirement(row: Dict[str, Any]) -> Dict[str, Any]:
    """Estimate required VRAM from the best available evidence.

    Returns {required_vram_gb, gpu_class_basis, gpu_class_required}. A None
    requirement means unknown, which must never be silently read as zero.
    """
    # Rung 1: a min_compute.yml that somebody actually edited.
    if row.get("min_compute_present") and not row.get("min_compute_is_template"):
        text = row.get("min_compute_text", "") or ""
        m = _MIN_VRAM_RE.search(text)
        if m:
            vram = int(m.group(1))
            # The template writes min_vram in bytes-ish units in some forks.
            if vram > 1000:
                vram = vram // 1024
            return {"required_vram_gb": vram, "gpu_class_basis": BASIS_MIN_COMPUTE,
                    "gpu_class_required": _label(vram)}
        g = _GPU_REQUIRED_RE.search(text)
        if g and g.group(1).lower() == "false":
            return {"required_vram_gb": 0, "gpu_class_basis": BASIS_MIN_COMPUTE,
                    "gpu_class_required": "cpu-only"}

    full = row.get("readme_text", "") or ""
    readme = _miner_scope(full)
    if readme:
        # Rung 2: an EXPLICIT VRAM figure stated in the README. This must be
        # checked BEFORE model-name keywords. Doing it the other way round was a
        # real bug: sn26's README states "8+ GB VRAM" but the word "efficientnet"
        # matched a 24 GB hint, so the pipeline priced an RTX 4090 and understated
        # the margin. A number the author wrote always beats a number we inferred
        # from a model name they happened to mention.
        #
        # When several are stated, take the smallest: READMEs conventionally give
        # "minimum X, recommended Y", and the entry requirement is what decides
        # whether you can play at all.
        stated = [int(m.group(1)) for m in _VRAM_RE.finditer(readme)]
        stated += [int(m.group(1)) for m in _VRAM_RE_REVERSED.finditer(readme)]
        stated = [v for v in stated if 1 <= v <= 640]
        if stated:
            vram = min(stated)
            return {"required_vram_gb": vram, "gpu_class_basis": BASIS_README_STATED,
                    "gpu_class_required": _label(vram)}

        # Rung 3: the miner submits code and the validator runs it, so the miner
        # needs a development box, not a served GPU. Ranked below an explicit
        # VRAM statement: if a README says miners need 24 GB, believe it — they
        # may well be building the submission locally.
        #
        # Matched against the FULL document, not the miner-scoped text. Who
        # executes the code is a property of the protocol and is usually stated
        # in an architecture section; sn15 ORO says "Miners submit Python agents"
        # under "For Miners" but "Validators run each agent in an isolated Docker
        # sandbox" under "How It Works", so scoping to the miner section alone
        # sees only half the pattern. Sizing stays scoped; architecture does not.
        if (_SUBMITS.search(full) and _VALIDATOR_EXECUTES.search(full)
                and not _TRAINS.search(full)):
            return {"required_vram_gb": 0, "gpu_class_basis": BASIS_SUBMISSION,
                    "gpu_class_required": "cpu-only (dev box)"}

        # Rung 4: model-name keywords. Explicitly a guess.
        #
        # A "CPU-only" phrase sitting alongside any GPU-requiring signal is a
        # CONTRADICTION, not a cheaper answer. Resolving it toward CPU is the
        # expensive direction to be wrong in: it prices a $30/month box and
        # inflates the margin by orders of magnitude. Report no evidence and let
        # the assumed default carry it, with confidence paying the cost.
        hits = [vram for pat, vram in _HINTS if pat.search(readme)]
        if hits:
            contradicted = any(v > 0 for v in hits) or bool(_GPU_PRESENT.search(readme))
            if 0 in hits and contradicted:
                return {"required_vram_gb": None, "gpu_class_basis": BASIS_NONE,
                        "gpu_class_required": "unknown"}
            vram = hits[0]
            return {"required_vram_gb": vram, "gpu_class_basis": BASIS_README,
                    "gpu_class_required": _label(vram)}

    return {"required_vram_gb": None, "gpu_class_basis": BASIS_NONE,
            "gpu_class_required": "unknown"}


# "A GPU is required" signals, used ONLY to detect contradiction — never to size
# the requirement. Deliberately made of tokens that cannot appear inside a
# negation: "no GPU required" contains none of them, while "NVIDIA GPU",
# "nvidia-smi", "CUDA" and "GPU host" all imply real silicon.
#
# This exists because sn106 slipped through the first fix: its README says
# "CPU-only validator host" in a setup snippet and "Miner | GPU host, supported
# NVIDIA GPU, working nvidia-smi" in a table, neither under a heading the scoper
# could drop. No sizing keyword matched, so the CPU phrase won unopposed.
_GPU_PRESENT = re.compile(
    r"(nvidia|cuda|nvidia-smi|vram|\brtx\s*\d|\ba100\b|\bh100\b|\bh200\b|tesla|gpu host)",
    re.I,
)

_HEADING_RE = re.compile(r"^(#{1,6})\s*(.+?)\s*$", re.M)
_MINER_HEAD = re.compile(r"\bminer|mining\b", re.I)
_VALIDATOR_HEAD = re.compile(r"\bvalidator|validating|auditor|gateway\b", re.I)


def _miner_scope(readme: str) -> str:
    """The part of a README that describes what a MINER needs.

    Requirement text must be read in miner context. sn53 is the worked example:
    its README says "engy serves frontier open models on consumer GPUs" for
    miners, and — thirty lines later, inside the validator runbook — "CPU-only;
    no GPU, no database". A whole-document keyword scan read the second sentence,
    concluded miners need no GPU, priced a $30/month CPU box against $2,767/day
    of income and ranked the subnet 8th on a margin that does not exist.

    So: drop sections whose heading is about validators/auditors/gateways. If any
    explicitly miner-headed sections remain, use only those; otherwise use what
    is left of the document.
    """
    if not readme:
        return ""
    marks = list(_HEADING_RE.finditer(readme))
    if not marks:
        return readme

    preamble = readme[: marks[0].start()]
    miner_parts, neutral_parts = [], [preamble]
    for i, m in enumerate(marks):
        end = marks[i + 1].start() if i + 1 < len(marks) else len(readme)
        head, body = m.group(2), readme[m.end():end]
        if _VALIDATOR_HEAD.search(head) and not _MINER_HEAD.search(head):
            continue                      # validator-only section: not our answer
        (miner_parts if _MINER_HEAD.search(head) else neutral_parts).append(body)

    scoped = "\n".join(miner_parts) if miner_parts else "\n".join(neutral_parts)
    return scoped if scoped.strip() else readme


def _label(vram: int) -> str:
    if vram <= 0:
        return "cpu-only"
    if vram <= 24:
        return "24GB consumer"
    if vram <= 48:
        return "48GB"
    if vram <= 80:
        return "80GB datacentre"
    return "multi-GPU"


def cheapest(machines: List[Dict[str, Any]], required_vram_gb: Optional[int]) -> Optional[Dict[str, Any]]:
    """Cheapest class meeting the VRAM floor. None if nothing satisfies it."""
    if required_vram_gb is None:
        return None
    for m in machines:  # already sorted by usd_month
        if m["vram_gb"] >= required_vram_gb:
            return m
    return None


# When hardware evidence is absent (~98 of 128 subnets, because min_compute.yml
# is mostly missing or a template copy and READMEs rarely state a requirement),
# assume the common Bittensor miner box rather than refusing to compute a margin.
#
# Refusing was the first implementation and it was wrong: with no machine there
# is no margin, so income scored zero, and "we could not read the hardware" got
# silently ranked as "this subnet pays nothing". Those are different facts. The
# assumption is recorded in `machine_assumed` and already costs confidence via
# gpu_class_basis, so the uncertainty is expressed once, in the right place.
DEFAULT_ASSUMED_VRAM_GB = 24


def compute(row: Dict[str, Any], machines: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Attach requirement, machine choice and margin columns to one row."""
    out = dict(infer_requirement(row))
    req = out["required_vram_gb"]
    assumed = req is None
    m = cheapest(machines, DEFAULT_ASSUMED_VRAM_GB if assumed else req)
    out["machine_assumed"] = assumed

    if m is None:
        # Only reachable when the requirement IS known and exceeds every class.
        out.update(machine_class_cheapest="", machine_cost_usd_day=None,
                   machine_vram_gb=None, machine_bandwidth_mbps=None,
                   net_margin_usd_day=None, net_margin_top_usd_day=None,
                   payback_days=None)
        return out

    cost_day = m["usd_month"] * 12.0 / 365.0

    def _income(key):
        v = row.get(key)
        return float(v) if v not in (None, "") else None

    # The SCORED margin uses the MEDIAN competitive miner, not the best one.
    # Scoring the ceiling ranked winner-take-all subnets above open ones: sn15
    # ORO's best competitive miner clears $10k/day while its median earner makes
    # $10.20, because one UID holds 93% of emission. The top figure is kept
    # alongside as upside, clearly labelled.
    realistic = _income("competitive_median_usd_day")
    ceiling = _income("competitive_miner_usd_day")

    out.update(
        machine_class_cheapest=m["class_id"],
        machine_cost_usd_day=round(cost_day, 4),
        machine_vram_gb=m["vram_gb"],
        machine_bandwidth_mbps=m["bandwidth_mbps"],
        net_margin_usd_day=(round(realistic - cost_day, 4) if realistic is not None else None),
        net_margin_top_usd_day=(round(ceiling - cost_day, 4) if ceiling is not None else None),
    )

    # Payback on the registration burn, at the current net margin.
    reg_usd = row.get("reg_cost_usd")
    net = out["net_margin_usd_day"]
    if reg_usd not in (None, "") and net is not None and net > 0:
        out["payback_days"] = round(float(reg_usd) / net, 2)
    else:
        out["payback_days"] = None
    return out
