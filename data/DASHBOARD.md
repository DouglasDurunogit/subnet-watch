# Subnet watch — dashboard

_snapshot 2026-09-20T21:44:55Z · block 9111519 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 56 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 95 | `miner_burn` < 0.99 |
| Ranked | 95 | passed every gate |
| **Positive margin** | **56** | income beats machine cost |
| New events this window | 4 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 61 | `████████████████████████████` |
| 0–0.2 | 10 | `█████` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 6 | `███` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 33 | `███████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn4 Targon | 77.9 | 7,884 | 22,133 | rtx4090* | 6 | 52% |
| 2 | sn3 Teutonic | 76.3 | 4,816 | 4,816 = | rtx4090* | 5 | 20% |
| 3 | sn102 ConnitoAI | 71.2 | 1,053 | 1,388 | rtx4090* | 5 | 29% |
| 4 | sn67 Harnyx | 70.7 | 14.92 | 385 | cpu-small | 128 | 12% |
| 5 | sn1 Apex | 70.5 | 863 | 1,060 | rtx4090* | 4 | 54% |
| 6 | sn91 cascade | 70.4 | 322 | 646 | cpu-small | 5 | 52% |
| 7 | sn107 Minos | 68.6 | 324 | 26,993 | cpu-small | 20 | 80% |
| 8 | sn56 Gradients | 68.4 | 459 | 1,906 | rtx4090* | 9 | 46% |
| 9 | sn15 ORO | 67.5 | 9.07 | 18.24 | cpu-small | 61 | 97% |
| 10 | sn124 Swarm | 66.4 | 267 | 855 | rtx4090* | 25 | 11% |
| 11 | sn38 ChronoLLM | 66.1 | 105 | 925 | cpu-small | 10 | 52% |
| 12 | sn111 Claims | 66 | 241 | 2,177 | rtx4090* | 5 | 61% |
| 13 | sn28 SayGM | 63.6 | 113 | 763 | rtx4090* | 57 | 39% |
| 14 | sn62 Ridges | 62 | 66.64 | 2,428 | rtx4090* | 19 | 30% |
| 15 | sn74 Gittensor | 61.5 | 64.18 | 260 | rtx4090* | 12 | 62% |
| 16 | sn51 lium.io | 60 | 47.23 | 2,090 | rtx4090* | 68 | 82% |
| 17 | sn81 Reliquary | 59.7 | 33.84 | 98.66 | rtx4090* | 25 | 79% |
| 18 | sn61 RedTeam | 57.9 | 19.57 | 812 | rtx4090* | 132 | 10% |
| 19 | sn80 OpenRoboto | 56.6 | 474 | 1,679 | rtx4090* | 5 | 43% |
| 20 | sn9 iota | 55.9 | 11,519 | 11,519 = | rtx4090* | 2 | 56% |

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
| concentrated (30–60%) | 25 |
| dominated (60–90%) | 18 |
| captured (>90%) | 23 |

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
| 2026-09-20T21:45 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: validator: admit reviewed successor on pr |
| 2026-09-20T21:45 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Fix normal validator scoring preflight an |
| 2026-09-20T21:45 | sn71 | README_TASK_DIFF | sn71 README task/scoring sections changed |
| 2026-09-20T21:45 | sn108 | BURN_DROP | sn108 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-09-20T19:25 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Bind protected verifier manifest to commi |
| 2026-09-20T19:25 | sn78 | RELEASE | sn78 released Open competition miner bundle v1 (feed config + pinned a |
| 2026-09-20T17:03 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Expose public scoring validator attributi |
| 2026-09-20T13:45 | sn11 | RELEASE | sn11 released v0.7.1 |
| 2026-09-20T13:45 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: admission: report the gate score per hori |
| 2026-09-20T13:45 | sn71 | BURN_DROP | sn71 burn fell 1.000 -> 0.750 - miners can earn again |
| 2026-09-20T13:45 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: test(arena): reject unrelated score failu |
| 2026-09-20T09:45 | sn11 | BURN_DROP | sn11 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-09-20T09:45 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Add Sep20 authority-preserving scoring re |
| 2026-09-20T09:45 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Reuse validated reserved publications acr |
| 2026-09-20T09:45 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: trainer: one GPU type per manifest — drop |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

