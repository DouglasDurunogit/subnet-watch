# Subnet watch — dashboard

_snapshot 2026-09-12T06:23:52Z · block 9049685 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 58 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 89 | `miner_burn` < 0.99 |
| Ranked | 90 | passed every gate |
| **Positive margin** | **58** | income beats machine cost |
| New events this window | 5 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 59 | `████████████████████████████` |
| 0–0.2 | 10 | `█████` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 3 | `█` |
| ≥0.99 dead | 39 | `███████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn92 MicroTensor | 79.7 | 149 | 449 | cpu-small | 9 | 24% |
| 2 | sn21 AdTAO | 75.6 | 52.82 | 130 | cpu-small | 21 | 34% |
| 3 | sn91 cascade | 71.4 | 1,122 | 3,006 | rtx4090* | 5 | 52% |
| 4 | sn96 Verathos | 70.5 | 37.84 | 315 | rtx4090 | 67 | 31% |
| 5 | sn14 Cacheon | 69.3 | 609 | 1,129 | rtx4090* | 12 | 18% |
| 6 | sn67 Harnyx | 68.8 | 9.06 | 1,059 | cpu-small | 124 | 33% |
| 7 | sn107 Minos | 68.7 | 335 | 29,792 | cpu-small | 20 | 81% |
| 8 | sn11 TrajectoryRL | 68.3 | 6,046 | 6,046 = | cpu-small | 1 | 100% |
| 9 | sn56 Gradients | 68 | 406 | 5,269 | rtx4090* | 9 | 48% |
| 10 | sn80 OpenRoboto | 67.4 | 342 | 1,217 | rtx4090* | 5 | 43% |
| 11 | sn124 Swarm | 66.5 | 268 | 868 | rtx4090* | 25 | 11% |
| 12 | sn111 Claims | 66.3 | 267 | 2,852 | rtx4090* | 5 | 73% |
| 13 | sn38 ChronoLLM | 66 | 99.44 | 1,359 | cpu-small | 10 | 52% |
| 14 | sn61 RedTeam | 65.7 | 206 | 306 | rtx4090* | 56 | 3% |
| 15 | sn55 NIOME | 62.3 | 74.47 | 612 | rtx4090* | 11 | 29% |
| 16 | sn28 SayGM | 61.9 | 68.18 | 2,175 | rtx4090* | 44 | 15% |
| 17 | sn23 Trishool | 60.3 | 548 | 548 = | cpu-small | 2 | 80% |
| 18 | sn62 Ridges | 59.6 | 32.80 | 109 | rtx4090* | 16 | 52% |
| 19 | sn102 ConnitoAI | 58.8 | 919 | 1,556 | rtx4090* | 6 | 32% |
| 20 | sn81 Reliquary | 58 | 19.60 | 164 | rtx4090* | 84 | 9% |

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
| dominated (60–90%) | 16 |
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
| 2026-09-12T06:24 | sn20 | BURN_DROP | sn20 burn fell 1.000 -> 0.742 - miners can earn again |
| 2026-09-12T06:24 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Reuse verified historical deployment comp |
| 2026-09-12T06:24 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-3439 - [P0] validator: outdated execu |
| 2026-09-12T06:24 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Use current billing schema in normal vali |
| 2026-09-12T06:24 | sn71 | README_TASK_DIFF | sn71 README task/scoring sections changed |
| 2026-09-12T01:27 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Sync disposable replay scratch once after |
| 2026-09-12T01:27 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Preserve Arena miner credential failure e |
| 2026-09-11T21:21 | sn20 | SCORING_COMMIT | sn20 commit touches scoring: Add grounded video scoring and hybrid mai |
| 2026-09-11T21:21 | sn25 | RELEASE | sn25 released v2026.9.11-1043550030 |
| 2026-09-11T21:21 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Verify in-flight Arena leases survive par |
| 2026-09-11T21:21 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: fix(proof): fail-closed harbor partial s |
| 2026-09-11T18:42 | sn15 | RELEASE | sn15 released v2.0.6 |
| 2026-09-11T18:42 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: chore(validator): pin oro-env-runtime 0.2 |
| 2026-09-11T18:42 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Observe provisional validator intents fro |
| 2026-09-11T18:42 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Accept Harvest plural current positions i |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

