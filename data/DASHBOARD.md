# Subnet watch — dashboard

_snapshot 2026-09-04T23:01:35Z · block 8997169 · run_status **ok**_

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
| New events this window | 3 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 57 | `████████████████████████████` |
| 0–0.2 | 12 | `██████` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 8 | `████` |
| ≥0.99 dead | 34 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn92 MicroTensor | 80.2 | 167 | 373 | cpu-small | 9 | 26% |
| 2 | sn107 Minos | 76.5 | 81.53 | 4,991 | cpu-small | 21 | 81% |
| 3 | sn3 Teutonic | 75.4 | 3,743 | 3,743 = | rtx4090* | 5 | 20% |
| 4 | sn76 Phylax | 72.8 | 26.74 | 70.93 | cpu-small | 21 | 20% |
| 5 | sn67 Harnyx | 71.2 | 16.90 | 88.63 | cpu-small | 144 | 17% |
| 6 | sn91 cascade | 70.3 | 823 | 3,318 | rtx4090* | 5 | 52% |
| 7 | sn15 ORO | 70.2 | 20.61 | 43.59 | cpu-small | 59 | 94% |
| 8 | sn96 Verathos | 69.3 | 28.37 | 285 | rtx4090 | 79 | 41% |
| 9 | sn56 Gradients | 68.9 | 527 | 1,310 | rtx4090* | 5 | 75% |
| 10 | sn102 ConnitoAI | 68.8 | 522 | 1,540 | rtx4090* | 7 | 29% |
| 11 | sn111 Claims | 68.3 | 458 | 2,032 | rtx4090* | 5 | 49% |
| 12 | sn124 Swarm | 66.4 | 259 | 800 | rtx4090* | 25 | 11% |
| 13 | sn80 OpenRoboto | 65.3 | 182 | 657 | rtx4090* | 5 | 71% |
| 14 | sn121 sundae_bar | 62.9 | 1,186 | 1,186 = | cpu-small | 2 | 60% |
| 15 | sn28 SayGM | 61 | 52.33 | 7,709 | rtx4090* | 46 | 52% |
| 16 | sn74 Gittensor | 60.5 | 46.13 | 353 | rtx4090 | 12 | 65% |
| 17 | sn101 Tag101 | 60.4 | 0.20 | 0.78 | cpu-small | 244 | 90% |
| 18 | sn41 Almanac | 59.5 | 31.10 | 93.43 | cpu-small | 88 | 9% |
| 19 | sn14 Cacheon | 59.1 | 1,011 | 1,927 | rtx4090* | 6 | 30% |
| 20 | sn51 lium.io | 58.8 | 34.15 | 2,202 | rtx4090* | 62 | 73% |

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
| wide (<30%) | 27 |
| concentrated (30–60%) | 19 |
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
| 2026-09-04T23:02 | sn7 | RELEASE | sn7 released release-20260904-214340: Bump version to 3.3.2 (#722) |
| 2026-09-04T23:02 | sn25 | RELEASE | sn25 released v2026.9.4-1037600680 |
| 2026-09-04T23:02 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: ci: classify bundle for the hidden-tests  |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

