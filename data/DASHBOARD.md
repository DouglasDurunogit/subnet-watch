# Subnet watch — dashboard

_snapshot 2026-07-30T23:32:33Z · block 8738162 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 59 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 98 | `miner_burn` < 0.99 |
| Ranked | 98 | passed every gate |
| **Positive margin** | **59** | income beats machine cost |
| New events this window | 4 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 60 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 8 | `████` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 10 | `█████` |
| ≥0.99 dead | 30 | `██████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn23 Trishool | 85.1 | 573 | 573 = | cpu-small | 5 | 20% |
| 2 | sn107 Minos | 77.5 | 98.39 | 29,234 | cpu-small | 20 | 90% |
| 3 | sn76 Phylax | 77.2 | 77.71 | 156 | cpu-small | 7 | 70% |
| 4 | sn67 Harnyx | 73.7 | 32.01 | 937 | cpu-small | 105 | 20% |
| 5 | sn62 Ridges | 70.8 | 928 | 4,278 | rtx4090* | 6 | 57% |
| 6 | sn56 Gradients | 69.6 | 660 | 1,270 | rtx4090* | 6 | 64% |
| 7 | sn101 Tag101 | 69.2 | 10.39 | 15.13 | cpu-small | 246 | 1% |
| 8 | sn26 Perturb | 68.7 | 23.82 | 207 | rtx3060 | 11 | 50% |
| 9 | sn15 ORO | 68.5 | 10.74 | 19.86 | cpu-small | 82 | 92% |
| 10 | sn124 Swarm | 67.3 | 338 | 658 | rtx4090* | 17 | 12% |
| 11 | sn53 engy | 63.3 | 98.90 | 2,402 | rtx4090 | 34 | 13% |
| 12 | sn38 ChronoLLM | 63.1 | 105 | 1,523 | rtx4090* | 10 | 52% |
| 13 | sn71 Leadpoet | 62.3 | 73.69 | 128 | rtx4090* | 4 | 91% |
| 14 | sn85 Vidaio | 61.4 | 55.41 | 504 | rtx4090* | 10 | 16% |
| 15 | sn28 gm | 58.9 | 27.58 | 2,878 | rtx4090* | 11 | 55% |
| 16 | sn61 RedTeam | 58.6 | 23.58 | 118 | rtx4090* | 88 | 4% |
| 17 | sn102 ConnitoAI | 54.9 | 7.33 | 1,086 | rtx4090* | 8 | 29% |
| 18 | sn97 Albedo | 52.9 | 3,217 | 3,217 = | rtx4090* | 5 | 20% |
| 19 | sn9 iota | 52.6 | 2,824 | 4,874 | rtx4090* | 3 | 71% |
| 20 | sn90 KubeTEE AI Facto | 51.6 | 1,874 | 1,874 = | rtx4090* | 2 | 80% |

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
| concentrated (30–60%) | 19 |
| dominated (60–90%) | 22 |
| captured (>90%) | 29 |

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
| 2026-07-30T16:17 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Verify no-burn fallback allocation inputs |
| 2026-07-30T16:17 | sn98 | SCORING_COMMIT | sn98 commit touches scoring: fix(miner-cli): add log for hotkey ban (# |
| 2026-07-30T14:28 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: feat: DAH-2251 — pay referral incentive f |
| 2026-07-30T14:28 | sn74 | RELEASE | sn74 released release-20260730-140609 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

