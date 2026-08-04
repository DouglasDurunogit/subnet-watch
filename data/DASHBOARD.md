# Subnet watch — dashboard

_snapshot 2026-08-04T00:58:40Z · block 8767378 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 53 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 93 | `miner_burn` < 0.99 |
| Ranked | 93 | passed every gate |
| **Positive margin** | **53** | income beats machine cost |
| New events this window | 2 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 56 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 3 | `██` |
| 0.4–0.6 | 7 | `████` |
| 0.6–0.8 | 10 | `█████` |
| 0.8–0.99 | 11 | `██████` |
| ≥0.99 dead | 35 | `██████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn23 Trishool | 84.8 | 534 | 534 = | cpu-small | 5 | 20% |
| 2 | sn76 Phylax | 77.2 | 76.58 | 154 | cpu-small | 7 | 66% |
| 3 | sn107 Minos | 77.1 | 90.18 | 26,838 | cpu-small | 20 | 89% |
| 4 | sn60 Bitsec.ai | 76.4 | 1,935 | 1,935 = | cpu-small | 2 | 90% |
| 5 | sn98 NeverPlayAlone | 75.9 | 1,663 | 1,663 = | cpu-small | 1 | 100% |
| 6 | sn67 Harnyx | 73.3 | 28.85 | 736 | cpu-small | 129 | 18% |
| 7 | sn62 Ridges | 70 | 732 | 3,005 | rtx4090* | 7 | 39% |
| 8 | sn26 Perturb | 68.5 | 22.59 | 184 | rtx3060 | 11 | 50% |
| 9 | sn15 ORO | 67.4 | 8.23 | 17.12 | cpu-small | 86 | 93% |
| 10 | sn85 Vidaio | 66.8 | 285 | 499 | rtx4090* | 10 | 17% |
| 11 | sn124 Swarm | 66 | 232 | 678 | rtx4090* | 21 | 12% |
| 12 | sn74 Gittensor | 66 | 229 | 349 | rtx4090* | 8 | 18% |
| 13 | sn38 ChronoLLM | 65.4 | 197 | 3,315 | rtx4090* | 10 | 52% |
| 14 | sn21 AdTAO | 65.2 | 4.42 | 20.63 | cpu-small | 142 | 45% |
| 15 | sn53 engy | 64.1 | 126 | 2,957 | rtx4090 | 28 | 17% |
| 16 | sn41 Almanac | 58.5 | 1.31 | 66.43 | cpu-small | 34 | 93% |
| 17 | sn61 RedTeam | 58.2 | 21.24 | 75.24 | rtx4090* | 98 | 3% |
| 18 | sn28 gm | 56.3 | 13.05 | 2,595 | rtx4090* | 16 | 57% |
| 19 | sn9 iota | 55.2 | 8,653 | 8,653 = | rtx4090* | 3 | 50% |
| 20 | sn97 Albedo | 52.6 | 2,880 | 2,880 = | rtx4090* | 5 | 20% |

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
| wide (<30%) | 22 |
| concentrated (30–60%) | 22 |
| dominated (60–90%) | 21 |
| captured (>90%) | 27 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 104 |
| code-submission (validator runs it) | 9 |
| min_compute.yml (curated) | 9 |
| README keywords (GUESS) | 5 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-08-04T00:59 | sn61 | RELEASE | sn61 released 4.8.4 |
| 2026-08-04T00:59 | sn61 | SCORING_COMMIT | sn61 commit touches scoring: fix: handle miner hotkey changes in updat |
| 2026-08-03T23:17 | sn13 | RELEASE | sn13 released Release v1.18.69 |
| 2026-08-03T23:17 | sn54 | SCORING_COMMIT | sn54 commit touches scoring: Made miner process more Intuitive |
| 2026-08-03T20:39 | sn89 | SCORING_COMMIT | sn89 commit touches scoring: closers feed: per-key display-label overr |
| 2026-08-03T19:07 | sn80 | BURN_DROP | sn80 burn fell 1.000 -> 0.950 - miners can earn again |
| 2026-08-03T19:07 | sn112 | SCORING_COMMIT | sn112 commit touches scoring: chore(weights): champion burn 25% -> 80% |
| 2026-08-03T17:24 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: Add configurable PDF readers for claims  |
| 2026-08-03T17:24 | sn111 | README_TASK_DIFF | sn111 README task/scoring sections changed |
| 2026-08-03T17:24 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Refactor lora evaluation runtime (#603) |
| 2026-08-03T17:24 | sn120 | README_TASK_DIFF | sn120 README task/scoring sections changed |
| 2026-08-03T17:24 | sn121 | BURN_DROP | sn121 burn fell 1.000 -> 0.830 - miners can earn again |
| 2026-08-03T15:12 | sn14 | SCORING_COMMIT | sn14 commit touches scoring: Merge pull request #74 from latent-to/cod |
| 2026-08-03T15:12 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: fix(validator): resolve scoring to weekly |
| 2026-08-03T15:12 | sn28 | RELEASE | sn28 released v0.3.16 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

