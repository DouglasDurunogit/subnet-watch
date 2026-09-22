# Subnet watch — dashboard

_snapshot 2026-09-22T17:19:29Z · block 9124591 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 59 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 97 | `miner_burn` < 0.99 |
| Ranked | 97 | passed every gate |
| **Positive margin** | **59** | income beats machine cost |
| New events this window | 5 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 66 | `████████████████████████████` |
| 0–0.2 | 8 | `███` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 31 | `█████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn4 Targon | 78.5 | 9,370 | 26,309 | rtx4090* | 6 | 53% |
| 2 | sn3 Teutonic | 76.8 | 5,605 | 5,605 = | rtx4090* | 5 | 20% |
| 3 | sn91 cascade | 72.8 | 657 | 2,633 | cpu-small | 5 | 52% |
| 4 | sn102 ConnitoAI | 69.6 | 660 | 2,319 | rtx4090* | 5 | 47% |
| 5 | sn67 Harnyx | 69.5 | 10.81 | 1,368 | cpu-small | 126 | 37% |
| 6 | sn107 Minos | 68.9 | 355 | 29,873 | cpu-small | 20 | 80% |
| 7 | sn38 ChronoLLM | 68.2 | 187 | 2,541 | cpu-small | 10 | 52% |
| 8 | sn15 ORO | 68.1 | 11.74 | 24.13 | cpu-small | 64 | 96% |
| 9 | sn124 Swarm | 67.1 | 324 | 1,032 | rtx4090* | 25 | 11% |
| 10 | sn111 Claims | 66.4 | 268 | 3,171 | rtx4090* | 5 | 75% |
| 11 | sn28 SayGM | 62.4 | 79.02 | 1,531 | rtx4090* | 66 | 11% |
| 12 | sn74 Gittensor | 62.1 | 73.92 | 317 | rtx4090* | 13 | 63% |
| 13 | sn56 Gradients | 62.1 | 69.49 | 5,878 | rtx4090* | 18 | 40% |
| 14 | sn62 Ridges | 61.6 | 59.69 | 2,912 | rtx4090* | 19 | 30% |
| 15 | sn23 Trishool | 61.5 | 781 | 781 = | cpu-small | 2 | 80% |
| 16 | sn60 Bitsec.ai | 60.4 | 572 | 572 = | cpu-small | 3 | 50% |
| 17 | sn61 RedTeam | 59.1 | 29.47 | 819 | rtx4090* | 116 | 9% |
| 18 | sn14 Cacheon | 58.7 | 24.48 | 4,998 | rtx4090* | 15 | 61% |
| 19 | sn81 Reliquary | 58.5 | 23.01 | 85.65 | rtx4090* | 24 | 86% |
| 20 | sn51 lium.io | 58.2 | 32.07 | 1,858 | rtx4090* | 67 | 84% |

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
| wide (<30%) | 22 |
| concentrated (30–60%) | 25 |
| dominated (60–90%) | 21 |
| captured (>90%) | 26 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 98 |
| README keywords (GUESS) | 10 |
| min_compute.yml (curated) | 10 |
| code-submission (validator runs it) | 9 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-09-22T17:19 | sn1 | RELEASE | sn1 released v4.4.8 |
| 2026-09-22T17:19 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Make miner fault recovery durable and rec |
| 2026-09-22T17:19 | sn50 | RELEASE | sn50 released v1.13.0 |
| 2026-09-22T17:19 | sn74 | RELEASE | sn74 released release-20260922-171907 |
| 2026-09-22T17:19 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: rollouts: affine_gen_v1 shared store/tea |
| 2026-09-22T06:50 | sn15 | RELEASE | sn15 released v2.0.29 |
| 2026-09-22T06:50 | sn25 | RELEASE | sn25 released v2026.9.21-1052448720 |
| 2026-09-22T06:50 | sn26 | SCORING_COMMIT | sn26 commit touches scoring: fix: commitment snapshot carries the mode |
| 2026-09-22T06:50 | sn45 | SCORING_COMMIT | sn45 commit touches scoring: Owe a share again to a miner sent nothing |
| 2026-09-22T06:50 | sn51 | RELEASE | sn51 released executor-v1.134 |
| 2026-09-22T06:50 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-09-22T06:50 | sn78 | RELEASE | sn78 released Cohort 4 miner connection inputs (policy 8) |
| 2026-09-22T06:50 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Publish current C4 miner setup and verifi |
| 2026-09-22T06:50 | sn78 | README_TASK_DIFF | sn78 README task/scoring sections changed |
| 2026-09-22T06:50 | sn100 | BURN_DROP | sn100 burn fell 1.000 -> 0.803 - miners can earn again |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

