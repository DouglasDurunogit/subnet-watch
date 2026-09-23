# Subnet watch — dashboard

_snapshot 2026-09-23T01:37:55Z · block 9127083 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 60 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 98 | `miner_burn` < 0.99 |
| Ranked | 98 | passed every gate |
| **Positive margin** | **60** | income beats machine cost |
| New events this window | 2 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 66 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 30 | `█████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn114 SOMA | 91.6 | 3,000 | 7,503 | cpu-small | 4 | 50% |
| 2 | sn4 Targon | 78.5 | 9,394 | 26,411 | rtx4090* | 6 | 53% |
| 3 | sn3 Teutonic | 76.7 | 5,546 | 5,546 = | rtx4090* | 5 | 20% |
| 4 | sn69 Herald | 73.4 | 2,030 | 2,030 = | rtx4090* | 3 | 33% |
| 5 | sn91 cascade | 72.7 | 646 | 2,587 | cpu-small | 5 | 52% |
| 6 | sn1 Apex | 71 | 996 | 1,230 | rtx4090* | 4 | 55% |
| 7 | sn102 ConnitoAI | 70.7 | 912 | 1,574 | rtx4090* | 6 | 33% |
| 8 | sn67 Harnyx | 69.5 | 10.77 | 1,364 | cpu-small | 126 | 37% |
| 9 | sn107 Minos | 69 | 363 | 30,742 | cpu-small | 20 | 80% |
| 10 | sn56 Gradients | 68.6 | 483 | 5,897 | rtx4090* | 12 | 40% |
| 11 | sn15 ORO | 68.6 | 12.18 | 25.35 | cpu-small | 65 | 96% |
| 12 | sn38 ChronoLLM | 68.2 | 188 | 2,557 | cpu-small | 10 | 52% |
| 13 | sn124 Swarm | 67.1 | 329 | 1,049 | rtx4090* | 25 | 11% |
| 14 | sn111 Claims | 66.3 | 266 | 3,170 | rtx4090* | 5 | 76% |
| 15 | sn100 Cortex | 63.2 | 96.80 | 160 | rtx4090* | 11 | 71% |
| 16 | sn62 Ridges | 61.6 | 60.29 | 2,938 | rtx4090* | 19 | 30% |
| 17 | sn23 Trishool | 61.5 | 791 | 791 = | cpu-small | 2 | 80% |
| 18 | sn28 SayGM | 61.2 | 56.00 | 936 | rtx4090* | 64 | 41% |
| 19 | sn60 Bitsec.ai | 60.4 | 567 | 567 = | cpu-small | 3 | 50% |
| 20 | sn74 Gittensor | 60.4 | 45.68 | 309 | rtx4090* | 17 | 64% |

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
| dominated (60–90%) | 21 |
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
| 2026-09-22T06:50 | sn15 | RELEASE | sn15 released v2.0.29 |
| 2026-09-22T06:50 | sn25 | RELEASE | sn25 released v2026.9.21-1052448720 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

