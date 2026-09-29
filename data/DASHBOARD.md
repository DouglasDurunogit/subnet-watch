# Subnet watch — dashboard

_snapshot 2026-09-29T07:13:48Z · block 9171956 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 0 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 97 | `miner_burn` < 0.99 |
| Ranked | 97 | passed every gate |
| **Positive margin** | **0** | income beats machine cost |
| New events this window | 4 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 68 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 6 | `██` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 6 | `██` |
| ≥0.99 dead | 31 | `█████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn67 Harnyx | 50 | n/a | n/a | cpu-small | 120 | 38% |
| 2 | sn41 Almanac | 50 | n/a | n/a | cpu-small | 119 | 2% |
| 3 | sn21 AdTAO | 50 | n/a | n/a | cpu-small | 20 | 40% |
| 4 | sn15 ORO | 50 | n/a | n/a | cpu-small | 76 | 95% |
| 5 | sn96 Verathos | 46.2 | n/a | n/a | rtx4090 | 75 | 30% |
| 6 | sn26 Perturb | 46.2 | n/a | n/a | rtx3060 | 5 | 90% |
| 7 | sn91 cascade | 42.5 | n/a | n/a | cpu-small | 5 | 52% |
| 8 | sn81 Reliquary | 39.3 | n/a | n/a | rtx4090* | 35 | 81% |
| 9 | sn100 Cortex | 39.3 | n/a | n/a | rtx4090* | 26 | 70% |
| 10 | sn14 Cacheon | 39.3 | n/a | n/a | rtx4090* | 15 | 29% |
| 11 | sn56 Gradients | 39.3 | n/a | n/a | rtx4090* | 12 | 39% |
| 12 | sn1 Apex | 39.3 | n/a | n/a | rtx4090* | 4 | 52% |
| 13 | sn9 iota | 39.3 | n/a | n/a | rtx4090* | 2 | 74% |
| 14 | sn71 Leadpoet | 39.3 | n/a | n/a | rtx4090* | 2 | 71% |
| 15 | sn69 Herald | 39.3 | n/a | n/a | rtx4090* | 1 | 100% |
| 16 | sn45 AlphaRidge.ai | 39.3 | n/a | n/a | rtx4090* | 240 | 55% |
| 17 | sn62 Ridges | 39.3 | n/a | n/a | rtx4090* | 26 | 13% |
| 18 | sn88 Investing | 39.3 | n/a | n/a | rtx4090* | 71 | 44% |
| 19 | sn61 RedTeam | 39.3 | n/a | n/a | rtx4090* | 86 | 3% |
| 20 | sn102 ConnitoAI | 39.3 | n/a | n/a | rtx4090* | 6 | 33% |

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
| concentrated (30–60%) | 23 |
| dominated (60–90%) | 23 |
| captured (>90%) | 25 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 96 |
| README keywords (GUESS) | 12 |
| min_compute.yml (curated) | 10 |
| code-submission (validator runs it) | 9 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-09-29T07:14 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-2870 - [P2] protocol 1.4.0: pod_ssh a |
| 2026-09-29T07:14 | sn51 | README_TASK_DIFF | sn51 README task/scoring sections changed |
| 2026-09-29T07:14 | sn61 | RELEASE | sn61 released 4.10.8 |
| 2026-09-29T07:14 | sn61 | SCORING_COMMIT | sn61 commit touches scoring: refactor: move bot_virus to inactive chal |
| 2026-09-29T01:08 | sn15 | RELEASE | sn15 released v2.0.36: Send validator heartbeats every eight seconds |
| 2026-09-29T01:08 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: Send validator heartbeats every eight sec |
| 2026-09-28T21:19 | sn20 | SCORING_COMMIT | sn20 commit touches scoring: Allow verified Archive download mirrors f |
| 2026-09-28T21:19 | sn34 | SCORING_COMMIT | sn34 commit touches scoring: Show recent chain-verified reveals alongs |
| 2026-09-28T21:19 | sn45 | SCORING_COMMIT | sn45 commit touches scoring: Skip a validation sample when the validat |
| 2026-09-28T21:19 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-3804 - [P1] validator: a new node is  |
| 2026-09-28T21:19 | sn94 | RELEASE | sn94 released Cathedral static TDX verifier cathedral-tdx-verifier-v1. |
| 2026-09-28T21:19 | sn94 | SCORING_COMMIT | sn94 commit touches scoring: docs: state what the TDX and SNP validato |
| 2026-09-28T21:19 | sn94 | README_TASK_DIFF | sn94 README task/scoring sections changed |
| 2026-09-28T21:19 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: feat(master): send the completed epoch's |
| 2026-09-28T21:19 | sn121 | BURN_DROP | sn121 burn fell 1.000 -> 0.600 - miners can earn again |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

