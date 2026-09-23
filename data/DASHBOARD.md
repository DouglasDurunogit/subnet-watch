# Subnet watch — dashboard

_snapshot 2026-09-23T06:44:59Z · block 9128619 · run_status **ok**_

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
| New events this window | 2 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 66 | `████████████████████████████` |
| 0–0.2 | 8 | `███` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 8 | `███` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 30 | `█████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn114 SOMA | 91.7 | 3,049 | 7,625 | cpu-small | 4 | 50% |
| 2 | sn4 Targon | 78.5 | 9,442 | 26,546 | rtx4090* | 6 | 53% |
| 3 | sn3 Teutonic | 76.8 | 5,575 | 5,575 = | rtx4090* | 5 | 20% |
| 4 | sn91 cascade | 72.7 | 642 | 2,572 | cpu-small | 5 | 52% |
| 5 | sn102 ConnitoAI | 71.5 | 1,169 | 1,247 | rtx4090* | 5 | 26% |
| 6 | sn67 Harnyx | 71.4 | 18.19 | 1,252 | cpu-small | 114 | 34% |
| 7 | sn1 Apex | 70.9 | 974 | 1,208 | rtx4090* | 4 | 56% |
| 8 | sn56 Gradients | 69.6 | 651 | 5,945 | rtx4090* | 10 | 40% |
| 9 | sn111 Claims | 69.2 | 607 | 2,685 | rtx4090* | 5 | 64% |
| 10 | sn15 ORO | 69.1 | 14.42 | 21,967 | cpu-small | 67 | 96% |
| 11 | sn107 Minos | 68.9 | 358 | 29,817 | cpu-small | 20 | 80% |
| 12 | sn38 ChronoLLM | 68.3 | 191 | 2,605 | cpu-small | 10 | 52% |
| 13 | sn124 Swarm | 67.1 | 328 | 1,044 | rtx4090* | 25 | 11% |
| 14 | sn100 Cortex | 63.3 | 98.73 | 163 | rtx4090* | 11 | 70% |
| 15 | sn62 Ridges | 61.5 | 60.61 | 2,951 | rtx4090* | 19 | 30% |
| 16 | sn23 Trishool | 61.4 | 778 | 778 = | cpu-small | 2 | 80% |
| 17 | sn28 SayGM | 60.9 | 50.30 | 924 | rtx4090* | 59 | 42% |
| 18 | sn74 Gittensor | 60.8 | 50.56 | 324 | rtx4090* | 17 | 64% |
| 19 | sn60 Bitsec.ai | 60.4 | 574 | 574 = | cpu-small | 3 | 50% |
| 20 | sn61 RedTeam | 58.7 | 25.88 | 632 | rtx4090* | 119 | 7% |

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
| concentrated (30–60%) | 24 |
| dominated (60–90%) | 22 |
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
| 2026-09-23T06:45 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Retry interrupted miner downloads and red |
| 2026-09-23T06:45 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: wvk 23 live 17:20 UTC: AGENTS.md snapsho |
| 2026-09-23T01:38 | sn25 | RELEASE | sn25 released v2026.9.22-1053244730 |
| 2026-09-23T01:38 | sn100 | BURN_DROP | sn100 burn fell 1.000 -> 0.708 - miners can earn again |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

