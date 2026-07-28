# Subnet watch — dashboard

_snapshot 2026-07-28T16:57:54Z · block 8721800 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 51 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 91 | `miner_burn` < 0.99 |
| Ranked | 91 | passed every gate |
| **Positive margin** | **51** | income beats machine cost |
| New events this window | 6 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 57 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 8 | `████` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 8 | `████` |
| ≥0.99 dead | 37 | `██████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn67 Harnyx | 69 | 8.87 | 921 | cpu-small | 60 | 19% |
| 2 | sn85 Vidaio | 68.3 | 451 | 576 | rtx4090* | 10 | 19% |
| 3 | sn124 Swarm | 67.3 | 342 | 695 | rtx4090* | 16 | 13% |
| 4 | sn28 gm | 59.5 | 33.17 | 1,802 | rtx4090* | 10 | 63% |
| 5 | sn102 ConnitoAI | 56.7 | 12.94 | 1,293 | rtx4090* | 8 | 34% |
| 6 | sn23 Trishool | 52.3 | 997 | 997 = | cpu-small | 3 | 33% |
| 7 | sn71 Leadpoet | 50.8 | 1.44 | 297 | rtx4090* | 50 | 30% |
| 8 | sn120 Affine | 47.5 | 6,401 | 6,401 = | rtx4090* | 5 | 20% |
| 9 | sn4 Targon | 46 | 4,114 | 7,252 | rtx4090* | 8 | 30% |
| 10 | sn107 Minos | 42.1 | 89.19 | 26,521 | cpu-small | 20 | 90% |
| 11 | sn1 Apex | 41.5 | 1,065 | 2,004 | rtx4090* | 5 | 42% |
| 12 | sn74 Gittensor | 39.3 | -1.30 | 450 | rtx4090* | 60 | 17% |
| 13 | sn103 Djinn | 39.3 | -7.31 | -7.23 | rtx4090* | 250 | 79% |
| 14 | sn56 Gradients | 39.3 | -7.34 | 697 | rtx4090* | 22 | 71% |
| 15 | sn89 InfiniteQuant | 39.3 | -8.15 | 148 | rtx4090* | 34 | 44% |
| 16 | sn98 NeverPlayAlone | 38.5 | 170 | 170 = | cpu-small | 2 | 90% |
| 17 | sn77 Liquidity | 38.1 | 385 | 698 | rtx4090* | 11 | 19% |
| 18 | sn64 Chutes | 37.4 | 2,105 | 10,927 | a100-80 | 17 | 23% |
| 19 | sn101 Tag101 | 34.6 | 10.84 | 17.79 | cpu-small | 245 | 1% |
| 20 | sn96 Verathos | 34.1 | 27.57 | 162 | rtx4090 | 145 | 3% |

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
| dominated (60–90%) | 18 |
| captured (>90%) | 23 |

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
| 2026-07-28T12:59 | sn89 | SCORING_COMMIT | sn89 commit touches scoring: hf scoreboard: publish n_submitters_3d |
| 2026-07-28T12:10 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Verify durable chain settlement readback |
| 2026-07-28T11:29 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: Poll for validator image updates every tw |
| 2026-07-28T10:44 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

