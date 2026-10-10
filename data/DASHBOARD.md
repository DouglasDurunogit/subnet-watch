# Subnet watch — dashboard

_snapshot 2026-10-10T09:44:06Z · block 9251903 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 59 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 100 | `miner_burn` < 0.99 |
| Ranked | 100 | passed every gate |
| **Positive margin** | **59** | income beats machine cost |
| New events this window | 4 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 71 | `████████████████████████████` |
| 0–0.2 | 6 | `██` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 8 | `███` |
| 0.6–0.8 | 7 | `███` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 28 | `███████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 81.9 | 279 | 23,687 | cpu-small | 20 | 80% |
| 2 | sn3 Teutonic | 74.9 | 3,175 | 6,359 | rtx4090* | 5 | 30% |
| 3 | sn41 Almanac | 74.5 | 40.73 | 111 | cpu-small | 123 | 2% |
| 4 | sn101 Tag101 | 70.5 | 13.84 | 16.52 | cpu-small | 243 | 1% |
| 5 | sn49 Nepher Robotics | 69.7 | 683 | 4,833 | rtx4090* | 4 | 69% |
| 6 | sn80 OpenRoboto | 69.4 | 611 | 3,196 | rtx4090* | 7 | 35% |
| 7 | sn67 Harnyx | 69 | 9.24 | 897 | cpu-small | 129 | 32% |
| 8 | sn38 ChronoLLM | 68.8 | 217 | 991 | cpu-small | 9 | 52% |
| 9 | sn15 ORO | 66.9 | 7.05 | 19,112 | cpu-small | 50 | 98% |
| 10 | sn79 MVTRX | 66.7 | 7.33 | 53.01 | cpu-small | 247 | 2% |
| 11 | sn26 Perturb | 66.2 | 241 | 403 | rtx3060 | 4 | 60% |
| 12 | sn62 Ridges | 63.9 | 120 | 1,378 | rtx4090* | 36 | 17% |
| 13 | sn120 Affine | 62.6 | 139 | 453 | rtx4090* | 249 | 1% |
| 14 | sn65 True Performance | 62.5 | 82.63 | 174 | rtx4090* | 6 | 75% |
| 15 | sn61 RedTeam | 62.3 | 76.69 | 109 | rtx4090* | 126 | 1% |
| 16 | sn28 SayGM | 61.4 | 59.25 | 945 | rtx4090* | 70 | 29% |
| 17 | sn53 engy | 60.3 | 1,446 | 4,779 | rtx4090 | 18 | 17% |
| 18 | sn81 Reliquary | 59.7 | 33.55 | 219 | rtx4090* | 48 | 47% |
| 19 | sn23 Trishool | 59.4 | 421 | 421 = | cpu-small | 3 | 80% |
| 20 | sn91 cascade | 59.3 | 410 | 1,096 | cpu-small | 5 | 52% |

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
| concentrated (30–60%) | 25 |
| dominated (60–90%) | 25 |
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
| 2026-10-10T09:44 | sn25 | RELEASE | sn25 released v2026.10.10-1068162640 |
| 2026-10-10T09:44 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: NO-TICKET - [P1] validator: cap fresh vlo |
| 2026-10-10T09:44 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge pull request #328 from leadpoet/cod |
| 2026-10-10T09:44 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Document live epoch 116 distinct-task tr |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

