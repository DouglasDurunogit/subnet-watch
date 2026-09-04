# Subnet watch — dashboard

_snapshot 2026-09-04T18:31:41Z · block 8995822 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 54 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 92 | `miner_burn` < 0.99 |
| Ranked | 93 | passed every gate |
| **Positive margin** | **54** | income beats machine cost |
| New events this window | 11 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 58 | `████████████████████████████` |
| 0–0.2 | 12 | `██████` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 7 | `███` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 36 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn92 MicroTensor | 80.2 | 166 | 369 | cpu-small | 9 | 26% |
| 2 | sn107 Minos | 76.8 | 86.80 | 5,265 | cpu-small | 21 | 81% |
| 3 | sn3 Teutonic | 75.4 | 3,741 | 3,741 = | rtx4090* | 5 | 20% |
| 4 | sn76 Phylax | 73 | 27.56 | 73.07 | cpu-small | 21 | 20% |
| 5 | sn102 ConnitoAI | 71.6 | 1,178 | 1,376 | rtx4090* | 6 | 26% |
| 6 | sn67 Harnyx | 71.3 | 17.18 | 90.05 | cpu-small | 144 | 17% |
| 7 | sn91 cascade | 70.3 | 804 | 3,242 | rtx4090* | 5 | 52% |
| 8 | sn15 ORO | 70.1 | 20.60 | 43.57 | cpu-small | 59 | 94% |
| 9 | sn96 Verathos | 69 | 25.92 | 162 | rtx4090 | 82 | 41% |
| 10 | sn56 Gradients | 68.9 | 526 | 1,310 | rtx4090* | 5 | 75% |
| 11 | sn124 Swarm | 66.3 | 260 | 804 | rtx4090* | 25 | 11% |
| 12 | sn80 OpenRoboto | 65.3 | 180 | 650 | rtx4090* | 5 | 71% |
| 13 | sn111 Claims | 65.1 | 191 | 3,399 | rtx4090* | 5 | 82% |
| 14 | sn79 MVTRX | 64.6 | 4.60 | 398 | cpu-small | 225 | 9% |
| 15 | sn74 Gittensor | 61.2 | 56.31 | 367 | rtx4090 | 11 | 64% |
| 16 | sn41 Almanac | 59.7 | 32.59 | 94.62 | cpu-small | 88 | 9% |
| 17 | sn28 SayGM | 59.4 | 32.27 | 8,298 | rtx4090* | 46 | 58% |
| 18 | sn51 lium.io | 58.9 | 34.84 | 2,029 | rtx4090* | 64 | 73% |
| 19 | sn65 True Performance | 57.5 | 25.12 | 58.45 | rtx4090* | 6 | 91% |
| 20 | sn14 Cacheon | 56.5 | 465 | 3,588 | rtx4090* | 7 | 57% |

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
| wide (<30%) | 28 |
| concentrated (30–60%) | 19 |
| dominated (60–90%) | 18 |
| captured (>90%) | 24 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 98 |
| code-submission (validator runs it) | 11 |
| min_compute.yml (curated) | 11 |
| README keywords (GUESS) | 7 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-09-04T18:32 | sn7 | RELEASE | sn7 released release-20260904-155448: Add min_from_amount and candidat |
| 2026-09-04T18:32 | sn7 | SCORING_COMMIT | sn7 commit touches scoring: CLI: --send verifies source-address contro |
| 2026-09-04T18:32 | sn7 | README_TASK_DIFF | sn7 README task/scoring sections changed |
| 2026-09-04T18:32 | sn25 | RELEASE | sn25 released v2026.9.4-1037416540 |
| 2026-09-04T18:32 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Install FFmpeg for macOS miner tests |
| 2026-09-04T18:32 | sn96 | RELEASE | sn96 released Verathos v0.2.0 – Sleipnir: Verifiable Multi-Node Model  |
| 2026-09-04T18:32 | sn96 | SCORING_COMMIT | sn96 commit touches scoring: fix: qualify mesh scoring on protocol v3 |
| 2026-09-04T18:32 | sn96 | README_TASK_DIFF | sn96 README task/scoring sections changed |
| 2026-09-04T18:32 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: docs(miner): Proof + Bounty A→Z at 2000/ |
| 2026-09-04T18:32 | sn102 | RELEASE | sn102 released v0.5.5 — publish the round podium to a HuggingFace arch |
| 2026-09-04T18:32 | sn102 | SCORING_COMMIT | sn102 commit touches scoring: 🏷️ refactor(validator): name podium fold |
| 2026-09-04T15:09 | sn3 | SCORING_COMMIT | sn3 commit touches scoring: Show model digests for queued and active e |
| 2026-09-04T15:09 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: fix(validator): reference loop uses bt.Wa |
| 2026-09-04T15:09 | sn25 | RELEASE | sn25 released v2026.9.4-1037327320 |
| 2026-09-04T15:09 | sn47 | SCORING_COMMIT | sn47 commit touches scoring: new datasets list and verifier |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

