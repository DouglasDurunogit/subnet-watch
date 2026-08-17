# Subnet watch — dashboard

_snapshot 2026-08-17T07:12:40Z · block 8862833 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 53 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 90 | `miner_burn` < 0.99 |
| Ranked | 90 | passed every gate |
| **Positive margin** | **53** | income beats machine cost |
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
| 1 | sn107 Minos | 78.2 | 115 | 33,029 | cpu-small | 20 | 90% |
| 2 | sn76 Phylax | 76.8 | 69.24 | 340 | cpu-small | 10 | 27% |
| 3 | sn67 Harnyx | 72.1 | 20.79 | 389 | cpu-small | 128 | 11% |
| 4 | sn26 Perturb | 70.8 | 40.69 | 74.63 | rtx3060 | 10 | 70% |
| 5 | sn1 Apex | 70.6 | 876 | 981 | rtx4090* | 4 | 54% |
| 6 | sn91 cascade | 69.1 | 569 | 2,299 | rtx4090* | 5 | 51% |
| 7 | sn15 ORO | 69.1 | 13.27 | 12,825 | cpu-small | 65 | 93% |
| 8 | sn96 Verathos | 68.9 | 25.28 | 382 | rtx4090 | 60 | 43% |
| 9 | sn56 Gradients | 68.7 | 502 | 960 | rtx4090* | 7 | 68% |
| 10 | sn41 Almanac | 68.7 | 9.64 | 53.60 | cpu-small | 75 | 70% |
| 11 | sn85 Vidaio | 68.6 | 493 | 493 = | rtx4090* | 10 | 16% |
| 12 | sn62 Ridges | 68.5 | 466 | 2,160 | rtx4090* | 6 | 40% |
| 13 | sn21 AdTAO | 67.7 | 7.66 | 34.32 | cpu-small | 88 | 45% |
| 14 | sn38 ChronoLLM | 66.1 | 101 | 1,379 | cpu-small | 10 | 52% |
| 15 | sn124 Swarm | 65.9 | 224 | 721 | rtx4090* | 24 | 11% |
| 16 | sn98 NeverPlayAlone | 64.1 | 1,695 | 1,695 = | cpu-small | 1 | 100% |
| 17 | sn2 DSperse | 61.9 | 65.58 | 229 | rtx4090* | 4 | 82% |
| 18 | sn55 NIOME | 61.5 | 57.79 | 487 | rtx4090* | 11 | 29% |
| 19 | sn60 Bitsec.ai | 59 | 373 | 373 = | cpu-small | 3 | 50% |
| 20 | sn74 Gittensor | 58.3 | 24.01 | 214 | rtx4090* | 14 | 63% |

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
| concentrated (30–60%) | 20 |
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

