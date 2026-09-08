# Subnet watch — dashboard

_snapshot 2026-09-08T22:52:16Z · block 9025868 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 56 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 91 | `miner_burn` < 0.99 |
| Ranked | 92 | passed every gate |
| **Positive margin** | **56** | income beats machine cost |
| New events this window | 7 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 60 | `████████████████████████████` |
| 0–0.2 | 8 | `████` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 37 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn114 SOMA | 87.3 | 1,000 | 8,008 | cpu-small | 4 | 80% |
| 2 | sn107 Minos | 83.7 | 428 | 34,872 | cpu-small | 20 | 79% |
| 3 | sn92 MicroTensor | 79 | 125 | 377 | cpu-small | 9 | 50% |
| 4 | sn3 Teutonic | 76 | 4,482 | 4,482 = | rtx4090* | 5 | 20% |
| 5 | sn15 ORO | 71.1 | 24.94 | 52.57 | cpu-small | 76 | 93% |
| 6 | sn67 Harnyx | 70.8 | 15.31 | 1,351 | cpu-small | 124 | 37% |
| 7 | sn91 cascade | 70.2 | 782 | 3,151 | rtx4090* | 5 | 52% |
| 8 | sn96 Verathos | 70.1 | 34.23 | 471 | rtx4090 | 83 | 33% |
| 9 | sn14 Cacheon | 69.7 | 685 | 1,268 | rtx4090* | 12 | 18% |
| 10 | sn11 TrajectoryRL | 68.7 | 6,815 | 6,815 = | cpu-small | 1 | 100% |
| 11 | sn62 Ridges | 68.2 | 427 | 1,269 | rtx4090* | 13 | 26% |
| 12 | sn56 Gradients | 67.8 | 384 | 5,946 | rtx4090* | 9 | 47% |
| 13 | sn80 OpenRoboto | 67.5 | 346 | 1,231 | rtx4090* | 5 | 43% |
| 14 | sn111 Claims | 65.8 | 232 | 3,500 | rtx4090* | 5 | 80% |
| 15 | sn38 ChronoLLM | 65.8 | 97.22 | 1,329 | cpu-small | 10 | 52% |
| 16 | sn121 sundae_bar | 63.3 | 1,342 | 1,342 = | cpu-small | 2 | 60% |
| 17 | sn28 SayGM | 62.9 | 91.09 | 6,494 | rtx4090* | 42 | 38% |
| 18 | sn65 True Performance | 62.6 | 91.46 | 191 | rtx4090* | 6 | 75% |
| 19 | sn41 Almanac | 60.7 | 42.89 | 119 | cpu-small | 85 | 3% |
| 20 | sn51 lium.io | 57.8 | 28.10 | 2,815 | rtx4090* | 65 | 79% |

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
| concentrated (30–60%) | 21 |
| dominated (60–90%) | 20 |
| captured (>90%) | 20 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 99 |
| min_compute.yml (curated) | 11 |
| code-submission (validator runs it) | 10 |
| README keywords (GUESS) | 7 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-09-08T22:52 | sn15 | RELEASE | sn15 released v1.2.13: compose: forward SUBTENSOR_CHAIN_ENDPOINT to th |
| 2026-09-08T22:52 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: compose: forward SUBTENSOR_CHAIN_ENDPOINT |
| 2026-09-08T22:52 | sn25 | RELEASE | sn25 released v2026.9.8-1040985530 |
| 2026-09-08T22:52 | sn28 | RELEASE | sn28 released v0.4.15 |
| 2026-09-08T22:52 | sn28 | SCORING_COMMIT | sn28 commit touches scoring: fix(miner): render node secret last and p |
| 2026-09-08T22:52 | sn28 | README_TASK_DIFF | sn28 README task/scoring sections changed |
| 2026-09-08T22:52 | sn78 | WEIGHTS_VERSION_BUMP | sn78 weights_version 0 -> 1 |
| 2026-09-08T20:19 | sn2 | RELEASE | sn2 released 14.14.3 |
| 2026-09-08T20:19 | sn2 | SCORING_COMMIT | sn2 commit touches scoring: Introduce weight commit guard for epochs w |
| 2026-09-08T20:19 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge remote-tracking branch 'origin/main |
| 2026-09-08T20:19 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Fix bootstrap image revision validation |
| 2026-09-08T20:19 | sn96 | RELEASE | sn96 released Verathos v0.2.2 – Consistent Validator Decisions and Mic |
| 2026-09-08T17:34 | sn25 | RELEASE | sn25 released v2026.9.8-1040779940 |
| 2026-09-08T17:34 | sn34 | BURN_DROP | sn34 burn fell 1.000 -> 0.799 - miners can earn again |
| 2026-09-08T17:34 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge remote-tracking branch 'origin/main |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

