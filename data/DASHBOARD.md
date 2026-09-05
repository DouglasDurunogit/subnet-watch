# Subnet watch — dashboard

_snapshot 2026-09-05T12:59:24Z · block 9001354 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 55 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 95 | `miner_burn` < 0.99 |
| Ranked | 96 | passed every gate |
| **Positive margin** | **55** | income beats machine cost |
| New events this window | 2 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 57 | `████████████████████████████` |
| 0–0.2 | 11 | `█████` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 9 | `████` |
| ≥0.99 dead | 33 | `████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn92 MicroTensor | 80.9 | 201 | 448 | cpu-small | 9 | 26% |
| 2 | sn107 Minos | 76.7 | 86.36 | 5,254 | cpu-small | 21 | 81% |
| 3 | sn3 Teutonic | 75.7 | 4,008 | 4,008 = | rtx4090* | 5 | 20% |
| 4 | sn67 Harnyx | 72.9 | 26.22 | 135 | cpu-small | 111 | 6% |
| 5 | sn102 ConnitoAI | 71.5 | 1,148 | 1,841 | rtx4090* | 5 | 33% |
| 6 | sn76 Phylax | 71.1 | 17.77 | 62.20 | cpu-small | 21 | 50% |
| 7 | sn15 ORO | 70.7 | 23.19 | 45.19 | cpu-small | 71 | 93% |
| 8 | sn91 cascade | 70.4 | 841 | 3,388 | rtx4090* | 5 | 52% |
| 9 | sn96 Verathos | 69.2 | 27.27 | 406 | rtx4090 | 79 | 40% |
| 10 | sn56 Gradients | 69.1 | 562 | 1,391 | rtx4090* | 5 | 75% |
| 11 | sn62 Ridges | 68.2 | 427 | 2,157 | rtx4090* | 13 | 26% |
| 12 | sn124 Swarm | 66.6 | 275 | 848 | rtx4090* | 25 | 11% |
| 13 | sn111 Claims | 66.4 | 270 | 3,374 | rtx4090* | 5 | 76% |
| 14 | sn80 OpenRoboto | 65.5 | 190 | 688 | rtx4090* | 5 | 71% |
| 15 | sn121 sundae_bar | 63.2 | 1,312 | 1,312 = | cpu-small | 2 | 60% |
| 16 | sn101 Tag101 | 62 | 0.71 | 0.89 | cpu-small | 242 | 90% |
| 17 | sn41 Almanac | 60 | 35.82 | 92.08 | cpu-small | 85 | 10% |
| 18 | sn14 Cacheon | 59.4 | 1,079 | 2,069 | rtx4090* | 6 | 30% |
| 19 | sn51 lium.io | 58.8 | 34.45 | 2,071 | rtx4090* | 62 | 76% |
| 20 | sn74 Gittensor | 58.3 | 24.39 | 159 | rtx4090 | 12 | 64% |

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
| 2026-09-05T12:59 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge pull request #177 from leadpoet/cod |
| 2026-09-05T12:59 | sn80 | README_TASK_DIFF | sn80 README task/scoring sections changed |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

