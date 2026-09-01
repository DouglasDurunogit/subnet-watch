# Subnet watch — dashboard

_snapshot 2026-09-01T00:34:20Z · block 8968838 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 59 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 93 | `miner_burn` < 0.99 |
| Ranked | 93 | passed every gate |
| **Positive margin** | **59** | income beats machine cost |
| New events this window | 2 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 65 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 7 | `███` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 35 | `███████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn92 MicroTensor | 81.4 | 229 | 2,234 | cpu-small | 9 | 60% |
| 2 | sn3 Teutonic | 75.6 | 3,904 | 3,904 = | rtx4090* | 5 | 20% |
| 3 | sn76 Phylax | 74.9 | 44.44 | 93.99 | cpu-small | 21 | 20% |
| 4 | sn67 Harnyx | 73 | 26.31 | 53.61 | cpu-small | 131 | 17% |
| 5 | sn23 Trishool | 72.3 | 562 | 562 = | cpu-small | 2 | 80% |
| 6 | sn102 ConnitoAI | 71.9 | 1,306 | 1,686 | rtx4090* | 5 | 29% |
| 7 | sn15 ORO | 71 | 22.49 | 40.31 | cpu-small | 61 | 94% |
| 8 | sn91 cascade | 68.9 | 538 | 2,903 | rtx4090* | 5 | 52% |
| 9 | sn96 Verathos | 68.4 | 22.87 | 165 | rtx4090 | 77 | 41% |
| 10 | sn111 Claims | 67.3 | 352 | 3,146 | rtx4090* | 5 | 70% |
| 11 | sn56 Gradients | 66.9 | 294 | 1,070 | rtx4090* | 11 | 71% |
| 12 | sn124 Swarm | 66.6 | 280 | 908 | rtx4090* | 25 | 11% |
| 13 | sn21 AdTAO | 66.6 | 6.28 | 1,162 | cpu-small | 14 | 45% |
| 14 | sn61 RedTeam | 65.1 | 170 | 249 | rtx4090* | 48 | 3% |
| 15 | sn107 Minos | 64.6 | 128 | 37,996 | cpu-small | 20 | 90% |
| 16 | sn60 Bitsec.ai | 64.4 | 1,888 | 1,888 = | cpu-small | 2 | 50% |
| 17 | sn81 Reliquary | 64.4 | 139 | 253 | rtx4090* | 37 | 6% |
| 18 | sn79 MVTRX | 64.4 | 4.03 | 437 | cpu-small | 227 | 10% |
| 19 | sn54 Yanez | 64.1 | 6.37 | 977 | a4000 | 93 | 35% |
| 20 | sn55 NIOME | 62.4 | 77.41 | 634 | rtx4090* | 11 | 29% |

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
| no evidence | 101 |
| code-submission (validator runs it) | 10 |
| min_compute.yml (curated) | 10 |
| README keywords (GUESS) | 6 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
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
| 2026-08-31T15:03 | sn56 | SCORING_COMMIT | sn56 commit touches scoring: Preserve replacement-task invariants acro |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

