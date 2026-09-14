# Subnet watch — dashboard

_snapshot 2026-09-14T22:26:29Z · block 9068849 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 52 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 90 | `miner_burn` < 0.99 |
| Ranked | 91 | passed every gate |
| **Positive margin** | **52** | income beats machine cost |
| New events this window | 5 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 62 | `████████████████████████████` |
| 0–0.2 | 10 | `█████` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 6 | `███` |
| 0.8–0.99 | 2 | `█` |
| ≥0.99 dead | 38 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn92 MicroTensor | 80.8 | 197 | 592 | cpu-small | 8 | 30% |
| 2 | sn91 cascade | 74.3 | 1,019 | 2,718 | cpu-small | 5 | 52% |
| 3 | sn1 Apex | 70.2 | 781 | 951 | rtx4090* | 4 | 54% |
| 4 | sn67 Harnyx | 69.4 | 10.67 | 10.67 = | cpu-small | 218 | 16% |
| 5 | sn107 Minos | 68.9 | 349 | 29,658 | cpu-small | 20 | 80% |
| 6 | sn96 Verathos | 68.4 | 22.83 | 211 | rtx4090 | 81 | 33% |
| 7 | sn38 ChronoLLM | 68.1 | 175 | 3,721 | cpu-small | 10 | 52% |
| 8 | sn80 OpenRoboto | 67.7 | 375 | 1,335 | rtx4090* | 5 | 43% |
| 9 | sn111 Claims | 67.1 | 332 | 1,495 | rtx4090* | 5 | 42% |
| 10 | sn124 Swarm | 66.4 | 265 | 858 | rtx4090* | 25 | 11% |
| 11 | sn28 SayGM | 64.8 | 158 | 2,754 | rtx4090* | 41 | 17% |
| 12 | sn61 RedTeam | 64 | 127 | 194 | rtx4090* | 96 | 2% |
| 13 | sn3 Teutonic | 63.8 | 4,078 | 4,078 = | rtx4090* | 5 | 20% |
| 14 | sn55 NIOME | 62 | 67.69 | 561 | rtx4090* | 11 | 29% |
| 15 | sn23 Trishool | 60.3 | 548 | 548 = | cpu-small | 2 | 80% |
| 16 | sn62 Ridges | 60.2 | 39.09 | 1,156 | rtx4090* | 18 | 35% |
| 17 | sn81 Reliquary | 59.9 | 35.67 | 222 | rtx4090* | 88 | 5% |
| 18 | sn102 ConnitoAI | 59 | 983 | 1,522 | rtx4090* | 5 | 32% |
| 19 | sn74 Gittensor | 58.6 | 27.05 | 187 | rtx4090 | 10 | 64% |
| 20 | sn51 lium.io | 58.4 | 31.13 | 1,402 | rtx4090* | 63 | 86% |

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
| concentrated (30–60%) | 25 |
| dominated (60–90%) | 14 |
| captured (>90%) | 22 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 95 |
| README keywords (GUESS) | 11 |
| min_compute.yml (curated) | 11 |
| code-submission (validator runs it) | 10 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-09-14T22:27 | sn62 | SCORING_COMMIT | sn62 commit touches scoring: add PublicEvaluationRun model |
| 2026-09-14T22:27 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Refresh protected source for verified par |
| 2026-09-14T22:27 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: docs(miner): credential path leads INSTAL |
| 2026-09-14T22:27 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Publish runtime-independent validator hos |
| 2026-09-14T22:27 | sn111 | RELEASE | sn111 released v0.2.0 |
| 2026-09-14T18:48 | sn1 | RELEASE | sn1 released v4.4.6 |
| 2026-09-14T18:48 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: scoring: the settle schedule is 10 / 17 / |
| 2026-09-14T18:48 | sn25 | RELEASE | sn25 released v2026.9.14-1046068620 |
| 2026-09-14T18:48 | sn40 | README_TASK_DIFF | sn40 README task/scoring sections changed |
| 2026-09-14T18:48 | sn45 | SCORING_COMMIT | sn45 commit touches scoring: Ignore per-validator runtime state and se |
| 2026-09-14T18:48 | sn50 | SCORING_COMMIT | sn50 commit touches scoring: feat(validator): add a volatility CRPS te |
| 2026-09-14T18:48 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-3457 - [P1] validator: a UUID listed  |
| 2026-09-14T18:48 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Verify retained weight reveals on runtime |
| 2026-09-14T18:48 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: Merge pull request #1 from heroncovelabs/ |
| 2026-09-14T18:48 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Retire verified redundant successor mater |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

