# Subnet watch — dashboard

_snapshot 2026-07-30T19:47:19Z · block 8737038 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 58 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 97 | `miner_burn` < 0.99 |
| Ranked | 97 | passed every gate |
| **Positive margin** | **58** | income beats machine cost |
| New events this window | 1 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 61 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 10 | `█████` |
| 0.6–0.8 | 7 | `███` |
| 0.8–0.99 | 9 | `████` |
| ≥0.99 dead | 31 | `██████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn23 Trishool | 85.1 | 574 | 574 = | cpu-small | 5 | 20% |
| 2 | sn107 Minos | 77.6 | 99.97 | 29,724 | cpu-small | 20 | 90% |
| 3 | sn76 Phylax | 77.3 | 78.33 | 158 | cpu-small | 7 | 70% |
| 4 | sn98 NeverPlayAlone | 76.1 | 1,748 | 1,748 = | cpu-small | 1 | 100% |
| 5 | sn67 Harnyx | 71.4 | 17.88 | 1,108 | cpu-small | 94 | 23% |
| 6 | sn56 Gradients | 69.6 | 662 | 1,289 | rtx4090* | 6 | 64% |
| 7 | sn101 Tag101 | 69.2 | 11.04 | 15.99 | cpu-small | 243 | 1% |
| 8 | sn26 Perturb | 68.6 | 23.52 | 208 | rtx3060 | 11 | 50% |
| 9 | sn15 ORO | 68.5 | 11.03 | 20.23 | cpu-small | 82 | 92% |
| 10 | sn124 Swarm | 67.3 | 339 | 659 | rtx4090* | 17 | 12% |
| 11 | sn28 gm | 64.1 | 130 | 2,533 | rtx4090* | 9 | 54% |
| 12 | sn53 engy | 63.2 | 96.63 | 2,351 | rtx4090 | 34 | 13% |
| 13 | sn38 ChronoLLM | 63.1 | 106 | 1,537 | rtx4090* | 10 | 52% |
| 14 | sn71 Leadpoet | 62.3 | 74.50 | 130 | rtx4090* | 4 | 91% |
| 15 | sn85 Vidaio | 61.4 | 55.79 | 550 | rtx4090* | 10 | 18% |
| 16 | sn61 RedTeam | 58.5 | 23.15 | 117 | rtx4090* | 88 | 4% |
| 17 | sn90 KubeTEE AI Facto | 55.3 | 8,948 | 8,948 = | rtx4090* | 1 | 100% |
| 18 | sn102 ConnitoAI | 54.5 | 6.37 | 1,133 | rtx4090* | 9 | 30% |
| 19 | sn9 iota | 53.6 | 4,326 | 7,826 | rtx4090* | 3 | 56% |
| 20 | sn97 Albedo | 52.9 | 3,203 | 3,203 = | rtx4090* | 5 | 20% |

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
| dominated (60–90%) | 19 |
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
| 2026-07-30T14:28 | sn100 | BURN_DROP | sn100 burn fell 1.000 -> 0.503 - miners can earn again |
| 2026-07-30T12:02 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-07-30T12:02 | sn92 | BURN_DROP | sn92 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-07-30T12:02 | sn97 | SCORING_COMMIT | sn97 commit touches scoring: update: Updated evaluator & judge prompts |
| 2026-07-30T09:58 | sn28 | RELEASE | sn28 released v0.3.14 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

