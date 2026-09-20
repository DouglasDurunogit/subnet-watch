# Subnet watch — dashboard

_snapshot 2026-09-20T23:36:04Z · block 9112075 · run_status **ok**_

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
| 0 (none) | 62 | `████████████████████████████` |
| 0–0.2 | 10 | `█████` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 6 | `███` |
| 0.6–0.8 | 7 | `███` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 32 | `██████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn4 Targon | 78 | 7,991 | 22,433 | rtx4090* | 6 | 52% |
| 2 | sn3 Teutonic | 76.3 | 4,877 | 4,877 = | rtx4090* | 5 | 20% |
| 3 | sn102 ConnitoAI | 71.2 | 1,053 | 1,431 | rtx4090* | 5 | 30% |
| 4 | sn67 Harnyx | 70.8 | 15.10 | 389 | cpu-small | 128 | 12% |
| 5 | sn91 cascade | 70.5 | 330 | 662 | cpu-small | 5 | 52% |
| 6 | sn107 Minos | 68.6 | 328 | 27,453 | cpu-small | 20 | 80% |
| 7 | sn56 Gradients | 68.4 | 465 | 1,929 | rtx4090* | 9 | 46% |
| 8 | sn15 ORO | 67.8 | 9.25 | 18.56 | cpu-small | 61 | 97% |
| 9 | sn124 Swarm | 66.5 | 271 | 865 | rtx4090* | 25 | 11% |
| 10 | sn111 Claims | 66.1 | 246 | 2,660 | rtx4090* | 5 | 74% |
| 11 | sn38 ChronoLLM | 66.1 | 106 | 933 | cpu-small | 10 | 52% |
| 12 | sn28 SayGM | 63.6 | 111 | 758 | rtx4090* | 54 | 38% |
| 13 | sn62 Ridges | 62 | 67.56 | 2,457 | rtx4090* | 19 | 30% |
| 14 | sn74 Gittensor | 61.6 | 64.99 | 263 | rtx4090* | 12 | 62% |
| 15 | sn51 lium.io | 61.2 | 63.38 | 2,138 | rtx4090* | 67 | 82% |
| 16 | sn81 Reliquary | 59.7 | 33.88 | 108 | rtx4090* | 23 | 80% |
| 17 | sn61 RedTeam | 58 | 19.89 | 817 | rtx4090* | 132 | 10% |
| 18 | sn80 OpenRoboto | 56.6 | 474 | 1,681 | rtx4090* | 5 | 43% |
| 19 | sn9 iota | 55.9 | 11,657 | 11,657 = | rtx4090* | 2 | 56% |
| 20 | sn11 TrajectoryRL | 54.5 | 6,444 | 6,444 = | rtx4090* | 1 | 100% |

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
| captured (>90%) | 24 |

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
| 2026-09-20T23:36 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: validator: preserve client key batch stee |
| 2026-09-20T23:36 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: fix: keep unrelated verifier guidance out |
| 2026-09-20T23:36 | sn74 | RELEASE | sn74 released release-20260920-225500 |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

