# Subnet watch — dashboard

_snapshot 2026-08-22T07:40:52Z · block 8898973 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 52 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 90 | `miner_burn` < 0.99 |
| Ranked | 90 | passed every gate |
| **Positive margin** | **52** | income beats machine cost |
| New events this window | 0 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 61 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 38 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 77.4 | 81.82 | 137 | cpu-small | 13 | 20% |
| 2 | sn102 ConnitoAI | 73 | 1,799 | 1,800 | rtx4090* | 4 | 26% |
| 3 | sn23 Trishool | 72.4 | 585 | 585 = | cpu-small | 2 | 80% |
| 4 | sn67 Harnyx | 72.4 | 23.72 | 462 | cpu-small | 137 | 12% |
| 5 | sn91 cascade | 70 | 738 | 2,975 | rtx4090* | 5 | 52% |
| 6 | sn56 Gradients | 69.9 | 719 | 1,108 | rtx4090* | 5 | 73% |
| 7 | sn15 ORO | 69.8 | 18.09 | 22,483 | cpu-small | 59 | 95% |
| 8 | sn1 Apex | 68.7 | 506 | 1,193 | rtx4090* | 5 | 54% |
| 9 | sn26 Perturb | 67.6 | 18.58 | 265 | rtx3060 | 10 | 70% |
| 10 | sn96 Verathos | 67 | 16.01 | 480 | rtx4090 | 92 | 41% |
| 11 | sn38 ChronoLLM | 66.5 | 113 | 1,542 | cpu-small | 10 | 52% |
| 12 | sn107 Minos | 65.4 | 153 | 45,686 | cpu-small | 20 | 90% |
| 13 | sn98 NeverPlayAlone | 64.6 | 1,975 | 1,975 = | cpu-small | 1 | 100% |
| 14 | sn85 Vidaio | 64 | 123 | 417 | rtx4090* | 13 | 42% |
| 15 | sn81 Reliquary | 63.2 | 97.76 | 223 | rtx4090* | 43 | 5% |
| 16 | sn108 Prometheon | 61.6 | 60.18 | 414 | rtx4090* | 8 | 66% |
| 17 | sn51 lium.io | 60.4 | 51.00 | 5,132 | rtx4090* | 52 | 68% |
| 18 | sn53 engy | 59.9 | 35.39 | 236 | rtx4090 | 144 | 63% |
| 19 | sn60 Bitsec.ai | 59.8 | 472 | 472 = | cpu-small | 3 | 50% |
| 20 | sn28 gm | 58.1 | 22.31 | 1,651 | rtx4090* | 55 | 14% |

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
| wide (<30%) | 26 |
| concentrated (30–60%) | 17 |
| dominated (60–90%) | 19 |
| captured (>90%) | 26 |

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

