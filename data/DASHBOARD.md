# Subnet watch — dashboard

_snapshot 2026-11-28T01:33:40Z · block 9602129 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 52 of 129

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 129 | everything on chain |
| Pays miners at all | 103 | `miner_burn` < 0.99 |
| Ranked | 103 | passed every gate |
| **Positive margin** | **52** | income beats machine cost |
| New events this window | 0 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 72 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 3 | `█` |
| 0.4–0.6 | 6 | `██` |
| 0.6–0.8 | 6 | `██` |
| 0.8–0.99 | 9 | `████` |
| ≥0.99 dead | 26 | `██████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn42 CADmind | 80.7 | 188 | 188 = | cpu-small | 5 | 20% |
| 2 | sn116 Carbon | 72.5 | 1,542 | 3,092 | rtx4090* | 3 | 50% |
| 3 | sn53 engy | 71.9 | 1,313 | 3,106 | rtx4090 | 8 | 49% |
| 4 | sn61 RedTeam | 70.3 | 804 | 1,050 | rtx4090* | 3 | 40% |
| 5 | sn67 Harnyx | 65.7 | 3.27 | 372 | cpu-small | 109 | 28% |
| 6 | sn124 Swarm | 65 | 173 | 1,156 | rtx4090* | 10 | 29% |
| 7 | sn56 Gradients | 62.1 | 472 | 2,448 | a100-80 | 9 | 33% |
| 8 | sn66 conjectures | 61.9 | 65.32 | 811 | rtx4090* | 4 | 81% |
| 9 | sn3 Teutonic | 60.8 | 1,693 | 1,693 = | rtx4090* | 4 | 40% |
| 10 | sn111 Claims | 59.9 | 36.17 | 147 | rtx4090* | 4 | 88% |
| 11 | sn28 SayGM | 59.1 | 30.57 | 477 | rtx4090* | 127 | 19% |
| 12 | sn127 Zils | 58.6 | 23.60 | 44.83 | rtx4090 | 6 | 88% |
| 13 | sn120 Affine | 57.2 | 19,983 | 19,983 = | rtx4090* | 1 | 100% |
| 14 | sn1 Apex | 56.9 | 524 | 569 | rtx4090* | 4 | 53% |
| 15 | sn25 UR | 54.9 | 7.24 | 83.07 | rtx4090* | 11 | 45% |
| 16 | sn38 ChronoLLM | 54.4 | 104 | 265 | cpu-small | 6 | 53% |
| 17 | sn107 Minos | 53.5 | 108 | 9,246 | cpu-small | 20 | 80% |
| 18 | sn46 Instant | 53.4 | 70.73 | 82.84 | cpu-small | 17 | 11% |
| 19 | sn99 Axonry | 52.7 | 2,926 | 2,926 = | rtx4090* | 2 | 50% |
| 20 | sn14 Cacheon | 52.2 | 2,365 | 2,833 | rtx4090* | 2 | 60% |

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
| concentrated (30–60%) | 27 |
| dominated (60–90%) | 20 |
| captured (>90%) | 27 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 97 |
| README keywords (GUESS) | 12 |
| min_compute.yml (curated) | 12 |
| code-submission (validator runs it) | 8 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-11-27T18:22 | sn71 | BURN_DROP | sn71 burn fell 1.000 -> 0.989 - miners can earn again |
| 2026-11-27T18:22 | sn91 | BURN_DROP | sn91 burn fell 1.000 -> 0.955 - miners can earn again |
| 2026-11-27T08:16 | sn30 | RELEASE | sn30 released v0.1.4 — Archive resilience and horizon-maturity blend,  |
| 2026-11-27T08:16 | sn51 | RELEASE | sn51 released executor-v1.202 |
| 2026-11-27T08:16 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-7201 - [P4] Validator: report a resta |
| 2026-11-27T08:16 | sn61 | RELEASE | sn61 released 4.12.0 |
| 2026-11-27T08:16 | sn61 | SCORING_COMMIT | sn61 commit touches scoring: refactor: update bot virus challenge vers |
| 2026-11-27T08:16 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Run standing funded experiments and verif |
| 2026-11-27T08:16 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: fix(lane-d): public half throughput: warm |
| 2026-11-27T08:16 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: fix(rewards): fix SN116 Subtensor chain  |
| 2026-11-27T08:16 | sn127 | RELEASE | sn127 released Release d92abe3 |
| 2026-11-27T00:03 | sn6 | README_TASK_DIFF | sn6 README task/scoring sections changed |
| 2026-11-27T00:03 | sn12 | RELEASE | sn12 released miner-staging-2026-11-26-45857591810-467-1: fix: stop th |
| 2026-11-27T00:03 | sn51 | RELEASE | sn51 released watchtower-v1.2.5 |
| 2026-11-27T00:03 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-5238 - [P4] Validator reads liumd's c |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

