# Subnet watch — dashboard

_snapshot 2026-10-10T02:47:51Z · block 9249822 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 53 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 100 | `miner_burn` < 0.99 |
| Ranked | 100 | passed every gate |
| **Positive margin** | **53** | income beats machine cost |
| New events this window | 4 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 70 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 6 | `██` |
| 0.6–0.8 | 8 | `███` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 28 | `███████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 81.8 | 273 | 23,106 | cpu-small | 20 | 80% |
| 2 | sn41 Almanac | 74.5 | 40.86 | 111 | cpu-small | 123 | 2% |
| 3 | sn80 OpenRoboto | 72.1 | 1,374 | 6,554 | rtx4090* | 7 | 35% |
| 4 | sn101 Tag101 | 70.4 | 13.52 | 16.44 | cpu-small | 243 | 1% |
| 5 | sn49 Nepher Robotics | 69.8 | 703 | 4,593 | rtx4090* | 4 | 68% |
| 6 | sn38 ChronoLLM | 68.7 | 212 | 967 | cpu-small | 9 | 52% |
| 7 | sn67 Harnyx | 68.5 | 7.99 | 835 | cpu-small | 149 | 30% |
| 8 | sn79 MVTRX | 66.8 | 7.57 | 69.44 | cpu-small | 247 | 3% |
| 9 | sn15 ORO | 66.1 | 6.00 | 12.40 | cpu-small | 46 | 98% |
| 10 | sn26 Perturb | 66 | 225 | 369 | rtx3060 | 4 | 61% |
| 11 | sn62 Ridges | 63.6 | 108 | 1,100 | rtx4090* | 35 | 17% |
| 12 | sn120 Affine | 63.3 | 156 | 315 | rtx4090* | 249 | 1% |
| 13 | sn61 RedTeam | 62.4 | 76.91 | 105 | rtx4090* | 126 | 1% |
| 14 | sn65 True Performance | 62.3 | 79.35 | 167 | rtx4090* | 6 | 75% |
| 15 | sn28 SayGM | 61.3 | 56.93 | 1,613 | rtx4090* | 71 | 23% |
| 16 | sn53 engy | 60.3 | 1,418 | 4,686 | rtx4090 | 18 | 17% |
| 17 | sn111 Claims | 59.5 | 32.45 | 3,104 | rtx4090* | 7 | 90% |
| 18 | sn23 Trishool | 59.3 | 409 | 409 = | cpu-small | 3 | 80% |
| 19 | sn91 cascade | 59.3 | 409 | 1,091 | cpu-small | 5 | 52% |
| 20 | sn1 Apex | 58.8 | 924 | 968 | rtx4090* | 4 | 55% |

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
| concentrated (30–60%) | 25 |
| dominated (60–90%) | 26 |
| captured (>90%) | 21 |

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
| 2026-10-10T02:48 | sn25 | RELEASE | sn25 released v2026.10.9-1067985620 |
| 2026-10-10T02:48 | sn62 | RELEASE | sn62 released v0.3.11 |
| 2026-10-10T02:48 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge pull request #322 from leadpoet/cod |
| 2026-10-10T02:48 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Support prospective nine-batch mining an |
| 2026-10-09T23:34 | sn14 | SCORING_COMMIT | sn14 commit touches scoring: Notify Discord when new hotkeys receive c |
| 2026-10-09T23:34 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Refresh protected scorer manifest for req |
| 2026-10-09T23:34 | sn116 | RELEASE | sn116 released producer-code-r6 |
| 2026-10-09T23:34 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Merge pull request #943 from carbonphysi |
| 2026-10-09T23:34 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Retain partial miner batches and advance |
| 2026-10-09T19:37 | sn13 | RELEASE | sn13 released Release v1.18.74 |
| 2026-10-09T19:37 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: docs(rewards): self-mining section lists  |
| 2026-10-09T19:37 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Name a rejected network sign-in in the va |
| 2026-10-09T19:37 | sn48 | README_TASK_DIFF | sn48 README task/scoring sections changed |
| 2026-10-09T19:37 | sn66 | README_TASK_DIFF | sn66 README task/scoring sections changed |
| 2026-10-09T19:37 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Include accepted host scores in closed bi |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

