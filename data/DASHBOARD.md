# Subnet watch — dashboard

_snapshot 2026-08-13T18:41:45Z · block 8837480 · run_status **ok**_

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
| New events this window | 1 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 56 | `████████████████████████████` |
| 0–0.2 | 7 | `████` |
| 0.2–0.4 | 2 | `█` |
| 0.4–0.6 | 10 | `█████` |
| 0.6–0.8 | 7 | `████` |
| 0.8–0.99 | 7 | `████` |
| ≥0.99 dead | 39 | `████████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 77.9 | 107 | 31,668 | cpu-small | 20 | 90% |
| 2 | sn76 Phylax | 74.6 | 39.04 | 187 | cpu-small | 10 | 34% |
| 3 | sn67 Harnyx | 71.3 | 17.38 | 714 | cpu-small | 148 | 19% |
| 4 | sn1 Apex | 70.4 | 842 | 1,150 | rtx4090* | 4 | 54% |
| 5 | sn91 cascade | 69.8 | 695 | 2,394 | rtx4090* | 5 | 50% |
| 6 | sn26 Perturb | 69.5 | 29.60 | 839 | rtx3060 | 11 | 50% |
| 7 | sn62 Ridges | 69 | 547 | 1,978 | rtx4090* | 7 | 35% |
| 8 | sn41 Almanac | 69 | 10.36 | 28.57 | cpu-small | 68 | 73% |
| 9 | sn56 Gradients | 68.9 | 529 | 980 | rtx4090* | 7 | 65% |
| 10 | sn96 Verathos | 68.6 | 23.57 | 281 | rtx4090 | 58 | 41% |
| 11 | sn38 ChronoLLM | 68 | 169 | 3,540 | cpu-small | 10 | 52% |
| 12 | sn6 Numinous | 67.9 | 9.51 | 504 | cpu-small | 19 | 29% |
| 13 | sn21 AdTAO | 67.6 | 7.60 | 34.11 | cpu-small | 88 | 45% |
| 14 | sn124 Swarm | 66.1 | 238 | 728 | rtx4090* | 23 | 11% |
| 15 | sn80 OpenRoboto | 65.3 | 180 | 651 | rtx4090* | 4 | 91% |
| 16 | sn85 Vidaio | 64.4 | 141 | 602 | rtx4090* | 10 | 18% |
| 17 | sn51 lium.io | 60.9 | 56.65 | 1,636 | rtx4090* | 48 | 72% |
| 18 | sn28 gm | 59.6 | 34.62 | 894 | rtx4090* | 31 | 59% |
| 19 | sn74 Gittensor | 58.2 | 23.84 | 215 | rtx4090* | 14 | 63% |
| 20 | sn61 RedTeam | 57.6 | 17.50 | 1,571 | rtx4090* | 66 | 35% |

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
| wide (<30%) | 24 |
| concentrated (30–60%) | 21 |
| dominated (60–90%) | 19 |
| captured (>90%) | 24 |

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
| 2026-08-13T17:45 | sn118 | BURN_DROP | sn118 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-08-13T16:39 | sn6 | WEIGHTS_VERSION_BUMP | sn6 weights_version 2018 -> 3000 |
| 2026-08-13T16:39 | sn38 | SCORING_COMMIT | sn38 commit touches scoring: Update validator image to latest version  |
| 2026-08-13T16:39 | sn38 | README_TASK_DIFF | sn38 README task/scoring sections changed |
| 2026-08-13T16:39 | sn90 | RELEASE | sn90 released v1.1.0 — Targon max $/card + raised GPU card caps |
| 2026-08-13T16:39 | sn90 | SCORING_COMMIT | sn90 commit touches scoring: chore(validator): bump version to 1.1.0 f |
| 2026-08-13T15:31 | sn26 | SCORING_COMMIT | sn26 commit touches scoring: Merge pull request #49 from 0xsigurd/feat |
| 2026-08-13T15:31 | sn26 | README_TASK_DIFF | sn26 README task/scoring sections changed |
| 2026-08-13T15:31 | sn51 | RELEASE | sn51 released executor-v1.119 |
| 2026-08-13T15:31 | sn75 | SCORING_COMMIT | sn75 commit touches scoring: updated validator weights submitter |
| 2026-08-13T15:31 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: fix(site): attribute arena weight per ch |
| 2026-08-13T14:10 | sn1 | RELEASE | sn1 released v4.3.1 |
| 2026-08-13T12:36 | sn90 | README_TASK_DIFF | sn90 README task/scoring sections changed |
| 2026-08-13T10:35 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-08-13T10:35 | sn67 | README_TASK_DIFF | sn67 README task/scoring sections changed |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

