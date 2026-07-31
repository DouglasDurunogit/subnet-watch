# Subnet watch — dashboard

_snapshot 2026-07-31T01:16:55Z · block 8738684 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 60 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 98 | `miner_burn` < 0.99 |
| Ranked | 98 | passed every gate |
| **Positive margin** | **60** | income beats machine cost |
| New events this window | 0 | see ALARMS.md |

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
| 0.6–0.8 | 10 | `█████` |
| 0.8–0.99 | 9 | `████` |
| ≥0.99 dead | 30 | `██████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn23 Trishool | 85.1 | 579 | 579 = | cpu-small | 5 | 20% |
| 2 | sn107 Minos | 77.5 | 97.46 | 29,000 | cpu-small | 20 | 90% |
| 3 | sn76 Phylax | 77.3 | 78.72 | 158 | cpu-small | 7 | 70% |
| 4 | sn98 NeverPlayAlone | 76.1 | 1,763 | 1,763 = | cpu-small | 1 | 100% |
| 5 | sn67 Harnyx | 73.8 | 32.89 | 931 | cpu-small | 110 | 19% |
| 6 | sn62 Ridges | 70.8 | 939 | 4,328 | rtx4090* | 6 | 57% |
| 7 | sn101 Tag101 | 69.8 | 11.44 | 15.17 | cpu-small | 247 | 1% |
| 8 | sn56 Gradients | 69.7 | 668 | 1,280 | rtx4090* | 6 | 64% |
| 9 | sn26 Perturb | 68.7 | 23.88 | 212 | rtx3060 | 11 | 50% |
| 10 | sn15 ORO | 68.7 | 10.89 | 20.13 | cpu-small | 82 | 92% |
| 11 | sn124 Swarm | 67.3 | 342 | 665 | rtx4090* | 17 | 12% |
| 12 | sn85 Vidaio | 64.8 | 155 | 508 | rtx4090* | 10 | 28% |
| 13 | sn53 engy | 63.3 | 101 | 2,452 | rtx4090 | 34 | 13% |
| 14 | sn38 ChronoLLM | 63.1 | 105 | 1,530 | rtx4090* | 10 | 52% |
| 15 | sn71 Leadpoet | 62.3 | 74.10 | 129 | rtx4090* | 4 | 91% |
| 16 | sn28 gm | 59.4 | 31.93 | 2,421 | rtx4090* | 12 | 59% |
| 17 | sn61 RedTeam | 58.6 | 24.13 | 120 | rtx4090* | 88 | 4% |
| 18 | sn102 ConnitoAI | 53.7 | 4.72 | 1,055 | rtx4090* | 9 | 28% |
| 19 | sn97 Albedo | 52.9 | 3,284 | 3,284 = | rtx4090* | 5 | 20% |
| 20 | sn9 iota | 52.6 | 2,849 | 4,929 | rtx4090* | 3 | 71% |

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
| dominated (60–90%) | 23 |
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

