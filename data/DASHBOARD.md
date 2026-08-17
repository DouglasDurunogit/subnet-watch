# Subnet watch — dashboard

_snapshot 2026-08-17T05:59:31Z · block 8862467 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 54 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 90 | `miner_burn` < 0.99 |
| Ranked | 90 | passed every gate |
| **Positive margin** | **54** | income beats machine cost |
| New events this window | 2 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 61 | `████████████████████████████` |
| 0–0.2 | 4 | `██` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 7 | `███` |
| 0.6–0.8 | 6 | `███` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 38 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 78.1 | 111 | 32,258 | cpu-small | 20 | 90% |
| 2 | sn67 Harnyx | 72 | 20.82 | 389 | cpu-small | 128 | 11% |
| 3 | sn26 Perturb | 70.8 | 40.54 | 74.37 | rtx3060 | 10 | 70% |
| 4 | sn1 Apex | 70.6 | 878 | 984 | rtx4090* | 4 | 54% |
| 5 | sn76 Phylax | 70.5 | 13.42 | 157 | cpu-small | 10 | 29% |
| 6 | sn85 Vidaio | 69.7 | 669 | 831 | rtx4090* | 10 | 27% |
| 7 | sn96 Verathos | 69.6 | 29.68 | 420 | rtx4090 | 55 | 41% |
| 8 | sn91 cascade | 69.1 | 569 | 2,302 | rtx4090* | 5 | 51% |
| 9 | sn15 ORO | 68.9 | 12.70 | 21.54 | cpu-small | 67 | 94% |
| 10 | sn56 Gradients | 68.7 | 501 | 958 | rtx4090* | 7 | 68% |
| 11 | sn41 Almanac | 68.7 | 9.67 | 53.42 | cpu-small | 75 | 70% |
| 12 | sn62 Ridges | 68.4 | 465 | 2,152 | rtx4090* | 6 | 40% |
| 13 | sn21 AdTAO | 67.7 | 7.63 | 34.20 | cpu-small | 88 | 45% |
| 14 | sn38 ChronoLLM | 66.1 | 100 | 1,368 | cpu-small | 10 | 52% |
| 15 | sn124 Swarm | 65.9 | 224 | 718 | rtx4090* | 24 | 11% |
| 16 | sn98 NeverPlayAlone | 64.1 | 1,690 | 1,690 = | cpu-small | 1 | 100% |
| 17 | sn2 DSperse | 61.9 | 65.94 | 229 | rtx4090* | 4 | 82% |
| 18 | sn55 NIOME | 61.4 | 56.84 | 474 | rtx4090* | 11 | 29% |
| 19 | sn60 Bitsec.ai | 59 | 374 | 374 = | cpu-small | 3 | 50% |
| 20 | sn28 gm | 58.9 | 28.09 | 2,313 | rtx4090* | 39 | 25% |

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
| concentrated (30–60%) | 18 |
| dominated (60–90%) | 18 |
| captured (>90%) | 26 |

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
| 2026-08-16T06:04 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-08-16T06:04 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Preserve production clocks in parity vali |
| 2026-08-16T04:08 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Regenerate validator protected workflow m |
| 2026-08-16T01:55 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Fix validator RPC boundary fixture |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

