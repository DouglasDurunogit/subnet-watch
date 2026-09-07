# Subnet watch — dashboard

_snapshot 2026-09-07T23:47:52Z · block 9018950 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 56 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 90 | `miner_burn` < 0.99 |
| Ranked | 91 | passed every gate |
| **Positive margin** | **56** | income beats machine cost |
| New events this window | 2 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 59 | `████████████████████████████` |
| 0–0.2 | 10 | `█████` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 38 | `██████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn114 SOMA | 87.2 | 994 | 7,957 | cpu-small | 4 | 80% |
| 2 | sn92 MicroTensor | 79 | 124 | 375 | cpu-small | 9 | 50% |
| 3 | sn107 Minos | 77.5 | 102 | 6,292 | cpu-small | 21 | 81% |
| 4 | sn3 Teutonic | 76.1 | 4,603 | 4,603 = | rtx4090* | 5 | 20% |
| 5 | sn67 Harnyx | 72.8 | 25.04 | 421 | cpu-small | 129 | 11% |
| 6 | sn96 Verathos | 71 | 43.49 | 468 | rtx4090 | 75 | 30% |
| 7 | sn102 ConnitoAI | 70.7 | 918 | 2,305 | rtx4090* | 5 | 41% |
| 8 | sn91 cascade | 70.5 | 859 | 3,462 | rtx4090* | 5 | 52% |
| 9 | sn80 OpenRoboto | 70.2 | 777 | 4,935 | rtx4090* | 5 | 43% |
| 10 | sn11 TrajectoryRL | 68.8 | 7,002 | 7,002 = | cpu-small | 1 | 100% |
| 11 | sn62 Ridges | 68.2 | 427 | 1,269 | rtx4090* | 13 | 26% |
| 12 | sn38 ChronoLLM | 67.2 | 138 | 2,925 | cpu-small | 10 | 52% |
| 13 | sn124 Swarm | 66.8 | 299 | 925 | rtx4090* | 25 | 11% |
| 14 | sn111 Claims | 66.6 | 290 | 2,604 | rtx4090* | 5 | 55% |
| 15 | sn14 Cacheon | 63.8 | 115 | 2,595 | rtx4090* | 10 | 36% |
| 16 | sn65 True Performance | 62.7 | 93.00 | 194 | rtx4090* | 6 | 75% |
| 17 | sn21 AdTAO | 62.4 | 2.91 | 250 | cpu-small | 16 | 45% |
| 18 | sn28 SayGM | 60.9 | 49.89 | 11,364 | rtx4090* | 59 | 71% |
| 19 | sn108 Prometheon | 60.7 | 46.26 | 137 | rtx4090* | 10 | 33% |
| 20 | sn41 Almanac | 60.5 | 41.17 | 104 | cpu-small | 85 | 7% |

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
| concentrated (30–60%) | 24 |
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
| 2026-09-07T23:48 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Checkpoint historical validator schedule  |
| 2026-09-07T23:48 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Fix pilot deployment validation |
| 2026-09-07T21:28 | sn10 | SCORING_COMMIT | sn10 commit touches scoring: Merge pull request #146 from Pareton-ai/a |
| 2026-09-07T21:28 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge remote-tracking branch 'origin/main |
| 2026-09-07T21:28 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Open miner pilot enrollment |
| 2026-09-07T21:28 | sn96 | RELEASE | sn96 released Verathos v0.2.1 – Sleipnir Cross-Machine Serving |
| 2026-09-07T21:28 | sn104 | SCORING_COMMIT | sn104 commit touches scoring: Merge pull request #10 from taostatus/fe |
| 2026-09-07T17:49 | sn1 | RELEASE | sn1 released v4.4.2 |
| 2026-09-07T17:49 | sn25 | RELEASE | sn25 released v2026.9.7-1039843330 |
| 2026-09-07T17:49 | sn34 | SCORING_COMMIT | sn34 commit touches scoring: Set explicit 100% burn and bypass reward  |
| 2026-09-07T17:49 | sn38 | SCORING_COMMIT | sn38 commit touches scoring: Update validator image to the latest vers |
| 2026-09-07T17:49 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: Merge pull request #76 from conjectures-i |
| 2026-09-07T12:22 | sn18 | RELEASE | sn18 released Release 2.1.4 |
| 2026-09-07T12:22 | sn18 | SCORING_COMMIT | sn18 commit touches scoring: Stop emissions for non-participating mine |
| 2026-09-07T12:22 | sn25 | RELEASE | sn25 released v2026.9.7-1039747440 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

