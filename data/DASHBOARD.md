# Subnet watch — dashboard

_snapshot 2026-10-03T18:39:46Z · block 9204186 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 62 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 97 | `miner_burn` < 0.99 |
| Ranked | 97 | passed every gate |
| **Positive margin** | **62** | income beats machine cost |
| New events this window | 1 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 65 | `████████████████████████████` |
| 0–0.2 | 8 | `███` |
| 0.2–0.4 | 7 | `███` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 31 | `█████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn41 Almanac | 74.3 | 38.66 | 128 | cpu-small | 124 | 2% |
| 2 | sn23 Trishool | 74 | 957 | 957 = | cpu-small | 2 | 79% |
| 3 | sn120 Affine | 73.1 | 1,905 | 2,858 | rtx4090* | 19 | 7% |
| 4 | sn26 Perturb | 72.8 | 68.09 | 116 | rtx3060 | 4 | 90% |
| 5 | sn91 cascade | 72.4 | 590 | 2,362 | cpu-small | 5 | 52% |
| 6 | sn53 engy | 71.9 | 1,288 | 3,530 | rtx4090 | 14 | 22% |
| 7 | sn46 Instant | 69.7 | 265 | 321 | cpu-small | 7 | 50% |
| 8 | sn1 Apex | 69.5 | 645 | 1,032 | rtx4090* | 4 | 61% |
| 9 | sn56 Gradients | 69.4 | 626 | 5,078 | rtx4090* | 8 | 39% |
| 10 | sn67 Harnyx | 68.7 | 8.61 | 1,107 | cpu-small | 118 | 36% |
| 11 | sn107 Minos | 68.6 | 329 | 27,947 | cpu-small | 20 | 80% |
| 12 | sn111 Claims | 66.6 | 275 | 2,438 | rtx4090* | 6 | 65% |
| 13 | sn15 ORO | 65.9 | 8.81 | 20,899 | cpu-small | 53 | 98% |
| 14 | sn4 Targon | 65.4 | 6,598 | 31,210 | rtx4090* | 5 | 70% |
| 15 | sn61 RedTeam | 62.6 | 81.84 | 148 | rtx4090* | 113 | 2% |
| 16 | sn14 Cacheon | 61.1 | 51.03 | 1,785 | rtx4090* | 13 | 23% |
| 17 | sn28 SayGM | 60.8 | 48.80 | 1,221 | rtx4090* | 65 | 20% |
| 18 | sn62 Ridges | 60.7 | 46.95 | 2,322 | rtx4090* | 29 | 26% |
| 19 | sn80 OpenRoboto | 59.5 | 1,118 | 3,391 | rtx4090* | 8 | 33% |
| 20 | sn5 Hone | 59.1 | 38.18 | 40.54 | rtx4090* | 243 | 0% |

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
| concentrated (30–60%) | 25 |
| dominated (60–90%) | 22 |
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
| 2026-10-03T05:11 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Record verified public full-model update |
| 2026-10-02T23:56 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: Validator v2.0.41: per-event market notic |
| 2026-10-02T23:56 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Reuse exact Arena verifier requests throu |
| 2026-10-02T23:56 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: fix(corpus): bound the audits of one judg |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

