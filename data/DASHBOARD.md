# Subnet watch — dashboard

_snapshot 2026-10-04T06:24:03Z · block 9207707 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 59 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 98 | `miner_burn` < 0.99 |
| Ranked | 98 | passed every gate |
| **Positive margin** | **59** | income beats machine cost |
| New events this window | 6 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 66 | `████████████████████████████` |
| 0–0.2 | 8 | `███` |
| 0.2–0.4 | 7 | `███` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 7 | `███` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 30 | `█████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn23 Trishool | 74.2 | 1,016 | 1,016 = | cpu-small | 2 | 78% |
| 2 | sn41 Almanac | 73.9 | 35.52 | 2,179 | cpu-small | 127 | 31% |
| 3 | sn53 engy | 71.9 | 1,307 | 3,582 | rtx4090 | 14 | 22% |
| 4 | sn91 cascade | 71.5 | 455 | 2,430 | cpu-small | 5 | 52% |
| 5 | sn67 Harnyx | 70.6 | 14.24 | 953 | cpu-small | 123 | 30% |
| 6 | sn46 Instant | 70.2 | 303 | 349 | cpu-small | 6 | 52% |
| 7 | sn56 Gradients | 69.6 | 650 | 5,271 | rtx4090* | 8 | 39% |
| 8 | sn1 Apex | 69.4 | 612 | 1,014 | rtx4090* | 4 | 63% |
| 9 | sn111 Claims | 68.8 | 526 | 2,329 | rtx4090* | 5 | 60% |
| 10 | sn120 Affine | 68.1 | 487 | 734 | rtx4090* | 77 | 2% |
| 11 | sn15 ORO | 67.3 | 9.10 | 21,911 | cpu-small | 52 | 98% |
| 12 | sn4 Targon | 65.6 | 6,839 | 32,346 | rtx4090* | 5 | 70% |
| 13 | sn62 Ridges | 64.7 | 151 | 2,312 | rtx4090* | 30 | 25% |
| 14 | sn28 SayGM | 63.3 | 103 | 983 | rtx4090* | 60 | 38% |
| 15 | sn61 RedTeam | 62.8 | 87.20 | 157 | rtx4090* | 113 | 2% |
| 16 | sn14 Cacheon | 61.2 | 53.24 | 1,852 | rtx4090* | 13 | 23% |
| 17 | sn26 Perturb | 59.8 | 37.58 | 69.92 | rtx3060 | 4 | 90% |
| 18 | sn5 Hone | 59 | 38.79 | 40.89 | rtx4090* | 244 | 0% |
| 19 | sn80 OpenRoboto | 58.7 | 896 | 3,347 | rtx4090* | 8 | 33% |
| 20 | sn38 ChronoLLM | 58.6 | 348 | 4,733 | cpu-small | 10 | 52% |

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
| concentrated (30–60%) | 27 |
| dominated (60–90%) | 20 |
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
| 2026-10-04T06:24 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Retain complete model success and actual  |
| 2026-10-04T06:24 | sn26 | SCORING_COMMIT | sn26 commit touches scoring: feat: rank scanning miners by stake-weigh |
| 2026-10-04T06:24 | sn26 | README_TASK_DIFF | sn26 README task/scoring sections changed |
| 2026-10-04T06:24 | sn30 | BURN_DROP | sn30 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-10-04T06:24 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge pull request #209 from leadpoet/cod |
| 2026-10-04T06:24 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Preserve checkpoint read access through  |
| 2026-10-04T00:33 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge pull request #205 from leadpoet/cod |
| 2026-10-04T00:33 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: feat(corpus): new jobs settle by period;  |
| 2026-10-03T21:49 | sn11 | RELEASE | sn11 released v0.7.4 |
| 2026-10-03T21:49 | sn11 | SCORING_COMMIT | sn11 commit touches scoring: [coding-agent] validator: weight-only by  |
| 2026-10-03T21:49 | sn22 | BURN_DROP | sn22 burn fell 1.000 -> 0.820 - miners can earn again |
| 2026-10-03T21:49 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Reject partial successor reward ownership |
| 2026-10-03T18:40 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Record verified five-role source staging |
| 2026-10-03T14:57 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Bind unverified homepage context to obser |
| 2026-10-03T14:57 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: Merge pull request #308 from reliquadotai |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

