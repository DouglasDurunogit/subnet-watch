# Subnet watch — dashboard

_snapshot 2026-08-15T13:38:46Z · block 8850364 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 50 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 89 | `miner_burn` < 0.99 |
| Ranked | 89 | passed every gate |
| **Positive margin** | **50** | income beats machine cost |
| New events this window | 2 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 61 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 3 | `█` |
| 0.4–0.6 | 8 | `████` |
| 0.6–0.8 | 4 | `██` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 39 | `██████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 78 | 109 | 31,916 | cpu-small | 20 | 90% |
| 2 | sn76 Phylax | 74.7 | 40.46 | 194 | cpu-small | 10 | 35% |
| 3 | sn67 Harnyx | 72.5 | 23.30 | 375 | cpu-small | 123 | 10% |
| 4 | sn26 Perturb | 70.9 | 41.28 | 75.25 | rtx3060 | 10 | 70% |
| 5 | sn1 Apex | 70.6 | 874 | 1,146 | rtx4090* | 4 | 54% |
| 6 | sn6 Numinous | 70.3 | 15.79 | 442 | cpu-small | 15 | 26% |
| 7 | sn41 Almanac | 69.6 | 12.11 | 53.86 | cpu-small | 72 | 66% |
| 8 | sn56 Gradients | 68.8 | 512 | 964 | rtx4090* | 7 | 67% |
| 9 | sn96 Verathos | 68.8 | 24.95 | 158 | rtx4090 | 64 | 41% |
| 10 | sn62 Ridges | 68.6 | 486 | 2,248 | rtx4090* | 6 | 40% |
| 11 | sn91 cascade | 68.5 | 481 | 1,117 | rtx4090* | 5 | 50% |
| 12 | sn15 ORO | 67.8 | 11.09 | 20.37 | cpu-small | 85 | 93% |
| 13 | sn21 AdTAO | 67.6 | 7.61 | 34.13 | cpu-small | 88 | 45% |
| 14 | sn85 Vidaio | 66.4 | 251 | 512 | rtx4090* | 10 | 17% |
| 15 | sn38 ChronoLLM | 66 | 97.57 | 1,334 | cpu-small | 10 | 52% |
| 16 | sn124 Swarm | 65.9 | 224 | 719 | rtx4090* | 24 | 11% |
| 17 | sn55 NIOME | 61.4 | 56.69 | 479 | rtx4090* | 11 | 29% |
| 18 | sn28 gm | 61 | 51.26 | 2,449 | rtx4090* | 36 | 27% |
| 19 | sn60 Bitsec.ai | 59.5 | 430 | 430 = | cpu-small | 3 | 50% |
| 20 | sn74 Gittensor | 57.7 | 20.27 | 213 | rtx4090* | 15 | 64% |

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
| concentrated (30–60%) | 19 |
| dominated (60–90%) | 17 |
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
| 2026-08-15T13:39 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: fix(prism): rename lattice_score to sati |
| 2026-08-15T12:56 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: feat(prism): live leaf from G2 benchmark |
| 2026-08-15T09:06 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-08-15T09:06 | sn67 | README_TASK_DIFF | sn67 README task/scoring sections changed |
| 2026-08-15T04:45 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-08-15T04:05 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Provision hotkey verification in gateway  |
| 2026-08-15T04:05 | sn108 | SCORING_COMMIT | sn108 commit touches scoring: feat(registry): require every evaluated  |
| 2026-08-15T03:25 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: chore(deploy): promote prod prism-challe |
| 2026-08-15T01:47 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Keep private ICP scores out of telemetry |
| 2026-08-14T23:33 | sn2 | BURN_DROP | sn2 burn fell 1.000 -> 0.824 - miners can earn again |
| 2026-08-14T23:33 | sn19 | BURN_DROP | sn19 burn fell 1.000 -> 0.986 - miners can earn again |
| 2026-08-14T22:36 | sn62 | RELEASE | sn62 released v0.2.7 |
| 2026-08-14T20:17 | sn55 | SCORING_COMMIT | sn55 commit touches scoring: commit weights after validation |
| 2026-08-14T20:17 | sn96 | RELEASE | sn96 released Verathos v0.1.40 — Capacity Audit Scheduling Stability |
| 2026-08-14T19:29 | sn121 | README_TASK_DIFF | sn121 README task/scoring sections changed |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

