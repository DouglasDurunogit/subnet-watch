# Subnet watch — dashboard

_snapshot 2026-07-30T16:16:58Z · block 8735986 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 55 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 95 | `miner_burn` < 0.99 |
| Ranked | 95 | passed every gate |
| **Positive margin** | **55** | income beats machine cost |
| New events this window | 4 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 61 | `████████████████████████████` |
| 0–0.2 | 4 | `██` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 8 | `████` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 9 | `████` |
| ≥0.99 dead | 33 | `███████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn23 Trishool | 85.1 | 581 | 581 = | cpu-small | 5 | 20% |
| 2 | sn107 Minos | 78.2 | 114 | 29,078 | cpu-small | 20 | 88% |
| 3 | sn76 Phylax | 77.1 | 75.47 | 152 | cpu-small | 7 | 70% |
| 4 | sn98 NeverPlayAlone | 76.1 | 1,749 | 1,749 = | cpu-small | 1 | 100% |
| 5 | sn67 Harnyx | 71.4 | 17.93 | 1,111 | cpu-small | 94 | 23% |
| 6 | sn56 Gradients | 69.6 | 666 | 1,314 | rtx4090* | 6 | 63% |
| 7 | sn101 Tag101 | 68.5 | 11.22 | 15.55 | cpu-small | 236 | 1% |
| 8 | sn15 ORO | 68.4 | 11.22 | 20.56 | cpu-small | 82 | 92% |
| 9 | sn124 Swarm | 67.5 | 361 | 716 | rtx4090* | 16 | 12% |
| 10 | sn102 ConnitoAI | 67.4 | 343 | 1,348 | rtx4090* | 7 | 36% |
| 11 | sn28 gm | 66.4 | 255 | 2,833 | rtx4090* | 9 | 49% |
| 12 | sn85 Vidaio | 63.9 | 119 | 647 | rtx4090* | 10 | 21% |
| 13 | sn38 ChronoLLM | 63 | 103 | 1,500 | rtx4090* | 10 | 52% |
| 14 | sn53 engy | 63 | 92.24 | 2,252 | rtx4090 | 34 | 13% |
| 15 | sn71 Leadpoet | 62.4 | 75.54 | 131 | rtx4090* | 4 | 91% |
| 16 | sn61 RedTeam | 58.6 | 24.09 | 137 | rtx4090* | 85 | 4% |
| 17 | sn26 Perturb | 55.2 | 1.43 | 208 | rtx3060 | 52 | 50% |
| 18 | sn9 iota | 53.6 | 4,351 | 7,819 | rtx4090* | 3 | 55% |
| 19 | sn97 Albedo | 53 | 3,317 | 3,317 = | rtx4090* | 5 | 20% |
| 20 | sn51 lium.io | 52 | 8.27 | 3,355 | rtx4090* | 40 | 61% |

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
| concentrated (30–60%) | 23 |
| dominated (60–90%) | 18 |
| captured (>90%) | 27 |

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
| 2026-07-30T09:58 | sn43 | BURN_DROP | sn43 burn fell 1.000 -> 0.800 - miners can earn again |
| 2026-07-30T09:58 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-2340, publish structured zero-incenti |
| 2026-07-30T09:58 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Keep validator epoch authority fresh duri |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

