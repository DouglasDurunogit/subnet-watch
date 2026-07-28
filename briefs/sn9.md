# sn9 — iota · challenge brief

`CONFIDENCE: DRAFT — assembled from fetched evidence; regenerate on alarm`

_snapshot 2026-07-28T06:37:33Z b8718699_

---

## ¶1 — Identity

**sn9 "iota"** (ι), 1004 days old. Snapshot 2026-07-28T06:37:33Z b8718699.

- on-chain repo: `https://github.com/macrocosm-os/iota`
- resolved: `https://github.com/macrocosm-os/iota` — **ok**

On-chain description: _The world's first permissionless pipeline parallel training architecture_ [VERIFIED: pack sn9, 2026-07-28]

## ¶2 — INPUT (what the validator hands you)

From README §**Overview** [VERIFIED: README §**Overview**]:

> - The orchestrator distributes model layers across heterogeneous miners and streams activations between them.
> - All network communication is mediated via the orchestrator, and a shared S3 bucket is used to store activations and layer weights.
> - Miners compete to process as many activations as possible in the training stage.
> - Miners periodically upload their local weights and merge their activations using a variant of Butterfly All-Reduce.
> - Validators spot-check miners to ensure that work was performed as required.
> 
> For a more comprehensive overview, please refer to our technical paper [here](https://www.macrocosmos.ai/research/iota_primer.pdf). You can also find the report on [

## ¶3 — BOX TYPE

**UNKNOWN** — reward path not located in the repo (checked `neurons/validator.py`, `validator/reward.py`, `validator/scoring.py`, `reward.py`, `scoring.py`, `validator/forward.py`); per the glossary we do not infer box type from the subnet's description.

None of `neurons/validator.py`, `validator/reward.py`, `validator/scoring.py`, `reward.py`, `scoring.py`, `validator/forward.py` exist in this repo. Roughly half of subnet repos use none of the conventional paths, so this is a gap in evidence, not proof of a black box.

## ¶4 — The box (what you actually build)

**[UNKNOWN]** The README does not describe the computation a miner must perform.

## ¶5 — OUTPUT (what you return)

**[UNKNOWN]** The README does not describe the artifact a miner returns.

## ¶6 — SCORING

**[UNKNOWN]** The README does not describe how responses are scored.

## ¶7 — RESOURCES

- requirement: **24GB consumer** (~24 GB VRAM) — basis: **README keywords (GUESS)**
- `min_compute.yml` present: False, unmodified template: False

- cheapest satisfying machine: **RTX 4090 (24 GB)** — $250.0/mo, 24 GB VRAM, 8 vCPU, 32 GB RAM, 1000 Mbps [margin:9.rtx4090]

## ¶8 — ECONOMICS

- registration: **0.0005 TAO** (~$0.093845), open=True
- `miner_burn`: **0.796693**
- achievable income (`competitive_miner_usd_day`): **$2635.47/day** (uid 21)
- machine cost: $8.2192/day
- **net margin: $2627.25/day**, payback on registration 0 days

> The headline top miner earns $14,999/day but is owner=True / validator-permitted=True — **not achievable**. The competitive figure above is 6x lower. [VERIFIED: pack sn9, 2026-07-28]

## ¶9 — COMPETITIVE SHAPE

- earners: **3**, gini 0.488945, top-1 share 0.796713, top-10 share 1
- shape: **highly concentrated** — the top miner takes 80% of miner emission

**(display only — not scored)**

## ¶10 — VERDICT

**BUILD-CANDIDATE** (score 44.5, rank 14, confidence 0.85 — hardware from README keywords, not curated)

**First step:** locate the scoring code — it is not at any conventional path.

**Open questions:**
- Where is the scoring code? Box type cannot be decided without it.

---

_Assembled from `data/subnets/sn9.md` and the repo README. Every claim is either quoted with a [VERIFIED] tag or marked [UNKNOWN]. Regenerate when this subnet appears in ALARMS.md under NEW SINCE LAST RUN._
