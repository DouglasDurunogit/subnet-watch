# Subnet watch — dashboard

_snapshot 2026-08-14T16:03:25Z · block 8843888 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 52 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 91 | `miner_burn` < 0.99 |
| Ranked | 91 | passed every gate |
| **Positive margin** | **52** | income beats machine cost |
| New events this window | 4 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 60 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 8 | `████` |
| 0.6–0.8 | 5 | `██` |
| 0.8–0.99 | 8 | `████` |
| ≥0.99 dead | 37 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 77.2 | 91.72 | 30,763 | cpu-small | 19 | 90% |
| 2 | sn76 Phylax | 74.4 | 37.66 | 181 | cpu-small | 10 | 34% |
| 3 | sn60 Bitsec.ai | 73.2 | 742 | 1,039 | cpu-small | 3 | 50% |
| 4 | sn67 Harnyx | 73.1 | 27.67 | 471 | cpu-small | 124 | 13% |
| 5 | sn26 Perturb | 70.8 | 40.78 | 74.80 | rtx3060 | 10 | 70% |
| 6 | sn1 Apex | 70 | 750 | 1,092 | rtx4090* | 4 | 57% |
| 7 | sn91 cascade | 69.5 | 639 | 2,205 | rtx4090* | 5 | 50% |
| 8 | sn41 Almanac | 69 | 10.35 | 25.70 | cpu-small | 68 | 72% |
| 9 | sn56 Gradients | 68.8 | 512 | 955 | rtx4090* | 7 | 66% |
| 10 | sn62 Ridges | 68.1 | 419 | 1,947 | rtx4090* | 7 | 35% |
| 11 | sn38 ChronoLLM | 67.6 | 151 | 3,164 | cpu-small | 10 | 52% |
| 12 | sn15 ORO | 67.6 | 10.56 | 21.12 | cpu-small | 84 | 93% |
| 13 | sn21 AdTAO | 67.6 | 7.50 | 33.69 | cpu-small | 88 | 45% |
| 14 | sn96 Verathos | 66.8 | 15.00 | 103 | rtx4090 | 82 | 41% |
| 15 | sn6 Numinous | 66.6 | 7.38 | 541 | cpu-small | 19 | 32% |
| 16 | sn124 Swarm | 65.8 | 219 | 709 | rtx4090* | 24 | 11% |
| 17 | sn80 OpenRoboto | 65 | 164 | 595 | rtx4090* | 4 | 91% |
| 18 | sn85 Vidaio | 64.5 | 143 | 630 | rtx4090* | 10 | 20% |
| 19 | sn55 NIOME | 63.7 | 114 | 318 | rtx4090* | 11 | 20% |
| 20 | sn51 lium.io | 60.1 | 45.54 | 1,346 | rtx4090* | 43 | 80% |

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
| concentrated (30–60%) | 23 |
| dominated (60–90%) | 17 |
| captured (>90%) | 27 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 103 |
| code-submission (validator runs it) | 9 |
| min_compute.yml (curated) | 9 |
| README keywords (GUESS) | 6 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-08-14T16:03 | sn126 | SCORING_COMMIT | sn126 commit touches scoring: docs: describe continuous miner training |
| 2026-08-14T15:05 | sn20 | BURN_DROP | sn20 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-08-14T15:05 | sn39 | BURN_DROP | sn39 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-08-14T15:05 | sn96 | RELEASE | sn96 released Verathos v0.1.39 — Hard-Proof Timing Stability |
| 2026-08-14T14:04 | sn55 | README_TASK_DIFF | sn55 README task/scoring sections changed |
| 2026-08-14T12:30 | sn90 | RELEASE | sn90 released v1.1.2 |
| 2026-08-14T12:30 | sn90 | SCORING_COMMIT | sn90 commit touches scoring: fix(validator): set_weights on the config |
| 2026-08-14T11:32 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-08-14T11:32 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Refresh SOURCE_ADD reward ancestry identi |
| 2026-08-14T11:32 | sn96 | RELEASE | sn96 released Verathos v0.1.38 — Runtime and Proof Stability |
| 2026-08-14T11:32 | sn96 | SCORING_COMMIT | sn96 commit touches scoring: fix: retry validator updates after partia |
| 2026-08-14T11:32 | sn97 | SCORING_COMMIT | sn97 commit touches scoring: feat: win both evaluations; increase step |
| 2026-08-14T09:18 | sn2 | BURN_DROP | sn2 burn fell 1.000 -> 0.822 - miners can earn again |
| 2026-08-14T09:18 | sn44 | SCORING_COMMIT | sn44 commit touches scoring: Merge pull request #52 from score-technol |
| 2026-08-14T09:18 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-2622: floor a live miner's weight at  |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

