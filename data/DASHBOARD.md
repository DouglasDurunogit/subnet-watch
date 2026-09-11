# Subnet watch — dashboard

_snapshot 2026-09-11T06:21:57Z · block 9042489 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 60 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 90 | `miner_burn` < 0.99 |
| Ranked | 91 | passed every gate |
| **Positive margin** | **60** | income beats machine cost |
| New events this window | 12 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 60 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 8 | `████` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 38 | `██████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn114 SOMA | 83.9 | 432 | 6,932 | cpu-small | 6 | 80% |
| 2 | sn92 MicroTensor | 78.5 | 108 | 327 | cpu-small | 9 | 50% |
| 3 | sn3 Teutonic | 75.7 | 4,085 | 4,085 = | rtx4090* | 5 | 20% |
| 4 | sn91 cascade | 71.4 | 1,132 | 3,031 | rtx4090* | 5 | 52% |
| 5 | sn67 Harnyx | 70.5 | 14.11 | 677 | cpu-small | 156 | 21% |
| 6 | sn102 ConnitoAI | 69.5 | 634 | 1,386 | rtx4090* | 7 | 26% |
| 7 | sn14 Cacheon | 69.4 | 618 | 1,146 | rtx4090* | 12 | 18% |
| 8 | sn107 Minos | 69.4 | 389 | 31,550 | cpu-small | 20 | 79% |
| 9 | sn96 Verathos | 69.3 | 28.05 | 282 | rtx4090 | 77 | 31% |
| 10 | sn56 Gradients | 68 | 414 | 5,371 | rtx4090* | 9 | 48% |
| 11 | sn80 OpenRoboto | 67.5 | 351 | 1,248 | rtx4090* | 5 | 43% |
| 12 | sn124 Swarm | 66.5 | 275 | 888 | rtx4090* | 25 | 11% |
| 13 | sn21 AdTAO | 66.3 | 5.95 | 110 | cpu-small | 16 | 45% |
| 14 | sn111 Claims | 66.2 | 253 | 3,115 | rtx4090* | 5 | 76% |
| 15 | sn38 ChronoLLM | 66.2 | 106 | 1,444 | cpu-small | 10 | 52% |
| 16 | sn61 RedTeam | 66.1 | 232 | 353 | rtx4090* | 51 | 3% |
| 17 | sn121 sundae_bar | 62.8 | 1,148 | 1,148 = | cpu-small | 2 | 60% |
| 18 | sn108 Prometheon | 62.6 | 80.77 | 259 | rtx4090* | 13 | 27% |
| 19 | sn28 SayGM | 61.5 | 59.27 | 4,193 | rtx4090* | 38 | 29% |
| 20 | sn41 Almanac | 60.5 | 40.02 | 115 | cpu-small | 81 | 3% |

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
| wide (<30%) | 26 |
| concentrated (30–60%) | 24 |
| dominated (60–90%) | 18 |
| captured (>90%) | 19 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 96 |
| min_compute.yml (curated) | 11 |
| code-submission (validator runs it) | 10 |
| README keywords (GUESS) | 10 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-09-11T06:22 | sn7 | RELEASE | sn7 released release-20260911-013831 |
| 2026-09-11T06:22 | sn7 | SCORING_COMMIT | sn7 commit touches scoring: Miner wizard: funding step, one shared EVM |
| 2026-09-11T06:22 | sn7 | README_TASK_DIFF | sn7 README task/scoring sections changed |
| 2026-09-11T06:22 | sn15 | RELEASE | sn15 released v2.0.4 |
| 2026-09-11T06:22 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Honor transition limits for typed validat |
| 2026-09-11T06:22 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-3019 - [P1] validator reports verific |
| 2026-09-11T06:22 | sn53 | SCORING_COMMIT | sn53 commit touches scoring: Merge pull request #47 from hanlinai/fix/ |
| 2026-09-11T06:22 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-09-11T06:22 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Fix normal validator dependency and distr |
| 2026-09-11T06:22 | sn71 | README_TASK_DIFF | sn71 README task/scoring sections changed |
| 2026-09-11T06:22 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Harden validator supervisor container sta |
| 2026-09-11T06:22 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: fix(proof): retain failed experiment vms |
| 2026-09-11T01:19 | sn20 | BURN_DROP | sn20 burn fell 1.000 -> 0.770 - miners can earn again |
| 2026-09-11T01:19 | sn36 | SCORING_COMMIT | sn36 commit touches scoring: Fix the private-upload commands in the mi |
| 2026-09-11T01:19 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Keep testnet Arena setup aligned with val |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

