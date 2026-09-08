# Subnet watch — dashboard

_snapshot 2026-09-08T04:27:26Z · block 9020347 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 57 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 91 | `miner_burn` < 0.99 |
| Ranked | 92 | passed every gate |
| **Positive margin** | **57** | income beats machine cost |
| New events this window | 6 | see ALARMS.md |

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
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 37 | `██████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn114 SOMA | 87.2 | 982 | 7,866 | cpu-small | 4 | 80% |
| 2 | sn92 MicroTensor | 79.2 | 131 | 395 | cpu-small | 9 | 50% |
| 3 | sn107 Minos | 77.4 | 99.80 | 6,173 | cpu-small | 21 | 81% |
| 4 | sn3 Teutonic | 76.1 | 4,580 | 4,580 = | rtx4090* | 5 | 20% |
| 5 | sn96 Verathos | 71 | 42.93 | 399 | rtx4090 | 78 | 31% |
| 6 | sn67 Harnyx | 70.7 | 15.22 | 1,344 | cpu-small | 116 | 37% |
| 7 | sn91 cascade | 70.5 | 869 | 3,500 | rtx4090* | 5 | 52% |
| 8 | sn80 OpenRoboto | 70.2 | 776 | 4,930 | rtx4090* | 5 | 43% |
| 9 | sn11 TrajectoryRL | 68.8 | 6,879 | 6,879 = | cpu-small | 1 | 100% |
| 10 | sn14 Cacheon | 68.4 | 457 | 1,223 | rtx4090* | 14 | 17% |
| 11 | sn62 Ridges | 68.1 | 422 | 1,255 | rtx4090* | 13 | 26% |
| 12 | sn102 ConnitoAI | 67.4 | 347 | 2,008 | rtx4090* | 7 | 36% |
| 13 | sn38 ChronoLLM | 67.1 | 135 | 2,870 | cpu-small | 10 | 52% |
| 14 | sn124 Swarm | 66.8 | 293 | 909 | rtx4090* | 25 | 11% |
| 15 | sn111 Claims | 66 | 244 | 3,669 | rtx4090* | 5 | 80% |
| 16 | sn65 True Performance | 62.6 | 91.73 | 192 | rtx4090* | 6 | 75% |
| 17 | sn21 AdTAO | 62.5 | 2.93 | 251 | cpu-small | 16 | 45% |
| 18 | sn41 Almanac | 60.6 | 41.63 | 115 | cpu-small | 84 | 3% |
| 19 | sn108 Prometheon | 60.1 | 39.22 | 135 | rtx4090* | 11 | 33% |
| 20 | sn28 SayGM | 59.3 | 31.88 | 328 | rtx4090* | 58 | 77% |

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
| concentrated (30–60%) | 22 |
| dominated (60–90%) | 20 |
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
| 2026-09-07T21:28 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Open miner pilot enrollment |
| 2026-09-07T21:28 | sn96 | RELEASE | sn96 released Verathos v0.2.1 – Sleipnir Cross-Machine Serving |
| 2026-09-07T21:28 | sn104 | SCORING_COMMIT | sn104 commit touches scoring: Merge pull request #10 from taostatus/fe |
| 2026-09-07T17:49 | sn1 | RELEASE | sn1 released v4.4.2 |
| 2026-09-07T17:49 | sn25 | RELEASE | sn25 released v2026.9.7-1039843330 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

