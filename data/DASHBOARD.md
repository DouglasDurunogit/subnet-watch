# Subnet watch — dashboard

_snapshot 2026-11-12T11:38:23Z · block 9489980 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 61 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 101 | `miner_burn` < 0.99 |
| Ranked | 101 | passed every gate |
| **Positive margin** | **61** | income beats machine cost |
| New events this window | 6 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 72 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 11 | `████` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 27 | `██████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn120 Affine | 74.2 | 2,616 | 2,616 = | rtx4090* | 10 | 10% |
| 2 | sn3 Teutonic | 72.5 | 1,559 | 3,125 | rtx4090* | 7 | 25% |
| 3 | sn97 Ingot | 72.1 | 1,378 | 1,378 = | rtx4090* | 5 | 20% |
| 4 | sn56 Gradients | 70.4 | 836 | 4,407 | rtx4090* | 6 | 50% |
| 5 | sn41 Almanac | 70.3 | 14.47 | 196 | cpu-small | 156 | 3% |
| 6 | sn34 Yugos | 69.9 | 737 | 6,331 | rtx4090* | 3 | 85% |
| 7 | sn58 Attune | 69.5 | 644 | 1,036 | rtx4090* | 5 | 70% |
| 8 | sn67 Harnyx | 68.5 | 7.74 | 132 | cpu-small | 137 | 8% |
| 9 | sn124 Swarm | 67.2 | 333 | 1,796 | rtx4090* | 10 | 31% |
| 10 | sn46 Instant | 67.2 | 126 | 188 | cpu-small | 10 | 42% |
| 11 | sn15 ORO | 65.7 | 6.51 | 10,617 | cpu-small | 72 | 95% |
| 12 | sn53 engy | 64.9 | 161 | 897 | rtx4090 | 23 | 40% |
| 13 | sn38 ChronoLLM | 63.6 | 53.37 | 367 | cpu-small | 9 | 52% |
| 14 | sn14 Cacheon | 62.4 | 77.23 | 197 | rtx4090* | 4 | 95% |
| 15 | sn127 Zils | 62.2 | 72.31 | 72.31 = | rtx4090* | 4 | 88% |
| 16 | sn62 Ridges | 60.9 | 47.67 | 845 | rtx4090* | 41 | 18% |
| 17 | sn55 NIOME | 60.3 | 40.79 | 359 | rtx4090* | 11 | 30% |
| 18 | sn4 Targon | 58.2 | 10,946 | 20,872 | rtx4090* | 5 | 60% |
| 19 | sn5 Hone | 57.7 | 21.69 | 46.33 | rtx4090* | 241 | 1% |
| 20 | sn117 everyframe.studi | 57.7 | 19.16 | 430 | rtx4090* | 40 | 28% |

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
| concentrated (30–60%) | 20 |
| dominated (60–90%) | 28 |
| captured (>90%) | 24 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 98 |
| README keywords (GUESS) | 12 |
| min_compute.yml (curated) | 9 |
| code-submission (validator runs it) | 8 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-11-12T11:38 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: docs(rewards): the 40-day count belongs t |
| 2026-11-12T11:38 | sn38 | README_TASK_DIFF | sn38 README task/scoring sections changed |
| 2026-11-12T11:38 | sn51 | RELEASE | sn51 released executor-v1.180 |
| 2026-11-12T11:38 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-6222 - [P1] Validator: a filler the v |
| 2026-11-12T11:38 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge pull request #1204 from leadpoet/fi |
| 2026-11-12T11:38 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: perf(audit): score drawn records ahead of |
| 2026-11-12T03:14 | sn17 | SCORING_COMMIT | sn17 commit touches scoring: Improve validation Pod recovery and place |
| 2026-11-12T03:14 | sn25 | README_TASK_DIFF | sn25 README task/scoring sections changed |
| 2026-11-12T03:14 | sn45 | SCORING_COMMIT | sn45 commit touches scoring: AlphaRidge 4.0.5: chain calls have a dead |
| 2026-11-12T03:14 | sn66 | RELEASE | sn66 released v2026.11.12.2 |
| 2026-11-12T03:14 | sn70 | RELEASE | sn70 released Fugal Subnet v0.3.2 |
| 2026-11-12T03:14 | sn70 | SCORING_COMMIT | sn70 commit touches scoring: release: v0.3.2 (validator-only collectio |
| 2026-11-12T03:14 | sn94 | BURN_DROP | sn94 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-11-12T03:14 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: Publish mainnet miner burn allocation po |
| 2026-11-12T03:14 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Merge miner app catalog practice-only (e |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

