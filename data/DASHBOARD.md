# Subnet watch — dashboard

_snapshot 2026-08-21T23:02:57Z · block 8896383 · run_status **ok**_

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
| New events this window | 2 | see ALARMS.md |

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
| 1 | sn76 Phylax | 77.3 | 81.76 | 137 | cpu-small | 13 | 20% |
| 2 | sn23 Trishool | 72.4 | 591 | 591 = | cpu-small | 2 | 80% |
| 3 | sn62 Ridges | 71.3 | 1,095 | 2,063 | rtx4090* | 5 | 36% |
| 4 | sn15 ORO | 70.7 | 22.34 | 21,789 | cpu-small | 77 | 93% |
| 5 | sn67 Harnyx | 70.3 | 13.74 | 945 | cpu-small | 162 | 23% |
| 6 | sn1 Apex | 70.2 | 793 | 1,254 | rtx4090* | 4 | 52% |
| 7 | sn91 cascade | 70 | 735 | 2,963 | rtx4090* | 5 | 52% |
| 8 | sn56 Gradients | 70 | 730 | 1,125 | rtx4090* | 5 | 73% |
| 9 | sn26 Perturb | 68.1 | 21.10 | 401 | rtx3060 | 10 | 70% |
| 10 | sn38 ChronoLLM | 67.9 | 165 | 3,491 | cpu-small | 10 | 52% |
| 11 | sn96 Verathos | 66.2 | 13.45 | 600 | rtx4090 | 98 | 40% |
| 12 | sn107 Minos | 65.5 | 159 | 45,809 | cpu-small | 20 | 90% |
| 13 | sn85 Vidaio | 65 | 167 | 431 | rtx4090* | 13 | 42% |
| 14 | sn121 sundae_bar | 63 | 1,248 | 1,248 = | cpu-small | 2 | 60% |
| 15 | sn81 Reliquary | 62.5 | 78.61 | 237 | rtx4090* | 46 | 5% |
| 16 | sn108 Prometheon | 61.5 | 59.10 | 407 | rtx4090* | 8 | 66% |
| 17 | sn34 BitMind | 61.2 | 370 | 370 = | a100-80 | 3 | 48% |
| 18 | sn51 lium.io | 60.3 | 49.47 | 1,656 | rtx4090* | 51 | 76% |
| 19 | sn53 engy | 60.2 | 38.92 | 256 | rtx4090 | 144 | 63% |
| 20 | sn60 Bitsec.ai | 59.7 | 468 | 468 = | cpu-small | 3 | 50% |

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
| wide (<30%) | 25 |
| concentrated (30–60%) | 18 |
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
| 2026-08-21T16:15 | sn102 | RELEASE | sn102 released v0.5.0 |
| 2026-08-21T16:15 | sn102 | SCORING_COMMIT | sn102 commit touches scoring: Merge pull request #223 from Connito-AI/ |
| 2026-08-21T14:50 | sn1 | RELEASE | sn1 released v4.3.6 |
| 2026-08-21T14:50 | sn25 | RELEASE | sn25 released v2026.8.21-1025223880 |
| 2026-08-21T13:57 | sn108 | SCORING_COMMIT | sn108 commit touches scoring: fix(evaluation): reuse the prefix cache  |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

