# sn2 — DSperse · challenge brief

`CONFIDENCE: DRAFT — assembled from fetched evidence; regenerate on alarm`

_snapshot 2026-07-28T06:37:33Z b8718699_

---

## ¶1 — Identity

**sn2 "DSperse"** (β), 831.2 days old. Snapshot 2026-07-28T06:37:33Z b8718699.

- on-chain repo: `https://github.com/inference-labs-inc/subnet-2`
- resolved: `https://github.com/inference-labs-inc/subnet-2` — **ok**

On-chain description: _Verifiable and distributed inference on Bittensor_ [VERIFIED: pack sn2, 2026-07-28]

## ¶2 — INPUT (what the validator hands you)

From README §Miners [VERIFIED: README §Miners]:

> - Receive input data from validators on the subnet
> - Generate predictions using custom, verifiable AI models that have been converted into zero-knowledge circuits
> - Return the generated content to the requesting validator for validation and distribution

## ¶3 — BOX TYPE

**UNKNOWN** — reward path not located in the repo (checked `neurons/validator.py`, `validator/reward.py`, `validator/scoring.py`, `reward.py`, `scoring.py`, `validator/forward.py`); per the glossary we do not infer box type from the subnet's description.

None of `neurons/validator.py`, `validator/reward.py`, `validator/scoring.py`, `reward.py`, `scoring.py`, `validator/forward.py` exist in this repo. Roughly half of subnet repos use none of the conventional paths, so this is a gap in evidence, not proof of a black box.

## ¶4 — The box (what you actually build)

From README §Architecture [VERIFIED: README §Architecture]:

> The codebase is organized as a Rust workspace with the following crates:
> 
> | Crate | Purpose |
> |-------|---------|
> | `sn2-types` | Shared types, constants, and protocol definitions |
> | `sn2-chain` | Wallet, metagraph, registration, weights, and auto-update |
> | `sn2-verify` | Proof verification via the [Expander](https://github.com/inference-labs-inc/Expander) backend |
> | `sn2-validator` | Validator binary |
> | `sn2-miner` | Miner binary |
> 
> Both binaries communicate with miners/validators over HTTP (axum) and QUIC ([btlightning](https://github.com/inference-labs-inc/lightning)). Chain interactions use [subxt](https://github.com/paritytech/subxt) for direct Substrate RPC.
> 


## ¶5 — OUTPUT (what you return)

**[UNKNOWN]** The README does not describe the artifact a miner returns.

## ¶6 — SCORING

From README §Incentive Mechanism and Reward Structure [VERIFIED: README §Incentive Mechanism and Reward Structure]:

> Subnet 2 incentivizes miners and validators to contribute to the generation and validation of high-quality, secure, and efficient verified AI predictions using a specialized reward mechanism aligned with the unique aspects of zero-knowledge machine learning (zk-ML) and decentralized AI. Zero-knowledge proofs are generally more CPU computationally intensive and open the opportunity for non-GPU miners to participate, however the end goal is to further incentivize the development of proving systems optimized for GPU-based operations. The incentives are based around miners creating succinct and efficient models which can be circuitized with a zero-knowledge proving system.
> 
> The reward mechan

## ¶7 — RESOURCES

- requirement: **unknown** (~? GB VRAM) — basis: **no evidence**
- `min_compute.yml` present: False, unmodified template: False

- cheapest satisfying machine: **RTX 4090 (24 GB)** — $250.0/mo, 24 GB VRAM, 8 vCPU, 32 GB RAM, 1000 Mbps [margin:2.rtx4090]

> No hardware evidence was found, so a default 24 GB box was assumed. **The margin below is indicative, not a measured requirement.**

## ¶8 — ECONOMICS

- registration: **0.0005 TAO** (~$0.093845), open=True
- `miner_burn`: **0.830967**
- achievable income (`competitive_miner_usd_day`): **$129.711/day** (uid 15)
- machine cost: $8.2192/day
- **net margin: $121.491/day**, payback on registration 0 days

> The headline top miner earns $2,224/day but is owner=True / validator-permitted=True — **not achievable**. The competitive figure above is 17x lower. [VERIFIED: pack sn2, 2026-07-28]

## ¶9 — COMPETITIVE SHAPE

- earners: **10**, gini 0.813274, top-1 share 0.831049, top-10 share 1
- shape: **highly concentrated** — the top miner takes 83% of miner emission

**(display only — not scored)**

## ¶10 — VERDICT

**BUILD-CANDIDATE** (score 34.2, rank 49, confidence 0.85 — hardware requirement unknown)

**First step:** locate the scoring code — it is not at any conventional path.

**Open questions:**
- Where is the scoring code? Box type cannot be decided without it.
- What hardware does this actually need? No evidence was found.

---

_Assembled from `data/subnets/sn2.md` and the repo README. Every claim is either quoted with a [VERIFIED] tag or marked [UNKNOWN]. Regenerate when this subnet appears in ALARMS.md under NEW SINCE LAST RUN._
