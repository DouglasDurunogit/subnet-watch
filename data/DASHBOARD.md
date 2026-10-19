# Subnet watch — dashboard

_snapshot 2026-10-19T21:39:01Z · block 9320277 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 60 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 100 | `miner_burn` < 0.99 |
| Ranked | 100 | passed every gate |
| **Positive margin** | **60** | income beats machine cost |
| New events this window | 9 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 65 | `████████████████████████████` |
| 0–0.2 | 8 | `███` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 7 | `███` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 28 | `████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn3 Teutonic | 74.3 | 2,680 | 7,161 | rtx4090* | 5 | 40% |
| 2 | sn41 Almanac | 73.6 | 32.89 | 129 | cpu-small | 127 | 8% |
| 3 | sn91 cascade | 72.4 | 593 | 1,582 | cpu-small | 5 | 52% |
| 4 | sn67 Harnyx | 69.4 | 10.45 | 262 | cpu-small | 167 | 11% |
| 5 | sn53 engy | 69 | 542 | 2,255 | rtx4090 | 24 | 16% |
| 6 | sn82 Noah | 68.7 | 681 | 712 | rtx4090* | 60 | 2% |
| 7 | sn1 Apex | 68.2 | 435 | 969 | rtx4090* | 5 | 56% |
| 8 | sn102 ConnitoAI | 67.7 | 372 | 1,483 | rtx4090* | 7 | 35% |
| 9 | sn107 Minos | 67.6 | 255 | 21,645 | cpu-small | 20 | 80% |
| 10 | sn23 Trishool | 67.6 | 236 | 236 = | cpu-small | 4 | 80% |
| 11 | sn15 ORO | 66.3 | 6.08 | 15,851 | cpu-small | 56 | 98% |
| 12 | sn120 Affine | 64.2 | 150 | 244 | rtx4090* | 241 | 1% |
| 13 | sn66 conjectures | 63.7 | 111 | 231 | rtx4090* | 4 | 80% |
| 14 | sn14 Cacheon | 63.6 | 109 | 4,274 | rtx4090* | 11 | 63% |
| 15 | sn55 NIOME | 62.3 | 72.95 | 601 | rtx4090* | 11 | 30% |
| 16 | sn61 RedTeam | 61.5 | 60.17 | 109 | rtx4090* | 121 | 1% |
| 17 | sn97 Ingot | 61.4 | 1,989 | 1,989 = | rtx4090* | 5 | 20% |
| 18 | sn80 OpenRoboto | 60.9 | 1,689 | 2,680 | rtx4090* | 11 | 35% |
| 19 | sn92 REAX | 60.3 | 76.54 | 3,033 | rtx4090 | 237 | 11% |
| 20 | sn111 Claims | 59.4 | 31.58 | 2,839 | rtx4090* | 6 | 90% |

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
| wide (<30%) | 28 |
| concentrated (30–60%) | 21 |
| dominated (60–90%) | 27 |
| captured (>90%) | 23 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 95 |
| README keywords (GUESS) | 13 |
| min_compute.yml (curated) | 10 |
| code-submission (validator runs it) | 9 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-10-19T21:39 | sn7 | BURN_DROP | sn7 burn fell 1.000 -> 0.505 - miners can earn again |
| 2026-10-19T21:39 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: fix: use validator lockfile for local tes |
| 2026-10-19T21:39 | sn41 | SCORING_COMMIT | sn41 commit touches scoring: Updating default miner alpha to 3600, or  |
| 2026-10-19T21:39 | sn50 | SCORING_COMMIT | sn50 commit touches scoring: burn 22% of miner emission (#341) |
| 2026-10-19T21:39 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-4195 - [P2] Skip could-not-reach rows |
| 2026-10-19T21:39 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Record verified runtime recovery release  |
| 2026-10-19T21:39 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: docs(validator): cover both profile vers |
| 2026-10-19T21:39 | sn111 | RELEASE | sn111 released v1.1.0 |
| 2026-10-19T21:39 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: Integrate approved-group fractional cove |
| 2026-10-19T17:12 | sn7 | RELEASE | sn7 released release-20261019-165322 |
| 2026-10-19T17:12 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: feat(scoring): the pooled count score can |
| 2026-10-19T17:12 | sn22 | SCORING_COMMIT | sn22 commit touches scoring: fix(task-api): reference vectors finish a |
| 2026-10-19T17:12 | sn25 | RELEASE | sn25 released v2026.10.19-1076177550 |
| 2026-10-19T17:12 | sn28 | RELEASE | sn28 released v0.5.3-dev |
| 2026-10-19T17:12 | sn51 | RELEASE | sn51 released miner-v1.008 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

