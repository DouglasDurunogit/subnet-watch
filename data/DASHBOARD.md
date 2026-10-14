# Subnet watch — dashboard

_snapshot 2026-10-14T05:28:40Z · block 9279425 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 55 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 99 | `miner_burn` < 0.99 |
| Ranked | 99 | passed every gate |
| **Positive margin** | **55** | income beats machine cost |
| New events this window | 11 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 68 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 11 | `█████` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 29 | `████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 82.1 | 288 | 24,433 | cpu-small | 20 | 80% |
| 2 | sn3 Teutonic | 74.8 | 3,107 | 3,107 = | rtx4090* | 5 | 40% |
| 3 | sn91 cascade | 72.6 | 631 | 2,021 | cpu-small | 5 | 52% |
| 4 | sn53 engy | 71.7 | 1,213 | 2,675 | rtx4090 | 18 | 17% |
| 5 | sn101 Tag101 | 70.4 | 13.91 | 15.10 | cpu-small | 244 | 1% |
| 6 | sn67 Harnyx | 70 | 12.01 | 699 | cpu-small | 145 | 26% |
| 7 | sn58 Attune | 68.7 | 513 | 825 | rtx4090* | 5 | 71% |
| 8 | sn15 ORO | 67.2 | 7.85 | 16.41 | cpu-small | 57 | 97% |
| 9 | sn79 MVTRX | 66.9 | 6.95 | 54.54 | cpu-small | 249 | 2% |
| 10 | sn4 Targon | 66.8 | 10,017 | 29,535 | rtx4090* | 5 | 70% |
| 11 | sn26 Perturb | 65.2 | 331 | 409 | rtx3060 | 4 | 60% |
| 12 | sn41 Almanac | 65 | 4.79 | 158 | cpu-small | 120 | 5% |
| 13 | sn62 Ridges | 64.1 | 127 | 1,279 | rtx4090* | 37 | 17% |
| 14 | sn120 Affine | 64 | 134 | 435 | rtx4090* | 249 | 1% |
| 15 | sn61 RedTeam | 61.9 | 69.20 | 91.93 | rtx4090* | 128 | 1% |
| 16 | sn28 SayGM | 61.3 | 56.37 | 2,730 | rtx4090* | 73 | 29% |
| 17 | sn111 Claims | 59.9 | 36.57 | 3,189 | rtx4090* | 6 | 90% |
| 18 | sn23 Trishool | 59.2 | 400 | 400 = | cpu-small | 3 | 80% |
| 19 | sn80 OpenRoboto | 58.9 | 927 | 3,713 | rtx4090* | 10 | 35% |
| 20 | sn49 Nepher Robotics | 57.4 | 601 | 1,209 | rtx4090* | 4 | 69% |

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
| concentrated (30–60%) | 22 |
| dominated (60–90%) | 28 |
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
| 2026-10-14T05:29 | sn25 | RELEASE | sn25 released v2026.10.13-1071515580 |
| 2026-10-14T05:29 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Merge v2/gate-miner-tests into main |
| 2026-10-14T05:29 | sn37 | SCORING_COMMIT | sn37 commit touches scoring: docs: describe planned stake-retention me |
| 2026-10-14T05:29 | sn37 | README_TASK_DIFF | sn37 README task/scoring sections changed |
| 2026-10-14T05:29 | sn41 | SCORING_COMMIT | sn41 commit touches scoring: Score update |
| 2026-10-14T05:29 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-4035 - [P0] Validator: connect to a h |
| 2026-10-14T05:29 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge pull request #418: Preserve verifie |
| 2026-10-14T05:29 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: security: validate repository scope befor |
| 2026-10-14T05:29 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Merge pull request #248 from Umi-BitSign/ |
| 2026-10-14T05:29 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: fix(validator): carry staged promotions a |
| 2026-10-14T05:29 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Merge pull request #1335 from carbonphys |
| 2026-10-14T00:39 | sn7 | RELEASE | sn7 released release-20261013-222136 |
| 2026-10-14T00:39 | sn7 | SCORING_COMMIT | sn7 commit touches scoring: Ban a miner from scoring for 12 rounds whe |
| 2026-10-14T00:39 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Merge the validator test and correctness  |
| 2026-10-14T00:39 | sn45 | SCORING_COMMIT | sn45 commit touches scoring: soak report: read rotated validator logs |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

