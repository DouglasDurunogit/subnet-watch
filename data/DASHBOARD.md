# Subnet watch — dashboard

_snapshot 2026-10-06T23:03:13Z · block 9227103 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 60 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 100 | `miner_burn` < 0.99 |
| Ranked | 100 | passed every gate |
| **Positive margin** | **60** | income beats machine cost |
| New events this window | 9 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 66 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 7 | `███` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 28 | `████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn26 Perturb | 79.7 | 379 | 1,281 | rtx3060 | 4 | 60% |
| 2 | sn41 Almanac | 73.7 | 33.34 | 123 | cpu-small | 132 | 2% |
| 3 | sn91 cascade | 72.1 | 536 | 2,145 | cpu-small | 5 | 52% |
| 4 | sn67 Harnyx | 70.4 | 13.14 | 1,083 | cpu-small | 138 | 35% |
| 5 | sn46 Instant | 69.3 | 237 | 249 | cpu-small | 8 | 50% |
| 6 | sn1 Apex | 69.1 | 571 | 1,159 | rtx4090* | 4 | 66% |
| 7 | sn80 OpenRoboto | 68.6 | 481 | 2,177 | rtx4090* | 8 | 25% |
| 8 | sn15 ORO | 67.5 | 8.96 | 17.55 | cpu-small | 53 | 98% |
| 9 | sn4 Targon | 67.2 | 11,011 | 32,465 | rtx4090* | 5 | 70% |
| 10 | sn111 Claims | 66 | 225 | 2,527 | rtx4090* | 6 | 67% |
| 11 | sn120 Affine | 64.8 | 220 | 477 | rtx4090* | 193 | 1% |
| 12 | sn62 Ridges | 64 | 123 | 1,623 | rtx4090* | 33 | 19% |
| 13 | sn23 Trishool | 62.6 | 1,113 | 1,113 = | cpu-small | 2 | 77% |
| 14 | sn65 True Performance | 62.6 | 85.25 | 179 | rtx4090* | 6 | 75% |
| 15 | sn61 RedTeam | 62.2 | 75.90 | 116 | rtx4090* | 129 | 1% |
| 16 | sn14 Cacheon | 60.7 | 46.03 | 1,121 | rtx4090* | 7 | 83% |
| 17 | sn53 engy | 60.3 | 1,425 | 3,903 | rtx4090 | 14 | 22% |
| 18 | sn102 ConnitoAI | 58.6 | 855 | 1,632 | rtx4090* | 6 | 34% |
| 19 | sn74 Gittensor | 58.4 | 26.48 | 156 | rtx4090* | 21 | 50% |
| 20 | sn5 Hone | 58.2 | 38.11 | 42.31 | rtx4090* | 244 | 0% |

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
| wide (<30%) | 22 |
| concentrated (30–60%) | 25 |
| dominated (60–90%) | 24 |
| captured (>90%) | 25 |

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
| 2026-10-06T23:03 | sn10 | BURN_DROP | sn10 burn fell 1.000 -> 0.902 - miners can earn again |
| 2026-10-06T23:03 | sn25 | RELEASE | sn25 released v2026.10.6-1065229510 |
| 2026-10-06T23:03 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Merge feat/operator-discovery-miner into  |
| 2026-10-06T23:03 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Prove dynamic Deepline tools through base |
| 2026-10-06T23:03 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Reduce intake seal contention and isolate |
| 2026-10-06T23:03 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: feat(validator): default miner burn to 9 |
| 2026-10-06T23:03 | sn116 | RELEASE | sn116 released worker-images-v1 |
| 2026-10-06T23:03 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Fix main: rank the hidden-pool score var |
| 2026-10-06T23:03 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Admit exact ROOT-pinned retired verifier |
| 2026-10-06T19:07 | sn10 | SCORING_COMMIT | sn10 commit touches scoring: feat(ops): add private PRO6000 FP8 campai |
| 2026-10-06T19:07 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: fix(validator): /health in daily mode no  |
| 2026-10-06T19:07 | sn28 | RELEASE | sn28 released v0.4.26 |
| 2026-10-06T19:07 | sn50 | SCORING_COMMIT | sn50 commit touches scoring: perf(validator): write predictions to Big |
| 2026-10-06T19:07 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-3947 - [P2] lium-io drops celium-coll |
| 2026-10-06T19:07 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge PR #238: retain validated company e |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

