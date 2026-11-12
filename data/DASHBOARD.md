# Subnet watch — dashboard

_snapshot 2026-11-12T03:13:42Z · block 9487456 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 63 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 99 | `miner_burn` < 0.99 |
| Ranked | 99 | passed every gate |
| **Positive margin** | **63** | income beats machine cost |
| New events this window | 9 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 68 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 8 | `███` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 29 | `████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn120 Affine | 74.3 | 2,658 | 2,658 = | rtx4090* | 10 | 10% |
| 2 | sn3 Teutonic | 72.5 | 1,593 | 3,194 | rtx4090* | 7 | 25% |
| 3 | sn54 Yanez | 72.5 | 1,547 | 1,737 | a4000 | 3 | 53% |
| 4 | sn97 Ingot | 72.1 | 1,400 | 1,400 = | rtx4090* | 5 | 20% |
| 5 | sn56 Gradients | 70.5 | 849 | 4,477 | rtx4090* | 6 | 50% |
| 6 | sn41 Almanac | 69.8 | 12.89 | 197 | cpu-small | 162 | 3% |
| 7 | sn58 Attune | 69.4 | 628 | 1,010 | rtx4090* | 5 | 70% |
| 8 | sn67 Harnyx | 68.6 | 7.89 | 135 | cpu-small | 137 | 8% |
| 9 | sn46 Instant | 67.4 | 132 | 160 | cpu-small | 10 | 42% |
| 10 | sn124 Swarm | 67.2 | 328 | 1,766 | rtx4090* | 10 | 31% |
| 11 | sn103 Terza Inference | 67 | 300 | 378 | rtx4090* | 5 | 39% |
| 12 | sn15 ORO | 66.7 | 6.71 | 10,718 | cpu-small | 80 | 95% |
| 13 | sn82 Noah | 66 | 261 | 351 | rtx4090* | 67 | 2% |
| 14 | sn53 engy | 64.9 | 159 | 889 | rtx4090 | 23 | 40% |
| 15 | sn14 Cacheon | 62.5 | 78.38 | 199 | rtx4090* | 4 | 95% |
| 16 | sn127 Zils | 62.1 | 70.37 | 70.37 = | rtx4090* | 4 | 88% |
| 17 | sn62 Ridges | 60.9 | 48.63 | 860 | rtx4090* | 41 | 18% |
| 18 | sn55 NIOME | 60.3 | 40.06 | 354 | rtx4090* | 11 | 30% |
| 19 | sn60 Bitsec.ai | 59.3 | 408 | 629 | cpu-small | 3 | 50% |
| 20 | sn4 Targon | 58.3 | 11,170 | 21,285 | rtx4090* | 5 | 60% |

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
| dominated (60–90%) | 25 |
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
| 2026-11-12T03:14 | sn17 | SCORING_COMMIT | sn17 commit touches scoring: Improve validation Pod recovery and place |
| 2026-11-12T03:14 | sn25 | README_TASK_DIFF | sn25 README task/scoring sections changed |
| 2026-11-12T03:14 | sn45 | SCORING_COMMIT | sn45 commit touches scoring: AlphaRidge 4.0.5: chain calls have a dead |
| 2026-11-12T03:14 | sn66 | RELEASE | sn66 released v2026.11.12.2 |
| 2026-11-12T03:14 | sn70 | RELEASE | sn70 released Fugal Subnet v0.3.2 |
| 2026-11-12T03:14 | sn70 | SCORING_COMMIT | sn70 commit touches scoring: release: v0.3.2 (validator-only collectio |
| 2026-11-12T03:14 | sn94 | BURN_DROP | sn94 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-11-12T03:14 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: Publish mainnet miner burn allocation po |
| 2026-11-12T03:14 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Merge miner app catalog practice-only (e |
| 2026-11-11T22:18 | sn8 | SCORING_COMMIT | sn8 commit touches scoring: New regular miners (#975) |
| 2026-11-11T22:18 | sn12 | RELEASE | sn12 released validator-staging-2026-11-11-43092055737-629-1: fix: upg |
| 2026-11-11T22:18 | sn17 | SCORING_COMMIT | sn17 commit touches scoring: Publish verdicts and launch the next vali |
| 2026-11-11T22:18 | sn45 | SCORING_COMMIT | sn45 commit touches scoring: AlphaRidge 4.0.3: validator watchdog; the |
| 2026-11-11T22:18 | sn51 | RELEASE | sn51 released watchtower-v1.2.3 |
| 2026-11-11T22:18 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-6169 - Validator signs the whole requ |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

