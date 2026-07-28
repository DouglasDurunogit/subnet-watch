# sn5 — Hone · challenge brief

`CONFIDENCE: DRAFT — assembled from fetched evidence; regenerate on alarm`

_snapshot 2026-07-28T06:37:33Z b8718699_

---

## ¶1 — Identity

**sn5 "Hone"** (ε), 864.9 days old. Snapshot 2026-07-28T06:37:33Z b8718699.

- on-chain repo: `https://github.com/manifold-inc/hone`
- resolved: `https://github.com/manifold-inc/hone` — **ok**

On-chain description: _Hone training_ [VERIFIED: pack sn5, 2026-07-28]

## ¶2 — INPUT (what the validator hands you)

From README §How It Works [VERIFIED: README §How It Works]:

> 1. **Miners** expose an HTTP endpoint (`/info`) that returns a pointer to their solution repository
> 2. **Validators** fetch miner info, submit jobs to a **Sandbox Runner** (secure GPU execution service)
> 3. The Sandbox Runner clones the miner's repo, builds a Docker image, runs prep (with internet) and inference (isolated), then calculates metrics
> 4. Validators aggregate `exact_match_rate` scores and set on-chain weights using exponential distribution

## ¶3 — BOX TYPE

**WHITE** — the scoring function is in the repo (`validator/scoring.py`) and the README describes no hidden ground truth, future outcome, or judge — so you can compute your own score before submitting.

Reward code found at: `validator/scoring.py` [VERIFIED: repo file probe, 2026-07-28]

## ¶4 — The box (what you actually build)

From README §Architecture [VERIFIED: README §Architecture]:

> ```
> ┌─────────────────────────────────────────────────────────────────────────────┐
> │                              BITTENSOR CHAIN                                │
> │                    (miner registration, weights, stake)                     │
> └─────────────────────────────────────────────────────────────────────────────┘
>                                       │
>                  ┌────────────────────┼────────────────────┐
>                  │                    │                    │
>                  ▼                    ▼                    ▼
>           ┌─────────────┐      ┌─────────────┐      ┌─────────────┐
>           │  VALIDATOR  │      │  VALIDATOR  │      │  VALIDATOR 

## ¶5 — OUTPUT (what you return)

From README §Output Format [VERIFIED: README §Output Format]:

> `/output/results.json`:
> ```json
> {
>   "phase": "inference",
>   "status": "success",
>   "predictions": [
>     {
>       "problem_index": 0,
>       "task_hash": "abc123...",
>       "predicted_output": [[6,5,4],[3,2,1]]
>     }
>   ]
> }
> ```

## ¶6 — SCORING

From README §Scoring Mechanism [VERIFIED: README §Scoring Mechanism]:

> - **Metric**: `exact_match_rate` — percentage of ARC problems solved correctly
> - **Minimum floor**: 20% accuracy required to qualify
> - **Top 5** miners above floor receive rewards
> - **Miner rewards**: Rewards distributed via exponential decay (factor 0.8 per rank)
> - **No qualifiers**: If no miners meet the floor, 100% is burned

## ¶7 — RESOURCES

- requirement: **multi-GPU** (~141 GB VRAM) — basis: **README keywords (GUESS)**
- `min_compute.yml` present: False, unmodified template: False

- cheapest satisfying machine: **H200 (141 GB)** — $2400.0/mo, 141 GB VRAM, 24 vCPU, 256 GB RAM, 5000 Mbps [margin:5.h200-141]

## ¶8 — ECONOMICS

**Miners earn nothing here.** `miner_burn` is 1.000 — 100.0% of miner emission is withheld by owner-controlled hotkeys and destroyed. [VERIFIED: pack sn5, 2026-07-28]

## ¶9 — COMPETITIVE SHAPE

- earners: **1**, gini 0, top-1 share 1, top-10 share 1
- shape: **highly concentrated** — the top miner takes 100% of miner emission

**(display only — not scored)**

## ¶10 — VERDICT

**SKIP** (score n/a, rank n/a, confidence n/a)

**First step:** gated: miner_burn=1.000 - 100.0% of miner emission is withheld by owner-controlled hotkeys, so miners earn nothing here.

**Open questions:**
- None — the evidence is complete for a first pass.

---

_Assembled from `data/subnets/sn5.md` and the repo README. Every claim is either quoted with a [VERIFIED] tag or marked [UNKNOWN]. Regenerate when this subnet appears in ALARMS.md under NEW SINCE LAST RUN._
