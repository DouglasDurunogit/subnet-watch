# Subnet watch — dashboard

_snapshot 2026-11-04T09:56:10Z · block 9431875 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 64 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 100 | `miner_burn` < 0.99 |
| Ranked | 100 | passed every gate |
| **Positive margin** | **64** | income beats machine cost |
| New events this window | 13 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 66 | `████████████████████████████` |
| 0–0.2 | 10 | `████` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 7 | `███` |
| 0.6–0.8 | 8 | `███` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 28 | `████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn120 Affine | 74.5 | 2,863 | 2,863 = | rtx4090* | 10 | 10% |
| 2 | sn97 Ingot | 72.5 | 1,566 | 1,566 = | rtx4090* | 5 | 20% |
| 3 | sn34 Yugos | 70.3 | 814 | 6,980 | rtx4090* | 3 | 85% |
| 4 | sn103 Terza Inference | 68.5 | 468 | 1,230 | rtx4090* | 5 | 38% |
| 5 | sn1 Apex | 67.8 | 379 | 773 | rtx4090* | 4 | 68% |
| 6 | sn53 engy | 67.3 | 328 | 1,916 | rtx4090 | 29 | 26% |
| 7 | sn56 Gradients | 67 | 305 | 5,029 | rtx4090* | 7 | 51% |
| 8 | sn15 ORO | 66.7 | 6.96 | 11,542 | cpu-small | 75 | 95% |
| 9 | sn82 Noah | 66.4 | 395 | 450 | rtx4090* | 64 | 2% |
| 10 | sn107 Minos | 66.1 | 179 | 15,203 | cpu-small | 20 | 80% |
| 11 | sn102 ConnitoAI | 65.1 | 173 | 1,272 | rtx4090* | 10 | 35% |
| 12 | sn67 Harnyx | 65 | 3.90 | 472 | cpu-small | 130 | 25% |
| 13 | sn38 ChronoLLM | 63.6 | 54.77 | 488 | cpu-small | 10 | 52% |
| 14 | sn124 Swarm | 62.2 | 81.41 | 1,848 | rtx4090* | 15 | 31% |
| 15 | sn121 sundae_bar | 62 | 923 | 923 = | cpu-small | 2 | 60% |
| 16 | sn62 Ridges | 61.6 | 60.31 | 1,424 | rtx4090* | 36 | 25% |
| 17 | sn3 Teutonic | 61.2 | 1,884 | 1,884 = | rtx4090* | 7 | 25% |
| 18 | sn55 NIOME | 61.1 | 51.15 | 437 | rtx4090* | 11 | 30% |
| 19 | sn117 everyframe.studi | 60.8 | 47.34 | 3,432 | rtx4090* | 18 | 78% |
| 20 | sn60 Bitsec.ai | 57.3 | 227 | 227 = | cpu-small | 3 | 50% |

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
| concentrated (30–60%) | 18 |
| dominated (60–90%) | 28 |
| captured (>90%) | 23 |

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
| 2026-11-04T09:56 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Merge fix/validator-tunnel-tls-timeout: a |
| 2026-11-04T09:56 | sn28 | RELEASE | sn28 released v0.5.19 |
| 2026-11-04T09:56 | sn37 | README_TASK_DIFF | sn37 README task/scoring sections changed |
| 2026-11-04T09:56 | sn51 | RELEASE | sn51 released executor-v1.168 |
| 2026-11-04T09:56 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-5682 - [P0] Validator: port check can |
| 2026-11-04T09:56 | sn51 | README_TASK_DIFF | sn51 README task/scoring sections changed |
| 2026-11-04T09:56 | sn55 | SCORING_COMMIT | sn55 commit touches scoring: update validation block number |
| 2026-11-04T09:56 | sn70 | BURN_DROP | sn70 burn fell 1.000 -> 0.101 - miners can earn again |
| 2026-11-04T09:56 | sn70 | SCORING_COMMIT | sn70 commit touches scoring: Merge pull request #126 from fugal-ai/doc |
| 2026-11-04T09:56 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Reuse validated scoring source within one |
| 2026-11-04T09:56 | sn89 | SCORING_COMMIT | sn89 commit touches scoring: Agent competition v2: receipts, anchoring |
| 2026-11-04T09:56 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: fix(funded): small our-side losses rerun  |
| 2026-11-04T09:56 | sn108 | SCORING_COMMIT | sn108 commit touches scoring: Validator hardware requirements (minimum |
| 2026-11-04T02:38 | sn70 | SCORING_COMMIT | sn70 commit touches scoring: Merge pull request #125 from fugal-ai/dia |
| 2026-11-04T02:38 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Accept asserted acquisition-completion an |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

