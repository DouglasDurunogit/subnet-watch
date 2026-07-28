# sn4 — Targon · challenge brief

`CONFIDENCE: DRAFT — assembled from fetched evidence; regenerate on alarm`

_snapshot 2026-07-28T06:37:33Z b8718699_

---

## ¶1 — Identity

**sn4 "Targon"** (δ), 1014.9 days old. Snapshot 2026-07-28T06:37:33Z b8718699.

- on-chain repo: `https://github.com/manifold-inc/targon`
- resolved: `https://github.com/manifold-inc/targon` — **ok**

On-chain description: _Incentivized Compute Marketplace powered by the Targon Virtual Machine (TVM)._ [VERIFIED: pack sn4, 2026-07-28]

## ¶2 — INPUT (what the validator hands you)

**[UNKNOWN]** The README does not describe what a miner receives each round.

## ¶3 — BOX TYPE

**UNKNOWN** — reward path not located in the repo (checked `neurons/validator.py`, `validator/reward.py`, `validator/scoring.py`, `reward.py`, `scoring.py`, `validator/forward.py`); per the glossary we do not infer box type from the subnet's description.

None of `neurons/validator.py`, `validator/reward.py`, `validator/scoring.py`, `reward.py`, `scoring.py`, `validator/forward.py` exist in this repo. Roughly half of subnet repos use none of the conventional paths, so this is a gap in evidence, not proof of a black box.

## ¶4 — The box (what you actually build)

From README §Current Implementation [VERIFIED: README §Current Implementation]:

> - NVIDIA Confidential Compute integration OR
> - NVIDIA PPCIE
> - Hardware-level security guarantees
> - Protected inference execution
> - Remote attestation capabilities
> - Secure memory encryption
> - Isolated compute resources

## ¶5 — OUTPUT (what you return)

**[UNKNOWN]** The README does not describe the artifact a miner returns.

## ¶6 — SCORING

**[UNKNOWN]** The README does not describe how responses are scored.

## ¶7 — RESOURCES

- requirement: **unknown** (~? GB VRAM) — basis: **no evidence**
- `min_compute.yml` present: False, unmodified template: False

- cheapest satisfying machine: **RTX 4090 (24 GB)** — $250.0/mo, 24 GB VRAM, 8 vCPU, 32 GB RAM, 1000 Mbps [margin:4.rtx4090]

> No hardware evidence was found, so a default 24 GB box was assumed. **The margin below is indicative, not a measured requirement.**

## ¶8 — ECONOMICS

- registration: **0.0005 TAO** (~$0.093845), open=True
- `miner_burn`: **0**
- achievable income (`competitive_miner_usd_day`): **$7154.93/day** (uid 7)
- machine cost: $8.2192/day
- **net margin: $7146.71/day**, payback on registration 0 days

## ¶9 — COMPETITIVE SHAPE

- earners: **8**, gini 0.430275, top-1 share 0.301888, top-10 share 1
- shape: **concentrated** — the top miner takes 30% of miner emission

**(display only — not scored)**

## ¶10 — VERDICT

**BUILD-CANDIDATE** (score 47.9, rank 5, confidence 0.85 — hardware requirement unknown)

**First step:** locate the scoring code — it is not at any conventional path.

**Open questions:**
- Where is the scoring code? Box type cannot be decided without it.
- What hardware does this actually need? No evidence was found.

---

_Assembled from `data/subnets/sn4.md` and the repo README. Every claim is either quoted with a [VERIFIED] tag or marked [UNKNOWN]. Regenerate when this subnet appears in ALARMS.md under NEW SINCE LAST RUN._
