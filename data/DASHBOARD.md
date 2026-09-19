# Subnet watch — dashboard

_snapshot 2026-09-19T19:36:52Z · block 9103772 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 58 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 94 | `miner_burn` < 0.99 |
| Ranked | 94 | passed every gate |
| **Positive margin** | **58** | income beats machine cost |
| New events this window | 2 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 60 | `████████████████████████████` |
| 0–0.2 | 10 | `█████` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 34 | `████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn4 Targon | 78 | 8,009 | 22,484 | rtx4090* | 6 | 52% |
| 2 | sn3 Teutonic | 76.5 | 5,112 | 5,112 = | rtx4090* | 5 | 20% |
| 3 | sn69 Herald | 73.1 | 1,846 | 1,846 = | rtx4090* | 3 | 33% |
| 4 | sn91 cascade | 72.8 | 657 | 2,630 | cpu-small | 5 | 52% |
| 5 | sn102 ConnitoAI | 70.9 | 962 | 1,422 | rtx4090* | 6 | 29% |
| 6 | sn1 Apex | 70.1 | 768 | 996 | rtx4090* | 4 | 58% |
| 7 | sn67 Harnyx | 69.6 | 10.89 | 1,034 | cpu-small | 124 | 33% |
| 8 | sn107 Minos | 68.8 | 339 | 28,731 | cpu-small | 20 | 80% |
| 9 | sn56 Gradients | 68.5 | 477 | 5,631 | rtx4090* | 9 | 46% |
| 10 | sn111 Claims | 66.6 | 286 | 2,566 | rtx4090* | 5 | 70% |
| 11 | sn124 Swarm | 66.6 | 278 | 871 | rtx4090* | 25 | 11% |
| 12 | sn38 ChronoLLM | 66 | 102 | 904 | cpu-small | 10 | 52% |
| 13 | sn15 ORO | 62.2 | 4.00 | 7.99 | cpu-small | 22 | 100% |
| 14 | sn28 SayGM | 61.9 | 66.83 | 2,540 | rtx4090* | 61 | 16% |
| 15 | sn62 Ridges | 61 | 50.15 | 3,543 | rtx4090* | 17 | 42% |
| 16 | sn23 Trishool | 60.9 | 670 | 670 = | cpu-small | 2 | 80% |
| 17 | sn74 Gittensor | 60.5 | 46.65 | 207 | rtx4090* | 11 | 63% |
| 18 | sn81 Reliquary | 59.5 | 31.82 | 95.82 | rtx4090* | 29 | 74% |
| 19 | sn61 RedTeam | 58.7 | 25.49 | 2,136 | rtx4090* | 130 | 20% |
| 20 | sn51 lium.io | 58.3 | 31.19 | 2,062 | rtx4090* | 69 | 82% |

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
| concentrated (30–60%) | 25 |
| dominated (60–90%) | 19 |
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
| 2026-09-19T19:37 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Read retained validator runtime through r |
| 2026-09-19T19:37 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Bound uncontended dispatch by the longest |
| 2026-09-19T17:29 | sn11 | SCORING_COMMIT | sn11 commit touches scoring: docs: Season 2 pass over the public docs  |
| 2026-09-19T17:29 | sn11 | README_TASK_DIFF | sn11 README task/scoring sections changed |
| 2026-09-19T17:29 | sn34 | SCORING_COMMIT | sn34 commit touches scoring: Merge testnet into reward fix; retain rel |
| 2026-09-19T17:29 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Route Luna across verified Azure regions |
| 2026-09-19T14:37 | sn11 | SCORING_COMMIT | sn11 commit touches scoring: docs(roadmap): the protocol (objective =  |
| 2026-09-19T14:37 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Bind rerun316 to fixed scorer image |
| 2026-09-19T11:19 | sn10 | BURN_DROP | sn10 burn fell 1.000 -> 0.830 - miners can earn again |
| 2026-09-19T11:19 | sn11 | RELEASE | sn11 released v0.7.0 |
| 2026-09-19T11:19 | sn11 | SCORING_COMMIT | sn11 commit touches scoring: Season 2 (transition): routing-policy eva |
| 2026-09-19T11:19 | sn25 | RELEASE | sn25 released v2026.9.19-1050096260 |
| 2026-09-19T11:19 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Pass saved stage evidence to Arena verifi |
| 2026-09-19T11:19 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: fix(price): publish the target miners are |
| 2026-09-19T11:19 | sn112 | BURN_DROP | sn112 burn fell 1.000 -> 0.867 - miners can earn again |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

