# Subnet watch — dashboard

_snapshot 2026-08-30T01:45:18Z · block 8954793 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 60 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 94 | `miner_burn` < 0.99 |
| Ranked | 94 | passed every gate |
| **Positive margin** | **60** | income beats machine cost |
| New events this window | 4 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 63 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 7 | `███` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 34 | `███████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn11 TrajectoryRL | 79.9 | 5,503 | 5,503 = | cpu-small | 1 | 100% |
| 2 | sn92 MicroTensor | 76.1 | 60.20 | 1,099 | cpu-small | 9 | 67% |
| 3 | sn3 Teutonic | 75.7 | 4,012 | 4,012 = | rtx4090* | 5 | 20% |
| 4 | sn76 Phylax | 75.3 | 48.87 | 198 | cpu-small | 21 | 20% |
| 5 | sn67 Harnyx | 73 | 26.00 | 490 | cpu-small | 116 | 13% |
| 6 | sn102 ConnitoAI | 71.1 | 1,020 | 2,483 | rtx4090* | 5 | 40% |
| 7 | sn15 ORO | 70.8 | 21.62 | 40.95 | cpu-small | 72 | 94% |
| 8 | sn21 AdTAO | 70.2 | 14.16 | 605 | cpu-small | 14 | 45% |
| 9 | sn56 Gradients | 68.3 | 451 | 1,074 | rtx4090* | 7 | 70% |
| 10 | sn96 Verathos | 68.3 | 22.36 | 166 | rtx4090 | 79 | 41% |
| 11 | sn80 OpenRoboto | 67.8 | 384 | 1,737 | rtx4090* | 5 | 71% |
| 12 | sn91 cascade | 67 | 309 | 626 | rtx4090* | 5 | 52% |
| 13 | sn124 Swarm | 66.6 | 281 | 911 | rtx4090* | 25 | 11% |
| 14 | sn79 MVTRX | 66.1 | 4.25 | 420 | cpu-small | 228 | 9% |
| 15 | sn81 Reliquary | 65.3 | 182 | 282 | rtx4090* | 28 | 6% |
| 16 | sn108 Prometheon | 65.2 | 176 | 439 | rtx4090* | 9 | 23% |
| 17 | sn61 RedTeam | 64.8 | 155 | 230 | rtx4090* | 40 | 4% |
| 18 | sn107 Minos | 64.5 | 126 | 36,950 | cpu-small | 20 | 90% |
| 19 | sn54 Yanez | 64.1 | 6.39 | 1,041 | a4000 | 101 | 35% |
| 20 | sn121 sundae_bar | 63 | 1,238 | 1,238 = | cpu-small | 2 | 60% |

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
| concentrated (30–60%) | 21 |
| dominated (60–90%) | 16 |
| captured (>90%) | 30 |

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
| 2026-08-29T15:10 | sn49 | BURN_DROP | sn49 burn fell 0.990 -> 0.000 - miners can earn again |
| 2026-08-29T15:10 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: chore(config): shorten validator query i |
| 2026-08-29T10:19 | sn25 | RELEASE | sn25 released v2026.8.28-1031763440 |
| 2026-08-29T10:19 | sn47 | SCORING_COMMIT | sn47 commit touches scoring: rollout verification rules |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

