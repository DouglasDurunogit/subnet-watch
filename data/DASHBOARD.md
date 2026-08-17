# Subnet watch — dashboard

_snapshot 2026-08-17T19:36:18Z · block 8866551 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 51 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 91 | `miner_burn` < 0.99 |
| Ranked | 91 | passed every gate |
| **Positive margin** | **51** | income beats machine cost |
| New events this window | 3 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 62 | `████████████████████████████` |
| 0–0.2 | 3 | `█` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 7 | `███` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 37 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 78.4 | 105 | 204 | cpu-small | 10 | 20% |
| 2 | sn121 sundae_bar | 74.3 | 1,042 | 1,042 = | cpu-small | 2 | 61% |
| 3 | sn26 Perturb | 72 | 54.69 | 1,611 | rtx3060 | 10 | 70% |
| 4 | sn67 Harnyx | 71.9 | 20.22 | 379 | cpu-small | 129 | 11% |
| 5 | sn91 cascade | 68.8 | 522 | 2,111 | rtx4090* | 5 | 51% |
| 6 | sn41 Almanac | 68.7 | 9.79 | 53.86 | cpu-small | 75 | 69% |
| 7 | sn62 Ridges | 68.4 | 463 | 2,145 | rtx4090* | 6 | 40% |
| 8 | sn15 ORO | 68.1 | 10.77 | 20.92 | cpu-small | 66 | 94% |
| 9 | sn21 AdTAO | 67.7 | 7.73 | 34.61 | cpu-small | 88 | 45% |
| 10 | sn96 Verathos | 67.4 | 17.71 | 492 | rtx4090 | 69 | 41% |
| 11 | sn38 ChronoLLM | 66.3 | 107 | 1,461 | cpu-small | 10 | 52% |
| 12 | sn124 Swarm | 65.8 | 222 | 489 | rtx4090* | 24 | 11% |
| 13 | sn85 Vidaio | 64.6 | 146 | 523 | rtx4090* | 10 | 17% |
| 14 | sn107 Minos | 64.2 | 115 | 34,178 | cpu-small | 20 | 90% |
| 15 | sn2 DSperse | 62.9 | 88.94 | 126 | rtx4090* | 5 | 82% |
| 16 | sn55 NIOME | 61.7 | 60.89 | 499 | rtx4090* | 11 | 29% |
| 17 | sn60 Bitsec.ai | 59 | 373 | 373 = | cpu-small | 3 | 50% |
| 18 | sn102 ConnitoAI | 58.9 | 944 | 1,810 | rtx4090* | 5 | 35% |
| 19 | sn74 Gittensor | 57.9 | 21.78 | 206 | rtx4090* | 14 | 64% |
| 20 | sn61 RedTeam | 57.6 | 17.72 | 355 | rtx4090* | 83 | 8% |

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
| captured (>90%) | 27 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 102 |
| code-submission (validator runs it) | 10 |
| min_compute.yml (curated) | 9 |
| README keywords (GUESS) | 6 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-08-17T19:36 | sn51 | RELEASE | sn51 released executor-v1.121 |
| 2026-08-17T19:36 | sn65 | SCORING_COMMIT | sn65 commit touches scoring: Merge pull request #3 from taofu-labs/val |
| 2026-08-17T18:54 | sn21 | RELEASE | sn21 released SN21 training bundle (1977 records, refreshed 2026-08-17 |
| 2026-08-17T17:55 | sn123 | README_TASK_DIFF | sn123 README task/scoring sections changed |
| 2026-08-17T16:41 | sn10 | SCORING_COMMIT | sn10 commit touches scoring: feat: better miner commit patch logs (#83 |
| 2026-08-17T15:52 | sn121 | BURN_DROP | sn121 burn fell 1.000 -> 0.620 - miners can earn again |
| 2026-08-17T13:03 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: feat: add adaptive miner selection and r |
| 2026-08-17T13:03 | sn114 | SCORING_COMMIT | sn114 commit touches scoring: hotfix(scoring): exclude comp 112 stage  |
| 2026-08-17T11:12 | sn85 | SCORING_COMMIT | sn85 commit touches scoring: treat miner sandbox raised error as miner |
| 2026-08-17T10:46 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-08-17T10:46 | sn85 | SCORING_COMMIT | sn85 commit touches scoring: ensure comp scoring worker can access Mod |
| 2026-08-17T10:46 | sn114 | SCORING_COMMIT | sn114 commit touches scoring: perf(validator): reduce validator write  |
| 2026-08-17T09:54 | sn10 | SCORING_COMMIT | sn10 commit touches scoring: feat(bench): score the full workload trac |
| 2026-08-17T08:59 | sn85 | SCORING_COMMIT | sn85 commit touches scoring: reinvite miners rejected with flag INVITA |
| 2026-08-17T08:07 | sn51 | RELEASE | sn51 released executor-v1.120 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

