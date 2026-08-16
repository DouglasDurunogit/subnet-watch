# Subnet watch — dashboard

_snapshot 2026-08-16T17:31:21Z · block 8858727 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 50 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 91 | `miner_burn` < 0.99 |
| Ranked | 91 | passed every gate |
| **Positive margin** | **50** | income beats machine cost |
| New events this window | 3 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 61 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 8 | `████` |
| 0.6–0.8 | 5 | `██` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 37 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 78.2 | 114 | 34,235 | cpu-small | 20 | 90% |
| 2 | sn67 Harnyx | 72.5 | 23.50 | 416 | cpu-small | 137 | 11% |
| 3 | sn26 Perturb | 70.8 | 40.48 | 74.27 | rtx3060 | 10 | 70% |
| 4 | sn1 Apex | 70.1 | 754 | 1,041 | rtx4090* | 4 | 55% |
| 5 | sn96 Verathos | 70 | 33.06 | 262 | rtx4090 | 60 | 41% |
| 6 | sn76 Phylax | 70 | 11.45 | 154 | cpu-small | 10 | 29% |
| 7 | sn41 Almanac | 69.9 | 12.82 | 47.71 | cpu-small | 75 | 65% |
| 8 | sn91 cascade | 69.1 | 563 | 2,277 | rtx4090* | 5 | 51% |
| 9 | sn15 ORO | 68.8 | 12.58 | 20.97 | cpu-small | 63 | 94% |
| 10 | sn85 Vidaio | 68.7 | 507 | 674 | rtx4090* | 10 | 22% |
| 11 | sn56 Gradients | 68.7 | 503 | 958 | rtx4090* | 7 | 68% |
| 12 | sn62 Ridges | 68.5 | 474 | 2,195 | rtx4090* | 6 | 40% |
| 13 | sn21 AdTAO | 67.7 | 7.64 | 34.23 | cpu-small | 88 | 45% |
| 14 | sn11 TrajectoryRL | 67.1 | 4,128 | 4,128 = | cpu-small | 1 | 100% |
| 15 | sn38 ChronoLLM | 66 | 97.75 | 1,336 | cpu-small | 10 | 52% |
| 16 | sn124 Swarm | 65.9 | 224 | 720 | rtx4090* | 24 | 11% |
| 17 | sn55 NIOME | 61.4 | 55.78 | 483 | rtx4090* | 11 | 30% |
| 18 | sn28 gm | 59.6 | 33.89 | 2,087 | rtx4090* | 40 | 28% |
| 19 | sn60 Bitsec.ai | 59.2 | 393 | 393 = | cpu-small | 3 | 50% |
| 20 | sn74 Gittensor | 58.5 | 25.63 | 208 | rtx4090* | 14 | 63% |

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
| concentrated (30–60%) | 18 |
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
| 2026-08-16T01:55 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: Implement resilient batch scoring and wi |
| 2026-08-15T23:01 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: Raise tasks per round across all four tra |
| 2026-08-15T20:35 | sn108 | SCORING_COMMIT | sn108 commit touches scoring: docs(miner): drop the second artefact th |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

