# Subnet watch — dashboard

_snapshot 2026-08-14T20:16:41Z · block 8845153 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 50 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 90 | `miner_burn` < 0.99 |
| Ranked | 90 | passed every gate |
| **Positive margin** | **50** | income beats machine cost |
| New events this window | 3 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 60 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 7 | `███` |
| 0.6–0.8 | 6 | `███` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 38 | `██████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 78 | 109 | 31,416 | cpu-small | 20 | 90% |
| 2 | sn76 Phylax | 74.6 | 39.59 | 190 | cpu-small | 10 | 34% |
| 3 | sn121 sundae_bar | 74.4 | 1,067 | 1,067 = | cpu-small | 2 | 61% |
| 4 | sn67 Harnyx | 73.1 | 27.94 | 476 | cpu-small | 124 | 13% |
| 5 | sn26 Perturb | 71 | 42.64 | 78.10 | rtx3060 | 10 | 70% |
| 6 | sn1 Apex | 70.2 | 795 | 936 | rtx4090* | 4 | 60% |
| 7 | sn91 cascade | 69.5 | 645 | 2,226 | rtx4090* | 5 | 50% |
| 8 | sn41 Almanac | 69 | 10.49 | 26.07 | cpu-small | 68 | 72% |
| 9 | sn56 Gradients | 68.8 | 518 | 968 | rtx4090* | 7 | 66% |
| 10 | sn62 Ridges | 68.1 | 422 | 1,960 | rtx4090* | 7 | 35% |
| 11 | sn15 ORO | 67.8 | 10.50 | 21.02 | cpu-small | 84 | 93% |
| 12 | sn21 AdTAO | 67.6 | 7.53 | 33.81 | cpu-small | 88 | 45% |
| 13 | sn96 Verathos | 66.6 | 14.56 | 123 | rtx4090 | 84 | 42% |
| 14 | sn6 Numinous | 66.5 | 7.53 | 550 | cpu-small | 19 | 32% |
| 15 | sn85 Vidaio | 66.4 | 250 | 681 | rtx4090* | 10 | 22% |
| 16 | sn38 ChronoLLM | 66.2 | 105 | 1,429 | cpu-small | 10 | 52% |
| 17 | sn124 Swarm | 65.8 | 222 | 718 | rtx4090* | 24 | 11% |
| 18 | sn80 OpenRoboto | 64.9 | 163 | 592 | rtx4090* | 4 | 91% |
| 19 | sn55 NIOME | 63.8 | 115 | 319 | rtx4090* | 11 | 20% |
| 20 | sn60 Bitsec.ai | 61.2 | 725 | 1,016 | cpu-small | 3 | 50% |

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
| dominated (60–90%) | 18 |
| captured (>90%) | 26 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 102 |
| code-submission (validator runs it) | 10 |
| min_compute.yml (curated) | 9 |
| README keywords (GUESS) | 6 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-08-14T20:17 | sn55 | SCORING_COMMIT | sn55 commit touches scoring: commit weights after validation |
| 2026-08-14T20:17 | sn96 | RELEASE | sn96 released Verathos v0.1.40 — Capacity Audit Scheduling Stability |
| 2026-08-14T19:29 | sn121 | README_TASK_DIFF | sn121 README task/scoring sections changed |
| 2026-08-14T18:24 | sn55 | SCORING_COMMIT | sn55 commit touches scoring: print only valid scores |
| 2026-08-14T18:24 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: chore(deploy): promote prod prism-challe |
| 2026-08-14T17:08 | sn55 | SCORING_COMMIT | sn55 commit touches scoring: print only valid scores |
| 2026-08-14T16:03 | sn126 | SCORING_COMMIT | sn126 commit touches scoring: docs: describe continuous miner training |
| 2026-08-14T15:05 | sn20 | BURN_DROP | sn20 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-08-14T15:05 | sn39 | BURN_DROP | sn39 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-08-14T15:05 | sn96 | RELEASE | sn96 released Verathos v0.1.39 — Hard-Proof Timing Stability |
| 2026-08-14T14:04 | sn55 | README_TASK_DIFF | sn55 README task/scoring sections changed |
| 2026-08-14T12:30 | sn90 | RELEASE | sn90 released v1.1.2 |
| 2026-08-14T12:30 | sn90 | SCORING_COMMIT | sn90 commit touches scoring: fix(validator): set_weights on the config |
| 2026-08-14T11:32 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-08-14T11:32 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Refresh SOURCE_ADD reward ancestry identi |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

