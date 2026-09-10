# Subnet watch — dashboard

_snapshot 2026-09-10T23:18:52Z · block 9040379 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 59 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 90 | `miner_burn` < 0.99 |
| Ranked | 91 | passed every gate |
| **Positive margin** | **59** | income beats machine cost |
| New events this window | 6 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 61 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 8 | `████` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 3 | `█` |
| ≥0.99 dead | 38 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn114 SOMA | 84 | 436 | 6,992 | cpu-small | 6 | 80% |
| 2 | sn107 Minos | 83.2 | 371 | 31,553 | cpu-small | 20 | 80% |
| 3 | sn92 MicroTensor | 78.5 | 109 | 330 | cpu-small | 9 | 50% |
| 4 | sn3 Teutonic | 75.7 | 4,086 | 4,086 = | rtx4090* | 5 | 20% |
| 5 | sn67 Harnyx | 70.5 | 14.12 | 677 | cpu-small | 156 | 21% |
| 6 | sn91 cascade | 70 | 742 | 2,992 | rtx4090* | 5 | 52% |
| 7 | sn15 ORO | 69.7 | 15.44 | 32.92 | cpu-small | 81 | 94% |
| 8 | sn102 ConnitoAI | 69.4 | 624 | 2,269 | rtx4090* | 6 | 42% |
| 9 | sn14 Cacheon | 69.4 | 620 | 1,149 | rtx4090* | 12 | 18% |
| 10 | sn96 Verathos | 69.3 | 28.39 | 245 | rtx4090 | 78 | 30% |
| 11 | sn56 Gradients | 68.1 | 414 | 5,375 | rtx4090* | 9 | 48% |
| 12 | sn38 ChronoLLM | 67.5 | 150 | 3,184 | cpu-small | 10 | 52% |
| 13 | sn80 OpenRoboto | 67.3 | 327 | 1,163 | rtx4090* | 5 | 43% |
| 14 | sn124 Swarm | 66.6 | 277 | 763 | rtx4090* | 25 | 10% |
| 15 | sn21 AdTAO | 66.4 | 6.07 | 112 | cpu-small | 16 | 45% |
| 16 | sn111 Claims | 66.2 | 255 | 3,065 | rtx4090* | 5 | 76% |
| 17 | sn61 RedTeam | 65.8 | 214 | 321 | rtx4090* | 51 | 3% |
| 18 | sn121 sundae_bar | 62.7 | 1,129 | 1,129 = | cpu-small | 2 | 61% |
| 19 | sn108 Prometheon | 60.9 | 50.06 | 295 | rtx4090* | 11 | 30% |
| 20 | sn41 Almanac | 60.4 | 39.03 | 109 | cpu-small | 84 | 3% |

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
| dominated (60–90%) | 18 |
| captured (>90%) | 20 |

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
| 2026-09-10T23:19 | sn15 | RELEASE | sn15 released v2.0.3 |
| 2026-09-10T23:19 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: fix(validator): retry SimulatorCompletion |
| 2026-09-10T23:19 | sn20 | SCORING_COMMIT | sn20 commit touches scoring: Smooth mainnet rewards over configurable  |
| 2026-09-10T23:19 | sn62 | RELEASE | sn62 released v0.3.4 |
| 2026-09-10T23:19 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Ship shared SN78 validator bootstrap supe |
| 2026-09-10T23:19 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: docs(miner): minimal tbench Agent constr |
| 2026-09-10T21:14 | sn15 | RELEASE | sn15 released v2.0.2: Record search retries in validator traces (#280) |
| 2026-09-10T21:14 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: Record search retries in validator traces |
| 2026-09-10T21:14 | sn15 | README_TASK_DIFF | sn15 README task/scoring sections changed |
| 2026-09-10T21:14 | sn20 | SCORING_COMMIT | sn20 commit touches scoring: Clarify full burn when every miner has ze |
| 2026-09-10T21:14 | sn20 | README_TASK_DIFF | sn20 README task/scoring sections changed |
| 2026-09-10T21:14 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: perf(validator): time the phases of one e |
| 2026-09-10T21:14 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: fix(proof): tbench agent network, custom |
| 2026-09-10T18:37 | sn9 | RELEASE | sn9 released v4.12.17 |
| 2026-09-10T18:37 | sn15 | RELEASE | sn15 released v2.0.1 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

