# sn7 — Allways · challenge brief

`CONFIDENCE: DRAFT — assembled from fetched evidence; regenerate on alarm`

_snapshot 2026-07-28T06:37:33Z b8718699_

---

## ¶1 — Identity

**sn7 "Allways"** (η), 846 days old. Snapshot 2026-07-28T06:37:33Z b8718699.

- on-chain repo: `https://github.com/entrius/allways`
- resolved: `https://github.com/entrius/allways` — **ok**

On-chain description: _universal transaction layer_ [VERIFIED: pack sn7, 2026-07-28]

## ¶2 — INPUT (what the validator hands you)

From README §Overview [VERIFIED: README §Overview]:

> Allways creates a verification layer above independent systems. Assets move natively. Miners complete transactions, validators independently verify the results, and a smart contract enforces outcomes through collateral and slashing.
> 
> Currently live with BTC ↔ TAO. Designed to scale to any verifiable asset.

## ¶3 — BOX TYPE

**WHITE** — the scoring function is in the repo (`neurons/validator.py`) and the README describes no hidden ground truth, future outcome, or judge — so you can compute your own score before submitting.

Reward code found at: `neurons/validator.py` [VERIFIED: repo file probe, 2026-07-28]

## ¶4 — The box (what you actually build)

From README §Architecture [VERIFIED: README §Architecture]:

> - **Miners**: Post exchange rate pairs and collateral, fulfill swap orders
> - **Validators**: Monitor swaps, verify on-chain transactions, vote on outcomes
> - **Smart Contract**: Manages collateral, swap lifecycle, and validator voting
> - **CLI**: User interface for posting pairs, managing collateral, and executing swaps

## ¶5 — OUTPUT (what you return)

**[UNKNOWN]** The README does not describe the artifact a miner returns.

## ¶6 — SCORING

**[UNKNOWN]** The README does not describe how responses are scored.

## ¶7 — RESOURCES

- requirement: **unknown** (~? GB VRAM) — basis: **no evidence**
- `min_compute.yml` present: True, unmodified template: False

- cheapest satisfying machine: **RTX 4090 (24 GB)** — $250.0/mo, 24 GB VRAM, 8 vCPU, 32 GB RAM, 1000 Mbps [margin:7.rtx4090]

> No hardware evidence was found, so a default 24 GB box was assumed. **The margin below is indicative, not a measured requirement.**

## ¶8 — ECONOMICS

- registration: **0.15 TAO** (~$28.1535), open=True
- `miner_burn`: **0.982386**
- achievable income (`competitive_miner_usd_day`): **$20.2345/day** (uid 87)
- machine cost: $8.2192/day
- **net margin: $12.0153/day**, payback on registration 2.34 days

> The headline top miner earns $2,039/day but is owner=True / validator-permitted=True — **not achievable**. The competitive figure above is 101x lower. [VERIFIED: pack sn7, 2026-07-28]

## ¶9 — COMPETITIVE SHAPE

- earners: **9**, gini 0.883015, top-1 share 0.982511, top-10 share 1
- shape: **highly concentrated** — the top miner takes 98% of miner emission

**(display only — not scored)**

## ¶10 — VERDICT

**WATCH** (score 26, rank 67, confidence 0.85 — hardware requirement unknown)

**First step:** margin is positive but thin; re-check after the next sweep.

**Open questions:**
- What hardware does this actually need? No evidence was found.

---

_Assembled from `data/subnets/sn7.md` and the repo README. Every claim is either quoted with a [VERIFIED] tag or marked [UNKNOWN]. Regenerate when this subnet appears in ALARMS.md under NEW SINCE LAST RUN._
