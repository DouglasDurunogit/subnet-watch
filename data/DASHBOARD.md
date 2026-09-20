# Subnet watch — dashboard

_snapshot 2026-09-20T13:44:37Z · block 9109135 · run_status **ok**_

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
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 10 | `█████` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 33 | `███████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn4 Targon | 77.8 | 7,612 | 21,370 | rtx4090* | 6 | 52% |
| 2 | sn3 Teutonic | 76.2 | 4,655 | 4,655 = | rtx4090* | 5 | 20% |
| 3 | sn91 cascade | 71.7 | 474 | 1,265 | cpu-small | 5 | 52% |
| 4 | sn102 ConnitoAI | 70.7 | 921 | 2,459 | rtx4090* | 4 | 53% |
| 5 | sn67 Harnyx | 70.6 | 14.40 | 372 | cpu-small | 127 | 12% |
| 6 | sn1 Apex | 69.6 | 650 | 867 | rtx4090* | 4 | 61% |
| 7 | sn56 Gradients | 68.4 | 454 | 5,362 | rtx4090* | 9 | 46% |
| 8 | sn107 Minos | 68.4 | 306 | 25,972 | cpu-small | 20 | 80% |
| 9 | sn15 ORO | 67 | 8.73 | 17.85 | cpu-small | 60 | 97% |
| 10 | sn124 Swarm | 66.4 | 261 | 836 | rtx4090* | 25 | 11% |
| 11 | sn38 ChronoLLM | 66 | 99.79 | 883 | cpu-small | 10 | 52% |
| 12 | sn111 Claims | 65.9 | 232 | 2,092 | rtx4090* | 5 | 61% |
| 13 | sn74 Gittensor | 62.5 | 82.43 | 258 | rtx4090* | 11 | 61% |
| 14 | sn28 SayGM | 61.7 | 63.41 | 2,531 | rtx4090* | 59 | 17% |
| 15 | sn62 Ridges | 60.8 | 46.52 | 1,595 | rtx4090* | 18 | 33% |
| 16 | sn81 Reliquary | 59.3 | 29.49 | 85.23 | rtx4090* | 27 | 79% |
| 17 | sn51 lium.io | 58.2 | 30.12 | 2,221 | rtx4090* | 68 | 80% |
| 18 | sn61 RedTeam | 57.8 | 18.73 | 1,706 | rtx4090* | 130 | 20% |
| 19 | sn80 OpenRoboto | 56.3 | 434 | 1,541 | rtx4090* | 5 | 43% |
| 20 | sn9 iota | 55.8 | 11,120 | 11,120 = | rtx4090* | 2 | 56% |

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
| dominated (60–90%) | 21 |
| captured (>90%) | 23 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 98 |
| min_compute.yml (curated) | 11 |
| code-submission (validator runs it) | 9 |
| README keywords (GUESS) | 9 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-09-20T13:45 | sn11 | RELEASE | sn11 released v0.7.1 |
| 2026-09-20T13:45 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: admission: report the gate score per hori |
| 2026-09-20T13:45 | sn71 | BURN_DROP | sn71 burn fell 1.000 -> 0.750 - miners can earn again |
| 2026-09-20T13:45 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: test(arena): reject unrelated score failu |
| 2026-09-20T09:45 | sn11 | BURN_DROP | sn11 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-09-20T09:45 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Add Sep20 authority-preserving scoring re |
| 2026-09-20T09:45 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Reuse validated reserved publications acr |
| 2026-09-20T09:45 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: trainer: one GPU type per manifest — drop |
| 2026-09-20T09:45 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: feat(bounty): activate proportional vali |
| 2026-09-20T04:52 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Seal September 20 verifier and runtime re |
| 2026-09-20T00:07 | sn74 | RELEASE | sn74 released release-20260919-231145 |
| 2026-09-19T21:48 | sn11 | SCORING_COMMIT | sn11 commit touches scoring: Merge pull request #328 from trajectoryRL |
| 2026-09-19T21:48 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Retry proved miner-funded Responses throt |
| 2026-09-19T19:37 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Read retained validator runtime through r |
| 2026-09-19T19:37 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Bound uncontended dispatch by the longest |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

