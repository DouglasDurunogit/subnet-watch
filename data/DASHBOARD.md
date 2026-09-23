# Subnet watch — dashboard

_snapshot 2026-09-23T23:14:01Z · block 9133558 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 62 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 98 | `miner_burn` < 0.99 |
| Ranked | 98 | passed every gate |
| **Positive margin** | **62** | income beats machine cost |
| New events this window | 1 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 67 | `████████████████████████████` |
| 0–0.2 | 8 | `███` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 8 | `███` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 30 | `█████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn4 Targon | 80.1 | 14,823 | 26,812 | rtx4090* | 5 | 58% |
| 2 | sn3 Teutonic | 76.4 | 5,072 | 5,072 = | rtx4090* | 5 | 20% |
| 3 | sn91 cascade | 72.6 | 620 | 2,482 | cpu-small | 5 | 52% |
| 4 | sn114 SOMA | 72.1 | 748 | 7,488 | cpu-small | 8 | 50% |
| 5 | sn67 Harnyx | 71.1 | 16.24 | 1,125 | cpu-small | 124 | 34% |
| 6 | sn1 Apex | 70.3 | 804 | 1,016 | rtx4090* | 4 | 60% |
| 7 | sn56 Gradients | 69.1 | 559 | 5,442 | rtx4090* | 10 | 40% |
| 8 | sn15 ORO | 69 | 12.91 | 20,282 | cpu-small | 68 | 96% |
| 9 | sn107 Minos | 68.6 | 334 | 27,381 | cpu-small | 20 | 79% |
| 10 | sn38 ChronoLLM | 68.2 | 182 | 1,600 | cpu-small | 10 | 52% |
| 11 | sn124 Swarm | 66.8 | 298 | 948 | rtx4090* | 25 | 11% |
| 12 | sn14 Cacheon | 65.7 | 202 | 3,792 | rtx4090* | 11 | 50% |
| 13 | sn111 Claims | 65.6 | 221 | 2,999 | rtx4090* | 5 | 78% |
| 14 | sn100 Cortex | 63 | 90.16 | 149 | rtx4090* | 11 | 70% |
| 15 | sn23 Trishool | 61.7 | 829 | 829 = | cpu-small | 2 | 80% |
| 16 | sn28 SayGM | 61 | 52.32 | 738 | rtx4090* | 65 | 34% |
| 17 | sn62 Ridges | 61 | 50.50 | 2,081 | rtx4090* | 19 | 23% |
| 18 | sn74 Gittensor | 59.9 | 38.83 | 114 | rtx4090* | 18 | 63% |
| 19 | sn61 RedTeam | 58.4 | 23.38 | 619 | rtx4090* | 125 | 7% |
| 20 | sn80 OpenRoboto | 57.9 | 697 | 2,462 | rtx4090* | 5 | 43% |

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
| concentrated (30–60%) | 25 |
| dominated (60–90%) | 20 |
| captured (>90%) | 26 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 99 |
| min_compute.yml (curated) | 10 |
| code-submission (validator runs it) | 9 |
| README keywords (GUESS) | 9 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-09-23T23:14 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Merge PR #66 (cursor/band-backfill-outco |
| 2026-09-23T20:35 | sn14 | SCORING_COMMIT | sn14 commit touches scoring: Drain evaluation workers and remove redun |
| 2026-09-23T20:35 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: docs: correct local-test EnvPack size, fa |
| 2026-09-23T20:35 | sn25 | RELEASE | sn25 released v2026.9.23-1053868550 |
| 2026-09-23T20:35 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Preserve validator readback transport err |
| 2026-09-23T20:35 | sn28 | RELEASE | sn28 released v0.4.21-dev |
| 2026-09-23T20:35 | sn28 | SCORING_COMMIT | sn28 commit touches scoring: feat(image): route Chutes -TEE requests t |
| 2026-09-23T20:35 | sn28 | README_TASK_DIFF | sn28 README task/scoring sections changed |
| 2026-09-23T17:21 | sn9 | RELEASE | sn9 released v4.13.2 |
| 2026-09-23T17:21 | sn25 | RELEASE | sn25 released v2026.9.23-1053753970 |
| 2026-09-23T17:21 | sn97 | SCORING_COMMIT | sn97 commit touches scoring: chore: show float score instead of a 0/1  |
| 2026-09-23T17:21 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Merge PR #3 (cursor/discord-mirror-1b92) |
| 2026-09-23T12:19 | sn28 | SCORING_COMMIT | sn28 commit touches scoring: ci: validate rendered Envoy configs with  |
| 2026-09-23T12:19 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-3505 - [P2] validator: keep the Docke |
| 2026-09-23T12:19 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

