# Subnet watch — dashboard

_snapshot 2026-08-22T04:17:35Z · block 8897957 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 54 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 91 | `miner_burn` < 0.99 |
| Ranked | 91 | passed every gate |
| **Positive margin** | **54** | income beats machine cost |
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
| 1 | sn76 Phylax | 77.6 | 87.62 | 147 | cpu-small | 13 | 20% |
| 2 | sn102 ConnitoAI | 73.1 | 1,863 | 1,865 | rtx4090* | 4 | 25% |
| 3 | sn23 Trishool | 72.6 | 628 | 628 = | cpu-small | 2 | 80% |
| 4 | sn15 ORO | 70.9 | 23.13 | 41.51 | cpu-small | 78 | 93% |
| 5 | sn67 Harnyx | 70.5 | 14.49 | 993 | cpu-small | 162 | 23% |
| 6 | sn1 Apex | 70.4 | 824 | 1,302 | rtx4090* | 4 | 53% |
| 7 | sn91 cascade | 70.2 | 794 | 3,201 | rtx4090* | 5 | 52% |
| 8 | sn56 Gradients | 70.2 | 774 | 1,193 | rtx4090* | 5 | 73% |
| 9 | sn26 Perturb | 67.9 | 20.09 | 284 | rtx3060 | 10 | 70% |
| 10 | sn96 Verathos | 67.7 | 19.05 | 607 | rtx4090 | 85 | 40% |
| 11 | sn38 ChronoLLM | 66.7 | 121 | 1,657 | cpu-small | 10 | 52% |
| 12 | sn107 Minos | 65.7 | 165 | 47,722 | cpu-small | 20 | 90% |
| 13 | sn98 NeverPlayAlone | 64.8 | 2,114 | 2,114 = | cpu-small | 1 | 100% |
| 14 | sn85 Vidaio | 64.8 | 156 | 458 | rtx4090* | 13 | 42% |
| 15 | sn81 Reliquary | 63.3 | 101 | 289 | rtx4090* | 45 | 6% |
| 16 | sn121 sundae_bar | 63.2 | 1,323 | 1,323 = | cpu-small | 2 | 60% |
| 17 | sn51 lium.io | 62.8 | 96.12 | 4,908 | rtx4090* | 49 | 69% |
| 18 | sn108 Prometheon | 61.8 | 64.11 | 438 | rtx4090* | 8 | 66% |
| 19 | sn28 gm | 60.1 | 39.57 | 1,762 | rtx4090* | 56 | 14% |
| 20 | sn53 engy | 60.1 | 37.83 | 250 | rtx4090 | 144 | 63% |

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
| dominated (60–90%) | 20 |
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

