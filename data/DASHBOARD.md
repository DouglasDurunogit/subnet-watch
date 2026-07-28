# Subnet watch — dashboard

_snapshot 2026-07-28T08:46:51Z · block 8719345 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 71 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 90 | `miner_burn` < 0.99 |
| Ranked | 90 | passed every gate |
| **Positive margin** | **71** | income beats machine cost |
| New events this window | 1 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 58 | `████████████████████████████` |
| 0–0.2 | 4 | `██` |
| 0.2–0.4 | 7 | `███` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 7 | `███` |
| 0.8–0.99 | 9 | `████` |
| ≥0.99 dead | 38 | `██████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day | machine | burn | earners | top-1 share |
|---:|---|---:|---:|---|---:|---:|---:|
| 1 | sn85 Vidaio | 69.2 | 580.33 | rtx4090* | 0.00 | 10 | 18% |
| 2 | sn107 Minos | 64.9 | 24549.70 | cpu-small | 0.00 | 20 | 90% |
| 3 | sn9 iota | 52.3 | 2625.42 | a4000 | 0.80 | 3 | 80% |
| 4 | sn79 MVTRX | 50.9 | 698.38 | cpu-small | 0.00 | 219 | 16% |
| 5 | sn15 ORO | 49 | 9956.10 | rtx4090* | 0.00 | 81 | 93% |
| 6 | sn54 Yanez MIID | 48.1 | 902.38 | a4000 | 0.31 | 104 | 35% |
| 7 | sn4 Targon | 48 | 7378.70 | rtx4090* | 0.00 | 7 | 37% |
| 8 | sn53 engy | 47.7 | 2624.59 | cpu-small | 0.00 | 38 | 18% |
| 9 | sn68 NOVA | 47.4 | 6301.42 | rtx4090* | 0.00 | 1 | 100% |
| 10 | sn120 Affine | 47.3 | 6149.37 | rtx4090* | 0.00 | 5 | 20% |
| 11 | sn11 TrajectoryRL | 46.8 | 5226.51 | rtx4090* | 0.00 | 1 | 100% |
| 12 | sn114 SOMA | 46.1 | 4231.35 | rtx4090* | 0.00 | 3 | 65% |
| 13 | sn91 cascade | 45.3 | 3329.67 | rtx4090* | 0.00 | 3 | 54% |
| 14 | sn51 lium.io | 45.3 | 3313.41 | rtx4090* | 0.00 | 39 | 63% |
| 15 | sn38 ChronoLLM | 45.1 | 3187.67 | rtx4090* | 0.00 | 10 | 52% |
| 16 | sn82 Compelle | 44.9 | 2934.76 | rtx4090* | 0.00 | 1 | 100% |
| 17 | sn78 Vocence | 44 | 2239.10 | rtx4090* | 0.00 | 1 | 100% |
| 18 | sn28 gm | 43.5 | 1951.15 | rtx4090* | 0.64 | 9 | 64% |
| 19 | sn1 Apex | 43.4 | 1899.96 | rtx4090* | 0.14 | 5 | 41% |
| 20 | sn63 Enigma | 43.2 | 4521.77 | h200-141 | 0.00 | 3 | 100% |

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
| dominated (60–90%) | 14 |
| captured (>90%) | 25 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 102 |
| README keywords (GUESS) | 12 |
| min_compute.yml (curated) | 9 |
| README stated VRAM (explicit) | 5 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-07-28T08:08 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: Read served ground truth so findings are  |
| 2026-07-28T07:30 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: Skip tracks with no task set instead of a |
| 2026-07-28T07:30 | sn85 | SCORING_COMMIT | sn85 commit touches scoring: defer scoring commit to DB (#180) |
| 2026-07-28T07:30 | sn104 | BURN_DROP | sn104 burn fell 1.000 -> 0.965 - miners can earn again |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

