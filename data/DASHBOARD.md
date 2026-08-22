# Subnet watch — dashboard

_snapshot 2026-08-22T02:43:10Z · block 8897485 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 54 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 89 | `miner_burn` < 0.99 |
| Ranked | 89 | passed every gate |
| **Positive margin** | **54** | income beats machine cost |
| New events this window | 3 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 58 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 39 | `███████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 77.5 | 85.31 | 143 | cpu-small | 13 | 20% |
| 2 | sn102 ConnitoAI | 73 | 1,832 | 1,834 | rtx4090* | 4 | 25% |
| 3 | sn23 Trishool | 72.5 | 613 | 613 = | cpu-small | 2 | 80% |
| 4 | sn15 ORO | 70.7 | 22.29 | 41.44 | cpu-small | 78 | 93% |
| 5 | sn67 Harnyx | 70.4 | 14.09 | 967 | cpu-small | 162 | 23% |
| 6 | sn1 Apex | 70.3 | 808 | 1,277 | rtx4090* | 4 | 53% |
| 7 | sn56 Gradients | 70.1 | 756 | 1,164 | rtx4090* | 5 | 73% |
| 8 | sn91 cascade | 70 | 750 | 3,026 | rtx4090* | 5 | 52% |
| 9 | sn26 Perturb | 67.8 | 19.46 | 276 | rtx3060 | 10 | 70% |
| 10 | sn96 Verathos | 67.1 | 16.60 | 609 | rtx4090 | 84 | 41% |
| 11 | sn38 ChronoLLM | 66.6 | 118 | 1,613 | cpu-small | 10 | 52% |
| 12 | sn107 Minos | 65.7 | 165 | 46,746 | cpu-small | 20 | 90% |
| 13 | sn85 Vidaio | 65.1 | 174 | 446 | rtx4090* | 13 | 42% |
| 14 | sn98 NeverPlayAlone | 64.7 | 2,058 | 2,058 = | cpu-small | 1 | 100% |
| 15 | sn121 sundae_bar | 63.2 | 1,292 | 1,292 = | cpu-small | 2 | 60% |
| 16 | sn81 Reliquary | 63.2 | 98.10 | 294 | rtx4090* | 45 | 6% |
| 17 | sn51 lium.io | 62.7 | 92.48 | 4,255 | rtx4090* | 49 | 68% |
| 18 | sn108 Prometheon | 61.7 | 62.20 | 426 | rtx4090* | 8 | 66% |
| 19 | sn53 engy | 60.1 | 38.39 | 253 | rtx4090 | 144 | 63% |
| 20 | sn60 Bitsec.ai | 59.9 | 490 | 490 = | cpu-small | 3 | 50% |

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
| dominated (60–90%) | 21 |
| captured (>90%) | 23 |

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
| 2026-08-21T19:06 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: Install the signer's keypair and verify t |
| 2026-08-21T18:14 | sn25 | RELEASE | sn25 released v2026.8.21-1025339670 |
| 2026-08-21T17:00 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: Turn provenance off until the run store c |
| 2026-08-21T16:15 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: docs: quickstart matches production — mir |
| 2026-08-21T16:15 | sn21 | README_TASK_DIFF | sn21 README task/scoring sections changed |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

