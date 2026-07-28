# sn8 — Vanta · challenge brief

`CONFIDENCE: DRAFT — assembled from fetched evidence; regenerate on alarm`

_snapshot 2026-07-28T06:37:33Z b8718699_

---

## ¶1 — Identity

**sn8 "Vanta"** (θ), 1005.8 days old. Snapshot 2026-07-28T06:37:33Z b8718699.

- on-chain repo: `https://github.com/taoshidev/vanta-network`
- resolved: `https://github.com/taoshidev/vanta-network` — **ok**

On-chain description: _The first decentralized & trustless liquidity and execution engine for prop firms and traders_ [VERIFIED: pack sn8, 2026-07-28]

## ¶2 — INPUT (what the validator hands you)

From README §Miners [VERIFIED: README §Miners]:

> Miners run machine learning models. They send signals to the Validators.

## ¶3 — BOX TYPE

**WHITE** — the scoring function is in the repo (`neurons/validator.py`) and the README describes no hidden ground truth, future outcome, or judge — so you can compute your own score before submitting.

Reward code found at: `neurons/validator.py` [VERIFIED: repo file probe, 2026-07-28]

## ¶4 — The box (what you actually build)

**[UNKNOWN]** The README does not describe the computation a miner must perform.

## ¶5 — OUTPUT (what you return)

**[UNKNOWN]** The README does not describe the artifact a miner returns.

## ¶6 — SCORING

**[UNKNOWN]** The README does not describe how responses are scored.

## ¶7 — RESOURCES

- requirement: **unknown** (~? GB VRAM) — basis: **no evidence**
- `min_compute.yml` present: False, unmodified template: False

- cheapest satisfying machine: **RTX 4090 (24 GB)** — $250.0/mo, 24 GB VRAM, 8 vCPU, 32 GB RAM, 1000 Mbps [margin:8.rtx4090]

> No hardware evidence was found, so a default 24 GB box was assumed. **The margin below is indicative, not a measured requirement.**

## ¶8 — ECONOMICS

- registration: **0.0005 TAO** (~$0.093845), open=True
- `miner_burn`: **0.952861**
- achievable income (`competitive_miner_usd_day`): **$143.751/day** (uid 97)
- machine cost: $8.2192/day
- **net margin: $135.532/day**, payback on registration 0 days

> The headline top miner earns $14,549/day but is owner=True / validator-permitted=True — **not achievable**. The competitive figure above is 101x lower. [VERIFIED: pack sn8, 2026-07-28]

## ¶9 — COMPETITIVE SHAPE

- earners: **31**, gini 0.963378, top-1 share 0.953271, top-10 share 0.999435
- shape: **highly concentrated** — the top miner takes 95% of miner emission

**(display only — not scored)**

## ¶10 — VERDICT

**BUILD-CANDIDATE** (score 34.6, rank 47, confidence 0.85 — hardware requirement unknown)

**First step:** read `neurons/validator.py` and reproduce the score locally.

**Open questions:**
- What hardware does this actually need? No evidence was found.

---

_Assembled from `data/subnets/sn8.md` and the repo README. Every claim is either quoted with a [VERIFIED] tag or marked [UNKNOWN]. Regenerate when this subnet appears in ALARMS.md under NEW SINCE LAST RUN._
