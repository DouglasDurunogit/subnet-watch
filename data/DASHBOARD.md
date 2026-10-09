# Subnet watch — dashboard

_snapshot 2026-10-09T19:36:33Z · block 9247666 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 54 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 100 | `miner_burn` < 0.99 |
| Ranked | 100 | passed every gate |
| **Positive margin** | **54** | income beats machine cost |
| New events this window | 14 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 69 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 7 | `███` |
| 0.6–0.8 | 8 | `███` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 28 | `███████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 81.7 | 265 | 22,539 | cpu-small | 20 | 80% |
| 2 | sn41 Almanac | 74.8 | 43.90 | 111 | cpu-small | 121 | 2% |
| 3 | sn80 OpenRoboto | 72 | 1,331 | 6,351 | rtx4090* | 7 | 35% |
| 4 | sn1 Apex | 70.8 | 940 | 985 | rtx4090* | 4 | 53% |
| 5 | sn101 Tag101 | 70.1 | 13.01 | 16.92 | cpu-small | 244 | 1% |
| 6 | sn38 ChronoLLM | 68.7 | 209 | 952 | cpu-small | 9 | 52% |
| 7 | sn67 Harnyx | 68.3 | 7.86 | 823 | cpu-small | 149 | 30% |
| 8 | sn79 MVTRX | 67.5 | 8.07 | 52.27 | cpu-small | 245 | 2% |
| 9 | sn4 Targon | 66.8 | 9,831 | 28,987 | rtx4090* | 5 | 70% |
| 10 | sn26 Perturb | 66.2 | 237 | 397 | rtx3060 | 4 | 60% |
| 11 | sn15 ORO | 65.4 | 6.02 | 12.46 | cpu-small | 47 | 98% |
| 12 | sn62 Ridges | 63.5 | 106 | 1,080 | rtx4090* | 35 | 17% |
| 13 | sn65 True Performance | 62.3 | 78.15 | 165 | rtx4090* | 6 | 75% |
| 14 | sn61 RedTeam | 62.3 | 76.11 | 102 | rtx4090* | 126 | 1% |
| 15 | sn53 engy | 60.1 | 1,345 | 4,448 | rtx4090 | 18 | 17% |
| 16 | sn111 Claims | 59.7 | 34.60 | 3,053 | rtx4090* | 6 | 90% |
| 17 | sn91 cascade | 59.3 | 414 | 1,106 | cpu-small | 5 | 52% |
| 18 | sn23 Trishool | 59.2 | 400 | 400 = | cpu-small | 3 | 80% |
| 19 | sn5 Hone | 58 | 33.73 | 35.59 | rtx4090* | 243 | 0% |
| 20 | sn56 Gradients | 57.8 | 669 | 4,631 | rtx4090* | 9 | 39% |

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
| concentrated (30–60%) | 26 |
| dominated (60–90%) | 26 |
| captured (>90%) | 22 |

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
| 2026-10-09T19:37 | sn13 | RELEASE | sn13 released Release v1.18.74 |
| 2026-10-09T19:37 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: docs(rewards): self-mining section lists  |
| 2026-10-09T19:37 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Name a rejected network sign-in in the va |
| 2026-10-09T19:37 | sn48 | README_TASK_DIFF | sn48 README task/scoring sections changed |
| 2026-10-09T19:37 | sn66 | README_TASK_DIFF | sn66 README task/scoring sections changed |
| 2026-10-09T19:37 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Include accepted host scores in closed bi |
| 2026-10-09T19:37 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: Pool deliveries: claim-refusal backoff +  |
| 2026-10-09T19:37 | sn79 | README_TASK_DIFF | sn79 README task/scoring sections changed |
| 2026-10-09T19:37 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: feat(env): score reliquary/stdio-program/ |
| 2026-10-09T19:37 | sn104 | MECHANISM_ADDED | sn104 now runs 2 incentive mechanisms (was 1) |
| 2026-10-09T19:37 | sn116 | RELEASE | sn116 released producer-code-r5 |
| 2026-10-09T19:37 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Merge pull request #935 from carbonphysi |
| 2026-10-09T19:37 | sn117 | README_TASK_DIFF | sn117 README task/scoring sections changed |
| 2026-10-09T19:37 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Recover hourly miner weight submissions  |
| 2026-10-09T14:20 | sn3 | SCORING_COMMIT | sn3 commit touches scoring: Add competition filters to evaluation hist |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

