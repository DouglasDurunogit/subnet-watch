# Subnet watch — dashboard

_snapshot 2026-07-28T10:43:35Z · block 8719929 · run_status **ok**_

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
| New events this window | 3 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 59 | `████████████████████████████` |
| 0–0.2 | 3 | `█` |
| 0.2–0.4 | 8 | `████` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 8 | `████` |
| ≥0.99 dead | 37 | `██████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day | machine | burn | earners | top-1 share |
|---:|---|---:|---:|---|---:|---:|---:|
| 1 | sn67 Harnyx | 70.7 | 900.65 | rtx4090* | 0.58 | 60 | 58% |
| 2 | sn85 Vidaio | 69.9 | 716.46 | rtx4090* | 0.00 | 10 | 23% |
| 3 | sn107 Minos | 65 | 25178.00 | cpu-small | 0.00 | 20 | 91% |
| 4 | sn9 iota | 52.4 | 2640.19 | a4000 | 0.80 | 3 | 80% |
| 5 | sn79 MVTRX | 50.8 | 683.84 | cpu-small | 0.00 | 215 | 16% |
| 6 | sn15 ORO | 49 | 10191.60 | rtx4090* | 0.00 | 81 | 93% |
| 7 | sn54 Yanez MIID | 48 | 883.33 | a4000 | 0.30 | 103 | 35% |
| 8 | sn53 engy | 47.9 | 2766.56 | cpu-small | 0.00 | 38 | 18% |
| 9 | sn4 Targon | 47.8 | 7126.78 | rtx4090* | 0.00 | 8 | 30% |
| 10 | sn68 NOVA | 47.4 | 6314.32 | rtx4090* | 0.00 | 1 | 100% |
| 11 | sn120 Affine | 47.4 | 6260.16 | rtx4090* | 0.00 | 5 | 20% |
| 12 | sn11 TrajectoryRL | 46.8 | 5256.36 | rtx4090* | 0.00 | 1 | 100% |
| 13 | sn114 SOMA | 45.9 | 4032.65 | rtx4090* | 0.00 | 3 | 65% |
| 14 | sn51 lium.io | 45.5 | 3565.38 | rtx4090* | 0.00 | 40 | 63% |
| 15 | sn91 cascade | 45.2 | 3258.51 | rtx4090* | 0.00 | 3 | 54% |
| 16 | sn38 ChronoLLM | 44.7 | 2797.77 | rtx4090* | 0.00 | 10 | 52% |
| 17 | sn78 Vocence | 43.8 | 2151.59 | rtx4090* | 0.00 | 1 | 100% |
| 18 | sn1 Apex | 43.4 | 1884.13 | rtx4090* | 0.15 | 5 | 40% |
| 19 | sn63 Enigma | 43.3 | 4528.99 | h200-141 | 0.00 | 3 | 100% |
| 20 | sn102 ConnitoAI | 43 | 1678.34 | rtx4090* | 0.25 | 6 | 44% |

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
| no evidence | 102 |
| README keywords (GUESS) | 12 |
| min_compute.yml (curated) | 9 |
| README stated VRAM (explicit) | 5 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-07-28T10:44 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-07-28T10:44 | sn67 | README_TASK_DIFF | sn67 README task/scoring sections changed |
| 2026-07-28T10:44 | sn117 | BURN_DROP | sn117 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-07-28T08:08 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: Read served ground truth so findings are  |
| 2026-07-28T07:30 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: Skip tracks with no task set instead of a |
| 2026-07-28T07:30 | sn85 | SCORING_COMMIT | sn85 commit touches scoring: defer scoring commit to DB (#180) |
| 2026-07-28T07:30 | sn104 | BURN_DROP | sn104 burn fell 1.000 -> 0.965 - miners can earn again |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

