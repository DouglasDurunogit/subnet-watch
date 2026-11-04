# Subnet watch — dashboard

_snapshot 2026-11-04T02:38:11Z · block 9429685 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 63 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 99 | `miner_burn` < 0.99 |
| Ranked | 99 | passed every gate |
| **Positive margin** | **63** | income beats machine cost |
| New events this window | 2 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 66 | `████████████████████████████` |
| 0–0.2 | 9 | `████` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 8 | `███` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 29 | `████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn114 SOMA | 85.1 | 581 | 7,564 | cpu-small | 8 | 65% |
| 2 | sn120 Affine | 74.4 | 2,748 | 2,748 = | rtx4090* | 10 | 10% |
| 3 | sn97 Ingot | 72.4 | 1,509 | 1,509 = | rtx4090* | 5 | 20% |
| 4 | sn103 Terza Inference | 69.3 | 605 | 1,328 | rtx4090* | 5 | 36% |
| 5 | sn1 Apex | 67.8 | 379 | 769 | rtx4090* | 4 | 67% |
| 6 | sn53 engy | 67.5 | 350 | 1,967 | rtx4090 | 29 | 26% |
| 7 | sn67 Harnyx | 67.1 | 6.10 | 78.13 | cpu-small | 153 | 4% |
| 8 | sn56 Gradients | 66.9 | 293 | 4,839 | rtx4090* | 7 | 51% |
| 9 | sn15 ORO | 66.5 | 6.32 | 11,133 | cpu-small | 76 | 95% |
| 10 | sn82 Noah | 66.2 | 382 | 433 | rtx4090* | 64 | 2% |
| 11 | sn107 Minos | 65.9 | 172 | 14,619 | cpu-small | 20 | 80% |
| 12 | sn102 ConnitoAI | 65 | 165 | 1,311 | rtx4090* | 9 | 38% |
| 13 | sn38 ChronoLLM | 63.5 | 53.38 | 476 | cpu-small | 10 | 52% |
| 14 | sn124 Swarm | 62.1 | 77.95 | 1,777 | rtx4090* | 15 | 31% |
| 15 | sn121 sundae_bar | 61.9 | 889 | 889 = | cpu-small | 2 | 60% |
| 16 | sn62 Ridges | 61.5 | 57.77 | 1,372 | rtx4090* | 36 | 25% |
| 17 | sn3 Teutonic | 61.1 | 1,819 | 3,646 | rtx4090* | 7 | 25% |
| 18 | sn117 everyframe.studi | 61.1 | 52.63 | 3,334 | rtx4090* | 15 | 79% |
| 19 | sn111 Claims | 58.4 | 23.67 | 2,383 | rtx4090* | 6 | 90% |
| 20 | sn80 OpenRoboto | 58.3 | 796 | 1,044 | rtx4090* | 12 | 15% |

`=` after the ceiling means it equals the median exactly - either one competitive
miner exists, or they all earn the same. Both columns use identical precision;
if they ever disagree the data is wrong, since a median cannot exceed its own max.

`net $/day (median)` is what a newcomer should expect: the MEDIAN non-owner,
non-permitted miner, minus machine cost. `ceiling $/day` is the BEST competitive
miner - reachable only by beating everyone already there. Where the two diverge
wildly, the subnet is winner-take-all and the ceiling is not a plan.

`*` = machine is an assumed default; no hardware evidence was found for that subnet.

![top 20 by score](charts/top20.svg)

## Concentration — reported, never scored

A low top-1 share means many miners share the emission. A high one means a
single UID takes almost everything, so the headline income is not reachable.
**This is deliberately excluded from the score** — judge the shape yourself.

| top-1 share | subnets (of those that pay) |
|---|---:|
| wide (<30%) | 30 |
| concentrated (30–60%) | 16 |
| dominated (60–90%) | 28 |
| captured (>90%) | 24 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 99 |
| README keywords (GUESS) | 11 |
| min_compute.yml (curated) | 9 |
| code-submission (validator runs it) | 8 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-11-04T02:38 | sn70 | SCORING_COMMIT | sn70 commit touches scoring: Merge pull request #125 from fugal-ai/dia |
| 2026-11-04T02:38 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Accept asserted acquisition-completion an |
| 2026-11-03T22:27 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Merge fix/validator-ledger-startup-prefix |
| 2026-11-03T22:27 | sn28 | RELEASE | sn28 released v0.5.19-dev |
| 2026-11-03T22:27 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-5635 - [P1] Validator: hide an unreac |
| 2026-11-03T22:27 | sn70 | SCORING_COMMIT | sn70 commit touches scoring: fix(validator): keep a proof's JSON numbe |
| 2026-11-03T22:27 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge pull request #988 from leadpoet/fea |
| 2026-11-03T22:27 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Merge PR #503: reuse completed work and p |
| 2026-11-03T22:27 | sn78 | README_TASK_DIFF | sn78 README task/scoring sections changed |
| 2026-11-03T22:27 | sn82 | README_TASK_DIFF | sn82 README task/scoring sections changed |
| 2026-11-03T22:27 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: fix(trainer): carry infra-failed challeng |
| 2026-11-03T22:27 | sn108 | SCORING_COMMIT | sn108 commit touches scoring: Neuron 1.0.1: when the challenge server  |
| 2026-11-03T22:27 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: Separate competition intake from sequent |
| 2026-11-03T22:27 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Kit local scorer: a thin caller of the o |
| 2026-11-03T22:27 | sn126 | BURN_DROP | sn126 burn fell 1.000 -> 0.956 - miners can earn again |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

