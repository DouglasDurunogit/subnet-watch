# Subnet watch — dashboard

_snapshot 2026-08-22T06:02:27Z · block 8898481 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 53 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 90 | `miner_burn` < 0.99 |
| Ranked | 90 | passed every gate |
| **Positive margin** | **53** | income beats machine cost |
| New events this window | 3 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 61 | `████████████████████████████` |
| 0–0.2 | 4 | `██` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 38 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 77.4 | 82.12 | 138 | cpu-small | 13 | 20% |
| 2 | sn23 Trishool | 72.4 | 588 | 588 = | cpu-small | 2 | 80% |
| 3 | sn67 Harnyx | 72.4 | 23.61 | 472 | cpu-small | 131 | 13% |
| 4 | sn102 ConnitoAI | 71.6 | 1,198 | 2,811 | rtx4090* | 5 | 40% |
| 5 | sn1 Apex | 70.1 | 766 | 1,210 | rtx4090* | 4 | 54% |
| 6 | sn91 cascade | 70 | 748 | 3,017 | rtx4090* | 5 | 52% |
| 7 | sn56 Gradients | 69.9 | 723 | 1,115 | rtx4090* | 5 | 73% |
| 8 | sn15 ORO | 69.5 | 17.18 | 22,734 | cpu-small | 58 | 96% |
| 9 | sn26 Perturb | 67.6 | 18.66 | 266 | rtx3060 | 10 | 70% |
| 10 | sn96 Verathos | 67 | 16.04 | 536 | rtx4090 | 89 | 40% |
| 11 | sn38 ChronoLLM | 66.5 | 114 | 1,554 | cpu-small | 10 | 52% |
| 12 | sn107 Minos | 65.4 | 154 | 45,306 | cpu-small | 20 | 90% |
| 13 | sn98 NeverPlayAlone | 64.6 | 1,982 | 1,982 = | cpu-small | 1 | 100% |
| 14 | sn85 Vidaio | 63.8 | 116 | 417 | rtx4090* | 13 | 42% |
| 15 | sn81 Reliquary | 63 | 90.15 | 253 | rtx4090* | 43 | 6% |
| 16 | sn51 lium.io | 62.5 | 88.75 | 4,562 | rtx4090* | 49 | 69% |
| 17 | sn108 Prometheon | 61.6 | 60.43 | 416 | rtx4090* | 8 | 66% |
| 18 | sn60 Bitsec.ai | 59.8 | 476 | 476 = | cpu-small | 3 | 50% |
| 19 | sn53 engy | 59.8 | 34.95 | 234 | rtx4090 | 144 | 63% |
| 20 | sn28 gm | 57.3 | 17.61 | 1,413 | rtx4090* | 55 | 24% |

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
| wide (<30%) | 24 |
| concentrated (30–60%) | 18 |
| dominated (60–90%) | 21 |
| captured (>90%) | 25 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 101 |
| code-submission (validator runs it) | 10 |
| min_compute.yml (curated) | 10 |
| README keywords (GUESS) | 6 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-08-22T05:38 | sn25 | RELEASE | sn25 released v2026.8.21-1025763520 |
| 2026-08-22T05:38 | sn92 | RELEASE | sn92 released v0.1.1 |
| 2026-08-22T05:38 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: Package the version validators actually r |
| 2026-08-22T04:17 | sn53 | RELEASE | sn53 released v0.4.5: Merge pull request #42 from hanlinai/release/0.4 |
| 2026-08-22T04:17 | sn100 | RELEASE | sn100 released v3.3.29 |
| 2026-08-22T02:43 | sn53 | SCORING_COMMIT | sn53 commit touches scoring: fix(validator): reuse one chain connectio |
| 2026-08-22T02:43 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: Sort the constants import in the validato |
| 2026-08-22T01:47 | sn25 | RELEASE | sn25 released v2026.8.21-1025613560 |
| 2026-08-22T00:02 | sn97 | SCORING_COMMIT | sn97 commit touches scoring: feat: weighted reference-anchored scoring |
| 2026-08-21T23:35 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: chore: remove dead BackendClient top-mine |
| 2026-08-21T22:02 | sn90 | RELEASE | sn90 released v1.1.5 |
| 2026-08-21T22:02 | sn90 | SCORING_COMMIT | sn90 commit touches scoring: fix(validator): fall back to CoinGecko TA |
| 2026-08-21T19:06 | sn89 | SCORING_COMMIT | sn89 commit touches scoring: Scoring: build the qualified-win as-of wi |
| 2026-08-21T19:06 | sn90 | README_TASK_DIFF | sn90 README task/scoring sections changed |
| 2026-08-21T19:06 | sn92 | RELEASE | sn92 released v0.1.0 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

