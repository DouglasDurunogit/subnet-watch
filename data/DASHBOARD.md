# Subnet watch — dashboard

_snapshot 2026-09-28T21:19:03Z · block 9168982 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 61 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 97 | `miner_burn` < 0.99 |
| Ranked | 97 | passed every gate |
| **Positive margin** | **61** | income beats machine cost |
| New events this window | 9 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 67 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 2 | `█` |
| 0.6–0.8 | 11 | `█████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 31 | `█████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn41 Almanac | 75.9 | 58.30 | 127 | cpu-small | 113 | 2% |
| 2 | sn102 ConnitoAI | 72.2 | 1,410 | 1,410 | rtx4090* | 4 | 25% |
| 3 | sn91 cascade | 72.2 | 553 | 2,214 | cpu-small | 5 | 52% |
| 4 | sn1 Apex | 71.3 | 1,077 | 1,182 | rtx4090* | 4 | 52% |
| 5 | sn26 Perturb | 70.5 | 38.89 | 124 | rtx3060 | 5 | 90% |
| 6 | sn67 Harnyx | 69.3 | 9.96 | 1,213 | cpu-small | 116 | 36% |
| 7 | sn107 Minos | 69 | 366 | 29,729 | cpu-small | 20 | 80% |
| 8 | sn96 Verathos | 68.2 | 22.18 | 225 | rtx4090 | 76 | 30% |
| 9 | sn15 ORO | 68.2 | 13.03 | 19,839 | cpu-small | 75 | 95% |
| 10 | sn111 Claims | 65.3 | 203 | 3,236 | rtx4090* | 5 | 80% |
| 11 | sn3 Teutonic | 64.6 | 5,160 | 5,160 = | rtx4090* | 5 | 20% |
| 12 | sn62 Ridges | 64.4 | 138 | 1,195 | rtx4090* | 26 | 13% |
| 13 | sn66 conjectures | 63.3 | 101 | 412 | rtx4090* | 4 | 81% |
| 14 | sn61 RedTeam | 63 | 91.11 | 261 | rtx4090* | 86 | 3% |
| 15 | sn23 Trishool | 61.9 | 893 | 893 = | cpu-small | 2 | 80% |
| 16 | sn14 Cacheon | 61.1 | 51.37 | 2,352 | rtx4090* | 14 | 30% |
| 17 | sn28 SayGM | 59.7 | 36.21 | 1,838 | rtx4090* | 69 | 36% |
| 18 | sn100 Cortex | 59.6 | 32.66 | 226 | rtx4090* | 19 | 70% |
| 19 | sn80 OpenRoboto | 59.2 | 1,016 | 3,144 | rtx4090* | 8 | 33% |
| 20 | sn74 Gittensor | 58.4 | 26.39 | 254 | rtx4090* | 20 | 62% |

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
| concentrated (30–60%) | 21 |
| dominated (60–90%) | 23 |
| captured (>90%) | 26 |

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
| 2026-09-28T21:19 | sn20 | SCORING_COMMIT | sn20 commit touches scoring: Allow verified Archive download mirrors f |
| 2026-09-28T21:19 | sn34 | SCORING_COMMIT | sn34 commit touches scoring: Show recent chain-verified reveals alongs |
| 2026-09-28T21:19 | sn45 | SCORING_COMMIT | sn45 commit touches scoring: Skip a validation sample when the validat |
| 2026-09-28T21:19 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-3804 - [P1] validator: a new node is  |
| 2026-09-28T21:19 | sn94 | RELEASE | sn94 released Cathedral static TDX verifier cathedral-tdx-verifier-v1. |
| 2026-09-28T21:19 | sn94 | SCORING_COMMIT | sn94 commit touches scoring: docs: state what the TDX and SNP validato |
| 2026-09-28T21:19 | sn94 | README_TASK_DIFF | sn94 README task/scoring sections changed |
| 2026-09-28T21:19 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: feat(master): send the completed epoch's |
| 2026-09-28T21:19 | sn121 | BURN_DROP | sn121 burn fell 1.000 -> 0.600 - miners can earn again |
| 2026-09-28T15:21 | sn20 | SCORING_COMMIT | sn20 commit touches scoring: Initialize public Witness subnet with bou |
| 2026-09-28T15:21 | sn26 | SCORING_COMMIT | sn26 commit touches scoring: fix: seed evaluation sampling from the pi |
| 2026-09-28T15:21 | sn28 | RELEASE | sn28 released v0.4.24 |
| 2026-09-28T15:21 | sn28 | SCORING_COMMIT | sn28 commit touches scoring: chore(release): promote gm-miner 0.4.24 ( |
| 2026-09-28T15:21 | sn41 | SCORING_COMMIT | sn41 commit touches scoring: Merge pull request #49 from corvxai/forec |
| 2026-09-28T15:21 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: NO-TICKET - [P1] validator: an idle node  |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

