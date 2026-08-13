# Subnet watch — dashboard

_snapshot 2026-08-13T17:44:37Z · block 8837194 · run_status **ok**_

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
| New events this window | 6 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 56 | `████████████████████████████` |
| 0–0.2 | 7 | `████` |
| 0.2–0.4 | 2 | `█` |
| 0.4–0.6 | 9 | `████` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 7 | `████` |
| ≥0.99 dead | 39 | `████████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 78 | 110 | 31,919 | cpu-small | 20 | 90% |
| 2 | sn76 Phylax | 74.6 | 38.91 | 186 | cpu-small | 10 | 34% |
| 3 | sn67 Harnyx | 71.3 | 17.29 | 711 | cpu-small | 148 | 19% |
| 4 | sn91 cascade | 69.8 | 694 | 2,392 | rtx4090* | 5 | 50% |
| 5 | sn62 Ridges | 69 | 546 | 1,974 | rtx4090* | 7 | 35% |
| 6 | sn56 Gradients | 68.9 | 529 | 978 | rtx4090* | 7 | 65% |
| 7 | sn41 Almanac | 68.9 | 10.34 | 28.52 | cpu-small | 68 | 73% |
| 8 | sn96 Verathos | 68.2 | 21.42 | 263 | rtx4090 | 61 | 41% |
| 9 | sn38 ChronoLLM | 68 | 167 | 3,505 | cpu-small | 10 | 52% |
| 10 | sn6 Numinous | 67.9 | 9.49 | 503 | cpu-small | 19 | 29% |
| 11 | sn26 Perturb | 67.8 | 19.54 | 838 | rtx3060 | 11 | 50% |
| 12 | sn21 AdTAO | 67.6 | 7.58 | 34.00 | cpu-small | 88 | 45% |
| 13 | sn124 Swarm | 66 | 233 | 498 | rtx4090* | 23 | 11% |
| 14 | sn85 Vidaio | 65.6 | 202 | 610 | rtx4090* | 10 | 21% |
| 15 | sn80 OpenRoboto | 65.4 | 187 | 675 | rtx4090* | 4 | 91% |
| 16 | sn1 Apex | 63.8 | 117 | 869 | rtx4090* | 4 | 76% |
| 17 | sn28 gm | 60.8 | 48.08 | 976 | rtx4090* | 28 | 49% |
| 18 | sn51 lium.io | 60 | 44.91 | 1,715 | rtx4090* | 46 | 72% |
| 19 | sn74 Gittensor | 58.3 | 24.27 | 215 | rtx4090* | 13 | 63% |
| 20 | sn61 RedTeam | 57.4 | 16.56 | 1,514 | rtx4090* | 66 | 35% |

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
| concentrated (30–60%) | 20 |
| dominated (60–90%) | 20 |
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

