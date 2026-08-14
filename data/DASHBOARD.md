# Subnet watch — dashboard

_snapshot 2026-08-14T11:32:00Z · block 8842531 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 53 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 89 | `miner_burn` < 0.99 |
| Ranked | 89 | passed every gate |
| **Positive margin** | **53** | income beats machine cost |
| New events this window | 5 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 57 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 8 | `████` |
| 0.6–0.8 | 7 | `███` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 39 | `███████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 77.7 | 103 | 30,852 | cpu-small | 20 | 90% |
| 2 | sn76 Phylax | 74.6 | 39.70 | 190 | cpu-small | 10 | 34% |
| 3 | sn60 Bitsec.ai | 73.2 | 732 | 1,026 | cpu-small | 3 | 50% |
| 4 | sn67 Harnyx | 73.1 | 27.89 | 483 | cpu-small | 123 | 13% |
| 5 | sn26 Perturb | 70.9 | 41.24 | 76.30 | rtx3060 | 10 | 70% |
| 6 | sn1 Apex | 70.2 | 785 | 1,139 | rtx4090* | 4 | 56% |
| 7 | sn96 Verathos | 69.3 | 27.75 | 178 | rtx4090 | 66 | 41% |
| 8 | sn41 Almanac | 69 | 10.58 | 26.24 | cpu-small | 68 | 72% |
| 9 | sn56 Gradients | 68.8 | 521 | 971 | rtx4090* | 7 | 66% |
| 10 | sn91 cascade | 68.6 | 494 | 1,136 | rtx4090* | 5 | 50% |
| 11 | sn85 Vidaio | 68.3 | 449 | 776 | rtx4090* | 10 | 24% |
| 12 | sn15 ORO | 68.3 | 11.36 | 12,501 | cpu-small | 83 | 93% |
| 13 | sn62 Ridges | 68.1 | 425 | 1,971 | rtx4090* | 7 | 35% |
| 14 | sn21 AdTAO | 67.7 | 7.64 | 34.25 | cpu-small | 88 | 45% |
| 15 | sn11 TrajectoryRL | 67.2 | 4,255 | 4,255 = | cpu-small | 1 | 100% |
| 16 | sn6 Numinous | 66.7 | 7.47 | 547 | cpu-small | 19 | 32% |
| 17 | sn38 ChronoLLM | 66.5 | 111 | 1,523 | cpu-small | 10 | 52% |
| 18 | sn124 Swarm | 65.9 | 224 | 723 | rtx4090* | 24 | 11% |
| 19 | sn80 OpenRoboto | 65.2 | 176 | 637 | rtx4090* | 4 | 91% |
| 20 | sn28 gm | 62.1 | 70.88 | 2,949 | rtx4090* | 30 | 31% |

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
| concentrated (30–60%) | 22 |
| dominated (60–90%) | 18 |
| captured (>90%) | 25 |

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
| 2026-08-14T11:32 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-08-14T11:32 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Refresh SOURCE_ADD reward ancestry identi |
| 2026-08-14T11:32 | sn96 | RELEASE | sn96 released Verathos v0.1.38 — Runtime and Proof Stability |
| 2026-08-14T11:32 | sn96 | SCORING_COMMIT | sn96 commit touches scoring: fix: retry validator updates after partia |
| 2026-08-14T11:32 | sn97 | SCORING_COMMIT | sn97 commit touches scoring: feat: win both evaluations; increase step |
| 2026-08-14T09:18 | sn2 | BURN_DROP | sn2 burn fell 1.000 -> 0.822 - miners can earn again |
| 2026-08-14T09:18 | sn44 | SCORING_COMMIT | sn44 commit touches scoring: Merge pull request #52 from score-technol |
| 2026-08-14T09:18 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-2622: floor a live miner's weight at  |
| 2026-08-14T09:18 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: chore(deploy): promote prod prism-challe |
| 2026-08-14T06:06 | sn90 | RELEASE | sn90 released v1.1.1 |
| 2026-08-14T06:06 | sn90 | SCORING_COMMIT | sn90 commit touches scoring: fix(validator): always apply the Targon s |
| 2026-08-14T06:06 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: chore(deploy): promote prod prism-challe |
| 2026-08-13T23:12 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: miner dashboard: label warm-start checkpo |
| 2026-08-13T22:10 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: chore(deps): bump msgpack from 1.1.2 to 1 |
| 2026-08-13T22:10 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: miner dashboard: show warm-start init + n |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

