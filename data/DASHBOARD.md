# Subnet watch — dashboard

_snapshot 2026-09-08T09:01:29Z · block 9021717 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 57 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 90 | `miner_burn` < 0.99 |
| Ranked | 91 | passed every gate |
| **Positive margin** | **57** | income beats machine cost |
| New events this window | 5 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 59 | `████████████████████████████` |
| 0–0.2 | 9 | `████` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 38 | `██████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn114 SOMA | 87.2 | 972 | 7,785 | cpu-small | 4 | 80% |
| 2 | sn92 MicroTensor | 79.3 | 133 | 401 | cpu-small | 9 | 50% |
| 3 | sn107 Minos | 77.4 | 100 | 6,138 | cpu-small | 21 | 81% |
| 4 | sn3 Teutonic | 76.1 | 4,505 | 4,505 = | rtx4090* | 5 | 20% |
| 5 | sn96 Verathos | 71 | 42.75 | 447 | rtx4090 | 77 | 30% |
| 6 | sn67 Harnyx | 70.7 | 15.02 | 1,328 | cpu-small | 122 | 37% |
| 7 | sn91 cascade | 70.4 | 847 | 3,411 | rtx4090* | 5 | 52% |
| 8 | sn102 ConnitoAI | 69.5 | 630 | 1,538 | rtx4090* | 7 | 28% |
| 9 | sn14 Cacheon | 68.9 | 540 | 1,223 | rtx4090* | 12 | 18% |
| 10 | sn11 TrajectoryRL | 68.7 | 6,698 | 6,698 = | cpu-small | 1 | 100% |
| 11 | sn62 Ridges | 68.1 | 422 | 1,256 | rtx4090* | 13 | 26% |
| 12 | sn80 OpenRoboto | 67.7 | 369 | 1,314 | rtx4090* | 5 | 43% |
| 13 | sn38 ChronoLLM | 67 | 131 | 2,776 | cpu-small | 10 | 52% |
| 14 | sn124 Swarm | 66.7 | 290 | 894 | rtx4090* | 25 | 11% |
| 15 | sn111 Claims | 66.5 | 282 | 2,528 | rtx4090* | 5 | 56% |
| 16 | sn65 True Performance | 62.6 | 90.60 | 189 | rtx4090* | 6 | 75% |
| 17 | sn108 Prometheon | 60.6 | 44.99 | 131 | rtx4090* | 11 | 33% |
| 18 | sn41 Almanac | 60.6 | 41.09 | 114 | cpu-small | 84 | 3% |
| 19 | sn28 SayGM | 60.1 | 40.36 | 515 | rtx4090* | 59 | 70% |
| 20 | sn51 lium.io | 57.3 | 24.70 | 2,870 | rtx4090* | 63 | 78% |

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
| wide (<30%) | 26 |
| concentrated (30–60%) | 23 |
| dominated (60–90%) | 17 |
| captured (>90%) | 20 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 99 |
| min_compute.yml (curated) | 11 |
| code-submission (validator runs it) | 10 |
| README keywords (GUESS) | 7 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-09-08T09:02 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: Release 259 reviewed targets with immutab |
| 2026-09-08T09:02 | sn66 | README_TASK_DIFF | sn66 README task/scoring sections changed |
| 2026-09-08T09:02 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Parse Arena drain quiescence in validator |
| 2026-09-08T09:02 | sn80 | SCORING_COMMIT | sn80 commit touches scoring: docs: link shared real-robot task catalog |
| 2026-09-08T09:02 | sn80 | README_TASK_DIFF | sn80 README task/scoring sections changed |
| 2026-09-08T04:27 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-09-08T04:27 | sn67 | README_TASK_DIFF | sn67 README task/scoring sections changed |
| 2026-09-08T04:27 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Verify staging SOURCE_ADD restart isolati |
| 2026-09-08T04:27 | sn74 | RELEASE | sn74 released release-20260908-031700 |
| 2026-09-08T04:27 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: cost is total task latency for every syst |
| 2026-09-08T04:27 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: fix(proof): stage proxy model + holdout  |
| 2026-09-07T23:48 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Checkpoint historical validator schedule  |
| 2026-09-07T23:48 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Fix pilot deployment validation |
| 2026-09-07T21:28 | sn10 | SCORING_COMMIT | sn10 commit touches scoring: Merge pull request #146 from Pareton-ai/a |
| 2026-09-07T21:28 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge remote-tracking branch 'origin/main |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

