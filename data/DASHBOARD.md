# Subnet watch — dashboard

_snapshot 2026-09-05T05:40:12Z · block 8999159 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 57 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 94 | `miner_burn` < 0.99 |
| Ranked | 95 | passed every gate |
| **Positive margin** | **57** | income beats machine cost |
| New events this window | 4 | see ALARMS.md |

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
| 1 | sn92 MicroTensor | 80.4 | 178 | 396 | cpu-small | 9 | 26% |
| 2 | sn107 Minos | 76.7 | 83.98 | 5,369 | cpu-small | 21 | 80% |
| 3 | sn3 Teutonic | 75.6 | 3,876 | 3,876 = | rtx4090* | 5 | 20% |
| 4 | sn76 Phylax | 72.9 | 27.35 | 72.54 | cpu-small | 21 | 20% |
| 5 | sn67 Harnyx | 72.8 | 25.25 | 130 | cpu-small | 108 | 6% |
| 6 | sn102 ConnitoAI | 70.5 | 854 | 2,003 | rtx4090* | 6 | 37% |
| 7 | sn91 cascade | 70.4 | 831 | 3,349 | rtx4090* | 5 | 52% |
| 8 | sn15 ORO | 70 | 20.49 | 43.70 | cpu-small | 62 | 94% |
| 9 | sn56 Gradients | 68.9 | 538 | 1,335 | rtx4090* | 5 | 75% |
| 10 | sn96 Verathos | 68.8 | 24.96 | 269 | rtx4090 | 78 | 40% |
| 11 | sn11 TrajectoryRL | 67.9 | 5,324 | 5,324 = | cpu-small | 1 | 100% |
| 12 | sn62 Ridges | 67.9 | 400 | 2,024 | rtx4090* | 13 | 26% |
| 13 | sn124 Swarm | 66.4 | 265 | 817 | rtx4090* | 25 | 11% |
| 14 | sn80 OpenRoboto | 65.3 | 183 | 661 | rtx4090* | 5 | 71% |
| 15 | sn111 Claims | 65.2 | 195 | 2,091 | rtx4090* | 5 | 50% |
| 16 | sn98 NeverPlayAlone | 64.4 | 1,857 | 1,857 = | cpu-small | 1 | 100% |
| 17 | sn121 sundae_bar | 63 | 1,240 | 1,240 = | cpu-small | 2 | 60% |
| 18 | sn101 Tag101 | 61.5 | 0.63 | 0.85 | cpu-small | 234 | 90% |
| 19 | sn74 Gittensor | 60.5 | 45.33 | 361 | rtx4090 | 12 | 64% |
| 20 | sn28 SayGM | 60.5 | 44.64 | 738 | rtx4090* | 56 | 64% |

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
| concentrated (30–60%) | 19 |
| dominated (60–90%) | 21 |
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
| 2026-09-05T05:40 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: docs(scoring): standing and resolution am |
| 2026-09-05T05:40 | sn62 | RELEASE | sn62 released v0.3.0 |
| 2026-09-05T05:40 | sn62 | SCORING_COMMIT | sn62 commit touches scoring: test: :white_check_mark: Add tests valida |
| 2026-09-05T05:40 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: fix: validate retained gateway archives b |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

