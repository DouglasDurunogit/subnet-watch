# Subnet watch — dashboard

_snapshot 2026-09-24T17:34:39Z · block 9139061 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 61 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 98 | `miner_burn` < 0.99 |
| Ranked | 98 | passed every gate |
| **Positive margin** | **61** | income beats machine cost |
| New events this window | 5 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 63 | `████████████████████████████` |
| 0–0.2 | 9 | `████` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 10 | `████` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 30 | `█████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn4 Targon | 80.1 | 15,064 | 27,248 | rtx4090* | 5 | 58% |
| 2 | sn3 Teutonic | 76.5 | 5,201 | 5,201 = | rtx4090* | 5 | 20% |
| 3 | sn91 cascade | 72.6 | 627 | 2,512 | cpu-small | 5 | 52% |
| 4 | sn26 Perturb | 71.2 | 45.45 | 49.78 | rtx3060 | 5 | 90% |
| 5 | sn1 Apex | 69.9 | 728 | 944 | rtx4090* | 4 | 62% |
| 6 | sn14 Cacheon | 69 | 549 | 2,235 | rtx4090* | 12 | 29% |
| 7 | sn67 Harnyx | 68.7 | 8.76 | 1,158 | cpu-small | 124 | 35% |
| 8 | sn107 Minos | 68.6 | 329 | 29,227 | cpu-small | 20 | 80% |
| 9 | sn38 ChronoLLM | 68.5 | 197 | 1,739 | cpu-small | 10 | 52% |
| 10 | sn56 Gradients | 68.4 | 459 | 5,617 | rtx4090* | 10 | 40% |
| 11 | sn102 ConnitoAI | 68.3 | 440 | 1,454 | rtx4090* | 7 | 30% |
| 12 | sn15 ORO | 67.2 | 10.09 | 22.15 | cpu-small | 58 | 97% |
| 13 | sn124 Swarm | 66.9 | 308 | 909 | rtx4090* | 25 | 11% |
| 14 | sn111 Claims | 65.4 | 210 | 1,900 | rtx4090* | 5 | 49% |
| 15 | sn100 Cortex | 62.6 | 81.32 | 140 | rtx4090* | 13 | 71% |
| 16 | sn23 Trishool | 62 | 904 | 904 = | cpu-small | 2 | 80% |
| 17 | sn28 SayGM | 62 | 68.99 | 869 | rtx4090* | 71 | 19% |
| 18 | sn62 Ridges | 61.7 | 62.42 | 1,870 | rtx4090* | 20 | 21% |
| 19 | sn61 RedTeam | 59.8 | 35.66 | 378 | rtx4090* | 126 | 4% |
| 20 | sn74 Gittensor | 59.1 | 31.85 | 120 | rtx4090* | 19 | 64% |

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
| wide (<30%) | 23 |
| concentrated (30–60%) | 26 |
| dominated (60–90%) | 20 |
| captured (>90%) | 26 |

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
| 2026-09-24T17:35 | sn20 | SCORING_COMMIT | sn20 commit touches scoring: Ground native semantic scoring in clip ev |
| 2026-09-24T17:35 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Derive policy rollover activations from v |
| 2026-09-24T17:35 | sn28 | RELEASE | sn28 released v0.4.22-dev |
| 2026-09-24T17:35 | sn28 | SCORING_COMMIT | sn28 commit touches scoring: chore(release): gm-miner 0.4.22-dev (#277 |
| 2026-09-24T17:35 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: chore(release): bind verifier evidence re |
| 2026-09-24T12:42 | sn1 | RELEASE | sn1 released v4.4.9 |
| 2026-09-24T12:42 | sn9 | RELEASE | sn9 released v4.13.3 |
| 2026-09-24T12:42 | sn22 | SCORING_COMMIT | sn22 commit touches scoring: feat: reject sources a miner could have s |
| 2026-09-24T12:42 | sn28 | RELEASE | sn28 released v0.4.21 |
| 2026-09-24T12:42 | sn28 | SCORING_COMMIT | sn28 commit touches scoring: chore(release): promote gm-miner 0.4.21 ( |
| 2026-09-24T12:42 | sn51 | RELEASE | sn51 released executor-v1.135 |
| 2026-09-24T12:42 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: Validator: pull a present image when the  |
| 2026-09-24T12:42 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Preserve local visible article headers in |
| 2026-09-24T06:47 | sn21 | RELEASE | sn21 released SN21 rich training data v3 (slice 2) |
| 2026-09-24T06:47 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-3521 - [P1] validator: a custom build |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

