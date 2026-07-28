# Subnet watch — dashboard

_snapshot 2026-07-28T12:08:40Z · block 8720354 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 51 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 90 | `miner_burn` < 0.99 |
| Ranked | 90 | passed every gate |
| **Positive margin** | **51** | income beats machine cost |
| New events this window | 2 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 58 | `████████████████████████████` |
| 0–0.2 | 4 | `██` |
| 0.2–0.4 | 8 | `████` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 38 | `██████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn67 Harnyx | 69 | 8.88 | 923 | cpu-small | 60 | 19% |
| 2 | sn85 Vidaio | 67.9 | 398.09 | 529 | rtx4090* | 10 | 17% |
| 3 | sn23 Trishool | 52.5 | 1044.16 | 1044 | cpu-small | 3 | 33% |
| 4 | sn71 Leadpoet | 50.3 | 1.13 | 287 | rtx4090* | 50 | 30% |
| 5 | sn11 TrajectoryRL | 50 | 5278.20 | 5278 | cpu-small | 1 | 100% |
| 6 | sn120 Affine | 47.4 | 6289.69 | 6290 | rtx4090* | 5 | 20% |
| 7 | sn4 Targon | 46 | 4063.60 | 7164 | rtx4090* | 8 | 30% |
| 8 | sn114 SOMA | 42.7 | 1528.69 | 3988 | rtx4090* | 3 | 65% |
| 9 | sn107 Minos | 42.1 | 89.01 | 25266 | cpu-small | 20 | 90% |
| 10 | sn1 Apex | 41.5 | 1088.32 | 1911 | rtx4090* | 5 | 41% |
| 11 | sn102 ConnitoAI | 40.4 | 773.79 | 1201 | rtx4090* | 6 | 32% |
| 12 | sn98 NeverPlayAlone | 38 | 148.87 | 149 | cpu-small | 2 | 91% |
| 13 | sn77 Liquidity | 37.9 | 365.18 | 651 | rtx4090* | 11 | 18% |
| 14 | sn64 Chutes | 37.3 | 2054.66 | 10632 | a100-80 | 17 | 23% |
| 15 | sn124 Swarm | 37.2 | 306.40 | 484 | rtx4090* | 16 | 13% |
| 16 | sn96 Verathos | 34.5 | 29.29 | 170 | rtx4090 | 143 | 3% |
| 17 | sn101 Tag101 | 34.3 | 9.88 | 17 | cpu-small | 244 | 1% |
| 18 | sn38 ChronoLLM | 33.9 | 123.39 | 2767 | rtx4090* | 10 | 52% |
| 19 | sn55 NIOME | 33.8 | 108.56 | 303 | rtx4090* | 11 | 20% |
| 20 | sn68 NOVA | 33.5 | 6296.16 | 6296 | rtx4090* | 1 | 100% |

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
| dominated (60–90%) | 15 |
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
| 2026-07-28T12:10 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Verify durable chain settlement readback |
| 2026-07-28T11:29 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: Poll for validator image updates every tw |
| 2026-07-28T10:44 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-07-28T10:44 | sn67 | README_TASK_DIFF | sn67 README task/scoring sections changed |
| 2026-07-28T10:44 | sn117 | BURN_DROP | sn117 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-07-28T08:08 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: Read served ground truth so findings are  |
| 2026-07-28T07:30 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: Skip tracks with no task set instead of a |
| 2026-07-28T07:30 | sn85 | SCORING_COMMIT | sn85 commit touches scoring: defer scoring commit to DB (#180) |
| 2026-07-28T07:30 | sn104 | BURN_DROP | sn104 burn fell 1.000 -> 0.965 - miners can earn again |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

