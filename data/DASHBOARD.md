# Subnet watch — dashboard

_snapshot 2026-08-22T04:59:17Z · block 8898165 · run_status **ok**_

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
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 37 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 77.6 | 87.74 | 147 | cpu-small | 13 | 20% |
| 2 | sn67 Harnyx | 72.7 | 25.27 | 504 | cpu-small | 131 | 13% |
| 3 | sn23 Trishool | 72.6 | 627 | 627 = | cpu-small | 2 | 80% |
| 4 | sn102 ConnitoAI | 71.8 | 1,275 | 2,990 | rtx4090* | 5 | 40% |
| 5 | sn15 ORO | 70.8 | 23.31 | 41.82 | cpu-small | 78 | 93% |
| 6 | sn1 Apex | 70.4 | 822 | 1,299 | rtx4090* | 4 | 54% |
| 7 | sn91 cascade | 70.3 | 801 | 3,230 | rtx4090* | 5 | 52% |
| 8 | sn56 Gradients | 70.1 | 773 | 1,191 | rtx4090* | 5 | 73% |
| 9 | sn26 Perturb | 67.9 | 20.12 | 284 | rtx3060 | 10 | 70% |
| 10 | sn96 Verathos | 67.3 | 17.68 | 573 | rtx4090 | 89 | 40% |
| 11 | sn38 ChronoLLM | 66.7 | 122 | 1,659 | cpu-small | 10 | 52% |
| 12 | sn107 Minos | 65.5 | 159 | 47,897 | cpu-small | 20 | 90% |
| 13 | sn98 NeverPlayAlone | 64.8 | 2,116 | 2,116 = | cpu-small | 1 | 100% |
| 14 | sn85 Vidaio | 64 | 124 | 447 | rtx4090* | 13 | 42% |
| 15 | sn121 sundae_bar | 63.2 | 1,323 | 1,323 = | cpu-small | 2 | 60% |
| 16 | sn81 Reliquary | 63.2 | 96.79 | 270 | rtx4090* | 43 | 6% |
| 17 | sn51 lium.io | 62.8 | 96.23 | 4,913 | rtx4090* | 49 | 69% |
| 18 | sn108 Prometheon | 61.8 | 65.07 | 444 | rtx4090* | 8 | 66% |
| 19 | sn53 engy | 60.1 | 37.52 | 248 | rtx4090 | 144 | 63% |
| 20 | sn60 Bitsec.ai | 60 | 509 | 509 = | cpu-small | 3 | 50% |

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
| concentrated (30–60%) | 19 |
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
| 2026-08-21T19:06 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: Install the signer's keypair and verify t |
| 2026-08-21T18:14 | sn25 | RELEASE | sn25 released v2026.8.21-1025339670 |
| 2026-08-21T17:00 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: Turn provenance off until the run store c |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

