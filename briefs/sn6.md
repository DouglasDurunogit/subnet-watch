# sn6 — Numinous · challenge brief

`CONFIDENCE: DRAFT — assembled from fetched evidence; regenerate on alarm`

_snapshot 2026-07-28T06:37:33Z b8718699_

---

## ¶1 — Identity

**sn6 "Numinous"** (ζ), 763.7 days old. Snapshot 2026-07-28T06:37:33Z b8718699.

- on-chain repo: `https://github.com/numinouslabs/numinous`
- resolved: `https://github.com/numinouslabs/numinous` — **ok**

On-chain description: _Numinous is a forecasting protocol whose goal is to aggregate agents into superhuman LLM forecasters._ [VERIFIED: pack sn6, 2026-07-28]

## ¶2 — INPUT (what the validator hands you)

From README §For Miners [VERIFIED: README §For Miners]:

> Develop and deploy forecasting agents that compete for the daily reward pool.
> 
>   * [**Miner Setup Guide**](docs/miner-setup.md) – Installation, wallet registration, and deployment.
>   * [**Gateway Guide**](docs/gateway-guide.md) – How to use the Desearch and Chutes APIs.

## ¶3 — BOX TYPE

**BLACK** — scoring code is at `neurons/validator.py`, but the README indicates the score depends on future outcome — which a miner cannot evaluate locally before submitting.

Reward code found at: `neurons/validator.py` [VERIFIED: repo file probe, 2026-07-28]

## ¶4 — The box (what you actually build)

From README §🏗 System Architecture [VERIFIED: README §🏗 System Architecture]:

> The Numinous subnet operates on a strictly defined lifecycle: **Code Submission $\to$ Sandbox Execution $\to$ Resolution $\to$ Weight Setting.**
> 
> Validators spin up parallel sandboxes where miners are evaluated on batches of events. Agents operate inside Docker containers with a secure proxy gateway to access external tools.

## ¶5 — OUTPUT (what you return)

**[UNKNOWN]** The README does not describe the artifact a miner returns.

## ¶6 — SCORING

From README §⚠️ Rules & Scoring [VERIFIED: README §⚠️ Rules & Scoring]:

> To survive in the Numinous arena, agents must adhere to strict constraints. Violating these constraints results in execution failure (or less consistency across validators in case of the caching).

## ¶7 — RESOURCES

- requirement: **unknown** (~? GB VRAM) — basis: **no evidence**
- `min_compute.yml` present: False, unmodified template: False

- cheapest satisfying machine: **RTX 4090 (24 GB)** — $250.0/mo, 24 GB VRAM, 8 vCPU, 32 GB RAM, 1000 Mbps [margin:6.rtx4090]

> No hardware evidence was found, so a default 24 GB box was assumed. **The margin below is indicative, not a measured requirement.**

## ¶8 — ECONOMICS

- registration: **0.2 TAO** (~$37.538), open=True
- `miner_burn`: **0**
- achievable income (`competitive_miner_usd_day`): **$202.853/day** (uid 253)
- machine cost: $8.2192/day
- **net margin: $194.634/day**, payback on registration 0.19 days

## ¶9 — COMPETITIVE SHAPE

- earners: **223**, gini 0.954701, top-1 share 0.169448, top-10 share 0.894171
- shape: **wide** — the top miner takes 17% of miner emission

**(display only — not scored)**

## ¶10 — VERDICT

**BUILD-CANDIDATE** (score 35.7, rank 41, confidence 0.85 — hardware requirement unknown)

**First step:** read `neurons/validator.py` and reproduce the score locally.

**Open questions:**
- What hardware does this actually need? No evidence was found.

---

_Assembled from `data/subnets/sn6.md` and the repo README. Every claim is either quoted with a [VERIFIED] tag or marked [UNKNOWN]. Regenerate when this subnet appears in ALARMS.md under NEW SINCE LAST RUN._
