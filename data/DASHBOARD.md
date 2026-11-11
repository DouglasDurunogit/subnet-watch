# Subnet watch — dashboard

_snapshot 2026-11-11T22:18:24Z · block 9485979 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 61 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 99 | `miner_burn` < 0.99 |
| Ranked | 99 | passed every gate |
| **Positive margin** | **61** | income beats machine cost |
| New events this window | 11 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 69 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 8 | `███` |
| 0.8–0.99 | 6 | `██` |
| ≥0.99 dead | 29 | `████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn104 TAOstatus | 77 | 2,342 | 2,342 = | cpu-small | 1 | 100% |
| 2 | sn120 Affine | 74.4 | 2,727 | 2,727 = | rtx4090* | 10 | 10% |
| 3 | sn3 Teutonic | 72.6 | 1,632 | 3,273 | rtx4090* | 7 | 25% |
| 4 | sn54 Yanez | 72.5 | 1,570 | 1,789 | a4000 | 3 | 54% |
| 5 | sn97 Ingot | 72.2 | 1,435 | 1,435 = | rtx4090* | 5 | 20% |
| 6 | sn56 Gradients | 70.5 | 870 | 4,586 | rtx4090* | 6 | 50% |
| 7 | sn41 Almanac | 70.2 | 14.11 | 161 | cpu-small | 161 | 5% |
| 8 | sn58 Attune | 69.4 | 628 | 1,010 | rtx4090* | 5 | 70% |
| 9 | sn67 Harnyx | 68.7 | 8.12 | 138 | cpu-small | 137 | 8% |
| 10 | sn103 Terza Inference | 67.7 | 376 | 448 | rtx4090* | 5 | 35% |
| 11 | sn46 Instant | 67.5 | 136 | 167 | cpu-small | 10 | 44% |
| 12 | sn124 Swarm | 67.3 | 338 | 1,781 | rtx4090* | 10 | 31% |
| 13 | sn15 ORO | 66.5 | 6.71 | 11,002 | cpu-small | 78 | 95% |
| 14 | sn82 Noah | 66.1 | 274 | 363 | rtx4090* | 66 | 2% |
| 15 | sn111 Claims | 65.5 | 196 | 1,780 | rtx4090* | 5 | 70% |
| 16 | sn53 engy | 65.1 | 169 | 909 | rtx4090 | 23 | 40% |
| 17 | sn14 Cacheon | 62.6 | 80.61 | 205 | rtx4090* | 4 | 95% |
| 18 | sn127 Zils | 62.3 | 73.71 | 73.71 = | rtx4090* | 4 | 88% |
| 19 | sn62 Ridges | 61 | 50.03 | 881 | rtx4090* | 41 | 18% |
| 20 | sn55 NIOME | 60.3 | 40.77 | 359 | rtx4090* | 11 | 30% |

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
| concentrated (30–60%) | 19 |
| dominated (60–90%) | 27 |
| captured (>90%) | 25 |

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
| 2026-11-11T22:18 | sn8 | SCORING_COMMIT | sn8 commit touches scoring: New regular miners (#975) |
| 2026-11-11T22:18 | sn12 | RELEASE | sn12 released validator-staging-2026-11-11-43092055737-629-1: fix: upg |
| 2026-11-11T22:18 | sn17 | SCORING_COMMIT | sn17 commit touches scoring: Publish verdicts and launch the next vali |
| 2026-11-11T22:18 | sn45 | SCORING_COMMIT | sn45 commit touches scoring: AlphaRidge 4.0.3: validator watchdog; the |
| 2026-11-11T22:18 | sn51 | RELEASE | sn51 released watchtower-v1.2.3 |
| 2026-11-11T22:18 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-6169 - Validator signs the whole requ |
| 2026-11-11T22:18 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: feat(validator): elastic bench host — ren |
| 2026-11-11T22:18 | sn111 | RELEASE | sn111 released v2.0.0 |
| 2026-11-11T22:18 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: Allocate competition weights to miners a |
| 2026-11-11T22:18 | sn126 | BURN_DROP | sn126 burn fell 1.000 -> 0.952 - miners can earn again |
| 2026-11-11T22:18 | sn127 | RELEASE | sn127 released Release f9174a9 |
| 2026-11-11T15:30 | sn17 | RELEASE | sn17 released Witness SDK 0.3.0 |
| 2026-11-11T15:30 | sn17 | SCORING_COMMIT | sn17 commit touches scoring: Run resumable candidate validation on Run |
| 2026-11-11T15:30 | sn51 | RELEASE | sn51 released watchtower-v1.2.2: DAH-5053: lium-watchtower 1.2.2, the  |
| 2026-11-11T15:30 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: Miner: name the executors a pubkey upload |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

