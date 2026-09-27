# Subnet watch — dashboard

_snapshot 2026-09-27T10:39:38Z · block 9158586 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 54 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 95 | `miner_burn` < 0.99 |
| Ranked | 95 | passed every gate |
| **Positive margin** | **54** | income beats machine cost |
| New events this window | 5 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 64 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 8 | `████` |
| 0.4–0.6 | 2 | `█` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 33 | `██████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn91 cascade | 71.7 | 481 | 1,285 | cpu-small | 5 | 52% |
| 2 | sn1 Apex | 71.3 | 1,096 | 1,209 | rtx4090* | 4 | 55% |
| 3 | sn38 ChronoLLM | 70.5 | 357 | 3,141 | cpu-small | 10 | 52% |
| 4 | sn67 Harnyx | 70.1 | 12.68 | 1,302 | cpu-small | 111 | 35% |
| 5 | sn102 ConnitoAI | 69.9 | 719 | 1,779 | rtx4090* | 7 | 28% |
| 6 | sn56 Gradients | 69.5 | 635 | 6,169 | rtx4090* | 8 | 40% |
| 7 | sn15 ORO | 69.5 | 14.21 | 22,331 | cpu-small | 74 | 95% |
| 8 | sn107 Minos | 69.4 | 399 | 31,546 | cpu-small | 20 | 79% |
| 9 | sn96 Verathos | 68.8 | 25.72 | 247 | rtx4090 | 76 | 30% |
| 10 | sn4 Targon | 68.6 | 16,940 | 30,640 | rtx4090* | 5 | 58% |
| 11 | sn111 Claims | 67.2 | 342 | 3,057 | rtx4090* | 5 | 70% |
| 12 | sn124 Swarm | 67.2 | 338 | 1,015 | rtx4090* | 25 | 11% |
| 13 | sn3 Teutonic | 65 | 5,787 | 5,787 = | rtx4090* | 5 | 20% |
| 14 | sn62 Ridges | 64.1 | 127 | 1,351 | rtx4090* | 25 | 14% |
| 15 | sn14 Cacheon | 63.7 | 112 | 2,580 | rtx4090* | 14 | 30% |
| 16 | sn23 Trishool | 62.4 | 1,025 | 1,025 = | cpu-small | 2 | 80% |
| 17 | sn61 RedTeam | 62.2 | 72.79 | 279 | rtx4090* | 128 | 2% |
| 18 | sn28 SayGM | 61 | 52.05 | 1,013 | rtx4090* | 71 | 37% |
| 19 | sn100 Cortex | 60.2 | 39.52 | 2,560 | rtx4090* | 18 | 70% |
| 20 | sn51 lium.io | 59.3 | 41.94 | 3,145 | rtx4090* | 68 | 76% |

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
| concentrated (30–60%) | 22 |
| dominated (60–90%) | 21 |
| captured (>90%) | 24 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 97 |
| README keywords (GUESS) | 11 |
| min_compute.yml (curated) | 10 |
| code-submission (validator runs it) | 9 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-09-27T10:40 | sn15 | RELEASE | sn15 released v2.0.34: Authorize inference without a shared Compose mo |
| 2026-09-27T10:40 | sn61 | RELEASE | sn61 released 4.10.7 |
| 2026-09-27T10:40 | sn61 | SCORING_COMMIT | sn61 commit touches scoring: Merge pull request #149 from RedTeamSubne |
| 2026-09-27T10:40 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Bind verifier evidence continuity to revi |
| 2026-09-27T10:40 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: wvk 25 δ fork: flip time 08:35 UTC in AG |
| 2026-09-27T05:12 | sn25 | RELEASE | sn25 released v2026.9.26-1056759680 |
| 2026-09-27T05:12 | sn34 | SCORING_COMMIT | sn34 commit touches scoring: Merge pull request #464 from BitMind-AI/d |
| 2026-09-27T05:12 | sn34 | README_TASK_DIFF | sn34 README task/scoring sections changed |
| 2026-09-27T05:12 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Preserve fresh investigation budget when  |
| 2026-09-26T23:56 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Bind verified homepage navigation source |
| 2026-09-26T21:37 | sn15 | RELEASE | sn15 released v2.0.32: fix(validator): save downloaded agent source as |
| 2026-09-26T21:37 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: fix(validator): save downloaded agent sou |
| 2026-09-26T21:37 | sn25 | RELEASE | sn25 released v2026.9.26-1056505490 |
| 2026-09-26T21:37 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Reuse verified investigator source for at |
| 2026-09-26T18:34 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Bind protected manifest to evidence quali |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

