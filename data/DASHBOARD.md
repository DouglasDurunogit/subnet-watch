# Subnet watch — dashboard

_snapshot 2026-09-22T01:34:53Z · block 9119869 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 55 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 96 | `miner_burn` < 0.99 |
| Ranked | 96 | passed every gate |
| **Positive margin** | **55** | income beats machine cost |
| New events this window | 3 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 64 | `████████████████████████████` |
| 0–0.2 | 11 | `█████` |
| 0.2–0.4 | 3 | `█` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 6 | `███` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 32 | `██████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn4 Targon | 78.5 | 9,458 | 26,558 | rtx4090* | 6 | 53% |
| 2 | sn3 Teutonic | 76.9 | 5,811 | 5,874 | rtx4090* | 5 | 20% |
| 3 | sn91 cascade | 73.1 | 715 | 2,862 | cpu-small | 5 | 52% |
| 4 | sn107 Minos | 69.3 | 385 | 32,611 | cpu-small | 20 | 80% |
| 5 | sn67 Harnyx | 69.1 | 9.81 | 1,326 | cpu-small | 142 | 36% |
| 6 | sn102 ConnitoAI | 68.9 | 535 | 1,527 | rtx4090* | 7 | 30% |
| 7 | sn15 ORO | 68.1 | 10.29 | 20.52 | cpu-small | 55 | 97% |
| 8 | sn124 Swarm | 67.2 | 337 | 1,074 | rtx4090* | 25 | 11% |
| 9 | sn38 ChronoLLM | 67 | 133 | 1,178 | cpu-small | 10 | 52% |
| 10 | sn111 Claims | 66.8 | 304 | 3,127 | rtx4090* | 5 | 73% |
| 11 | sn14 Cacheon | 66 | 227 | 2,350 | rtx4090* | 16 | 28% |
| 12 | sn28 SayGM | 62.8 | 88.96 | 1,699 | rtx4090* | 65 | 11% |
| 13 | sn62 Ridges | 62 | 66.78 | 2,936 | rtx4090* | 19 | 30% |
| 14 | sn23 Trishool | 61.5 | 786 | 786 = | cpu-small | 2 | 80% |
| 15 | sn74 Gittensor | 61.3 | 63.16 | 324 | rtx4090* | 14 | 62% |
| 16 | sn51 lium.io | 60.5 | 54.83 | 1,836 | rtx4090* | 69 | 81% |
| 17 | sn61 RedTeam | 59.3 | 29.38 | 931 | rtx4090* | 125 | 9% |
| 18 | sn81 Reliquary | 58.9 | 25.85 | 90.88 | rtx4090* | 24 | 86% |
| 19 | sn80 OpenRoboto | 57.8 | 672 | 2,374 | rtx4090* | 5 | 43% |
| 20 | sn9 iota | 56.2 | 13,237 | 13,237 = | rtx4090* | 3 | 56% |

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
| concentrated (30–60%) | 25 |
| dominated (60–90%) | 19 |
| captured (>90%) | 24 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 98 |
| README keywords (GUESS) | 10 |
| min_compute.yml (curated) | 10 |
| code-submission (validator runs it) | 9 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-09-22T01:35 | sn25 | RELEASE | sn25 released v2026.9.21-1052359470 |
| 2026-09-22T01:35 | sn78 | RELEASE | sn78 released Cohort 3: provisional scores (uncertified) |
| 2026-09-22T01:35 | sn91 | RELEASE | sn91 released worker-v0.12.0 |
| 2026-09-21T22:51 | sn62 | RELEASE | sn62 released v0.3.6 |
| 2026-09-21T22:51 | sn66 | README_TASK_DIFF | sn66 README task/scoring sections changed |
| 2026-09-21T22:51 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: fix(validator): make gateway authoritati |
| 2026-09-21T22:51 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: coverage: unverified / errored_only cell |
| 2026-09-21T19:40 | sn10 | BURN_DROP | sn10 burn fell 1.000 -> 0.810 - miners can earn again |
| 2026-09-21T19:40 | sn10 | SCORING_COMMIT | sn10 commit touches scoring: fix(bench): validate both baselines befor |
| 2026-09-21T19:40 | sn14 | SCORING_COMMIT | sn14 commit touches scoring: Merge pull request #120 from latent-to/re |
| 2026-09-21T19:40 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: fix(validator): fail fast on invalid pref |
| 2026-09-21T19:40 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: verify: the grouping recheck narrows to t |
| 2026-09-21T19:40 | sn26 | SCORING_COMMIT | sn26 commit touches scoring: feat: report model evaluations in the tra |
| 2026-09-21T19:40 | sn26 | README_TASK_DIFF | sn26 README task/scoring sections changed |
| 2026-09-21T19:40 | sn28 | RELEASE | sn28 released v0.4.20 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

