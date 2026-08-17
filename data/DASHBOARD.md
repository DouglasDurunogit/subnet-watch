# Subnet watch — dashboard

_snapshot 2026-08-17T09:54:07Z · block 8863640 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 50 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 90 | `miner_burn` < 0.99 |
| Ranked | 90 | passed every gate |
| **Positive margin** | **50** | income beats machine cost |
| New events this window | 2 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 62 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 7 | `███` |
| 0.6–0.8 | 5 | `██` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 38 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 78.4 | 104 | 202 | cpu-small | 10 | 20% |
| 2 | sn107 Minos | 78.1 | 111 | 32,739 | cpu-small | 20 | 90% |
| 3 | sn67 Harnyx | 72 | 20.58 | 385 | cpu-small | 129 | 11% |
| 4 | sn26 Perturb | 70.8 | 40.15 | 73.71 | rtx3060 | 10 | 70% |
| 5 | sn91 cascade | 69.1 | 564 | 2,280 | rtx4090* | 5 | 51% |
| 6 | sn41 Almanac | 68.7 | 9.67 | 52.97 | cpu-small | 75 | 69% |
| 7 | sn85 Vidaio | 68.6 | 483 | 483 = | rtx4090* | 10 | 16% |
| 8 | sn96 Verathos | 68.5 | 22.98 | 417 | rtx4090 | 67 | 41% |
| 9 | sn62 Ridges | 68.4 | 460 | 2,134 | rtx4090* | 6 | 40% |
| 10 | sn15 ORO | 68.3 | 11.51 | 13,058 | cpu-small | 66 | 94% |
| 11 | sn21 AdTAO | 67.6 | 7.55 | 33.89 | cpu-small | 88 | 45% |
| 12 | sn38 ChronoLLM | 66.1 | 99.71 | 1,363 | cpu-small | 10 | 52% |
| 13 | sn124 Swarm | 65.8 | 221 | 710 | rtx4090* | 24 | 11% |
| 14 | sn2 DSperse | 63.3 | 101 | 109 | rtx4090* | 5 | 82% |
| 15 | sn55 NIOME | 61.4 | 56.24 | 475 | rtx4090* | 11 | 29% |
| 16 | sn28 gm | 60.3 | 41.62 | 2,050 | rtx4090* | 44 | 22% |
| 17 | sn60 Bitsec.ai | 58.9 | 363 | 363 = | cpu-small | 3 | 50% |
| 18 | sn74 Gittensor | 58.1 | 22.94 | 206 | rtx4090* | 14 | 63% |
| 19 | sn51 lium.io | 57 | 21.65 | 2,502 | rtx4090* | 56 | 79% |
| 20 | sn61 RedTeam | 56.9 | 13.94 | 394 | rtx4090* | 84 | 10% |

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
| concentrated (30–60%) | 21 |
| dominated (60–90%) | 17 |
| captured (>90%) | 27 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 102 |
| code-submission (validator runs it) | 10 |
| min_compute.yml (curated) | 9 |
| README keywords (GUESS) | 6 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-08-17T09:54 | sn10 | SCORING_COMMIT | sn10 commit touches scoring: feat(bench): score the full workload trac |
| 2026-08-17T08:59 | sn85 | SCORING_COMMIT | sn85 commit touches scoring: reinvite miners rejected with flag INVITA |
| 2026-08-17T08:07 | sn51 | RELEASE | sn51 released executor-v1.120 |
| 2026-08-17T08:07 | sn75 | SCORING_COMMIT | sn75 commit touches scoring: feat(compute-scoring): root-settable dedi |
| 2026-08-17T06:00 | sn2 | BURN_DROP | sn2 burn fell 1.000 -> 0.823 - miners can earn again |
| 2026-08-17T06:00 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Refresh provider failures during recovery |
| 2026-08-17T01:52 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Bound validator worker startup verificati |
| 2026-08-16T17:31 | sn100 | RELEASE | sn100 released v3.3.24 |
| 2026-08-16T17:03 | sn85 | SCORING_COMMIT | sn85 commit touches scoring: retry inviting rejected miner UIDs in com |
| 2026-08-16T16:38 | sn75 | SCORING_COMMIT | sn75 commit touches scoring: Merge pull request #49 from thenervelab/f |
| 2026-08-16T16:00 | sn100 | RELEASE | sn100 released v3.3.23 |
| 2026-08-16T13:40 | sn68 | SCORING_COMMIT | sn68 commit touches scoring: discard individual validator processing f |
| 2026-08-16T12:00 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: Download only the tasks a validator drew |
| 2026-08-16T08:44 | sn100 | RELEASE | sn100 released v3.3.22 |
| 2026-08-16T07:41 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: Match CWEs numerically, draw tasks per va |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

