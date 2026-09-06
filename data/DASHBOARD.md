# Subnet watch — dashboard

_snapshot 2026-09-06T16:12:00Z · block 9009490 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 60 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 94 | `miner_burn` < 0.99 |
| Ranked | 95 | passed every gate |
| **Positive margin** | **60** | income beats machine cost |
| New events this window | 2 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 60 | `████████████████████████████` |
| 0–0.2 | 10 | `█████` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 11 | `█████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 34 | `████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn92 MicroTensor | 81.3 | 223 | 497 | cpu-small | 9 | 26% |
| 2 | sn107 Minos | 76.9 | 88.95 | 5,493 | cpu-small | 21 | 81% |
| 3 | sn3 Teutonic | 75.8 | 4,190 | 4,190 = | rtx4090* | 5 | 20% |
| 4 | sn114 SOMA | 74 | 955 | 955 = | cpu-small | 3 | 80% |
| 5 | sn67 Harnyx | 72.3 | 22.12 | 1,143 | cpu-small | 108 | 31% |
| 6 | sn91 cascade | 70.7 | 903 | 3,638 | rtx4090* | 5 | 52% |
| 7 | sn15 ORO | 70.4 | 22.54 | 21,806 | cpu-small | 81 | 92% |
| 8 | sn96 Verathos | 69.7 | 31.09 | 544 | rtx4090 | 81 | 40% |
| 9 | sn111 Claims | 69.4 | 637 | 2,814 | rtx4090* | 5 | 62% |
| 10 | sn102 ConnitoAI | 69.3 | 607 | 1,489 | rtx4090* | 7 | 27% |
| 11 | sn11 TrajectoryRL | 68.6 | 6,523 | 6,523 = | cpu-small | 1 | 100% |
| 12 | sn62 Ridges | 68.2 | 435 | 2,201 | rtx4090* | 13 | 26% |
| 13 | sn56 Gradients | 67.7 | 375 | 3,520 | rtx4090* | 7 | 49% |
| 14 | sn124 Swarm | 66.7 | 289 | 890 | rtx4090* | 25 | 11% |
| 15 | sn80 OpenRoboto | 65.6 | 196 | 707 | rtx4090* | 5 | 71% |
| 16 | sn121 sundae_bar | 63.2 | 1,329 | 1,329 = | cpu-small | 2 | 60% |
| 17 | sn108 Prometheon | 63 | 92.12 | 354 | rtx4090* | 10 | 33% |
| 18 | sn65 True Performance | 62.6 | 90.27 | 189 | rtx4090* | 6 | 75% |
| 19 | sn101 Tag101 | 62.2 | 0.77 | 0.77 = | cpu-small | 248 | 90% |
| 20 | sn28 SayGM | 61.9 | 67.78 | 11,187 | rtx4090* | 54 | 70% |

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
| concentrated (30–60%) | 18 |
| dominated (60–90%) | 23 |
| captured (>90%) | 23 |

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
| 2026-09-05T18:13 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: build: refresh reviewed gateway verifier  |
| 2026-09-05T16:00 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: validator: add private bounded attempt re |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

