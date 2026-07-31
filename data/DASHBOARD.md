# Subnet watch — dashboard

_snapshot 2026-07-31T13:05:02Z · block 8742221 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 56 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 98 | `miner_burn` < 0.99 |
| Ranked | 98 | passed every gate |
| **Positive margin** | **56** | income beats machine cost |
| New events this window | 1 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 61 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 8 | `████` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 9 | `████` |
| ≥0.99 dead | 30 | `██████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 77.5 | 97.71 | 29,398 | cpu-small | 20 | 90% |
| 2 | sn76 Phylax | 77.2 | 77.30 | 156 | cpu-small | 7 | 70% |
| 3 | sn98 NeverPlayAlone | 76.1 | 1,751 | 1,751 = | cpu-small | 1 | 100% |
| 4 | sn67 Harnyx | 73.8 | 32.71 | 925 | cpu-small | 118 | 19% |
| 5 | sn23 Trishool | 72.4 | 591 | 591 = | cpu-small | 5 | 20% |
| 6 | sn62 Ridges | 71 | 986 | 4,540 | rtx4090* | 6 | 57% |
| 7 | sn56 Gradients | 69.6 | 666 | 1,228 | rtx4090* | 6 | 64% |
| 8 | sn26 Perturb | 68.6 | 23.21 | 43.73 | rtx3060 | 11 | 50% |
| 9 | sn101 Tag101 | 68.5 | 8.62 | 31.85 | cpu-small | 242 | 1% |
| 10 | sn15 ORO | 67.9 | 9.62 | 20.04 | cpu-small | 79 | 93% |
| 11 | sn124 Swarm | 67.1 | 322 | 705 | rtx4090* | 19 | 12% |
| 12 | sn85 Vidaio | 64.1 | 126 | 599 | rtx4090* | 10 | 19% |
| 13 | sn53 engy | 63.5 | 106 | 2,559 | rtx4090 | 34 | 13% |
| 14 | sn38 ChronoLLM | 63.3 | 111 | 1,600 | rtx4090* | 10 | 52% |
| 15 | sn71 Leadpoet | 62.3 | 73.85 | 129 | rtx4090* | 4 | 91% |
| 16 | sn61 RedTeam | 58.8 | 25.35 | 124 | rtx4090* | 88 | 4% |
| 17 | sn28 gm | 58.4 | 23.95 | 3,153 | rtx4090* | 13 | 51% |
| 18 | sn102 ConnitoAI | 54.7 | 6.87 | 1,188 | rtx4090* | 9 | 32% |
| 19 | sn51 lium.io | 54.4 | 12.71 | 6,433 | rtx4090* | 43 | 41% |
| 20 | sn97 Albedo | 52.9 | 3,271 | 3,271 = | rtx4090* | 5 | 20% |

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
| concentrated (30–60%) | 23 |
| dominated (60–90%) | 20 |
| captured (>90%) | 28 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 106 |
| min_compute.yml (curated) | 9 |
| code-submission (validator runs it) | 8 |
| README keywords (GUESS) | 4 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-07-31T13:05 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: Hold inference keys in the proxy, enforce |
| 2026-07-31T11:05 | sn8 | BURN_DROP | sn8 burn fell 0.998 -> 0.000 - miners can earn again |
| 2026-07-31T11:05 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: Evaluate two agents at a time within a tr |
| 2026-07-31T08:08 | sn80 | SCORING_COMMIT | sn80 commit touches scoring: docs: document public /api/v1/scan-reject |
| 2026-07-30T23:33 | sn8 | SCORING_COMMIT | sn8 commit touches scoring: create subaccount elimination cache on ent |
| 2026-07-30T23:33 | sn62 | RELEASE | sn62 released v0.2.3 |
| 2026-07-30T23:33 | sn115 | BURN_DROP | sn115 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-07-30T23:33 | sn124 | SCORING_COMMIT | sn124 commit touches scoring: Kill host workers when the validator pro |
| 2026-07-30T22:16 | sn14 | SCORING_COMMIT | sn14 commit touches scoring: Add object-store proposal transport and v |
| 2026-07-30T19:47 | sn28 | RELEASE | sn28 released v0.3.15 |
| 2026-07-30T17:57 | sn55 | BURN_DROP | sn55 burn fell 1.000 -> 0.022 - miners can earn again |
| 2026-07-30T17:57 | sn89 | SCORING_COMMIT | sn89 commit touches scoring: hf board: share of the MINER pool, not of |
| 2026-07-30T17:57 | sn121 | BURN_DROP | sn121 burn fell 1.000 -> 0.826 - miners can earn again |
| 2026-07-30T16:17 | sn26 | README_TASK_DIFF | sn26 README task/scoring sections changed |
| 2026-07-30T16:17 | sn49 | SCORING_COMMIT | sn49 commit touches scoring: Updated Discord link across documentation |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

