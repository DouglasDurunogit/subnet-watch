# Subnet watch — dashboard

_snapshot 2026-09-07T12:21:35Z · block 9015524 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 57 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 93 | `miner_burn` < 0.99 |
| Ranked | 94 | passed every gate |
| **Positive margin** | **57** | income beats machine cost |
| New events this window | 10 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 58 | `████████████████████████████` |
| 0–0.2 | 11 | `█████` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 35 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn92 MicroTensor | 79.6 | 143 | 430 | cpu-small | 9 | 50% |
| 2 | sn107 Minos | 77.2 | 97.21 | 5,898 | cpu-small | 21 | 81% |
| 3 | sn3 Teutonic | 76.1 | 4,551 | 4,551 = | rtx4090* | 5 | 20% |
| 4 | sn114 SOMA | 74.3 | 1,029 | 1,029 = | cpu-small | 3 | 80% |
| 5 | sn67 Harnyx | 72.8 | 25.92 | 435 | cpu-small | 129 | 11% |
| 6 | sn91 cascade | 71 | 996 | 4,007 | rtx4090* | 5 | 52% |
| 7 | sn15 ORO | 70.8 | 24.45 | 22,995 | cpu-small | 75 | 92% |
| 8 | sn96 Verathos | 70.3 | 36.58 | 507 | rtx4090 | 80 | 40% |
| 9 | sn11 TrajectoryRL | 69 | 7,302 | 7,302 = | cpu-small | 1 | 100% |
| 10 | sn14 Cacheon | 68.4 | 460 | 878 | rtx4090* | 6 | 67% |
| 11 | sn62 Ridges | 68.3 | 452 | 1,341 | rtx4090* | 13 | 26% |
| 12 | sn102 ConnitoAI | 68.1 | 416 | 1,900 | rtx4090* | 7 | 33% |
| 13 | sn80 OpenRoboto | 67.8 | 383 | 1,363 | rtx4090* | 5 | 51% |
| 14 | sn124 Swarm | 66.9 | 306 | 942 | rtx4090* | 25 | 11% |
| 15 | sn111 Claims | 66.2 | 255 | 2,297 | rtx4090* | 5 | 48% |
| 16 | sn65 True Performance | 62.8 | 96.20 | 201 | rtx4090* | 6 | 75% |
| 17 | sn108 Prometheon | 60.7 | 46.78 | 138 | rtx4090* | 10 | 33% |
| 18 | sn28 SayGM | 60.5 | 44.87 | 434 | rtx4090* | 49 | 45% |
| 19 | sn41 Almanac | 60.5 | 40.11 | 102 | cpu-small | 86 | 10% |
| 20 | sn51 lium.io | 58.3 | 31.58 | 2,988 | rtx4090* | 64 | 73% |

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
| concentrated (30–60%) | 23 |
| dominated (60–90%) | 19 |
| captured (>90%) | 22 |

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
| 2026-09-07T12:22 | sn18 | RELEASE | sn18 released Release 2.1.4 |
| 2026-09-07T12:22 | sn18 | SCORING_COMMIT | sn18 commit touches scoring: Stop emissions for non-participating mine |
| 2026-09-07T12:22 | sn25 | RELEASE | sn25 released v2026.9.7-1039747440 |
| 2026-09-07T12:22 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: [P1] feat: run the miners tests and ruff  |
| 2026-09-07T12:22 | sn66 | RELEASE | sn66 released v.1.0.3: Web submissions, payouts, contributions... |
| 2026-09-07T12:22 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-09-07T12:22 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: chore: bind verified controller upgrade r |
| 2026-09-07T12:22 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Harden macOS validator audit origin |
| 2026-09-07T12:22 | sn80 | README_TASK_DIFF | sn80 README task/scoring sections changed |
| 2026-09-07T12:22 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: archive: a rewarded system is archived wh |
| 2026-09-07T06:01 | sn25 | RELEASE | sn25 released v2026.9.6-1039587510 |
| 2026-09-07T06:01 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: fix: verify active provider cache persist |
| 2026-09-07T00:57 | sn34 | RELEASE | sn34 released 5.0.0 — King of the Hill |
| 2026-09-07T00:57 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: receipt: publish every duelled challenger |
| 2026-09-06T22:52 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Record recovery checkpoints and post-pull |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

