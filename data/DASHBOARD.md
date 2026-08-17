# Subnet watch — dashboard

_snapshot 2026-08-17T15:08:11Z · block 8865211 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 50 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 90 | `miner_burn` < 0.99 |
| Ranked | 90 | passed every gate |
| **Positive margin** | **50** | income beats machine cost |
| New events this window | 0 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 62 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 3 | `█` |
| 0.4–0.6 | 7 | `███` |
| 0.6–0.8 | 5 | `██` |
| 0.8–0.99 | 8 | `████` |
| ≥0.99 dead | 38 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 78.4 | 120 | 33,873 | cpu-small | 20 | 90% |
| 2 | sn76 Phylax | 78.4 | 105 | 202 | cpu-small | 10 | 20% |
| 3 | sn26 Perturb | 72 | 54.87 | 1,617 | rtx3060 | 10 | 70% |
| 4 | sn67 Harnyx | 72 | 20.56 | 385 | cpu-small | 129 | 11% |
| 5 | sn91 cascade | 69.1 | 565 | 2,283 | rtx4090* | 5 | 51% |
| 6 | sn41 Almanac | 68.7 | 9.73 | 53.41 | cpu-small | 75 | 69% |
| 7 | sn62 Ridges | 68.5 | 466 | 2,160 | rtx4090* | 6 | 40% |
| 8 | sn96 Verathos | 68.4 | 22.29 | 530 | rtx4090 | 69 | 41% |
| 9 | sn85 Vidaio | 67.2 | 318 | 552 | rtx4090* | 10 | 17% |
| 10 | sn15 ORO | 67 | 10.89 | 12,410 | cpu-small | 66 | 94% |
| 11 | sn38 ChronoLLM | 66.1 | 101 | 1,382 | cpu-small | 10 | 52% |
| 12 | sn124 Swarm | 65.8 | 222 | 489 | rtx4090* | 24 | 11% |
| 13 | sn2 DSperse | 62.8 | 86.26 | 134 | rtx4090* | 5 | 82% |
| 14 | sn55 NIOME | 61.5 | 58.00 | 506 | rtx4090* | 11 | 30% |
| 15 | sn60 Bitsec.ai | 59 | 372 | 372 = | cpu-small | 3 | 50% |
| 16 | sn74 Gittensor | 58.2 | 23.40 | 207 | rtx4090* | 14 | 63% |
| 17 | sn102 ConnitoAI | 57.6 | 632 | 1,234 | rtx4090* | 7 | 25% |
| 18 | sn51 lium.io | 57.3 | 23.11 | 2,558 | rtx4090* | 56 | 79% |
| 19 | sn61 RedTeam | 57.1 | 15.15 | 411 | rtx4090* | 83 | 10% |
| 20 | sn28 gm | 55.9 | 11.75 | 417 | rtx4090* | 39 | 83% |

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
| wide (<30%) | 25 |
| concentrated (30–60%) | 19 |
| dominated (60–90%) | 19 |
| captured (>90%) | 26 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 104 |
| code-submission (validator runs it) | 10 |
| min_compute.yml (curated) | 8 |
| README keywords (GUESS) | 5 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-08-17T13:03 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: feat: add adaptive miner selection and r |
| 2026-08-17T13:03 | sn114 | SCORING_COMMIT | sn114 commit touches scoring: hotfix(scoring): exclude comp 112 stage  |
| 2026-08-17T11:12 | sn85 | SCORING_COMMIT | sn85 commit touches scoring: treat miner sandbox raised error as miner |
| 2026-08-17T10:46 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-08-17T10:46 | sn85 | SCORING_COMMIT | sn85 commit touches scoring: ensure comp scoring worker can access Mod |
| 2026-08-17T10:46 | sn114 | SCORING_COMMIT | sn114 commit touches scoring: perf(validator): reduce validator write  |
| 2026-08-17T09:54 | sn10 | SCORING_COMMIT | sn10 commit touches scoring: feat(bench): score the full workload trac |
| 2026-08-17T08:59 | sn85 | SCORING_COMMIT | sn85 commit touches scoring: reinvite miners rejected with flag INVITA |
| 2026-08-17T08:07 | sn51 | RELEASE | sn51 released executor-v1.120 |
| 2026-08-17T08:07 | sn75 | SCORING_COMMIT | sn75 commit touches scoring: feat(compute-scoring): root-settable dedi |
| 2026-08-17T06:00 | sn2 | BURN_DROP | sn2 burn fell 1.000 -> 0.823 - miners can earn again |
| 2026-08-17T06:00 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Refresh provider failures during recovery |
| 2026-08-17T01:52 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Bound validator worker startup verificati |
| 2026-08-16T17:31 | sn100 | RELEASE | sn100 released v3.3.24 |
| 2026-08-16T17:03 | sn85 | SCORING_COMMIT | sn85 commit touches scoring: retry inviting rejected miner UIDs in com |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

