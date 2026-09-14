# Subnet watch — dashboard

_snapshot 2026-09-14T18:48:23Z · block 9067765 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 54 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 89 | `miner_burn` < 0.99 |
| Ranked | 90 | passed every gate |
| **Positive margin** | **54** | income beats machine cost |
| New events this window | 12 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 62 | `████████████████████████████` |
| 0–0.2 | 9 | `████` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 7 | `███` |
| 0.8–0.99 | 2 | `█` |
| ≥0.99 dead | 39 | `██████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn92 MicroTensor | 80.8 | 193 | 582 | cpu-small | 8 | 30% |
| 2 | sn91 cascade | 74.4 | 1,060 | 2,829 | cpu-small | 5 | 52% |
| 3 | sn67 Harnyx | 69.3 | 11.13 | 11.13 = | cpu-small | 216 | 17% |
| 4 | sn107 Minos | 68.8 | 340 | 30,399 | cpu-small | 20 | 80% |
| 5 | sn11 TrajectoryRL | 68.2 | 5,882 | 5,882 = | cpu-small | 1 | 100% |
| 6 | sn96 Verathos | 68.1 | 21.02 | 228 | rtx4090 | 80 | 31% |
| 7 | sn80 OpenRoboto | 67.7 | 375 | 1,333 | rtx4090* | 5 | 43% |
| 8 | sn38 ChronoLLM | 66.9 | 126 | 1,718 | cpu-small | 10 | 52% |
| 9 | sn124 Swarm | 66.5 | 272 | 882 | rtx4090* | 25 | 11% |
| 10 | sn111 Claims | 65.3 | 198 | 1,793 | rtx4090* | 5 | 50% |
| 11 | sn28 SayGM | 64.4 | 142 | 2,439 | rtx4090* | 46 | 15% |
| 12 | sn3 Teutonic | 63.9 | 4,164 | 4,164 = | rtx4090* | 5 | 20% |
| 13 | sn61 RedTeam | 63.9 | 125 | 191 | rtx4090* | 96 | 2% |
| 14 | sn55 NIOME | 62.1 | 70.05 | 579 | rtx4090* | 11 | 29% |
| 15 | sn81 Reliquary | 60.8 | 46.87 | 226 | rtx4090* | 85 | 5% |
| 16 | sn51 lium.io | 60.5 | 52.50 | 1,535 | rtx4090* | 61 | 81% |
| 17 | sn23 Trishool | 60.4 | 562 | 562 = | cpu-small | 2 | 80% |
| 18 | sn62 Ridges | 60.3 | 40.11 | 1,181 | rtx4090* | 18 | 35% |
| 19 | sn2 DSperse | 58.6 | 24.17 | 53.79 | rtx4090* | 10 | 88% |
| 20 | sn74 Gittensor | 58 | 22.57 | 191 | rtx4090 | 11 | 64% |

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
| concentrated (30–60%) | 23 |
| dominated (60–90%) | 16 |
| captured (>90%) | 21 |

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
| 2026-09-14T18:48 | sn90 | SCORING_COMMIT | sn90 commit touches scoring: docs: BTLABS (UID 97) live — first produc |
| 2026-09-14T18:48 | sn90 | README_TASK_DIFF | sn90 README task/scoring sections changed |
| 2026-09-14T13:23 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: chore(validator): bump oro-env-runtime 0. |
| 2026-09-14T13:23 | sn25 | RELEASE | sn25 released v2026.9.14-1045806490 |
| 2026-09-14T13:23 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Validate capture ownership against growin |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

