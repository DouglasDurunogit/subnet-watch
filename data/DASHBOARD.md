# Subnet watch — dashboard

_snapshot 2026-08-31T15:02:30Z · block 8965979 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 62 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 93 | `miner_burn` < 0.99 |
| Ranked | 93 | passed every gate |
| **Positive margin** | **62** | income beats machine cost |
| New events this window | 7 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 67 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 6 | `███` |
| 0.6–0.8 | 7 | `███` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 35 | `███████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn92 MicroTensor | 81.2 | 214 | 2,093 | cpu-small | 9 | 60% |
| 2 | sn11 TrajectoryRL | 79.7 | 5,124 | 5,124 = | cpu-small | 1 | 100% |
| 3 | sn3 Teutonic | 75.5 | 3,850 | 3,850 = | rtx4090* | 5 | 20% |
| 4 | sn76 Phylax | 74.9 | 44.55 | 94.22 | cpu-small | 21 | 20% |
| 5 | sn67 Harnyx | 72.8 | 24.86 | 632 | cpu-small | 131 | 17% |
| 6 | sn23 Trishool | 72.2 | 547 | 547 = | cpu-small | 2 | 80% |
| 7 | sn15 ORO | 70.7 | 22.49 | 21,377 | cpu-small | 59 | 95% |
| 8 | sn96 Verathos | 68.7 | 24.44 | 159 | rtx4090 | 73 | 41% |
| 9 | sn21 AdTAO | 68.7 | 9.94 | 1,166 | cpu-small | 14 | 45% |
| 10 | sn102 ConnitoAI | 67.7 | 379 | 1,868 | rtx4090* | 7 | 34% |
| 11 | sn111 Claims | 67.4 | 356 | 3,179 | rtx4090* | 5 | 70% |
| 12 | sn91 cascade | 67.1 | 316 | 641 | rtx4090* | 5 | 52% |
| 13 | sn124 Swarm | 66.6 | 281 | 912 | rtx4090* | 25 | 11% |
| 14 | sn61 RedTeam | 65.5 | 196 | 291 | rtx4090* | 42 | 4% |
| 15 | sn80 OpenRoboto | 65.5 | 193 | 696 | rtx4090* | 5 | 71% |
| 16 | sn81 Reliquary | 64.6 | 147 | 272 | rtx4090* | 33 | 6% |
| 17 | sn79 MVTRX | 64.6 | 4.09 | 435 | cpu-small | 225 | 10% |
| 18 | sn107 Minos | 64.5 | 125 | 37,207 | cpu-small | 20 | 90% |
| 19 | sn54 Yanez | 64.3 | 6.79 | 1,013 | a4000 | 93 | 35% |
| 20 | sn55 NIOME | 62.4 | 76.14 | 624 | rtx4090* | 11 | 29% |

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
| wide (<30%) | 23 |
| concentrated (30–60%) | 23 |
| dominated (60–90%) | 18 |
| captured (>90%) | 26 |

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
| 2026-08-31T15:03 | sn3 | SCORING_COMMIT | sn3 commit touches scoring: Implement evaluation reuse limit handling  |
| 2026-08-31T15:03 | sn50 | SCORING_COMMIT | sn50 commit touches scoring: feat(validator): blend VHFT (Synth Ultra) |
| 2026-08-31T15:03 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-2090, validate one executor on reques |
| 2026-08-31T15:03 | sn56 | SCORING_COMMIT | sn56 commit touches scoring: Preserve replacement-task invariants acro |
| 2026-08-31T15:03 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-08-31T15:03 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: Add the novel partition and blend it into |
| 2026-08-31T15:03 | sn97 | SCORING_COMMIT | sn97 commit touches scoring: fix: skip hidden files from validation |
| 2026-08-31T07:00 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: validator: multi-horizon calibration tele |
| 2026-08-31T07:00 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: Score module-shaped tasks in miner simula |
| 2026-08-31T07:00 | sn101 | SCORING_COMMIT | sn101 commit touches scoring: Harden tag normalization and duplicate-s |
| 2026-08-31T07:00 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: feat(selection): make adaptive miner sam |
| 2026-08-30T22:43 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: Lock the evaluation environment to the fl |
| 2026-08-30T22:43 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: feat(selection): expand miner pool with  |
| 2026-08-30T20:05 | sn25 | RELEASE | sn25 released v2026.8.30-1033129380 |
| 2026-08-30T17:40 | sn15 | RELEASE | sn15 released v1.2.11 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

