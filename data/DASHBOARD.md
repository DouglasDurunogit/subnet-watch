# Subnet watch — dashboard

_snapshot 2026-07-30T17:56:27Z · block 8736484 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 60 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 97 | `miner_burn` < 0.99 |
| Ranked | 97 | passed every gate |
| **Positive margin** | **60** | income beats machine cost |
| New events this window | 3 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 61 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 8 | `████` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 10 | `█████` |
| ≥0.99 dead | 31 | `██████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn23 Trishool | 85.1 | 573 | 573 = | cpu-small | 5 | 20% |
| 2 | sn107 Minos | 77.6 | 100 | 29,746 | cpu-small | 20 | 90% |
| 3 | sn76 Phylax | 77.2 | 77.42 | 156 | cpu-small | 7 | 70% |
| 4 | sn98 NeverPlayAlone | 76 | 1,735 | 1,735 = | cpu-small | 1 | 100% |
| 5 | sn67 Harnyx | 71.4 | 17.84 | 1,106 | cpu-small | 94 | 23% |
| 6 | sn56 Gradients | 69.6 | 661 | 1,299 | rtx4090* | 6 | 63% |
| 7 | sn101 Tag101 | 69.3 | 11.49 | 15.71 | cpu-small | 238 | 1% |
| 8 | sn102 ConnitoAI | 68.9 | 532 | 1,674 | rtx4090* | 6 | 45% |
| 9 | sn15 ORO | 68.4 | 11.12 | 20.39 | cpu-small | 82 | 92% |
| 10 | sn124 Swarm | 67.4 | 346 | 673 | rtx4090* | 17 | 12% |
| 11 | sn85 Vidaio | 65.3 | 181 | 522 | rtx4090* | 10 | 17% |
| 12 | sn28 gm | 65.1 | 172 | 1,440 | rtx4090* | 10 | 53% |
| 13 | sn38 ChronoLLM | 63.1 | 105 | 1,525 | rtx4090* | 10 | 52% |
| 14 | sn53 engy | 63.1 | 94.28 | 2,298 | rtx4090 | 34 | 13% |
| 15 | sn71 Leadpoet | 62.2 | 71.85 | 125 | rtx4090* | 4 | 91% |
| 16 | sn61 RedTeam | 58.6 | 23.97 | 132 | rtx4090* | 84 | 4% |
| 17 | sn26 Perturb | 55.2 | 1.42 | 207 | rtx3060 | 52 | 50% |
| 18 | sn90 KubeTEE AI Facto | 54.9 | 7,380 | 7,380 = | rtx4090* | 1 | 100% |
| 19 | sn9 iota | 53.6 | 4,309 | 7,763 | rtx4090* | 3 | 56% |
| 20 | sn97 Albedo | 52.9 | 3,215 | 3,215 = | rtx4090* | 5 | 20% |

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
| dominated (60–90%) | 18 |
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
| 2026-07-30T17:57 | sn55 | BURN_DROP | sn55 burn fell 1.000 -> 0.022 - miners can earn again |
| 2026-07-30T17:57 | sn89 | SCORING_COMMIT | sn89 commit touches scoring: hf board: share of the MINER pool, not of |
| 2026-07-30T17:57 | sn121 | BURN_DROP | sn121 burn fell 1.000 -> 0.826 - miners can earn again |
| 2026-07-30T16:17 | sn26 | README_TASK_DIFF | sn26 README task/scoring sections changed |
| 2026-07-30T16:17 | sn49 | SCORING_COMMIT | sn49 commit touches scoring: Updated Discord link across documentation |
| 2026-07-30T16:17 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Verify no-burn fallback allocation inputs |
| 2026-07-30T16:17 | sn98 | SCORING_COMMIT | sn98 commit touches scoring: fix(miner-cli): add log for hotkey ban (# |
| 2026-07-30T14:28 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: feat: DAH-2251 — pay referral incentive f |
| 2026-07-30T14:28 | sn74 | RELEASE | sn74 released release-20260730-140609 |
| 2026-07-30T14:28 | sn100 | BURN_DROP | sn100 burn fell 1.000 -> 0.503 - miners can earn again |
| 2026-07-30T12:02 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-07-30T12:02 | sn92 | BURN_DROP | sn92 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-07-30T12:02 | sn97 | SCORING_COMMIT | sn97 commit touches scoring: update: Updated evaluator & judge prompts |
| 2026-07-30T09:58 | sn28 | RELEASE | sn28 released v0.3.14 |
| 2026-07-30T09:58 | sn38 | SCORING_COMMIT | sn38 commit touches scoring: Add custom architecture registry for mine |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

