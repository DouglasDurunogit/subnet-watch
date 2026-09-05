# Subnet watch — dashboard

_snapshot 2026-09-05T09:27:03Z · block 9000292 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 55 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 94 | `miner_burn` < 0.99 |
| Ranked | 95 | passed every gate |
| **Positive margin** | **55** | income beats machine cost |
| New events this window | 4 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 56 | `████████████████████████████` |
| 0–0.2 | 12 | `██████` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 3 | `██` |
| 0.6–0.8 | 10 | `█████` |
| 0.8–0.99 | 8 | `████` |
| ≥0.99 dead | 34 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn92 MicroTensor | 80.7 | 189 | 422 | cpu-small | 9 | 26% |
| 2 | sn107 Minos | 76.8 | 86.43 | 5,236 | cpu-small | 21 | 81% |
| 3 | sn3 Teutonic | 75.7 | 4,050 | 4,050 = | rtx4090* | 5 | 20% |
| 4 | sn67 Harnyx | 72.9 | 26.17 | 135 | cpu-small | 110 | 6% |
| 5 | sn15 ORO | 70.7 | 22.91 | 44.99 | cpu-small | 68 | 93% |
| 6 | sn91 cascade | 70.5 | 854 | 3,442 | rtx4090* | 5 | 52% |
| 7 | sn96 Verathos | 69.2 | 27.46 | 279 | rtx4090 | 79 | 41% |
| 8 | sn56 Gradients | 69.1 | 562 | 1,392 | rtx4090* | 5 | 75% |
| 9 | sn62 Ridges | 68.1 | 420 | 2,124 | rtx4090* | 13 | 26% |
| 10 | sn76 Phylax | 67.5 | 7.63 | 28.01 | cpu-small | 21 | 77% |
| 11 | sn124 Swarm | 66.6 | 274 | 846 | rtx4090* | 25 | 11% |
| 12 | sn111 Claims | 66.4 | 270 | 3,368 | rtx4090* | 5 | 76% |
| 13 | sn80 OpenRoboto | 65.4 | 186 | 671 | rtx4090* | 5 | 71% |
| 14 | sn121 sundae_bar | 63.2 | 1,299 | 1,299 = | cpu-small | 2 | 60% |
| 15 | sn101 Tag101 | 62 | 0.70 | 0.89 | cpu-small | 246 | 90% |
| 16 | sn28 SayGM | 60.3 | 42.76 | 665 | rtx4090* | 44 | 57% |
| 17 | sn41 Almanac | 60 | 35.50 | 94.68 | cpu-small | 84 | 10% |
| 18 | sn14 Cacheon | 59.4 | 1,076 | 2,063 | rtx4090* | 6 | 30% |
| 19 | sn74 Gittensor | 58.4 | 25.08 | 162 | rtx4090 | 12 | 64% |
| 20 | sn51 lium.io | 57.4 | 24.76 | 2,227 | rtx4090* | 62 | 76% |

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
| wide (<30%) | 25 |
| concentrated (30–60%) | 19 |
| dominated (60–90%) | 22 |
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
| 2026-09-05T09:27 | sn47 | SCORING_COMMIT | sn47 commit touches scoring: refine evaluation system |
| 2026-09-05T09:27 | sn47 | README_TASK_DIFF | sn47 README task/scoring sections changed |
| 2026-09-05T09:27 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: fix: exclude stale validator build path f |
| 2026-09-05T09:27 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: fix(challenges): boot when sk/session pl |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

