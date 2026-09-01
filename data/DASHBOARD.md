# Subnet watch — dashboard

_snapshot 2026-09-01T15:13:52Z · block 8973235 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 58 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 95 | `miner_burn` < 0.99 |
| Ranked | 95 | passed every gate |
| **Positive margin** | **58** | income beats machine cost |
| New events this window | 8 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 66 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 8 | `███` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 33 | `██████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn92 MicroTensor | 78.8 | 118 | 533 | cpu-small | 9 | 60% |
| 2 | sn107 Minos | 78.6 | 128 | 38,057 | cpu-small | 20 | 91% |
| 3 | sn3 Teutonic | 75.4 | 3,689 | 3,689 = | rtx4090* | 5 | 20% |
| 4 | sn76 Phylax | 74.8 | 43.35 | 91.45 | cpu-small | 21 | 20% |
| 5 | sn67 Harnyx | 72.4 | 22.99 | 1,179 | cpu-small | 125 | 32% |
| 6 | sn15 ORO | 71.4 | 26.09 | 21,044 | cpu-small | 66 | 93% |
| 7 | sn91 cascade | 69.9 | 723 | 2,916 | rtx4090* | 5 | 52% |
| 8 | sn96 Verathos | 69.4 | 28.47 | 144 | rtx4090 | 81 | 41% |
| 9 | sn102 ConnitoAI | 68.6 | 483 | 1,737 | rtx4090* | 7 | 31% |
| 10 | sn56 Gradients | 67.7 | 371 | 1,028 | rtx4090* | 7 | 71% |
| 11 | sn111 Claims | 67.1 | 330 | 2,954 | rtx4090* | 5 | 70% |
| 12 | sn124 Swarm | 66.5 | 267 | 868 | rtx4090* | 25 | 11% |
| 13 | sn61 RedTeam | 64.9 | 161 | 234 | rtx4090* | 47 | 3% |
| 14 | sn81 Reliquary | 64.5 | 145 | 230 | rtx4090* | 33 | 5% |
| 15 | sn79 MVTRX | 64.5 | 4.19 | 397 | cpu-small | 227 | 9% |
| 16 | sn21 AdTAO | 64.5 | 3.98 | 530 | cpu-small | 16 | 45% |
| 17 | sn60 Bitsec.ai | 64.2 | 1,750 | 1,750 = | cpu-small | 2 | 50% |
| 18 | sn54 Yanez | 63.5 | 5.21 | 923 | a4000 | 96 | 35% |
| 19 | sn55 NIOME | 62.4 | 76.85 | 630 | rtx4090* | 11 | 29% |
| 20 | sn101 Tag101 | 62.3 | 0.87 | 0.87 = | cpu-small | 241 | 90% |

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
| concentrated (30–60%) | 21 |
| dominated (60–90%) | 20 |
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
| 2026-09-01T15:14 | sn10 | BURN_DROP | sn10 burn fell 1.000 -> 0.922 - miners can earn again |
| 2026-09-01T15:14 | sn23 | SCORING_COMMIT | sn23 commit touches scoring: Merge pull request #51 from TrishoolAI/q- |
| 2026-09-01T15:14 | sn92 | RELEASE | sn92 released v0.3.2 |
| 2026-09-01T15:14 | sn97 | SCORING_COMMIT | sn97 commit touches scoring: fix: Fixed private hotkey_already_validat |
| 2026-09-01T15:14 | sn107 | SCORING_COMMIT | sn107 commit touches scoring: Merge pull request #37 from minos-protoc |
| 2026-09-01T15:14 | sn107 | README_TASK_DIFF | sn107 README task/scoring sections changed |
| 2026-09-01T15:14 | sn108 | SCORING_COMMIT | sn108 commit touches scoring: docs(scoring): the split section still d |
| 2026-09-01T15:14 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: feat(scoring): cap minor-tier coverage a |
| 2026-09-01T10:31 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Verify carried conviction under its sourc |
| 2026-09-01T10:31 | sn63 | SCORING_COMMIT | sn63 commit touches scoring: Support multiple validations on single va |
| 2026-09-01T10:31 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-09-01T10:31 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: feat(selection): harden adaptive miner s |
| 2026-09-01T05:44 | sn80 | README_TASK_DIFF | sn80 README task/scoring sections changed |
| 2026-09-01T00:34 | sn25 | RELEASE | sn25 released v2026.8.31-1034210530 |
| 2026-09-01T00:34 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Batch carried fleet refresh verification |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

