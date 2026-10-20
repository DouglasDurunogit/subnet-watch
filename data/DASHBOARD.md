# Subnet watch — dashboard

_snapshot 2026-10-20T00:43:03Z · block 9321197 · run_status **ok**_

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
| New events this window | 6 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 67 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 6 | `███` |
| 0.6–0.8 | 8 | `███` |
| 0.8–0.99 | 8 | `███` |
| ≥0.99 dead | 28 | `████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn3 Teutonic | 74.3 | 2,693 | 7,194 | rtx4090* | 5 | 40% |
| 2 | sn91 cascade | 72.4 | 590 | 1,574 | cpu-small | 5 | 52% |
| 3 | sn41 Almanac | 72.4 | 24.33 | 101 | cpu-small | 125 | 27% |
| 4 | sn67 Harnyx | 69.4 | 10.50 | 263 | cpu-small | 168 | 11% |
| 5 | sn82 Noah | 68.8 | 681 | 712 | rtx4090* | 60 | 2% |
| 6 | sn53 engy | 68.8 | 514 | 2,139 | rtx4090 | 24 | 16% |
| 7 | sn1 Apex | 68.4 | 465 | 965 | rtx4090* | 5 | 55% |
| 8 | sn107 Minos | 67.6 | 256 | 21,784 | cpu-small | 20 | 80% |
| 9 | sn23 Trishool | 67.5 | 235 | 235 = | cpu-small | 4 | 80% |
| 10 | sn15 ORO | 66.3 | 6.10 | 15,908 | cpu-small | 56 | 98% |
| 11 | sn120 Affine | 64.2 | 147 | 246 | rtx4090* | 245 | 1% |
| 12 | sn14 Cacheon | 63.6 | 110 | 4,286 | rtx4090* | 11 | 63% |
| 13 | sn66 conjectures | 62.9 | 88.20 | 199 | rtx4090* | 4 | 84% |
| 14 | sn61 RedTeam | 61.5 | 60.39 | 110 | rtx4090* | 121 | 1% |
| 15 | sn97 Ingot | 61.4 | 1,997 | 1,997 = | rtx4090* | 5 | 20% |
| 16 | sn92 REAX | 60.2 | 80.40 | 3,074 | rtx4090 | 244 | 11% |
| 17 | sn80 OpenRoboto | 59.5 | 1,111 | 2,626 | rtx4090* | 11 | 36% |
| 18 | sn111 Claims | 59.4 | 31.73 | 2,851 | rtx4090* | 6 | 90% |
| 19 | sn81 Reliquary | 59.2 | 28.34 | 301 | rtx4090* | 8 | 85% |
| 20 | sn4 Targon | 57.9 | 9,873 | 29,110 | rtx4090* | 5 | 70% |

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
| concentrated (30–60%) | 20 |
| dominated (60–90%) | 27 |
| captured (>90%) | 24 |

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
| 2026-10-20T00:43 | sn22 | SCORING_COMMIT | sn22 commit touches scoring: fix(validators): embed checks wait up to  |
| 2026-10-20T00:43 | sn28 | RELEASE | sn28 released v0.5.4 |
| 2026-10-20T00:43 | sn28 | SCORING_COMMIT | sn28 commit touches scoring: chore(release): promote gm-miner 0.5.4 (# |
| 2026-10-20T00:43 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Regenerate protected scorer manifest from |
| 2026-10-20T00:43 | sn76 | BURN_DROP | sn76 burn fell 1.000 -> 0.989 - miners can earn again |
| 2026-10-20T00:43 | sn117 | BURN_DROP | sn117 burn fell 1.000 -> 0.884 - miners can earn again |
| 2026-10-19T21:39 | sn7 | BURN_DROP | sn7 burn fell 1.000 -> 0.505 - miners can earn again |
| 2026-10-19T21:39 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: fix: use validator lockfile for local tes |
| 2026-10-19T21:39 | sn41 | SCORING_COMMIT | sn41 commit touches scoring: Updating default miner alpha to 3600, or  |
| 2026-10-19T21:39 | sn50 | SCORING_COMMIT | sn50 commit touches scoring: burn 22% of miner emission (#341) |
| 2026-10-19T21:39 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-4195 - [P2] Skip could-not-reach rows |
| 2026-10-19T21:39 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Record verified runtime recovery release  |
| 2026-10-19T21:39 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: docs(validator): cover both profile vers |
| 2026-10-19T21:39 | sn111 | RELEASE | sn111 released v1.1.0 |
| 2026-10-19T21:39 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: Integrate approved-group fractional cove |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

