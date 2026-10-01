# Subnet watch — dashboard

_snapshot 2026-10-01T06:20:21Z · block 9186089 · run_status **ok**_

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
| New events this window | 7 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 66 | `████████████████████████████` |
| 0–0.2 | 9 | `████` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 30 | `█████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn41 Almanac | 74.5 | 40.66 | 532 | cpu-small | 121 | 8% |
| 2 | sn23 Trishool | 74.2 | 1,003 | 1,003 = | cpu-small | 2 | 80% |
| 3 | sn120 Affine | 73 | 1,846 | 1,846 = | rtx4090* | 23 | 4% |
| 4 | sn91 cascade | 72.3 | 577 | 2,310 | cpu-small | 5 | 52% |
| 5 | sn53 engy | 72.2 | 1,442 | 3,956 | rtx4090 | 14 | 22% |
| 6 | sn1 Apex | 70.9 | 980 | 1,150 | rtx4090* | 4 | 55% |
| 7 | sn56 Gradients | 69.6 | 661 | 5,358 | rtx4090* | 9 | 39% |
| 8 | sn46 Instant | 69.6 | 256 | 310 | cpu-small | 5 | 68% |
| 9 | sn107 Minos | 68.9 | 355 | 30,208 | cpu-small | 20 | 80% |
| 10 | sn15 ORO | 68.7 | 11.83 | 20,918 | cpu-small | 68 | 96% |
| 11 | sn102 ConnitoAI | 68.6 | 495 | 1,728 | rtx4090* | 7 | 34% |
| 12 | sn111 Claims | 68 | 419 | 2,551 | rtx4090* | 5 | 64% |
| 13 | sn96 Verathos | 67.2 | 17.55 | 273 | rtx4090 | 75 | 30% |
| 14 | sn4 Targon | 67.1 | 10,832 | 34,115 | rtx4090* | 3 | 72% |
| 15 | sn14 Cacheon | 64.9 | 161 | 2,369 | rtx4090* | 16 | 29% |
| 16 | sn3 Teutonic | 64.5 | 5,036 | 5,036 = | rtx4090* | 5 | 20% |
| 17 | sn62 Ridges | 63.8 | 115 | 1,433 | rtx4090* | 25 | 15% |
| 18 | sn61 RedTeam | 62.8 | 87.18 | 158 | rtx4090* | 112 | 2% |
| 19 | sn28 SayGM | 60.1 | 39.96 | 961 | rtx4090* | 71 | 19% |
| 20 | sn5 Hone | 59.6 | 40.41 | 43.09 | rtx4090* | 242 | 0% |

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
| concentrated (30–60%) | 24 |
| dominated (60–90%) | 23 |
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
| 2026-10-01T06:20 | sn25 | RELEASE | sn25 released v2026.9.30-1060350310 |
| 2026-10-01T06:20 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Verify and aggregate pinned mainnet image |
| 2026-10-01T06:20 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Bind protected workflows to verifier reco |
| 2026-10-01T06:20 | sn74 | RELEASE | sn74 released release-20261001-004737 |
| 2026-10-01T06:20 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Publish C5 miner inputs and connection gu |
| 2026-10-01T06:20 | sn78 | README_TASK_DIFF | sn78 README task/scoring sections changed |
| 2026-10-01T06:20 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Verify controlled native Agent tool roll |
| 2026-10-01T00:12 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Bind October verifier evidence release |
| 2026-10-01T00:12 | sn74 | RELEASE | sn74 released release-20260930-235444 |
| 2026-10-01T00:12 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Separate miner transport signer from coho |
| 2026-10-01T00:12 | sn117 | RELEASE | sn117 released everycli v0.1.4 |
| 2026-10-01T00:12 | sn117 | README_TASK_DIFF | sn117 README task/scoring sections changed |
| 2026-09-30T20:46 | sn5 | SCORING_COMMIT | sn5 commit touches scoring: Merge pull request #13 from hone-subnet-or |
| 2026-09-30T20:46 | sn8 | SCORING_COMMIT | sn8 commit touches scoring: disable miner daily summary (#934) |
| 2026-09-30T20:46 | sn41 | SCORING_COMMIT | sn41 commit touches scoring: Updates to handling excess miner emission |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

