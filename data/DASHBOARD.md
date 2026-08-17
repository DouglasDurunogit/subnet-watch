# Subnet watch — dashboard

_snapshot 2026-08-17T21:49:33Z · block 8867217 · run_status **ok**_

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
| New events this window | 1 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 62 | `████████████████████████████` |
| 0–0.2 | 3 | `█` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 8 | `████` |
| 0.6–0.8 | 7 | `███` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 37 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 78.3 | 103 | 198 | cpu-small | 10 | 20% |
| 2 | sn121 sundae_bar | 74.4 | 1,063 | 1,063 = | cpu-small | 2 | 61% |
| 3 | sn67 Harnyx | 71.9 | 20.27 | 380 | cpu-small | 129 | 11% |
| 4 | sn26 Perturb | 71.2 | 45.19 | 344 | rtx3060 | 10 | 70% |
| 5 | sn96 Verathos | 69.1 | 26.60 | 560 | rtx4090 | 53 | 42% |
| 6 | sn91 cascade | 68.8 | 519 | 2,100 | rtx4090* | 5 | 51% |
| 7 | sn41 Almanac | 68.7 | 9.75 | 53.66 | cpu-small | 75 | 69% |
| 8 | sn62 Ridges | 68.4 | 464 | 2,150 | rtx4090* | 6 | 40% |
| 9 | sn15 ORO | 67.9 | 10.81 | 20.99 | cpu-small | 66 | 94% |
| 10 | sn21 AdTAO | 67.9 | 7.99 | 35.68 | cpu-small | 88 | 45% |
| 11 | sn38 ChronoLLM | 66.3 | 105 | 1,429 | cpu-small | 10 | 52% |
| 12 | sn124 Swarm | 65.9 | 224 | 493 | rtx4090* | 24 | 11% |
| 13 | sn107 Minos | 64.3 | 116 | 34,440 | cpu-small | 20 | 90% |
| 14 | sn85 Vidaio | 64.2 | 130 | 1,319 | rtx4090* | 13 | 42% |
| 15 | sn55 NIOME | 61.6 | 59.98 | 501 | rtx4090* | 11 | 29% |
| 16 | sn60 Bitsec.ai | 59 | 374 | 374 = | cpu-small | 3 | 50% |
| 17 | sn74 Gittensor | 58.1 | 22.82 | 204 | rtx4090* | 14 | 63% |
| 18 | sn61 RedTeam | 57.5 | 16.93 | 344 | rtx4090* | 83 | 8% |
| 19 | sn102 ConnitoAI | 56.5 | 456 | 1,435 | rtx4090* | 7 | 28% |
| 20 | sn51 lium.io | 56.2 | 18.13 | 1,170 | rtx4090* | 55 | 82% |

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
| concentrated (30–60%) | 20 |
| dominated (60–90%) | 19 |
| captured (>90%) | 26 |

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
| 2026-08-17T21:09 | sn21 | RELEASE | sn21 released SN21 training bundle — 10,791 records, refreshed 2026-08 |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

