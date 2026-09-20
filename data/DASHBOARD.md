# Subnet watch — dashboard

_snapshot 2026-09-20T04:51:57Z · block 9106517 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 57 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 92 | `miner_burn` < 0.99 |
| Ranked | 92 | passed every gate |
| **Positive margin** | **57** | income beats machine cost |
| New events this window | 1 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 58 | `████████████████████████████` |
| 0–0.2 | 11 | `█████` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 36 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn4 Targon | 77.8 | 7,655 | 21,492 | rtx4090* | 6 | 52% |
| 2 | sn3 Teutonic | 76.1 | 4,534 | 4,534 = | rtx4090* | 5 | 20% |
| 3 | sn69 Herald | 72.9 | 1,763 | 1,763 = | rtx4090* | 3 | 33% |
| 4 | sn91 cascade | 71.6 | 469 | 1,251 | cpu-small | 5 | 52% |
| 5 | sn102 ConnitoAI | 71.1 | 1,024 | 1,218 | rtx4090* | 6 | 26% |
| 6 | sn67 Harnyx | 70.6 | 14.52 | 381 | cpu-small | 119 | 13% |
| 7 | sn1 Apex | 69.8 | 694 | 913 | rtx4090* | 4 | 59% |
| 8 | sn56 Gradients | 68.4 | 456 | 5,394 | rtx4090* | 9 | 46% |
| 9 | sn107 Minos | 68.2 | 299 | 25,351 | cpu-small | 20 | 80% |
| 10 | sn15 ORO | 67.6 | 8.88 | 18.15 | cpu-small | 60 | 97% |
| 11 | sn111 Claims | 66.5 | 273 | 2,450 | rtx4090* | 5 | 70% |
| 12 | sn124 Swarm | 66.4 | 263 | 841 | rtx4090* | 25 | 11% |
| 13 | sn38 ChronoLLM | 65.9 | 98.22 | 869 | cpu-small | 10 | 52% |
| 14 | sn28 SayGM | 61.7 | 64.42 | 1,354 | rtx4090* | 59 | 10% |
| 15 | sn74 Gittensor | 61.1 | 53.76 | 200 | rtx4090* | 11 | 61% |
| 16 | sn23 Trishool | 60.8 | 634 | 634 = | cpu-small | 2 | 80% |
| 17 | sn62 Ridges | 60.8 | 47.19 | 1,615 | rtx4090* | 18 | 33% |
| 18 | sn81 Reliquary | 58.6 | 24.21 | 83.86 | rtx4090* | 33 | 77% |
| 19 | sn51 lium.io | 58.2 | 30.09 | 2,100 | rtx4090* | 69 | 81% |
| 20 | sn61 RedTeam | 57.5 | 17.44 | 1,616 | rtx4090* | 130 | 20% |

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
| captured (>90%) | 21 |

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
| 2026-09-19T14:37 | sn11 | SCORING_COMMIT | sn11 commit touches scoring: docs(roadmap): the protocol (objective =  |
| 2026-09-19T14:37 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Bind rerun316 to fixed scorer image |
| 2026-09-19T11:19 | sn10 | BURN_DROP | sn10 burn fell 1.000 -> 0.830 - miners can earn again |
| 2026-09-19T11:19 | sn11 | RELEASE | sn11 released v0.7.0 |
| 2026-09-19T11:19 | sn11 | SCORING_COMMIT | sn11 commit touches scoring: Season 2 (transition): routing-policy eva |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

