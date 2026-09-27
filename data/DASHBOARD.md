# Subnet watch — dashboard

_snapshot 2026-09-27T15:20:08Z · block 9159989 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 60 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 95 | `miner_burn` < 0.99 |
| Ranked | 95 | passed every gate |
| **Positive margin** | **60** | income beats machine cost |
| New events this window | 4 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 61 | `████████████████████████████` |
| 0–0.2 | 10 | `█████` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 2 | `█` |
| 0.6–0.8 | 10 | `█████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 33 | `███████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn102 ConnitoAI | 71.9 | 1,297 | 1,733 | rtx4090* | 6 | 28% |
| 2 | sn91 cascade | 71.6 | 465 | 1,242 | cpu-small | 5 | 52% |
| 3 | sn1 Apex | 71.1 | 1,040 | 1,150 | rtx4090* | 4 | 56% |
| 4 | sn38 ChronoLLM | 70.2 | 324 | 2,848 | cpu-small | 10 | 52% |
| 5 | sn67 Harnyx | 70.1 | 12.25 | 1,262 | cpu-small | 113 | 35% |
| 6 | sn56 Gradients | 69.4 | 616 | 5,982 | rtx4090* | 8 | 40% |
| 7 | sn107 Minos | 68.9 | 355 | 30,779 | cpu-small | 20 | 80% |
| 8 | sn15 ORO | 68.9 | 13.69 | 21,572 | cpu-small | 74 | 95% |
| 9 | sn4 Targon | 68.5 | 16,405 | 29,673 | rtx4090* | 5 | 58% |
| 10 | sn96 Verathos | 68.3 | 22.60 | 231 | rtx4090 | 77 | 33% |
| 11 | sn111 Claims | 67.1 | 332 | 2,967 | rtx4090* | 5 | 70% |
| 12 | sn124 Swarm | 67.1 | 325 | 977 | rtx4090* | 25 | 11% |
| 13 | sn3 Teutonic | 64.9 | 5,609 | 5,609 = | rtx4090* | 5 | 20% |
| 14 | sn62 Ridges | 64 | 124 | 1,314 | rtx4090* | 25 | 14% |
| 15 | sn61 RedTeam | 63.9 | 121 | 350 | rtx4090* | 80 | 3% |
| 16 | sn14 Cacheon | 63.2 | 96.40 | 2,494 | rtx4090* | 14 | 30% |
| 17 | sn28 SayGM | 62.5 | 80.70 | 1,469 | rtx4090* | 62 | 16% |
| 18 | sn23 Trishool | 62.1 | 943 | 943 = | cpu-small | 2 | 80% |
| 19 | sn100 Cortex | 60.3 | 40.70 | 272 | rtx4090* | 19 | 68% |
| 20 | sn81 Reliquary | 59.5 | 31.49 | 121 | rtx4090* | 29 | 81% |

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
| dominated (60–90%) | 22 |
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
| 2026-09-27T15:20 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Bind verifier release to current Arena ba |
| 2026-09-27T15:20 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: perf(miner): default consensus review to |
| 2026-09-27T15:20 | sn111 | README_TASK_DIFF | sn111 README task/scoring sections changed |
| 2026-09-27T15:20 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Merge PR #78 (cursor/task-instruction-ga |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

