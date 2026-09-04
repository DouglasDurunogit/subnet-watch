# Subnet watch — dashboard

_snapshot 2026-09-04T21:04:07Z · block 8996584 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 56 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 94 | `miner_burn` < 0.99 |
| Ranked | 95 | passed every gate |
| **Positive margin** | **56** | income beats machine cost |
| New events this window | 9 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 58 | `████████████████████████████` |
| 0–0.2 | 11 | `█████` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 8 | `████` |
| ≥0.99 dead | 34 | `████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn92 MicroTensor | 80.2 | 168 | 375 | cpu-small | 9 | 26% |
| 2 | sn107 Minos | 76.8 | 85.65 | 5,105 | cpu-small | 21 | 81% |
| 3 | sn3 Teutonic | 75.5 | 3,778 | 3,778 = | rtx4090* | 5 | 20% |
| 4 | sn76 Phylax | 72.9 | 26.90 | 71.37 | cpu-small | 21 | 20% |
| 5 | sn67 Harnyx | 71.3 | 17.12 | 89.69 | cpu-small | 144 | 17% |
| 6 | sn91 cascade | 70.3 | 820 | 3,304 | rtx4090* | 5 | 52% |
| 7 | sn15 ORO | 70.3 | 20.81 | 43.99 | cpu-small | 59 | 94% |
| 8 | sn56 Gradients | 68.9 | 533 | 1,325 | rtx4090* | 5 | 75% |
| 9 | sn96 Verathos | 68.7 | 24.43 | 234 | rtx4090 | 84 | 41% |
| 10 | sn111 Claims | 68.3 | 469 | 2,078 | rtx4090* | 5 | 49% |
| 11 | sn124 Swarm | 66.4 | 261 | 807 | rtx4090* | 25 | 11% |
| 12 | sn80 OpenRoboto | 65.4 | 189 | 683 | rtx4090* | 5 | 71% |
| 13 | sn79 MVTRX | 64.5 | 4.81 | 401 | cpu-small | 222 | 9% |
| 14 | sn121 sundae_bar | 62.9 | 1,200 | 1,200 = | cpu-small | 2 | 60% |
| 15 | sn74 Gittensor | 60.7 | 48.61 | 370 | rtx4090 | 12 | 64% |
| 16 | sn28 SayGM | 60.7 | 47.44 | 8,625 | rtx4090* | 47 | 58% |
| 17 | sn101 Tag101 | 60 | 0.10 | 0.75 | cpu-small | 243 | 90% |
| 18 | sn41 Almanac | 59.5 | 31.34 | 94.67 | cpu-small | 88 | 9% |
| 19 | sn14 Cacheon | 59.2 | 1,029 | 1,912 | rtx4090* | 6 | 30% |
| 20 | sn51 lium.io | 58.1 | 28.54 | 2,131 | rtx4090* | 62 | 73% |

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
| wide (<30%) | 28 |
| concentrated (30–60%) | 18 |
| dominated (60–90%) | 20 |
| captured (>90%) | 25 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 98 |
| code-submission (validator runs it) | 11 |
| min_compute.yml (curated) | 11 |
| README keywords (GUESS) | 7 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-09-04T21:04 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: feat(scoring): measurement resolution app |
| 2026-09-04T21:04 | sn25 | RELEASE | sn25 released v2026.9.4-1037517570 |
| 2026-09-04T21:04 | sn34 | SCORING_COMMIT | sn34 commit touches scoring: burn discriminator incentive until KoTH s |
| 2026-09-04T21:04 | sn47 | SCORING_COMMIT | sn47 commit touches scoring: fix extraction and verifier |
| 2026-09-04T21:04 | sn47 | README_TASK_DIFF | sn47 README task/scoring sections changed |
| 2026-09-04T21:04 | sn63 | README_TASK_DIFF | sn63 README task/scoring sections changed |
| 2026-09-04T21:04 | sn71 | README_TASK_DIFF | sn71 README task/scoring sections changed |
| 2026-09-04T21:04 | sn85 | BURN_DROP | sn85 burn fell 1.000 -> 0.360 - miners can earn again |
| 2026-09-04T21:04 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: scoring: refuse sockets with a class so s |
| 2026-09-04T18:32 | sn7 | RELEASE | sn7 released release-20260904-155448: Add min_from_amount and candidat |
| 2026-09-04T18:32 | sn7 | SCORING_COMMIT | sn7 commit touches scoring: CLI: --send verifies source-address contro |
| 2026-09-04T18:32 | sn7 | README_TASK_DIFF | sn7 README task/scoring sections changed |
| 2026-09-04T18:32 | sn25 | RELEASE | sn25 released v2026.9.4-1037416540 |
| 2026-09-04T18:32 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Install FFmpeg for macOS miner tests |
| 2026-09-04T18:32 | sn96 | RELEASE | sn96 released Verathos v0.2.0 – Sleipnir: Verifiable Multi-Node Model  |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

