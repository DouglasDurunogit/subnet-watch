# Subnet watch — dashboard

_snapshot 2026-07-28T18:40:00Z · block 8722311 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 50 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 92 | `miner_burn` < 0.99 |
| Ranked | 92 | passed every gate |
| **Positive margin** | **50** | income beats machine cost |
| New events this window | 4 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 57 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 7 | `███` |
| 0.4–0.6 | 7 | `███` |
| 0.6–0.8 | 7 | `███` |
| 0.8–0.99 | 9 | `████` |
| ≥0.99 dead | 36 | `██████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 76.2 | 1,820 | 1,820 = | cpu-small | 1 | 100% |
| 2 | sn102 ConnitoAI | 70.8 | 945 | 945 = | rtx4090* | 4 | 25% |
| 3 | sn85 Vidaio | 68.9 | 541 | 545 | rtx4090* | 10 | 18% |
| 4 | sn67 Harnyx | 68.8 | 8.54 | 890 | cpu-small | 60 | 19% |
| 5 | sn98 NeverPlayAlone | 68.6 | 191 | 191 = | cpu-small | 2 | 89% |
| 6 | sn124 Swarm | 67.3 | 341 | 693 | rtx4090* | 16 | 13% |
| 7 | sn28 gm | 61.5 | 60.14 | 2,016 | rtx4090* | 9 | 60% |
| 8 | sn23 Trishool | 52.2 | 969 | 969 = | cpu-small | 3 | 33% |
| 9 | sn71 Leadpoet | 51.3 | 1.84 | 307 | rtx4090* | 50 | 30% |
| 10 | sn120 Affine | 47.5 | 6,371 | 6,371 = | rtx4090* | 5 | 20% |
| 11 | sn4 Targon | 46 | 4,071 | 7,177 | rtx4090* | 8 | 32% |
| 12 | sn107 Minos | 42 | 87.41 | 26,500 | cpu-small | 20 | 90% |
| 13 | sn1 Apex | 41.4 | 1,037 | 2,102 | rtx4090* | 5 | 44% |
| 14 | sn74 Gittensor | 39.3 | -2.06 | 278 | rtx4090* | 55 | 26% |
| 15 | sn103 Djinn | 39.3 | -7.33 | -7.22 | rtx4090* | 250 | 79% |
| 16 | sn56 Gradients | 39.3 | -7.34 | 695 | rtx4090* | 22 | 71% |
| 17 | sn89 InfiniteQuant | 39.3 | -8.15 | 148 | rtx4090* | 34 | 43% |
| 18 | sn77 Liquidity | 38.1 | 387 | 686 | rtx4090* | 11 | 19% |
| 19 | sn64 Chutes | 37.3 | 2,049 | 10,832 | a100-80 | 17 | 23% |
| 20 | sn101 Tag101 | 34.7 | 11.05 | 17.52 | cpu-small | 245 | 1% |

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
| concentrated (30–60%) | 22 |
| dominated (60–90%) | 14 |
| captured (>90%) | 26 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 107 |
| min_compute.yml (curated) | 9 |
| code-submission (validator runs it) | 8 |
| README keywords (GUESS) | 3 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-07-28T18:40 | sn69 | SCORING_COMMIT | sn69 commit touches scoring: Add miner/validator operator guides + val |
| 2026-07-28T18:40 | sn76 | BURN_DROP | sn76 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-07-28T18:40 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: Stop counting unrunnable tasks as wrong a |
| 2026-07-28T18:40 | sn98 | SCORING_COMMIT | sn98 commit touches scoring: feat: auto-prune old validator round work |
| 2026-07-28T16:58 | sn55 | BURN_DROP | sn55 burn fell 1.000 -> 0.020 - miners can earn again |
| 2026-07-28T16:58 | sn74 | RELEASE | sn74 released release-20260728-153232: chore(weights): zero metagraphe |
| 2026-07-28T16:58 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: Pay the reserved share in full from the f |
| 2026-07-28T16:58 | sn102 | RELEASE | sn102 released v0.3.2 |
| 2026-07-28T16:58 | sn102 | SCORING_COMMIT | sn102 commit touches scoring: 📊 telemetry: per-round baseline loss (va |
| 2026-07-28T16:58 | sn124 | SCORING_COMMIT | sn124 commit touches scoring: Start evaluation at the full worker widt |
| 2026-07-28T15:04 | sn28 | RELEASE | sn28 released v0.3.12 |
| 2026-07-28T15:04 | sn56 | SCORING_COMMIT | sn56 commit touches scoring: feat(validator): auto-balance emission sp |
| 2026-07-28T15:04 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: Retry validator self registration until i |
| 2026-07-28T15:04 | sn103 | RELEASE | sn103 released v2003: validator: restore miner burn fraction to 0.8 |
| 2026-07-28T15:04 | sn103 | SCORING_COMMIT | sn103 commit touches scoring: validator: restore miner burn fraction t |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

