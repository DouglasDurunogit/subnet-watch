# Subnet watch — dashboard

_snapshot 2026-09-22T23:07:58Z · block 9126334 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 60 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 97 | `miner_burn` < 0.99 |
| Ranked | 97 | passed every gate |
| **Positive margin** | **60** | income beats machine cost |
| New events this window | 2 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 66 | `████████████████████████████` |
| 0–0.2 | 8 | `███` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 8 | `███` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 31 | `█████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn114 SOMA | 91.6 | 2,978 | 7,446 | cpu-small | 4 | 50% |
| 2 | sn4 Targon | 78.5 | 9,412 | 26,463 | rtx4090* | 6 | 53% |
| 3 | sn3 Teutonic | 76.8 | 5,617 | 5,617 = | rtx4090* | 5 | 20% |
| 4 | sn69 Herald | 73.4 | 2,035 | 2,035 = | rtx4090* | 3 | 33% |
| 5 | sn91 cascade | 72.7 | 649 | 2,600 | cpu-small | 5 | 52% |
| 6 | sn1 Apex | 71.1 | 1,013 | 1,247 | rtx4090* | 4 | 55% |
| 7 | sn102 ConnitoAI | 70.8 | 934 | 1,611 | rtx4090* | 6 | 33% |
| 8 | sn67 Harnyx | 69.6 | 10.79 | 1,366 | cpu-small | 126 | 37% |
| 9 | sn107 Minos | 68.9 | 357 | 30,310 | cpu-small | 20 | 80% |
| 10 | sn15 ORO | 68.9 | 12.19 | 25.36 | cpu-small | 65 | 96% |
| 11 | sn56 Gradients | 68.6 | 483 | 5,905 | rtx4090* | 12 | 40% |
| 12 | sn38 ChronoLLM | 68.2 | 188 | 2,555 | cpu-small | 10 | 52% |
| 13 | sn124 Swarm | 67.1 | 327 | 1,043 | rtx4090* | 25 | 11% |
| 14 | sn111 Claims | 66.4 | 268 | 3,190 | rtx4090* | 5 | 76% |
| 15 | sn28 SayGM | 61.7 | 64.92 | 1,154 | rtx4090* | 62 | 35% |
| 16 | sn62 Ridges | 61.6 | 60.07 | 2,928 | rtx4090* | 19 | 30% |
| 17 | sn23 Trishool | 61.5 | 792 | 792 = | cpu-small | 2 | 80% |
| 18 | sn74 Gittensor | 60.4 | 45.66 | 313 | rtx4090* | 17 | 65% |
| 19 | sn60 Bitsec.ai | 60.3 | 549 | 549 = | cpu-small | 3 | 50% |
| 20 | sn51 lium.io | 59.8 | 46.32 | 2,684 | rtx4090* | 68 | 77% |

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
| dominated (60–90%) | 20 |
| captured (>90%) | 27 |

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
| 2026-09-22T23:08 | sn14 | RELEASE | sn14 released glm53-mock-submission-20260906: Merge m3-runtime-seed-re |
| 2026-09-22T23:08 | sn56 | SCORING_COMMIT | sn56 commit touches scoring: Add Runpod evaluation backend via dstack  |
| 2026-09-22T20:21 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Resume bounded parallel miner fault contr |
| 2026-09-22T20:21 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Verify shadow rounds under current Arena  |
| 2026-09-22T20:21 | sn74 | RELEASE | sn74 released release-20260922-190530: spark-hermes: full scoring conf |
| 2026-09-22T20:21 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: AA gap-fill go-live 1/2: affine_scitext  |
| 2026-09-22T17:19 | sn1 | RELEASE | sn1 released v4.4.8 |
| 2026-09-22T17:19 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Make miner fault recovery durable and rec |
| 2026-09-22T17:19 | sn50 | RELEASE | sn50 released v1.13.0 |
| 2026-09-22T17:19 | sn74 | RELEASE | sn74 released release-20260922-171907 |
| 2026-09-22T17:19 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: rollouts: affine_gen_v1 shared store/tea |
| 2026-09-22T06:50 | sn15 | RELEASE | sn15 released v2.0.29 |
| 2026-09-22T06:50 | sn25 | RELEASE | sn25 released v2026.9.21-1052448720 |
| 2026-09-22T06:50 | sn26 | SCORING_COMMIT | sn26 commit touches scoring: fix: commitment snapshot carries the mode |
| 2026-09-22T06:50 | sn45 | SCORING_COMMIT | sn45 commit touches scoring: Owe a share again to a miner sent nothing |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

