# Subnet watch — dashboard

_snapshot 2026-08-30T07:31:41Z · block 8956525 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 60 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 93 | `miner_burn` < 0.99 |
| Ranked | 93 | passed every gate |
| **Positive margin** | **60** | income beats machine cost |
| New events this window | 4 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 64 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 6 | `███` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 35 | `███████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn11 TrajectoryRL | 80 | 5,571 | 5,571 = | cpu-small | 1 | 100% |
| 2 | sn92 MicroTensor | 76.2 | 61.37 | 1,120 | cpu-small | 9 | 67% |
| 3 | sn3 Teutonic | 75.7 | 4,083 | 4,083 = | rtx4090* | 5 | 20% |
| 4 | sn76 Phylax | 75.7 | 54.48 | 220 | cpu-small | 21 | 20% |
| 5 | sn67 Harnyx | 72.1 | 20.58 | 895 | cpu-small | 124 | 23% |
| 6 | sn111 Claims | 70.7 | 939 | 3,307 | rtx4090* | 3 | 70% |
| 7 | sn15 ORO | 70.5 | 21.34 | 22,554 | cpu-small | 72 | 93% |
| 8 | sn21 AdTAO | 70.2 | 14.18 | 606 | cpu-small | 14 | 45% |
| 9 | sn96 Verathos | 68.6 | 23.58 | 186 | rtx4090 | 75 | 42% |
| 10 | sn102 ConnitoAI | 68.2 | 433 | 2,677 | rtx4090* | 7 | 43% |
| 11 | sn80 OpenRoboto | 67.7 | 373 | 1,686 | rtx4090* | 5 | 71% |
| 12 | sn56 Gradients | 67.4 | 341 | 671 | rtx4090* | 7 | 70% |
| 13 | sn91 cascade | 67 | 309 | 626 | rtx4090* | 5 | 52% |
| 14 | sn124 Swarm | 66.7 | 290 | 941 | rtx4090* | 25 | 11% |
| 15 | sn79 MVTRX | 66.2 | 4.70 | 457 | cpu-small | 218 | 10% |
| 16 | sn108 Prometheon | 65.3 | 184 | 489 | rtx4090* | 9 | 26% |
| 17 | sn81 Reliquary | 65 | 167 | 282 | rtx4090* | 32 | 6% |
| 18 | sn61 RedTeam | 64.8 | 159 | 238 | rtx4090* | 40 | 4% |
| 19 | sn107 Minos | 64.3 | 128 | 37,794 | cpu-small | 20 | 90% |
| 20 | sn54 Yanez | 64.2 | 6.56 | 1,049 | a4000 | 101 | 35% |

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
| dominated (60–90%) | 17 |
| captured (>90%) | 29 |

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
| 2026-08-30T07:32 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: fix(validator-api): serve the daily feeds |
| 2026-08-30T07:32 | sn45 | README_TASK_DIFF | sn45 README task/scoring sections changed |
| 2026-08-30T07:32 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-08-30T07:32 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: Satisfy strict typing across the validato |
| 2026-08-30T01:45 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Document miner SOURCE_ADD inputs (#153) |
| 2026-08-30T01:45 | sn71 | README_TASK_DIFF | sn71 README task/scoring sections changed |
| 2026-08-30T01:45 | sn89 | SCORING_COMMIT | sn89 commit touches scoring: scoring: the points qualify gate, and the |
| 2026-08-30T01:45 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: Validate commitments at discovery, guard  |
| 2026-08-29T23:29 | sn89 | SCORING_COMMIT | sn89 commit touches scoring: scoring: the points gate is per competiti |
| 2026-08-29T21:20 | sn89 | SCORING_COMMIT | sn89 commit touches scoring: limit-watcher: a miner-drawn band survive |
| 2026-08-29T18:44 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: fix(reporting): a published tier must mea |
| 2026-08-29T18:44 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Measure admitted model verifier latency |
| 2026-08-29T18:44 | sn89 | SCORING_COMMIT | sn89 commit touches scoring: HF: grade the band the miner declared, no |
| 2026-08-29T18:44 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: fix(validator): preserve completed run s |
| 2026-08-29T15:10 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: feat(scoring): honour the reference exemp |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

