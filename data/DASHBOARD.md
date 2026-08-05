# Subnet watch — dashboard

_snapshot 2026-08-05T21:45:17Z · block 8780806 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 53 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 91 | `miner_burn` < 0.99 |
| Ranked | 91 | passed every gate |
| **Positive margin** | **53** | income beats machine cost |
| New events this window | 3 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 55 | `████████████████████████████` |
| 0–0.2 | 8 | `████` |
| 0.2–0.4 | 3 | `██` |
| 0.4–0.6 | 7 | `████` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 10 | `█████` |
| ≥0.99 dead | 37 | `███████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 79.4 | 135 | 226 | cpu-small | 10 | 20% |
| 2 | sn107 Minos | 77.5 | 98.05 | 28,268 | cpu-small | 20 | 89% |
| 3 | sn60 Bitsec.ai | 77 | 2,296 | 2,296 = | cpu-small | 2 | 90% |
| 4 | sn67 Harnyx | 72.4 | 23.04 | 986 | cpu-small | 155 | 22% |
| 5 | sn96 Verathos | 72 | 54.14 | 246 | rtx4090 | 37 | 43% |
| 6 | sn114 SOMA | 71.5 | 1,168 | 4,362 | rtx4090* | 4 | 65% |
| 7 | sn91 cascade | 70.1 | 756 | 3,047 | rtx4090* | 5 | 52% |
| 8 | sn102 ConnitoAI | 69.5 | 647 | 2,030 | rtx4090* | 7 | 32% |
| 9 | sn62 Ridges | 69.4 | 627 | 2,578 | rtx4090* | 7 | 35% |
| 10 | sn26 Perturb | 68.9 | 25.17 | 201 | rtx3060 | 11 | 50% |
| 11 | sn41 Almanac | 68.4 | 8.98 | 66.12 | cpu-small | 60 | 78% |
| 12 | sn15 ORO | 67 | 8.32 | 18.66 | cpu-small | 76 | 93% |
| 13 | sn74 Gittensor | 66.1 | 234 | 255 | rtx4090* | 9 | 18% |
| 14 | sn124 Swarm | 65.8 | 222 | 637 | rtx4090* | 23 | 11% |
| 15 | sn38 ChronoLLM | 65.6 | 213 | 3,574 | rtx4090* | 10 | 52% |
| 16 | sn21 AdTAO | 65.5 | 4.74 | 21.91 | cpu-small | 142 | 45% |
| 17 | sn80 OpenRoboto | 62.2 | 71.36 | 270 | rtx4090* | 4 | 91% |
| 18 | sn61 RedTeam | 61.9 | 65.42 | 169 | rtx4090* | 40 | 5% |
| 19 | sn51 lium.io | 58.1 | 27.68 | 5,364 | rtx4090* | 47 | 63% |
| 20 | sn28 gm | 55.8 | 11.41 | 7,578 | rtx4090* | 17 | 83% |

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
| concentrated (30–60%) | 19 |
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
| 2026-08-05T21:45 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: Merge pull request #6 from ippcteam/docs/ |
| 2026-08-05T21:45 | sn21 | README_TASK_DIFF | sn21 README task/scoring sections changed |
| 2026-08-05T21:45 | sn62 | RELEASE | sn62 released v0.2.6 |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

