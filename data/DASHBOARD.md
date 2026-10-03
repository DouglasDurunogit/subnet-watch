# Subnet watch — dashboard

_snapshot 2026-10-03T14:56:55Z · block 9203071 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 60 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 97 | `miner_burn` < 0.99 |
| Ranked | 97 | passed every gate |
| **Positive margin** | **60** | income beats machine cost |
| New events this window | 3 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 66 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 7 | `███` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 8 | `███` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 31 | `█████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn41 Almanac | 74.3 | 38.99 | 129 | cpu-small | 124 | 2% |
| 2 | sn23 Trishool | 73.9 | 921 | 921 = | cpu-small | 2 | 80% |
| 3 | sn26 Perturb | 72.7 | 65.53 | 109 | rtx3060 | 4 | 91% |
| 4 | sn91 cascade | 72.4 | 580 | 2,324 | cpu-small | 5 | 52% |
| 5 | sn53 engy | 71.9 | 1,285 | 3,527 | rtx4090 | 14 | 22% |
| 6 | sn46 Instant | 70.3 | 318 | 342 | cpu-small | 6 | 50% |
| 7 | sn1 Apex | 69.7 | 671 | 1,061 | rtx4090* | 4 | 61% |
| 8 | sn56 Gradients | 69.4 | 625 | 5,073 | rtx4090* | 8 | 39% |
| 9 | sn107 Minos | 68.6 | 330 | 27,993 | cpu-small | 20 | 80% |
| 10 | sn67 Harnyx | 68.6 | 8.63 | 1,109 | cpu-small | 118 | 36% |
| 11 | sn111 Claims | 68.1 | 429 | 2,426 | rtx4090* | 5 | 64% |
| 12 | sn15 ORO | 66.9 | 8.86 | 21,038 | cpu-small | 51 | 98% |
| 13 | sn4 Targon | 65.4 | 6,592 | 31,183 | rtx4090* | 5 | 70% |
| 14 | sn61 RedTeam | 62.6 | 81.56 | 148 | rtx4090* | 113 | 2% |
| 15 | sn28 SayGM | 61.1 | 54.00 | 857 | rtx4090* | 72 | 21% |
| 16 | sn14 Cacheon | 61.1 | 50.92 | 1,782 | rtx4090* | 13 | 23% |
| 17 | sn62 Ridges | 60.1 | 38.54 | 2,804 | rtx4090* | 28 | 31% |
| 18 | sn5 Hone | 59.1 | 37.78 | 40.29 | rtx4090* | 242 | 0% |
| 19 | sn80 OpenRoboto | 58.7 | 897 | 3,352 | rtx4090* | 8 | 33% |
| 20 | sn38 ChronoLLM | 58.5 | 339 | 4,604 | cpu-small | 10 | 52% |

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
| wide (<30%) | 20 |
| concentrated (30–60%) | 26 |
| dominated (60–90%) | 22 |
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
| 2026-10-02T23:56 | sn117 | RELEASE | sn117 released everycli v0.2.3 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

