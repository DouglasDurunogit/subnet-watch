# Subnet watch — dashboard

_snapshot 2026-07-28T10:55:40Z · block 8719989 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 71 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 91 | `miner_burn` < 0.99 |
| Ranked | 91 | passed every gate |
| **Positive margin** | **71** | income beats machine cost |
| New events this window | 9 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 59 | `████████████████████████████` |
| 0–0.2 | 4 | `██` |
| 0.2–0.4 | 8 | `████` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 7 | `███` |
| 0.8–0.99 | 9 | `████` |
| ≥0.99 dead | 37 | `██████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day | machine | burn | earners | top-1 share |
|---:|---|---:|---:|---|---:|---:|---:|
| 1 | sn68 NOVA | 77.2 | 6308.20 | rtx4090* | 0.00 | 1 | 100% |
| 2 | sn67 Harnyx | 70.7 | 915.96 | rtx4090* | 0.09 | 60 | 19% |
| 3 | sn85 Vidaio | 68.9 | 532.96 | rtx4090* | 0.00 | 10 | 17% |
| 4 | sn107 Minos | 65 | 25185.30 | cpu-small | 0.00 | 20 | 91% |
| 5 | sn89 InfiniteQuant | 64.6 | 147.72 | rtx4090* | 0.71 | 33 | 42% |
| 6 | sn93 Bitcast | 62.1 | 69.75 | rtx4090* | 0.81 | 3 | 97% |
| 7 | sn79 MVTRX | 50 | 566.53 | cpu-small | 0.00 | 214 | 13% |
| 8 | sn15 ORO | 49 | 10144.90 | rtx4090* | 0.00 | 81 | 93% |
| 9 | sn54 Yanez MIID | 48 | 882.38 | a4000 | 0.30 | 103 | 35% |
| 10 | sn4 Targon | 47.9 | 7128.64 | rtx4090* | 0.00 | 8 | 30% |
| 11 | sn120 Affine | 47.4 | 6264.51 | rtx4090* | 0.00 | 5 | 20% |
| 12 | sn17 404—GEN | 47 | 5572.19 | rtx4090* | 0.00 | 1 | 100% |
| 13 | sn11 TrajectoryRL | 46.8 | 5257.04 | rtx4090* | 0.00 | 1 | 100% |
| 14 | sn63 Enigma | 46.4 | 4600.27 | rtx4090* | 0.00 | 3 | 100% |
| 15 | sn114 SOMA | 45.9 | 4029.66 | rtx4090* | 0.00 | 3 | 65% |
| 16 | sn51 lium.io | 45.6 | 3605.73 | rtx4090* | 0.00 | 40 | 63% |
| 17 | sn91 cascade | 45.2 | 3278.25 | rtx4090* | 0.00 | 3 | 54% |
| 18 | sn38 ChronoLLM | 44.7 | 2798.37 | rtx4090* | 0.00 | 10 | 52% |
| 19 | sn9 iota | 44.5 | 2639.60 | rtx4090* | 0.80 | 3 | 80% |
| 20 | sn78 Vocence | 43.8 | 2145.53 | rtx4090* | 0.00 | 1 | 100% |

`*` = machine is an assumed default; no hardware evidence was found for that subnet.

![top 20 by score](charts/top20.svg)

## Concentration — reported, never scored

A low top-1 share means many miners share the emission. A high one means a
single UID takes almost everything, so the headline income is not reachable.
**This is deliberately excluded from the score** — judge the shape yourself.

| top-1 share | subnets (of those that pay) |
|---|---:|
| wide (<30%) | 29 |
| concentrated (30–60%) | 19 |
| dominated (60–90%) | 14 |
| captured (>90%) | 26 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 114 |
| min_compute.yml (curated) | 9 |
| README keywords (GUESS) | 4 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-07-28T10:56 | sn44 | MECHANISM_ADDED | sn44 now runs 2 incentive mechanisms (was 1) |
| 2026-07-28T10:56 | sn68 | MECHANISM_ADDED | sn68 now runs 2 incentive mechanisms (was 1) |
| 2026-07-28T10:56 | sn87 | MECHANISM_ADDED | sn87 now runs 2 incentive mechanisms (was 1) |
| 2026-07-28T10:56 | sn89 | MECHANISM_ADDED | sn89 now runs 2 incentive mechanisms (was 1) |
| 2026-07-28T10:56 | sn93 | MECHANISM_ADDED | sn93 now runs 2 incentive mechanisms (was 1) |
| 2026-07-28T10:56 | sn113 | MECHANISM_ADDED | sn113 now runs 2 incentive mechanisms (was 1) |
| 2026-07-28T10:44 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-07-28T10:44 | sn67 | README_TASK_DIFF | sn67 README task/scoring sections changed |
| 2026-07-28T10:44 | sn117 | BURN_DROP | sn117 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-07-28T08:08 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: Read served ground truth so findings are  |
| 2026-07-28T07:30 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: Skip tracks with no task set instead of a |
| 2026-07-28T07:30 | sn85 | SCORING_COMMIT | sn85 commit touches scoring: defer scoring commit to DB (#180) |
| 2026-07-28T07:30 | sn104 | BURN_DROP | sn104 burn fell 1.000 -> 0.965 - miners can earn again |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

