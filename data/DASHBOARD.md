# Subnet watch — dashboard

_snapshot 2026-11-24T10:13:16Z · block 9575927 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 53 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 105 | `miner_burn` < 0.99 |
| Ranked | 105 | passed every gate |
| **Positive margin** | **53** | income beats machine cost |
| New events this window | 17 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 73 | `████████████████████████████` |
| 0–0.2 | 3 | `█` |
| 0.2–0.4 | 6 | `██` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 10 | `████` |
| 0.8–0.99 | 9 | `███` |
| ≥0.99 dead | 23 | `█████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn42 CADmind | 82.2 | 275 | 275 = | cpu-small | 4 | 25% |
| 2 | sn3 Teutonic | 73 | 1,841 | 3,691 | rtx4090* | 4 | 40% |
| 3 | sn124 Swarm | 65.4 | 196 | 1,212 | rtx4090* | 10 | 29% |
| 4 | sn67 Harnyx | 64.9 | 2.49 | 254 | cpu-small | 119 | 19% |
| 5 | sn53 engy | 62.9 | 89.04 | 3,165 | rtx4090 | 20 | 61% |
| 6 | sn120 Affine | 62.1 | 2,476 | 2,476 = | rtx4090* | 8 | 12% |
| 7 | sn58 Attune | 61.4 | 57.10 | 143 | rtx4090* | 57 | 30% |
| 8 | sn66 conjectures | 60.9 | 47.58 | 820 | rtx4090* | 4 | 85% |
| 9 | sn127 Zils | 60.8 | 46.49 | 65.66 | rtx4090 | 4 | 90% |
| 10 | sn62 Ridges | 60.6 | 43.76 | 379 | rtx4090* | 47 | 10% |
| 11 | sn111 Claims | 60 | 37.44 | 152 | rtx4090* | 4 | 88% |
| 12 | sn56 Gradients | 58.7 | 172 | 3,194 | a100-80 | 7 | 43% |
| 13 | sn25 UR | 58 | 20.04 | 20.04 = | rtx4090* | 10 | 45% |
| 14 | sn61 RedTeam | 57.5 | 20.91 | 39.43 | rtx4090* | 104 | 2% |
| 15 | sn4 Targon | 57.1 | 7,803 | 19,628 | rtx4090* | 3 | 67% |
| 16 | sn102 ConnitoAI | 56.9 | 513 | 524 | rtx4090* | 4 | 25% |
| 17 | sn28 SayGM | 55.9 | 13.21 | 4,086 | rtx4090* | 109 | 25% |
| 18 | sn116 Carbon | 55.4 | 9,339 | 9,339 = | rtx4090* | 1 | 100% |
| 19 | sn99 Axonry | 55.4 | 9,245 | 9,245 = | rtx4090* | 1 | 100% |
| 20 | sn46 Instant | 55.3 | 126 | 153 | cpu-small | 9 | 24% |

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
| wide (<30%) | 27 |
| concentrated (30–60%) | 19 |
| dominated (60–90%) | 27 |
| captured (>90%) | 28 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 97 |
| README keywords (GUESS) | 13 |
| min_compute.yml (curated) | 10 |
| code-submission (validator runs it) | 8 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-11-24T10:13 | sn2 | BURN_DROP | sn2 burn fell 1.000 -> 0.881 - miners can earn again |
| 2026-11-24T10:13 | sn39 | README_TASK_DIFF | sn39 README task/scoring sections changed |
| 2026-11-24T10:13 | sn51 | RELEASE | sn51 released executor-v1.196 |
| 2026-11-24T10:13 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-6847 - [P4] Validator: a GPU whose cl |
| 2026-11-24T10:13 | sn56 | SCORING_COMMIT | sn56 commit touches scoring: Bound the database use of the per-miner b |
| 2026-11-24T10:13 | sn61 | RELEASE | sn61 released 4.11.1 |
| 2026-11-24T10:13 | sn61 | SCORING_COMMIT | sn61 commit touches scoring: feat: update bot virus challenge configur |
| 2026-11-24T10:13 | sn70 | SCORING_COMMIT | sn70 commit touches scoring: Merge pull request #211 from fugal-ai/doc |
| 2026-11-24T10:13 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Authorize bounded fixed correction quotes |
| 2026-11-24T10:13 | sn82 | SCORING_COMMIT | sn82 commit touches scoring: Document live Mainnet V2.1 scoring |
| 2026-11-24T10:13 | sn82 | README_TASK_DIFF | sn82 README task/scoring sections changed |
| 2026-11-24T10:13 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: feat(laned): WB27 lane B miner levers, 12 |
| 2026-11-24T10:13 | sn91 | README_TASK_DIFF | sn91 README task/scoring sections changed |
| 2026-11-24T10:13 | sn98 | SCORING_COMMIT | sn98 commit touches scoring: feat: add light validator mode that copie |
| 2026-11-24T10:13 | sn99 | SCORING_COMMIT | sn99 commit touches scoring: Board: the champion's match row shows its |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

