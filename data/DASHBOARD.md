# Subnet watch — dashboard

_snapshot 2026-08-16T15:01:36Z · block 8857978 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 52 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 91 | `miner_burn` < 0.99 |
| Ranked | 91 | passed every gate |
| **Positive margin** | **52** | income beats machine cost |
| New events this window | 0 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 61 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 8 | `████` |
| 0.6–0.8 | 5 | `██` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 37 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 77.9 | 107 | 32,905 | cpu-small | 20 | 90% |
| 2 | sn76 Phylax | 73.8 | 31.76 | 157 | cpu-small | 10 | 29% |
| 3 | sn67 Harnyx | 72.5 | 23.71 | 419 | cpu-small | 137 | 11% |
| 4 | sn26 Perturb | 70.8 | 40.59 | 74.46 | rtx3060 | 10 | 70% |
| 5 | sn96 Verathos | 70.3 | 35.59 | 203 | rtx4090 | 54 | 43% |
| 6 | sn1 Apex | 70.1 | 765 | 1,055 | rtx4090* | 4 | 55% |
| 7 | sn41 Almanac | 69.9 | 12.84 | 47.83 | cpu-small | 75 | 65% |
| 8 | sn91 cascade | 69.1 | 565 | 2,283 | rtx4090* | 5 | 51% |
| 9 | sn15 ORO | 68.8 | 12.91 | 12,841 | cpu-small | 61 | 95% |
| 10 | sn85 Vidaio | 68.7 | 508 | 518 | rtx4090* | 10 | 17% |
| 11 | sn56 Gradients | 68.7 | 505 | 961 | rtx4090* | 7 | 68% |
| 12 | sn62 Ridges | 68.5 | 476 | 2,203 | rtx4090* | 6 | 40% |
| 13 | sn21 AdTAO | 67.7 | 7.65 | 34.29 | cpu-small | 88 | 45% |
| 14 | sn11 TrajectoryRL | 67 | 4,121 | 4,121 = | cpu-small | 1 | 100% |
| 15 | sn38 ChronoLLM | 66 | 96.72 | 1,323 | cpu-small | 10 | 52% |
| 16 | sn124 Swarm | 65.9 | 224 | 719 | rtx4090* | 24 | 11% |
| 17 | sn2 DSperse | 64.3 | 134 | 195 | rtx4090* | 4 | 82% |
| 18 | sn55 NIOME | 61.3 | 55.14 | 484 | rtx4090* | 11 | 30% |
| 19 | sn28 gm | 59.5 | 32.85 | 2,418 | rtx4090* | 40 | 27% |
| 20 | sn60 Bitsec.ai | 59.3 | 410 | 410 = | cpu-small | 3 | 50% |

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
| wide (<30%) | 26 |
| concentrated (30–60%) | 20 |
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
| 2026-08-15T17:59 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: Add a local evaluation command |
| 2026-08-15T13:39 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: fix(prism): rename lattice_score to sati |
| 2026-08-15T12:56 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: feat(prism): live leaf from G2 benchmark |
| 2026-08-15T09:06 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

