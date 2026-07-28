# Subnet watch — dashboard

_snapshot 2026-07-28T11:16:50Z · block 8720095 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 53 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 91 | `miner_burn` < 0.99 |
| Ranked | 91 | passed every gate |
| **Positive margin** | **53** | income beats machine cost |
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
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 7 | `███` |
| 0.8–0.99 | 8 | `████` |
| ≥0.99 dead | 37 | `██████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn85 Vidaio | 67.9 | 400.00 | 528 | rtx4090* | 10 | 17% |
| 2 | sn68 NOVA | 54.5 | 6285.40 | 6285 | rtx4090* | 1 | 100% |
| 3 | sn67 Harnyx | 50.6 | 1.61 | 913 | rtx4090* | 60 | 19% |
| 4 | sn120 Affine | 47.4 | 6264.07 | 6264 | rtx4090* | 5 | 20% |
| 5 | sn4 Targon | 45.9 | 4044.16 | 7130 | rtx4090* | 8 | 30% |
| 6 | sn93 Bitcast | 43.8 | 69.46 | 69 | rtx4090* | 3 | 97% |
| 7 | sn114 SOMA | 42.7 | 1522.97 | 3973 | rtx4090* | 3 | 65% |
| 8 | sn107 Minos | 41.9 | 86.20 | 25530 | cpu-small | 20 | 91% |
| 9 | sn23 Trishool | 41.4 | 1029.85 | 1030 | rtx4090* | 3 | 33% |
| 10 | sn1 Apex | 41.3 | 1017.95 | 1871 | rtx4090* | 5 | 40% |
| 11 | sn89 InfiniteQuant | 39.3 | -8.15 | 147 | rtx4090* | 33 | 42% |
| 12 | sn44 Score | 39.3 | n/a | n/a | rtx4090* | 1 | 100% |
| 13 | sn77 Liquidity | 37.9 | 363.79 | 648 | rtx4090* | 11 | 18% |
| 14 | sn64 Chutes | 37.3 | 2032.07 | 10557 | a100-80 | 17 | 23% |
| 15 | sn124 Swarm | 37.3 | 311.31 | 491 | rtx4090* | 16 | 13% |
| 16 | sn96 Verathos | 34.5 | 29.22 | 166 | rtx4090 | 141 | 3% |
| 17 | sn101 Tag101 | 34.4 | 10.17 | 17 | cpu-small | 245 | 1% |
| 18 | sn38 ChronoLLM | 34 | 124.41 | 2789 | rtx4090* | 10 | 52% |
| 19 | sn55 NIOME | 33.8 | 108.47 | 303 | rtx4090* | 11 | 20% |
| 20 | sn17 404—GEN | 33.2 | 5543.47 | 5543 | rtx4090* | 1 | 100% |

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
| concentrated (30–60%) | 21 |
| dominated (60–90%) | 14 |
| captured (>90%) | 25 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 115 |
| min_compute.yml (curated) | 9 |
| README keywords (GUESS) | 3 |
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

