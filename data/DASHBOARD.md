# Subnet watch — dashboard

_snapshot 2026-09-01T05:44:13Z · block 8970388 · run_status **ok**_

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
| Ranked | 93 | passed every gate |
| **Positive margin** | **57** | income beats machine cost |
| New events this window | 1 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 65 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 8 | `███` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 35 | `███████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn92 MicroTensor | 81.1 | 209 | 2,037 | cpu-small | 9 | 60% |
| 2 | sn3 Teutonic | 75.5 | 3,792 | 3,792 = | rtx4090* | 5 | 20% |
| 3 | sn76 Phylax | 75 | 45.26 | 95.72 | cpu-small | 21 | 20% |
| 4 | sn67 Harnyx | 72.9 | 26.19 | 53.38 | cpu-small | 131 | 17% |
| 5 | sn15 ORO | 70.8 | 23.10 | 40.45 | cpu-small | 64 | 94% |
| 6 | sn91 cascade | 69.8 | 702 | 2,833 | rtx4090* | 5 | 52% |
| 7 | sn96 Verathos | 68.6 | 23.63 | 173 | rtx4090 | 81 | 41% |
| 8 | sn102 ConnitoAI | 68 | 409 | 2,005 | rtx4090* | 7 | 35% |
| 9 | sn56 Gradients | 67.8 | 385 | 1,059 | rtx4090* | 7 | 71% |
| 10 | sn111 Claims | 67.2 | 334 | 2,989 | rtx4090* | 5 | 70% |
| 11 | sn124 Swarm | 66.5 | 272 | 884 | rtx4090* | 25 | 11% |
| 12 | sn61 RedTeam | 65 | 167 | 244 | rtx4090* | 48 | 3% |
| 13 | sn21 AdTAO | 64.7 | 4.24 | 110 | cpu-small | 14 | 45% |
| 14 | sn107 Minos | 64.6 | 127 | 37,735 | cpu-small | 20 | 90% |
| 15 | sn98 NeverPlayAlone | 64.5 | 1,951 | 1,951 = | cpu-small | 1 | 100% |
| 16 | sn60 Bitsec.ai | 64.5 | 1,901 | 1,901 = | cpu-small | 2 | 50% |
| 17 | sn79 MVTRX | 64.4 | 4.03 | 419 | cpu-small | 230 | 9% |
| 18 | sn81 Reliquary | 64 | 122 | 246 | rtx4090* | 36 | 6% |
| 19 | sn54 Yanez | 63.7 | 5.54 | 949 | a4000 | 97 | 35% |
| 20 | sn55 NIOME | 62.6 | 80.17 | 655 | rtx4090* | 11 | 29% |

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
| concentrated (30–60%) | 18 |
| dominated (60–90%) | 21 |
| captured (>90%) | 27 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 101 |
| code-submission (validator runs it) | 10 |
| min_compute.yml (curated) | 10 |
| README keywords (GUESS) | 6 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-09-01T05:44 | sn80 | README_TASK_DIFF | sn80 README task/scoring sections changed |
| 2026-09-01T00:34 | sn25 | RELEASE | sn25 released v2026.8.31-1034210530 |
| 2026-09-01T00:34 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Batch carried fleet refresh verification |
| 2026-08-31T20:48 | sn15 | RELEASE | sn15 released v1.2.12 |
| 2026-08-31T20:48 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: fix(validator): don't fail runs on incomp |
| 2026-08-31T20:48 | sn38 | SCORING_COMMIT | sn38 commit touches scoring: Update validator image to the latest vers |
| 2026-08-31T20:48 | sn38 | README_TASK_DIFF | sn38 README task/scoring sections changed |
| 2026-08-31T20:48 | sn50 | RELEASE | sn50 released v1.12.0 |
| 2026-08-31T20:48 | sn92 | RELEASE | sn92 released v0.3.0 |
| 2026-08-31T20:48 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: Grant the validator container the capabil |
| 2026-08-31T20:48 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: feat(selection): diversify adaptive mine |
| 2026-08-31T20:48 | sn124 | SCORING_COMMIT | sn124 commit touches scoring: Merge pull request #118 from swarm-subne |
| 2026-08-31T15:03 | sn3 | SCORING_COMMIT | sn3 commit touches scoring: Implement evaluation reuse limit handling  |
| 2026-08-31T15:03 | sn50 | SCORING_COMMIT | sn50 commit touches scoring: feat(validator): blend VHFT (Synth Ultra) |
| 2026-08-31T15:03 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-2090, validate one executor on reques |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

