# Subnet watch — dashboard

_snapshot 2026-10-03T21:48:46Z · block 9205131 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 61 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 98 | `miner_burn` < 0.99 |
| Ranked | 98 | passed every gate |
| **Positive margin** | **61** | income beats machine cost |
| New events this window | 4 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 65 | `████████████████████████████` |
| 0–0.2 | 10 | `████` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 8 | `███` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 30 | `█████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn41 Almanac | 74.4 | 39.46 | 130 | cpu-small | 124 | 2% |
| 2 | sn91 cascade | 72.4 | 586 | 2,348 | cpu-small | 5 | 52% |
| 3 | sn53 engy | 71.9 | 1,286 | 3,525 | rtx4090 | 14 | 22% |
| 4 | sn1 Apex | 69.5 | 643 | 1,036 | rtx4090* | 4 | 61% |
| 5 | sn56 Gradients | 69.5 | 636 | 5,158 | rtx4090* | 8 | 39% |
| 6 | sn67 Harnyx | 68.7 | 8.77 | 1,126 | cpu-small | 118 | 36% |
| 7 | sn46 Instant | 68.3 | 177 | 222 | cpu-small | 10 | 51% |
| 8 | sn15 ORO | 66.8 | 8.50 | 16.98 | cpu-small | 55 | 98% |
| 9 | sn111 Claims | 66.7 | 279 | 2,478 | rtx4090* | 6 | 65% |
| 10 | sn4 Targon | 65.5 | 6,713 | 31,753 | rtx4090* | 5 | 70% |
| 11 | sn62 Ridges | 63.2 | 97.54 | 2,278 | rtx4090* | 30 | 25% |
| 12 | sn61 RedTeam | 62.8 | 84.61 | 153 | rtx4090* | 113 | 2% |
| 13 | sn28 SayGM | 62.3 | 76.33 | 931 | rtx4090* | 62 | 14% |
| 14 | sn14 Cacheon | 61.1 | 52.01 | 1,815 | rtx4090* | 13 | 23% |
| 15 | sn80 OpenRoboto | 59.2 | 1,027 | 3,116 | rtx4090* | 8 | 33% |
| 16 | sn5 Hone | 59 | 37.77 | 40.00 | rtx4090* | 245 | 0% |
| 17 | sn38 ChronoLLM | 58.5 | 340 | 4,614 | cpu-small | 10 | 52% |
| 18 | sn49 Nepher Robotics | 58.2 | 763 | 1,534 | rtx4090* | 4 | 69% |
| 19 | sn74 Gittensor | 58.2 | 25.00 | 272 | rtx4090* | 21 | 50% |
| 20 | sn100 Cortex | 57.2 | 15.33 | 2,400 | rtx4090* | 26 | 70% |

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
| wide (<30%) | 23 |
| concentrated (30–60%) | 24 |
| dominated (60–90%) | 23 |
| captured (>90%) | 24 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 101 |
| README keywords (GUESS) | 12 |
| min_compute.yml (curated) | 8 |
| code-submission (validator runs it) | 7 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-10-03T21:49 | sn11 | RELEASE | sn11 released v0.7.4 |
| 2026-10-03T21:49 | sn11 | SCORING_COMMIT | sn11 commit touches scoring: [coding-agent] validator: weight-only by  |
| 2026-10-03T21:49 | sn22 | BURN_DROP | sn22 burn fell 1.000 -> 0.820 - miners can earn again |
| 2026-10-03T21:49 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Reject partial successor reward ownership |
| 2026-10-03T18:40 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Record verified five-role source staging |
| 2026-10-03T14:57 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Bind unverified homepage context to obser |
| 2026-10-03T14:57 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: Merge pull request #308 from reliquadotai |
| 2026-10-03T14:57 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Keep original audit source pins across a |
| 2026-10-03T10:31 | sn15 | RELEASE | sn15 released Validator v2.1.0: runtime contract on claim and delivery |
| 2026-10-03T10:31 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: Validator v2.1.0: runtime contract on cla |
| 2026-10-03T10:31 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Verify HTTP retry controls and preserve q |
| 2026-10-03T10:31 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: fix: prefer verified exact homepage brand |
| 2026-10-03T10:31 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Document verified successor, external mi |
| 2026-10-03T05:11 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Preserve concurrent verifier lease correc |
| 2026-10-03T05:11 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: perf(corpus): verify drand rounds by BLS  |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

