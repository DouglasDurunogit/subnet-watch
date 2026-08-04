# Subnet watch — dashboard

_snapshot 2026-08-04T10:08:34Z · block 8770128 · run_status **ok**_

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
| Ranked | 92 | passed every gate |
| **Positive margin** | **54** | income beats machine cost |
| New events this window | 2 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 56 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 3 | `██` |
| 0.4–0.6 | 8 | `████` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 11 | `██████` |
| ≥0.99 dead | 36 | `██████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn23 Trishool | 84.8 | 539 | 539 = | cpu-small | 5 | 20% |
| 2 | sn107 Minos | 78 | 109 | 27,868 | cpu-small | 20 | 90% |
| 3 | sn76 Phylax | 77.2 | 77.51 | 156 | cpu-small | 7 | 67% |
| 4 | sn98 NeverPlayAlone | 75.9 | 1,665 | 1,665 = | cpu-small | 1 | 100% |
| 5 | sn67 Harnyx | 71.8 | 20.56 | 693 | cpu-small | 149 | 17% |
| 6 | sn62 Ridges | 70 | 741 | 3,041 | rtx4090* | 7 | 39% |
| 7 | sn102 ConnitoAI | 69.9 | 725 | 725 = | rtx4090* | 4 | 25% |
| 8 | sn26 Perturb | 68.4 | 22.50 | 183 | rtx3060 | 11 | 50% |
| 9 | sn56 Gradients | 66.8 | 286 | 934 | rtx4090* | 8 | 71% |
| 10 | sn15 ORO | 66.2 | 7.88 | 10,433 | cpu-small | 70 | 94% |
| 11 | sn124 Swarm | 66 | 235 | 687 | rtx4090* | 21 | 12% |
| 12 | sn74 Gittensor | 66 | 224 | 357 | rtx4090* | 8 | 18% |
| 13 | sn38 ChronoLLM | 65.4 | 197 | 3,319 | rtx4090* | 10 | 52% |
| 14 | sn41 Almanac | 65.3 | 4.52 | 66.18 | cpu-small | 36 | 89% |
| 15 | sn21 AdTAO | 65.2 | 4.40 | 20.54 | cpu-small | 142 | 45% |
| 16 | sn53 engy | 64.2 | 130 | 3,040 | rtx4090 | 28 | 17% |
| 17 | sn80 OpenRoboto | 62.1 | 68.89 | 154 | rtx4090* | 4 | 94% |
| 18 | sn61 RedTeam | 58.3 | 21.61 | 76.33 | rtx4090* | 98 | 3% |
| 19 | sn9 iota | 55.2 | 8,639 | 8,639 = | rtx4090* | 3 | 51% |
| 20 | sn28 gm | 53.5 | 6.14 | 2,045 | rtx4090* | 17 | 63% |

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
| wide (<30%) | 24 |
| concentrated (30–60%) | 21 |
| dominated (60–90%) | 21 |
| captured (>90%) | 25 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 104 |
| code-submission (validator runs it) | 9 |
| min_compute.yml (curated) | 9 |
| README keywords (GUESS) | 5 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-08-04T10:09 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: Merge pull request #11 from conjectures-i |
| 2026-08-04T10:09 | sn89 | SCORING_COMMIT | sn89 commit touches scoring: closers 10% of total miner incentive (was |
| 2026-08-04T07:17 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-2546, gate 8x flagship unrented incen |
| 2026-08-04T07:17 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Bind scoring artifacts to exact commitmen |
| 2026-08-04T07:17 | sn104 | SCORING_COMMIT | sn104 commit touches scoring: fix the validator task resolution |
| 2026-08-04T07:17 | sn104 | README_TASK_DIFF | sn104 README task/scoring sections changed |
| 2026-08-04T04:26 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: Merge pull request #10 from conjectures-i |
| 2026-08-04T04:26 | sn66 | README_TASK_DIFF | sn66 README task/scoring sections changed |
| 2026-08-04T04:26 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-08-04T04:26 | sn107 | WEIGHTS_VERSION_BUMP | sn107 weights_version 13 -> 20 |
| 2026-08-04T04:26 | sn107 | README_TASK_DIFF | sn107 README task/scoring sections changed |
| 2026-08-04T00:59 | sn61 | RELEASE | sn61 released 4.8.4 |
| 2026-08-04T00:59 | sn61 | SCORING_COMMIT | sn61 commit touches scoring: fix: handle miner hotkey changes in updat |
| 2026-08-03T23:17 | sn13 | RELEASE | sn13 released Release v1.18.69 |
| 2026-08-03T23:17 | sn54 | SCORING_COMMIT | sn54 commit touches scoring: Made miner process more Intuitive |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

