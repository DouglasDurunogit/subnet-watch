# Subnet watch — dashboard

_snapshot 2026-09-08T13:32:23Z · block 9023072 · run_status **ok**_

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
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 7 | `███` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 38 | `██████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn114 SOMA | 87.1 | 970 | 7,769 | cpu-small | 4 | 80% |
| 2 | sn92 MicroTensor | 79 | 124 | 374 | cpu-small | 9 | 50% |
| 3 | sn107 Minos | 77.4 | 101 | 6,250 | cpu-small | 21 | 81% |
| 4 | sn3 Teutonic | 76 | 4,476 | 4,476 = | rtx4090* | 5 | 20% |
| 5 | sn96 Verathos | 71.1 | 43.86 | 405 | rtx4090 | 74 | 31% |
| 6 | sn67 Harnyx | 70.7 | 14.94 | 1,320 | cpu-small | 124 | 37% |
| 7 | sn91 cascade | 70.2 | 797 | 3,106 | rtx4090* | 5 | 51% |
| 8 | sn14 Cacheon | 69.6 | 665 | 1,216 | rtx4090* | 12 | 18% |
| 9 | sn11 TrajectoryRL | 68.6 | 6,621 | 6,621 = | cpu-small | 1 | 100% |
| 10 | sn62 Ridges | 68.1 | 414 | 1,232 | rtx4090* | 13 | 26% |
| 11 | sn80 OpenRoboto | 67.7 | 371 | 1,317 | rtx4090* | 5 | 43% |
| 12 | sn38 ChronoLLM | 67 | 130 | 2,771 | cpu-small | 10 | 52% |
| 13 | sn124 Swarm | 66.7 | 290 | 895 | rtx4090* | 25 | 11% |
| 14 | sn111 Claims | 66.3 | 265 | 3,237 | rtx4090* | 5 | 76% |
| 15 | sn56 Gradients | 63.3 | 101 | 5,846 | rtx4090* | 11 | 48% |
| 16 | sn65 True Performance | 62.6 | 90.35 | 189 | rtx4090* | 6 | 75% |
| 17 | sn28 SayGM | 61 | 52.31 | 10,677 | rtx4090* | 60 | 68% |
| 18 | sn41 Almanac | 60.5 | 40.91 | 113 | cpu-small | 84 | 3% |
| 19 | sn108 Prometheon | 60.4 | 42.26 | 124 | rtx4090* | 11 | 33% |
| 20 | sn102 ConnitoAI | 58.7 | 25.58 | 1,545 | rtx4090* | 8 | 28% |

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
| concentrated (30–60%) | 22 |
| dominated (60–90%) | 18 |
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
| 2026-09-08T13:32 | sn9 | RELEASE | sn9 released v4.12.14 |
| 2026-09-08T13:32 | sn10 | SCORING_COMMIT | sn10 commit touches scoring: Merge pull request #145 from Pareton-ai/b |
| 2026-09-08T13:32 | sn34 | SCORING_COMMIT | sn34 commit touches scoring: Bump version to 5.0.2 so validators autou |
| 2026-09-08T13:32 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Verify approved prior testnet release boo |
| 2026-09-08T13:32 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: fix(eval): install host cc for triton ji |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

