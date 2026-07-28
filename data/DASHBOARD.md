# Subnet watch — dashboard

_snapshot 2026-07-28T12:59:03Z · block 8720606 · run_status **ok**_

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
| 0 (none) | 57 | `████████████████████████████` |
| 0–0.2 | 4 | `██` |
| 0.2–0.4 | 8 | `████` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 8 | `████` |
| ≥0.99 dead | 38 | `███████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn67 Harnyx | 68.9 | 8.89 | 924 | cpu-small | 60 | 19% |
| 2 | sn85 Vidaio | 67.9 | 399 | 530 | rtx4090* | 10 | 17% |
| 3 | sn23 Trishool | 52.5 | 1,047 | 1,047 = | cpu-small | 3 | 33% |
| 4 | sn71 Leadpoet | 51.2 | 1.76 | 307 | rtx4090* | 50 | 30% |
| 5 | sn120 Affine | 47.4 | 6,306 | 6,306 = | rtx4090* | 5 | 20% |
| 6 | sn4 Targon | 46 | 4,066 | 7,167 | rtx4090* | 8 | 30% |
| 7 | sn114 SOMA | 42.7 | 1,525 | 3,978 | rtx4090* | 3 | 65% |
| 8 | sn107 Minos | 42.2 | 90.78 | 25,765 | cpu-small | 20 | 90% |
| 9 | sn1 Apex | 41.5 | 1,078 | 1,935 | rtx4090* | 5 | 41% |
| 10 | sn102 ConnitoAI | 40.4 | 766 | 1,189 | rtx4090* | 6 | 32% |
| 11 | sn89 InfiniteQuant | 39.3 | -8.15 | 148 | rtx4090* | 33 | 42% |
| 12 | sn98 NeverPlayAlone | 38 | 149 | 149 = | cpu-small | 2 | 91% |
| 13 | sn77 Liquidity | 37.9 | 366 | 652 | rtx4090* | 11 | 18% |
| 14 | sn64 Chutes | 37.3 | 2,062 | 10,668 | a100-80 | 17 | 23% |
| 15 | sn124 Swarm | 37.2 | 307 | 485 | rtx4090* | 16 | 13% |
| 16 | sn96 Verathos | 34.4 | 28.63 | 167 | rtx4090 | 143 | 3% |
| 17 | sn101 Tag101 | 34.3 | 9.96 | 17.25 | cpu-small | 242 | 1% |
| 18 | sn38 ChronoLLM | 34 | 124 | 2,787 | rtx4090* | 10 | 52% |
| 19 | sn55 NIOME | 33.8 | 109 | 304 | rtx4090* | 11 | 20% |
| 20 | sn68 NOVA | 33.5 | 6,312 | 6,312 = | rtx4090* | 1 | 100% |

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
| concentrated (30–60%) | 21 |
| dominated (60–90%) | 16 |
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
| 2026-07-28T12:59 | sn89 | SCORING_COMMIT | sn89 commit touches scoring: hf scoreboard: publish n_submitters_3d |
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

