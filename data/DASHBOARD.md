# Subnet watch — dashboard

_snapshot 2026-08-19T20:02:23Z · block 8881082 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 54 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 91 | `miner_burn` < 0.99 |
| Ranked | 91 | passed every gate |
| **Positive margin** | **54** | income beats machine cost |
| New events this window | 9 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 61 | `████████████████████████████` |
| 0–0.2 | 4 | `██` |
| 0.2–0.4 | 7 | `███` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 37 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 76.6 | 65.11 | 115 | cpu-small | 13 | 20% |
| 2 | sn121 sundae_bar | 74.5 | 1,089 | 1,089 = | cpu-small | 2 | 60% |
| 3 | sn62 Ridges | 72.5 | 1,563 | 4,139 | rtx4090* | 3 | 59% |
| 4 | sn67 Harnyx | 72.3 | 22.51 | 301 | cpu-small | 147 | 9% |
| 5 | sn23 Trishool | 71.9 | 507 | 507 = | cpu-small | 2 | 80% |
| 6 | sn26 Perturb | 70.9 | 41.15 | 75.45 | rtx3060 | 10 | 70% |
| 7 | sn15 ORO | 69.7 | 15.94 | 15,321 | cpu-small | 84 | 92% |
| 8 | sn56 Gradients | 69.5 | 638 | 965 | rtx4090* | 5 | 72% |
| 9 | sn91 cascade | 69.2 | 578 | 2,335 | rtx4090* | 5 | 52% |
| 10 | sn38 ChronoLLM | 67.5 | 146 | 3,092 | cpu-small | 10 | 52% |
| 11 | sn96 Verathos | 66.3 | 13.52 | 350 | rtx4090 | 89 | 41% |
| 12 | sn41 Almanac | 65.9 | 5.14 | 31.41 | cpu-small | 74 | 82% |
| 13 | sn85 Vidaio | 64 | 124 | 188 | rtx4090* | 13 | 42% |
| 14 | sn107 Minos | 62.9 | 87.15 | 36,478 | cpu-small | 17 | 93% |
| 15 | sn55 NIOME | 61.4 | 56.43 | 479 | rtx4090* | 11 | 29% |
| 16 | sn51 lium.io | 61.2 | 60.20 | 1,008 | rtx4090* | 51 | 79% |
| 17 | sn81 Reliquary | 61 | 50.20 | 199 | rtx4090* | 56 | 5% |
| 18 | sn28 gm | 60.2 | 40.62 | 1,216 | rtx4090* | 50 | 27% |
| 19 | sn53 engy | 59.8 | 34.70 | 12,076 | rtx4090 | 144 | 63% |
| 20 | sn21 AdTAO | 58.4 | 1.34 | 373 | cpu-small | 16 | 37% |

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
| concentrated (30–60%) | 18 |
| dominated (60–90%) | 18 |
| captured (>90%) | 28 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 101 |
| code-submission (validator runs it) | 10 |
| min_compute.yml (curated) | 10 |
| README keywords (GUESS) | 6 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-08-19T20:02 | sn25 | RELEASE | sn25 released v2026.8.19-1023689220 |
| 2026-08-19T20:02 | sn51 | RELEASE | sn51 released executor-v1.123 |
| 2026-08-19T20:02 | sn66 | README_TASK_DIFF | sn66 README task/scoring sections changed |
| 2026-08-19T20:02 | sn108 | SCORING_COMMIT | sn108 commit touches scoring: feat!: validators run miners' models; re |
| 2026-08-19T19:35 | sn46 | SCORING_COMMIT | sn46 commit touches scoring: Restore validator log visibility after th |
| 2026-08-19T18:50 | sn10 | README_TASK_DIFF | sn10 README task/scoring sections changed |
| 2026-08-19T18:50 | sn46 | SCORING_COMMIT | sn46 commit touches scoring: Merge pull request #21 from instant-subne |
| 2026-08-19T18:50 | sn90 | README_TASK_DIFF | sn90 README task/scoring sections changed |
| 2026-08-19T18:50 | sn103 | BURN_DROP | sn103 burn fell 1.000 -> 0.845 - miners can earn again |
| 2026-08-19T18:02 | sn1 | RELEASE | sn1 released v4.3.4 |
| 2026-08-19T16:56 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Retry pinned validator yum installs safel |
| 2026-08-19T16:12 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: feat(scoring): bound eligible claims and |
| 2026-08-19T15:42 | sn108 | SCORING_COMMIT | sn108 commit touches scoring: feat(miner): refuse an architecture the  |
| 2026-08-19T14:49 | sn108 | SCORING_COMMIT | sn108 commit touches scoring: docs(miner): say which architectures the |
| 2026-08-19T13:56 | sn14 | RELEASE | sn14 released v2.1.0 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

