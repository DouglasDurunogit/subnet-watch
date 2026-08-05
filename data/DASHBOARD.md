# Subnet watch — dashboard

_snapshot 2026-08-05T20:18:14Z · block 8780371 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 55 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 91 | `miner_burn` < 0.99 |
| Ranked | 91 | passed every gate |
| **Positive margin** | **55** | income beats machine cost |
| New events this window | 6 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 55 | `████████████████████████████` |
| 0–0.2 | 7 | `████` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 6 | `███` |
| 0.6–0.8 | 9 | `█████` |
| 0.8–0.99 | 10 | `█████` |
| ≥0.99 dead | 37 | `███████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 82.3 | 282 | 620 | cpu-small | 4 | 40% |
| 2 | sn107 Minos | 77.4 | 96.74 | 28,545 | cpu-small | 20 | 90% |
| 3 | sn60 Bitsec.ai | 76.9 | 2,268 | 2,268 = | cpu-small | 2 | 90% |
| 4 | sn98 NeverPlayAlone | 76 | 1,703 | 1,703 = | cpu-small | 1 | 100% |
| 5 | sn114 SOMA | 72.7 | 1,658 | 4,324 | rtx4090* | 3 | 65% |
| 6 | sn67 Harnyx | 72.3 | 22.92 | 982 | cpu-small | 155 | 22% |
| 7 | sn91 cascade | 70 | 747 | 3,013 | rtx4090* | 5 | 52% |
| 8 | sn62 Ridges | 69.5 | 630 | 2,591 | rtx4090* | 7 | 35% |
| 9 | sn26 Perturb | 68.9 | 25.35 | 202 | rtx3060 | 11 | 50% |
| 10 | sn41 Almanac | 68.4 | 8.98 | 66.44 | cpu-small | 60 | 78% |
| 11 | sn15 ORO | 67.3 | 8.57 | 19.19 | cpu-small | 76 | 93% |
| 12 | sn96 Verathos | 67 | 15.81 | 89.76 | rtx4090 | 113 | 41% |
| 13 | sn74 Gittensor | 66.3 | 246 | 255 | rtx4090* | 9 | 18% |
| 14 | sn124 Swarm | 65.8 | 220 | 631 | rtx4090* | 23 | 10% |
| 15 | sn38 ChronoLLM | 65.7 | 215 | 3,603 | rtx4090* | 10 | 52% |
| 16 | sn21 AdTAO | 65.6 | 4.79 | 22.10 | cpu-small | 142 | 45% |
| 17 | sn80 OpenRoboto | 62.3 | 72.81 | 276 | rtx4090* | 4 | 91% |
| 18 | sn61 RedTeam | 61.9 | 65.69 | 169 | rtx4090* | 40 | 5% |
| 19 | sn101 Tag101 | 59.3 | 0.04 | 0.70 | cpu-small | 245 | 90% |
| 20 | sn102 ConnitoAI | 58.9 | 26.14 | 1,974 | rtx4090* | 8 | 32% |

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
| wide (<30%) | 21 |
| concentrated (30–60%) | 20 |
| dominated (60–90%) | 23 |
| captured (>90%) | 26 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 104 |
| code-submission (validator runs it) | 9 |
| min_compute.yml (curated) | 9 |
| README keywords (GUESS) | 5 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-08-05T20:18 | sn2 | RELEASE | sn2 released 14.12.21 |
| 2026-08-05T20:18 | sn13 | RELEASE | sn13 released Release v1.18.70 |
| 2026-08-05T20:18 | sn13 | SCORING_COMMIT | sn13 commit touches scoring: Merge pull request #901 from macrocosm-os |
| 2026-08-05T20:18 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Refresh protected validator authority man |
| 2026-08-05T20:18 | sn88 | README_TASK_DIFF | sn88 README task/scoring sections changed |
| 2026-08-05T20:18 | sn96 | RELEASE | sn96 released v0.1.27 - Validator Boundary Hotfix |
| 2026-08-05T18:45 | sn36 | BURN_DROP | sn36 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-08-05T18:45 | sn96 | RELEASE | sn96 released v0.1.26 - Gleipnir Proof Protocol v3 |
| 2026-08-05T18:45 | sn96 | SCORING_COMMIT | sn96 commit touches scoring: fix: serialize validator block dispatch |
| 2026-08-05T16:50 | sn21 | README_TASK_DIFF | sn21 README task/scoring sections changed |
| 2026-08-05T16:50 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: Merge pull request #24 from conjectures-i |
| 2026-08-05T14:53 | sn21 | RELEASE | sn21 released SN21 training bundle |
| 2026-08-05T14:53 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: docs: resolve the first-basket date ambig |
| 2026-08-05T14:53 | sn21 | README_TASK_DIFF | sn21 README task/scoring sections changed |
| 2026-08-05T14:53 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: Merge pull request #23 from conjectures-i |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

