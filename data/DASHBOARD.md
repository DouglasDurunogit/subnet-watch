# Subnet watch — dashboard

_snapshot 2026-09-15T00:50:57Z · block 9069569 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 54 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 90 | `miner_burn` < 0.99 |
| Ranked | 91 | passed every gate |
| **Positive margin** | **54** | income beats machine cost |
| New events this window | 2 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 63 | `████████████████████████████` |
| 0–0.2 | 9 | `████` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 6 | `███` |
| 0.8–0.99 | 2 | `█` |
| ≥0.99 dead | 38 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn92 MicroTensor | 80.8 | 195 | 587 | cpu-small | 8 | 30% |
| 2 | sn91 cascade | 74.2 | 1,003 | 2,678 | cpu-small | 5 | 52% |
| 3 | sn1 Apex | 70.1 | 763 | 932 | rtx4090* | 4 | 55% |
| 4 | sn67 Harnyx | 69.2 | 10.49 | 10.49 = | cpu-small | 217 | 16% |
| 5 | sn107 Minos | 69.1 | 365 | 29,631 | cpu-small | 20 | 80% |
| 6 | sn96 Verathos | 68.6 | 23.91 | 215 | rtx4090 | 81 | 33% |
| 7 | sn11 TrajectoryRL | 68.1 | 5,695 | 5,695 = | cpu-small | 1 | 100% |
| 8 | sn38 ChronoLLM | 68 | 173 | 3,666 | cpu-small | 10 | 52% |
| 9 | sn80 OpenRoboto | 67.6 | 365 | 1,298 | rtx4090* | 5 | 43% |
| 10 | sn111 Claims | 67.1 | 330 | 1,485 | rtx4090* | 5 | 42% |
| 11 | sn124 Swarm | 66.4 | 263 | 852 | rtx4090* | 25 | 11% |
| 12 | sn3 Teutonic | 63.8 | 4,057 | 4,057 = | rtx4090* | 5 | 20% |
| 13 | sn61 RedTeam | 63.6 | 111 | 170 | rtx4090* | 95 | 2% |
| 14 | sn28 SayGM | 62.8 | 88.11 | 2,666 | rtx4090* | 47 | 17% |
| 15 | sn55 NIOME | 61.9 | 66.63 | 552 | rtx4090* | 11 | 29% |
| 16 | sn23 Trishool | 60.2 | 543 | 543 = | cpu-small | 2 | 80% |
| 17 | sn62 Ridges | 60.2 | 38.72 | 1,146 | rtx4090* | 18 | 35% |
| 18 | sn74 Gittensor | 59.2 | 31.92 | 186 | rtx4090 | 9 | 64% |
| 19 | sn81 Reliquary | 59.2 | 28.60 | 225 | rtx4090* | 89 | 5% |
| 20 | sn51 lium.io | 58.9 | 34.94 | 1,519 | rtx4090* | 62 | 81% |

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
| dominated (60–90%) | 15 |
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
| 2026-09-15T00:51 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Refresh reviewed scorer workflow protecti |
| 2026-09-15T00:51 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: Merge pull request #267 from reliquadotai |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

