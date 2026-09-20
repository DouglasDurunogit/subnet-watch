# Subnet watch — dashboard

_snapshot 2026-09-20T09:45:10Z · block 9107962 · run_status **ok**_

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
| New events this window | 5 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 61 | `████████████████████████████` |
| 0–0.2 | 9 | `████` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 35 | `████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn4 Targon | 77.9 | 7,712 | 21,650 | rtx4090* | 6 | 52% |
| 2 | sn3 Teutonic | 76.1 | 4,617 | 4,617 = | rtx4090* | 5 | 20% |
| 3 | sn69 Herald | 72.9 | 1,781 | 1,781 = | rtx4090* | 3 | 33% |
| 4 | sn91 cascade | 71.7 | 473 | 1,262 | cpu-small | 5 | 52% |
| 5 | sn67 Harnyx | 70.7 | 14.71 | 380 | cpu-small | 127 | 12% |
| 6 | sn1 Apex | 69.7 | 678 | 898 | rtx4090* | 4 | 61% |
| 7 | sn102 ConnitoAI | 68.6 | 489 | 1,434 | rtx4090* | 7 | 31% |
| 8 | sn56 Gradients | 68.4 | 460 | 5,440 | rtx4090* | 9 | 46% |
| 9 | sn107 Minos | 68.3 | 305 | 25,867 | cpu-small | 20 | 80% |
| 10 | sn15 ORO | 67.7 | 9.15 | 18.66 | cpu-small | 60 | 97% |
| 11 | sn124 Swarm | 66.4 | 264 | 846 | rtx4090* | 25 | 11% |
| 12 | sn111 Claims | 66 | 236 | 2,591 | rtx4090* | 5 | 74% |
| 13 | sn38 ChronoLLM | 66 | 102 | 903 | cpu-small | 10 | 52% |
| 14 | sn74 Gittensor | 62.4 | 79.25 | 261 | rtx4090* | 11 | 61% |
| 15 | sn28 SayGM | 62.3 | 76.59 | 1,145 | rtx4090* | 62 | 13% |
| 16 | sn62 Ridges | 60.8 | 47.61 | 1,627 | rtx4090* | 18 | 33% |
| 17 | sn81 Reliquary | 58.9 | 26.14 | 82.57 | rtx4090* | 30 | 78% |
| 18 | sn51 lium.io | 58.1 | 29.88 | 2,081 | rtx4090* | 68 | 80% |
| 19 | sn61 RedTeam | 57.6 | 17.61 | 1,643 | rtx4090* | 130 | 20% |
| 20 | sn14 Cacheon | 57.3 | 584 | 1,901 | rtx4090* | 13 | 28% |

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
| concentrated (30–60%) | 26 |
| dominated (60–90%) | 20 |
| captured (>90%) | 22 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 98 |
| min_compute.yml (curated) | 11 |
| code-submission (validator runs it) | 9 |
| README keywords (GUESS) | 9 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-09-20T09:45 | sn11 | BURN_DROP | sn11 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-09-20T09:45 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Add Sep20 authority-preserving scoring re |
| 2026-09-20T09:45 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Reuse validated reserved publications acr |
| 2026-09-20T09:45 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: trainer: one GPU type per manifest — drop |
| 2026-09-20T09:45 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: feat(bounty): activate proportional vali |
| 2026-09-20T04:52 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Seal September 20 verifier and runtime re |
| 2026-09-20T00:07 | sn74 | RELEASE | sn74 released release-20260919-231145 |
| 2026-09-19T21:48 | sn11 | SCORING_COMMIT | sn11 commit touches scoring: Merge pull request #328 from trajectoryRL |
| 2026-09-19T21:48 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Retry proved miner-funded Responses throt |
| 2026-09-19T19:37 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Read retained validator runtime through r |
| 2026-09-19T19:37 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Bound uncontended dispatch by the longest |
| 2026-09-19T17:29 | sn11 | SCORING_COMMIT | sn11 commit touches scoring: docs: Season 2 pass over the public docs  |
| 2026-09-19T17:29 | sn11 | README_TASK_DIFF | sn11 README task/scoring sections changed |
| 2026-09-19T17:29 | sn34 | SCORING_COMMIT | sn34 commit touches scoring: Merge testnet into reward fix; retain rel |
| 2026-09-19T17:29 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Route Luna across verified Azure regions |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

