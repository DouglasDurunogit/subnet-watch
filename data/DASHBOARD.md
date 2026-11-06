# Subnet watch — dashboard

_snapshot 2026-11-06T20:58:37Z · block 9449585 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 63 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 103 | `miner_burn` < 0.99 |
| Ranked | 103 | passed every gate |
| **Positive margin** | **63** | income beats machine cost |
| New events this window | 10 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 72 | `████████████████████████████` |
| 0–0.2 | 4 | `██` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 7 | `███` |
| 0.6–0.8 | 11 | `████` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 25 | `██████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn104 TAOstatus | 77.1 | 2,390 | 2,390 = | cpu-small | 1 | 100% |
| 2 | sn120 Affine | 74.4 | 2,786 | 2,786 = | rtx4090* | 10 | 10% |
| 3 | sn3 Teutonic | 72.9 | 1,757 | 3,436 | rtx4090* | 7 | 25% |
| 4 | sn14 Cacheon | 72.9 | 1,737 | 4,175 | rtx4090* | 3 | 68% |
| 5 | sn36 Weir | 69.5 | 647 | 1,266 | rtx4090* | 9 | 24% |
| 6 | sn56 Gradients | 69.3 | 607 | 3,593 | rtx4090* | 7 | 37% |
| 7 | sn58 Attune | 68.6 | 492 | 792 | rtx4090* | 5 | 70% |
| 8 | sn41 Almanac | 68.4 | 9.32 | 149 | cpu-small | 178 | 3% |
| 9 | sn46 Instant | 67.6 | 142 | 182 | cpu-small | 9 | 47% |
| 10 | sn1 Apex | 67.5 | 349 | 777 | rtx4090* | 4 | 71% |
| 11 | sn103 Terza Inference | 67.4 | 340 | 761 | rtx4090* | 5 | 35% |
| 12 | sn67 Harnyx | 66.8 | 5.24 | 238 | cpu-small | 127 | 13% |
| 13 | sn82 Noah | 66.7 | 351 | 424 | rtx4090* | 64 | 2% |
| 14 | sn15 ORO | 66 | 6.75 | 13.57 | cpu-small | 70 | 96% |
| 15 | sn107 Minos | 65.9 | 172 | 14,650 | cpu-small | 20 | 80% |
| 16 | sn38 ChronoLLM | 62.8 | 44.61 | 399 | cpu-small | 10 | 52% |
| 17 | sn66 conjectures | 61.1 | 51.49 | 141 | rtx4090* | 5 | 80% |
| 18 | sn62 Ridges | 61 | 50.17 | 1,069 | rtx4090* | 38 | 22% |
| 19 | sn55 NIOME | 60.9 | 49.07 | 422 | rtx4090* | 11 | 30% |
| 20 | sn97 Ingot | 60.5 | 1,503 | 1,503 = | rtx4090* | 5 | 20% |

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
| wide (<30%) | 31 |
| concentrated (30–60%) | 18 |
| dominated (60–90%) | 29 |
| captured (>90%) | 24 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 99 |
| README keywords (GUESS) | 11 |
| min_compute.yml (curated) | 9 |
| code-submission (validator runs it) | 8 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-11-06T20:59 | sn2 | SCORING_COMMIT | sn2 commit touches scoring: Prepare Finney SN2 validator onboarding an |
| 2026-11-06T20:59 | sn14 | SCORING_COMMIT | sn14 commit touches scoring: Release reward priority after completed w |
| 2026-11-06T20:59 | sn28 | RELEASE | sn28 released v0.5.22 |
| 2026-11-06T20:59 | sn28 | README_TASK_DIFF | sn28 README task/scoring sections changed |
| 2026-11-06T20:59 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Preserve consumed redirect provenance and |
| 2026-11-06T20:59 | sn88 | README_TASK_DIFF | sn88 README task/scoring sections changed |
| 2026-11-06T20:59 | sn104 | SCORING_COMMIT | sn104 commit touches scoring: fix(validator): sync live operational fi |
| 2026-11-06T20:59 | sn108 | SCORING_COMMIT | sn108 commit touches scoring: Validator requirements: 500 GB SSD recom |
| 2026-11-06T20:59 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Dashboard Updates page (miner Updates),  |
| 2026-11-06T20:59 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: sn120: gate task cap 32K -> 64K (Jacob p |
| 2026-11-06T15:16 | sn51 | RELEASE | sn51 released executor-v1.172 |
| 2026-11-06T15:16 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-5803 - [P1] Validator registry pull:  |
| 2026-11-06T15:16 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge pull request #1087 from leadpoet/fi |
| 2026-11-06T15:16 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Reuse each freshly validated proof receip |
| 2026-11-06T15:16 | sn108 | SCORING_COMMIT | sn108 commit touches scoring: Neuron 1.0.3: report the EDA server's di |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

