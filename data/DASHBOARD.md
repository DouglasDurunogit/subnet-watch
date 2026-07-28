# Subnet watch — dashboard

_snapshot 2026-07-28T15:03:42Z · block 8721229 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 49 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 90 | `miner_burn` < 0.99 |
| Ranked | 90 | passed every gate |
| **Positive margin** | **49** | income beats machine cost |
| New events this window | 5 | see ALARMS.md |

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
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 8 | `████` |
| ≥0.99 dead | 38 | `██████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn67 Harnyx | 68.8 | 8.75 | 910 | cpu-small | 60 | 19% |
| 2 | sn85 Vidaio | 68.6 | 483 | 498 | rtx4090* | 10 | 16% |
| 3 | sn28 gm | 61.6 | 62.11 | 1,796 | rtx4090* | 10 | 62% |
| 4 | sn23 Trishool | 52.5 | 1,045 | 1,045 = | cpu-small | 3 | 33% |
| 5 | sn71 Leadpoet | 50.4 | 1.17 | 288 | rtx4090* | 50 | 30% |
| 6 | sn120 Affine | 47.4 | 6,312 | 6,312 = | rtx4090* | 5 | 20% |
| 7 | sn4 Targon | 46 | 4,066 | 7,168 | rtx4090* | 8 | 30% |
| 8 | sn107 Minos | 41.9 | 86.33 | 25,688 | cpu-small | 20 | 90% |
| 9 | sn1 Apex | 41.4 | 1,057 | 1,988 | rtx4090* | 5 | 42% |
| 10 | sn103 Djinn | 39.3 | -3.79 | -3.58 | rtx4090* | 249 | 0% |
| 11 | sn56 Gradients | 39.3 | -7.35 | 699 | rtx4090* | 22 | 71% |
| 12 | sn89 InfiniteQuant | 39.3 | -8.15 | 149 | rtx4090* | 33 | 42% |
| 13 | sn98 NeverPlayAlone | 38.4 | 164 | 164 = | cpu-small | 2 | 90% |
| 14 | sn77 Liquidity | 37.9 | 366 | 651 | rtx4090* | 11 | 18% |
| 15 | sn64 Chutes | 37.3 | 2,073 | 10,712 | a100-80 | 17 | 23% |
| 16 | sn124 Swarm | 37.2 | 307 | 484 | rtx4090* | 16 | 13% |
| 17 | sn96 Verathos | 34.4 | 28.24 | 158 | rtx4090 | 146 | 3% |
| 18 | sn101 Tag101 | 34 | 9.20 | 19.55 | cpu-small | 242 | 1% |
| 19 | sn38 ChronoLLM | 33.9 | 124 | 2,772 | rtx4090* | 10 | 52% |
| 20 | sn68 NOVA | 33.5 | 6,298 | 6,298 = | rtx4090* | 1 | 100% |

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
| wide (<30%) | 27 |
| concentrated (30–60%) | 20 |
| dominated (60–90%) | 17 |
| captured (>90%) | 24 |

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
| 2026-07-28T15:04 | sn28 | RELEASE | sn28 released v0.3.12 |
| 2026-07-28T15:04 | sn56 | SCORING_COMMIT | sn56 commit touches scoring: feat(validator): auto-balance emission sp |
| 2026-07-28T15:04 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: Retry validator self registration until i |
| 2026-07-28T15:04 | sn103 | RELEASE | sn103 released v2003: validator: restore miner burn fraction to 0.8 |
| 2026-07-28T15:04 | sn103 | SCORING_COMMIT | sn103 commit touches scoring: validator: restore miner burn fraction t |
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

