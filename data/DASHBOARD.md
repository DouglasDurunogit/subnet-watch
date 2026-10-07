# Subnet watch — dashboard

_snapshot 2026-10-07T02:19:01Z · block 9228082 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 58 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 100 | `miner_burn` < 0.99 |
| Ranked | 100 | passed every gate |
| **Positive margin** | **58** | income beats machine cost |
| New events this window | 6 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 67 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 7 | `███` |
| 0.6–0.8 | 8 | `███` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 28 | `████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn26 Perturb | 79.5 | 359 | 1,214 | rtx3060 | 4 | 60% |
| 2 | sn41 Almanac | 73.2 | 29.60 | 115 | cpu-small | 133 | 2% |
| 3 | sn49 Nepher Robotics | 72.3 | 1,481 | 5,205 | rtx4090* | 4 | 69% |
| 4 | sn91 cascade | 72.1 | 535 | 2,141 | cpu-small | 5 | 52% |
| 5 | sn67 Harnyx | 70.1 | 12.47 | 1,032 | cpu-small | 138 | 35% |
| 6 | sn46 Instant | 69 | 213 | 257 | cpu-small | 8 | 50% |
| 7 | sn1 Apex | 68.9 | 537 | 1,090 | rtx4090* | 4 | 66% |
| 8 | sn80 OpenRoboto | 68.4 | 461 | 2,087 | rtx4090* | 8 | 25% |
| 9 | sn4 Targon | 67 | 10,505 | 30,971 | rtx4090* | 5 | 70% |
| 10 | sn15 ORO | 67 | 8.64 | 16.95 | cpu-small | 53 | 98% |
| 11 | sn111 Claims | 66.7 | 280 | 2,514 | rtx4090* | 5 | 70% |
| 12 | sn62 Ridges | 63.8 | 117 | 1,445 | rtx4090* | 34 | 17% |
| 13 | sn120 Affine | 63.6 | 185 | 415 | rtx4090* | 205 | 1% |
| 14 | sn65 True Performance | 62.4 | 80.85 | 170 | rtx4090* | 6 | 75% |
| 15 | sn61 RedTeam | 62.1 | 71.51 | 112 | rtx4090* | 128 | 1% |
| 16 | sn23 Trishool | 62 | 926 | 926 = | cpu-small | 2 | 80% |
| 17 | sn14 Cacheon | 60.6 | 43.53 | 1,069 | rtx4090* | 7 | 83% |
| 18 | sn53 engy | 60.2 | 1,369 | 3,751 | rtx4090 | 14 | 22% |
| 19 | sn74 Gittensor | 58.6 | 27.19 | 150 | rtx4090* | 21 | 50% |
| 20 | sn107 Minos | 57.9 | 315 | 26,756 | cpu-small | 20 | 80% |

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
| wide (<30%) | 21 |
| concentrated (30–60%) | 26 |
| dominated (60–90%) | 25 |
| captured (>90%) | 24 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 96 |
| README keywords (GUESS) | 12 |
| min_compute.yml (curated) | 10 |
| code-submission (validator runs it) | 9 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-10-07T02:19 | sn5 | SCORING_COMMIT | sn5 commit touches scoring: Merge pull request #18 from hone-subnet-or |
| 2026-10-07T02:19 | sn25 | RELEASE | sn25 released v2026.10.6-1065359600 |
| 2026-10-07T02:19 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Merge feat/operator-discovery-validator |
| 2026-10-07T02:19 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Preserve commercial terms sources in boun |
| 2026-10-07T02:19 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Merge pull request #723 from carbonphysi |
| 2026-10-07T02:19 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Prepare isolated all750 matched native e |
| 2026-10-06T23:03 | sn10 | BURN_DROP | sn10 burn fell 1.000 -> 0.902 - miners can earn again |
| 2026-10-06T23:03 | sn25 | RELEASE | sn25 released v2026.10.6-1065229510 |
| 2026-10-06T23:03 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Merge feat/operator-discovery-miner into  |
| 2026-10-06T23:03 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Prove dynamic Deepline tools through base |
| 2026-10-06T23:03 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Reduce intake seal contention and isolate |
| 2026-10-06T23:03 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: feat(validator): default miner burn to 9 |
| 2026-10-06T23:03 | sn116 | RELEASE | sn116 released worker-images-v1 |
| 2026-10-06T23:03 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Fix main: rank the hidden-pool score var |
| 2026-10-06T23:03 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Admit exact ROOT-pinned retired verifier |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

