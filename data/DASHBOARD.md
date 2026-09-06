# Subnet watch — dashboard

_snapshot 2026-09-06T18:30:25Z · block 9010180 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 61 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 95 | `miner_burn` < 0.99 |
| Ranked | 95 | passed every gate |
| **Positive margin** | **61** | income beats machine cost |
| New events this window | 2 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 59 | `████████████████████████████` |
| 0–0.2 | 11 | `█████` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 11 | `█████` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 33 | `████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn92 MicroTensor | 81.5 | 233 | 519 | cpu-small | 9 | 26% |
| 2 | sn107 Minos | 77.1 | 93.84 | 5,742 | cpu-small | 21 | 81% |
| 3 | sn3 Teutonic | 76 | 4,400 | 4,400 = | rtx4090* | 5 | 20% |
| 4 | sn114 SOMA | 74.2 | 1,004 | 1,004 = | cpu-small | 3 | 80% |
| 5 | sn67 Harnyx | 72.4 | 23.18 | 1,195 | cpu-small | 108 | 31% |
| 6 | sn14 Cacheon | 71.5 | 1,162 | 2,205 | rtx4090* | 6 | 30% |
| 7 | sn91 cascade | 70.8 | 950 | 3,824 | rtx4090* | 5 | 52% |
| 8 | sn96 Verathos | 70.3 | 36.31 | 618 | rtx4090 | 81 | 40% |
| 9 | sn15 ORO | 69.9 | 23.75 | 46.58 | cpu-small | 82 | 92% |
| 10 | sn102 ConnitoAI | 69.4 | 620 | 1,695 | rtx4090* | 7 | 29% |
| 11 | sn11 TrajectoryRL | 68.9 | 7,063 | 7,063 = | cpu-small | 1 | 100% |
| 12 | sn111 Claims | 68.6 | 504 | 2,233 | rtx4090* | 5 | 47% |
| 13 | sn62 Ridges | 68.4 | 455 | 2,298 | rtx4090* | 13 | 26% |
| 14 | sn56 Gradients | 67.9 | 392 | 3,676 | rtx4090* | 7 | 49% |
| 15 | sn124 Swarm | 66.9 | 304 | 936 | rtx4090* | 25 | 11% |
| 16 | sn80 OpenRoboto | 65.7 | 205 | 738 | rtx4090* | 5 | 71% |
| 17 | sn121 sundae_bar | 63.4 | 1,396 | 1,396 = | cpu-small | 2 | 60% |
| 18 | sn108 Prometheon | 63.2 | 97.18 | 372 | rtx4090* | 10 | 33% |
| 19 | sn65 True Performance | 62.8 | 95.72 | 200 | rtx4090* | 6 | 75% |
| 20 | sn101 Tag101 | 62.4 | 0.86 | 0.86 = | cpu-small | 243 | 90% |

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
| concentrated (30–60%) | 21 |
| dominated (60–90%) | 24 |
| captured (>90%) | 22 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 99 |
| min_compute.yml (curated) | 11 |
| code-submission (validator runs it) | 10 |
| README keywords (GUESS) | 7 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-09-06T18:30 | sn14 | RELEASE | sn14 released GLM-5.3 mock mainnet submissions (validator self-test, 2 |
| 2026-09-06T18:30 | sn93 | README_TASK_DIFF | sn93 README task/scoring sections changed |
| 2026-09-06T16:12 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Integrate qualified Solidity validator ac |
| 2026-09-06T16:12 | sn47 | BURN_DROP | sn47 burn fell 1.000 -> 0.942 - miners can earn again |
| 2026-09-06T12:51 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Checkpoint held repair sources and valida |
| 2026-09-06T04:34 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Isolate Arena failure regressions and ver |
| 2026-09-06T04:34 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Add public registered-miner endpoint pilo |
| 2026-09-06T00:06 | sn74 | RELEASE | sn74 released release-20260905-223823 |
| 2026-09-06T00:06 | sn74 | SCORING_COMMIT | sn74 commit touches scoring: serving miner: an attestation waits for p |
| 2026-09-05T22:21 | sn7 | RELEASE | sn7 released release-20260905-204833 |
| 2026-09-05T22:21 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: chore(validator): bind existing recovery  |
| 2026-09-05T20:34 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Protect validator seed custody and qualif |
| 2026-09-05T20:34 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Bind validator workflow to archive retry  |
| 2026-09-05T20:34 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Add external miner pilot launch handoffs |
| 2026-09-05T18:13 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: fix(reporting): rows shown with their acc |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

