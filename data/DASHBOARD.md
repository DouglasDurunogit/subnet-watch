# Subnet watch — dashboard

_snapshot 2026-09-10T21:14:00Z · block 9039755 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 59 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 91 | `miner_burn` < 0.99 |
| Ranked | 92 | passed every gate |
| **Positive margin** | **59** | income beats machine cost |
| New events this window | 7 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 62 | `████████████████████████████` |
| 0–0.2 | 8 | `████` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 3 | `█` |
| ≥0.99 dead | 37 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn114 SOMA | 84 | 444 | 7,115 | cpu-small | 6 | 80% |
| 2 | sn107 Minos | 83.2 | 375 | 31,915 | cpu-small | 20 | 80% |
| 3 | sn92 MicroTensor | 78.6 | 112 | 338 | cpu-small | 9 | 50% |
| 4 | sn3 Teutonic | 75.8 | 4,144 | 4,144 = | rtx4090* | 5 | 20% |
| 5 | sn102 ConnitoAI | 70.7 | 906 | 2,187 | rtx4090* | 5 | 40% |
| 6 | sn67 Harnyx | 70.6 | 14.45 | 692 | cpu-small | 154 | 21% |
| 7 | sn91 cascade | 70.2 | 779 | 3,141 | rtx4090* | 5 | 52% |
| 8 | sn96 Verathos | 69.7 | 31.31 | 252 | rtx4090 | 78 | 31% |
| 9 | sn14 Cacheon | 69.5 | 631 | 1,168 | rtx4090* | 12 | 18% |
| 10 | sn15 ORO | 69.3 | 15.63 | 32.94 | cpu-small | 81 | 94% |
| 11 | sn56 Gradients | 68.1 | 421 | 5,465 | rtx4090* | 9 | 48% |
| 12 | sn38 ChronoLLM | 67.5 | 149 | 3,158 | cpu-small | 10 | 52% |
| 13 | sn80 OpenRoboto | 67.3 | 331 | 1,178 | rtx4090* | 5 | 43% |
| 14 | sn124 Swarm | 66.6 | 277 | 861 | rtx4090* | 25 | 11% |
| 15 | sn21 AdTAO | 66.5 | 6.17 | 114 | cpu-small | 16 | 45% |
| 16 | sn111 Claims | 66.3 | 259 | 3,122 | rtx4090* | 5 | 76% |
| 17 | sn61 RedTeam | 65.7 | 206 | 309 | rtx4090* | 51 | 3% |
| 18 | sn121 sundae_bar | 62.8 | 1,148 | 1,148 = | cpu-small | 2 | 61% |
| 19 | sn108 Prometheon | 61 | 51.08 | 300 | rtx4090* | 11 | 30% |
| 20 | sn41 Almanac | 60.4 | 39.75 | 111 | cpu-small | 84 | 3% |

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
| wide (<30%) | 25 |
| concentrated (30–60%) | 24 |
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
| 2026-09-10T21:14 | sn15 | RELEASE | sn15 released v2.0.2: Record search retries in validator traces (#280) |
| 2026-09-10T21:14 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: Record search retries in validator traces |
| 2026-09-10T21:14 | sn15 | README_TASK_DIFF | sn15 README task/scoring sections changed |
| 2026-09-10T21:14 | sn20 | SCORING_COMMIT | sn20 commit touches scoring: Clarify full burn when every miner has ze |
| 2026-09-10T21:14 | sn20 | README_TASK_DIFF | sn20 README task/scoring sections changed |
| 2026-09-10T21:14 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: perf(validator): time the phases of one e |
| 2026-09-10T21:14 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: fix(proof): tbench agent network, custom |
| 2026-09-10T18:37 | sn9 | RELEASE | sn9 released v4.12.17 |
| 2026-09-10T18:37 | sn15 | RELEASE | sn15 released v2.0.1 |
| 2026-09-10T18:37 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: Select validator evaluator from claimed p |
| 2026-09-10T18:37 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: docs(rewards): restate the curve with an  |
| 2026-09-10T18:37 | sn25 | RELEASE | sn25 released v2026.9.10-1042581110 |
| 2026-09-10T18:37 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Validate deployed legacy coordinator comm |
| 2026-09-10T18:37 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Expose Linux validator setup |
| 2026-09-10T15:13 | sn9 | RELEASE | sn9 released v4.12.16 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

