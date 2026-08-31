# Subnet watch — dashboard

_snapshot 2026-08-31T20:47:50Z · block 8967706 · run_status **ok**_

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
| New events this window | 9 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 65 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 6 | `███` |
| 0.6–0.8 | 7 | `███` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 35 | `███████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn92 MicroTensor | 79 | 122 | 550 | cpu-small | 9 | 60% |
| 2 | sn3 Teutonic | 75.6 | 3,872 | 3,872 = | rtx4090* | 5 | 20% |
| 3 | sn76 Phylax | 74.9 | 44.06 | 93.20 | cpu-small | 21 | 20% |
| 4 | sn67 Harnyx | 72.9 | 25.31 | 51.60 | cpu-small | 131 | 17% |
| 5 | sn23 Trishool | 72.2 | 554 | 554 = | cpu-small | 2 | 80% |
| 6 | sn102 ConnitoAI | 71.9 | 1,289 | 1,549 | rtx4090* | 6 | 28% |
| 7 | sn15 ORO | 71.1 | 23.51 | 22,301 | cpu-small | 59 | 95% |
| 8 | sn91 cascade | 68.8 | 521 | 2,815 | rtx4090* | 5 | 52% |
| 9 | sn96 Verathos | 68.6 | 23.49 | 159 | rtx4090 | 74 | 41% |
| 10 | sn111 Claims | 68.5 | 494 | 3,031 | rtx4090* | 5 | 68% |
| 11 | sn11 TrajectoryRL | 67.8 | 5,207 | 5,207 = | cpu-small | 1 | 100% |
| 12 | sn124 Swarm | 66.6 | 275 | 893 | rtx4090* | 25 | 11% |
| 13 | sn21 AdTAO | 66.5 | 6.18 | 1,146 | cpu-small | 14 | 45% |
| 14 | sn80 OpenRoboto | 65.4 | 187 | 677 | rtx4090* | 5 | 71% |
| 15 | sn61 RedTeam | 65 | 166 | 244 | rtx4090* | 49 | 3% |
| 16 | sn107 Minos | 64.3 | 122 | 38,230 | cpu-small | 20 | 90% |
| 17 | sn54 Yanez | 64.3 | 6.61 | 996 | a4000 | 93 | 35% |
| 18 | sn81 Reliquary | 64.2 | 131 | 231 | rtx4090* | 36 | 5% |
| 19 | sn79 MVTRX | 63.7 | 4.10 | 440 | cpu-small | 229 | 10% |
| 20 | sn55 NIOME | 62.4 | 75.66 | 621 | rtx4090* | 11 | 29% |

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
| dominated (60–90%) | 18 |
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
| 2026-08-31T15:03 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-08-31T15:03 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: Add the novel partition and blend it into |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

