# Subnet watch — dashboard

_snapshot 2026-09-23T12:18:54Z · block 9130282 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 64 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 98 | `miner_burn` < 0.99 |
| Ranked | 98 | passed every gate |
| **Positive margin** | **64** | income beats machine cost |
| New events this window | 5 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 65 | `████████████████████████████` |
| 0–0.2 | 9 | `████` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 8 | `███` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 30 | `█████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn4 Targon | 80.4 | 16,255 | 26,133 | rtx4090* | 5 | 54% |
| 2 | sn3 Teutonic | 76.7 | 5,427 | 5,427 = | rtx4090* | 5 | 20% |
| 3 | sn114 SOMA | 75.7 | 1,834 | 3,670 | cpu-small | 5 | 50% |
| 4 | sn91 cascade | 72.6 | 625 | 2,504 | cpu-small | 5 | 52% |
| 5 | sn67 Harnyx | 71.3 | 17.66 | 1,218 | cpu-small | 124 | 34% |
| 6 | sn1 Apex | 70.7 | 913 | 1,140 | rtx4090* | 4 | 57% |
| 7 | sn56 Gradients | 69.5 | 633 | 5,784 | rtx4090* | 10 | 40% |
| 8 | sn107 Minos | 69.4 | 397 | 27,954 | cpu-small | 20 | 78% |
| 9 | sn15 ORO | 69.2 | 13.79 | 21,556 | cpu-small | 68 | 96% |
| 10 | sn111 Claims | 69.1 | 588 | 2,602 | rtx4090* | 5 | 64% |
| 11 | sn38 ChronoLLM | 68.3 | 193 | 2,621 | cpu-small | 10 | 52% |
| 12 | sn102 ConnitoAI | 68.1 | 424 | 1,404 | rtx4090* | 7 | 30% |
| 13 | sn124 Swarm | 67 | 318 | 1,013 | rtx4090* | 25 | 11% |
| 14 | sn100 Cortex | 63.2 | 96.06 | 159 | rtx4090* | 11 | 70% |
| 15 | sn62 Ridges | 61.3 | 58.21 | 2,848 | rtx4090* | 19 | 30% |
| 16 | sn26 Perturb | 61.3 | 57.42 | 57.42 = | rtx3060 | 4 | 90% |
| 17 | sn28 SayGM | 61.3 | 57.24 | 793 | rtx4090* | 59 | 43% |
| 18 | sn23 Trishool | 61.2 | 722 | 722 = | cpu-small | 2 | 81% |
| 19 | sn60 Bitsec.ai | 60.4 | 563 | 563 = | cpu-small | 3 | 50% |
| 20 | sn74 Gittensor | 60.3 | 50.77 | 126 | rtx4090* | 15 | 64% |

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
| concentrated (30–60%) | 23 |
| dominated (60–90%) | 23 |
| captured (>90%) | 25 |

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
| 2026-09-23T12:19 | sn28 | SCORING_COMMIT | sn28 commit touches scoring: ci: validate rendered Envoy configs with  |
| 2026-09-23T12:19 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-3505 - [P2] validator: keep the Docke |
| 2026-09-23T12:19 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-09-23T12:19 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Document company-only validator compatibi |
| 2026-09-23T12:19 | sn97 | SCORING_COMMIT | sn97 commit touches scoring: fix: show tasks and trajectories on the d |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

