# Subnet watch — dashboard

_snapshot 2026-10-04T00:32:56Z · block 9205951 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 59 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 97 | `miner_burn` < 0.99 |
| Ranked | 97 | passed every gate |
| **Positive margin** | **59** | income beats machine cost |
| New events this window | 2 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 64 | `████████████████████████████` |
| 0–0.2 | 9 | `████` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 7 | `███` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 31 | `██████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn41 Almanac | 74.4 | 39.74 | 133 | cpu-small | 126 | 2% |
| 2 | sn23 Trishool | 74.1 | 975 | 975 = | cpu-small | 2 | 79% |
| 3 | sn26 Perturb | 73 | 71.12 | 121 | rtx3060 | 4 | 90% |
| 4 | sn120 Affine | 72.4 | 1,583 | 1,583 = | rtx4090* | 33 | 4% |
| 5 | sn53 engy | 72 | 1,328 | 3,641 | rtx4090 | 14 | 22% |
| 6 | sn91 cascade | 71.5 | 453 | 2,419 | cpu-small | 5 | 52% |
| 7 | sn56 Gradients | 69.6 | 653 | 5,294 | rtx4090* | 8 | 39% |
| 8 | sn1 Apex | 69.5 | 643 | 1,046 | rtx4090* | 4 | 62% |
| 9 | sn46 Instant | 69.4 | 240 | 296 | cpu-small | 8 | 51% |
| 10 | sn111 Claims | 68.9 | 530 | 2,346 | rtx4090* | 5 | 60% |
| 11 | sn107 Minos | 68.8 | 345 | 29,357 | cpu-small | 20 | 80% |
| 12 | sn67 Harnyx | 68.8 | 9.03 | 1,155 | cpu-small | 120 | 36% |
| 13 | sn15 ORO | 66.8 | 8.75 | 17.46 | cpu-small | 55 | 98% |
| 14 | sn4 Targon | 65.6 | 6,890 | 32,590 | rtx4090* | 5 | 70% |
| 15 | sn62 Ridges | 63.3 | 101 | 2,330 | rtx4090* | 30 | 25% |
| 16 | sn61 RedTeam | 62.8 | 86.77 | 157 | rtx4090* | 113 | 2% |
| 17 | sn28 SayGM | 62.7 | 85.12 | 1,034 | rtx4090* | 63 | 24% |
| 18 | sn14 Cacheon | 61.2 | 53.59 | 1,863 | rtx4090* | 13 | 23% |
| 19 | sn80 OpenRoboto | 59.6 | 1,150 | 3,489 | rtx4090* | 8 | 34% |
| 20 | sn5 Hone | 59 | 39.15 | 41.26 | rtx4090* | 243 | 0% |

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
| concentrated (30–60%) | 25 |
| dominated (60–90%) | 21 |
| captured (>90%) | 24 |

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
| 2026-10-04T00:33 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge pull request #205 from leadpoet/cod |
| 2026-10-04T00:33 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: feat(corpus): new jobs settle by period;  |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

