# Subnet watch — dashboard

_snapshot 2026-11-27T18:20:43Z · block 9599964 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 49 of 129

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 129 | everything on chain |
| Pays miners at all | 104 | `miner_burn` < 0.99 |
| Ranked | 104 | passed every gate |
| **Positive margin** | **49** | income beats machine cost |
| New events this window | 2 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 73 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 3 | `█` |
| 0.4–0.6 | 7 | `███` |
| 0.6–0.8 | 6 | `██` |
| 0.8–0.99 | 10 | `████` |
| ≥0.99 dead | 25 | `██████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn120 Affine | 57.2 | 19,570 | 19,570 = | rtx4090* | 1 | 100% |
| 2 | sn14 Cacheon | 52.1 | 2,316 | 2,775 | rtx4090* | 2 | 60% |
| 3 | sn90 KubeTEE | 52.1 | 2,269 | 3,248 | rtx4090* | 3 | 43% |
| 4 | sn116 Carbon | 51.3 | 1,647 | 3,302 | rtx4090* | 3 | 50% |
| 5 | sn53 engy | 51 | 1,457 | 3,446 | rtx4090* | 8 | 49% |
| 6 | sn61 RedTeam | 49.9 | 915 | 1,057 | rtx4090* | 3 | 40% |
| 7 | sn70 Fugal | 48.9 | 597 | 597 = | rtx4090* | 2 | 50% |
| 8 | sn56 Gradients | 48.4 | 485 | 2,423 | rtx4090* | 9 | 33% |
| 9 | sn39 Kokoah | 46.3 | 199 | 383 | rtx4090* | 4 | 78% |
| 10 | sn9 iota | 46.2 | 6,667 | 6,667 = | rtx4090* | 2 | 50% |
| 11 | sn42 CADmind | 46.1 | 186 | 186 = | rtx4090* | 5 | 20% |
| 12 | sn124 Swarm | 45.8 | 172 | 1,143 | rtx4090* | 10 | 29% |
| 13 | sn17 404—GEN | 44.4 | 3,159 | 3,159 = | rtx4090* | 1 | 100% |
| 14 | sn66 conjectures | 43.8 | 68.33 | 844 | rtx4090* | 4 | 81% |
| 15 | sn91 cascade | 43.7 | 66.19 | 66.19 = | rtx4090* | 2 | 95% |
| 16 | sn3 Teutonic | 42.9 | 1,684 | 3,376 | rtx4090* | 4 | 40% |
| 17 | sn58 Attune | 42.9 | 46.48 | 1,526 | rtx4090* | 53 | 30% |
| 18 | sn28 SayGM | 42.7 | 46.28 | 1,041 | rtx4090* | 121 | 31% |
| 19 | sn111 Claims | 42.2 | 35.44 | 145 | rtx4090* | 4 | 88% |
| 20 | sn97 Ingot | 42 | 1,126 | 1,126 = | rtx4090* | 3 | 50% |

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
| concentrated (30–60%) | 28 |
| dominated (60–90%) | 22 |
| captured (>90%) | 26 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 129 |

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

