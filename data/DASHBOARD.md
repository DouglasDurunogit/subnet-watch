# Subnet watch — dashboard

_snapshot 2026-08-02T16:39:19Z · block 8757687 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 57 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 96 | `miner_burn` < 0.99 |
| Ranked | 96 | passed every gate |
| **Positive margin** | **57** | income beats machine cost |
| New events this window | 5 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 58 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 8 | `████` |
| 0.6–0.8 | 10 | `█████` |
| 0.8–0.99 | 9 | `████` |
| ≥0.99 dead | 32 | `███████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn23 Trishool | 85.1 | 572 | 572 = | cpu-small | 5 | 20% |
| 2 | sn11 TrajectoryRL | 79.6 | 4,974 | 4,974 = | cpu-small | 1 | 100% |
| 3 | sn107 Minos | 76.9 | 86.80 | 26,066 | cpu-small | 20 | 89% |
| 4 | sn98 NeverPlayAlone | 76 | 1,703 | 1,703 = | cpu-small | 1 | 100% |
| 5 | sn76 Phylax | 75.8 | 1,636 | 1,636 = | cpu-small | 1 | 100% |
| 6 | sn67 Harnyx | 73.3 | 28.74 | 851 | cpu-small | 125 | 19% |
| 7 | sn62 Ridges | 70.3 | 806 | 1,289 | rtx4090* | 6 | 57% |
| 8 | sn56 Gradients | 69.6 | 653 | 1,214 | rtx4090* | 6 | 64% |
| 9 | sn26 Perturb | 68.8 | 24.85 | 197 | rtx3060 | 11 | 50% |
| 10 | sn85 Vidaio | 68.6 | 485 | 485 = | rtx4090* | 10 | 16% |
| 11 | sn15 ORO | 68.2 | 10.89 | 18.58 | cpu-small | 93 | 91% |
| 12 | sn74 Gittensor | 66.3 | 252 | 334 | rtx4090* | 7 | 21% |
| 13 | sn124 Swarm | 65.9 | 228 | 679 | rtx4090* | 20 | 12% |
| 14 | sn38 ChronoLLM | 63 | 104 | 1,506 | rtx4090* | 10 | 52% |
| 15 | sn71 Leadpoet | 63 | 91.66 | 139 | rtx4090* | 9 | 70% |
| 16 | sn53 engy | 63 | 91.52 | 2,302 | rtx4090 | 34 | 13% |
| 17 | sn28 gm | 61.8 | 65.58 | 2,586 | rtx4090* | 14 | 56% |
| 18 | sn61 RedTeam | 58.7 | 24.68 | 94.53 | rtx4090* | 93 | 3% |
| 19 | sn9 iota | 55.8 | 10,938 | 10,938 = | rtx4090* | 3 | 55% |
| 20 | sn102 ConnitoAI | 55.7 | 9.50 | 1,523 | rtx4090* | 9 | 39% |

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
| concentrated (30–60%) | 22 |
| dominated (60–90%) | 21 |
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
| 2026-08-02T16:39 | sn24 | BURN_DROP | sn24 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-08-02T16:39 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Verify candidate recovery against pre-sig |
| 2026-08-02T16:39 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: Update scoring constants |
| 2026-08-02T15:37 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Bind verified auditor fallback workflow |
| 2026-08-02T15:37 | sn89 | SCORING_COMMIT | sn89 commit touches scoring: hf scoreboard: publish each hotkeys own r |
| 2026-08-02T12:34 | sn98 | BURN_DROP | sn98 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-08-02T12:34 | sn103 | RELEASE | sn103 released v2008 |
| 2026-08-02T12:34 | sn103 | SCORING_COMMIT | sn103 commit touches scoring: validator: release v2008 |
| 2026-08-02T11:08 | sn11 | SCORING_COMMIT | sn11 commit touches scoring: docs(incentive): takeover bar decays to a |
| 2026-08-02T11:08 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Delay candidate imports until verifier st |
| 2026-08-02T09:46 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Validate compact finalized weight ancestr |
| 2026-08-02T07:40 | sn16 | BURN_DROP | sn16 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-08-02T07:40 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-08-02T04:52 | sn61 | RELEASE | sn61 released 4.8.3 |
| 2026-08-02T04:52 | sn61 | SCORING_COMMIT | sn61 commit touches scoring: fix: set default user_id in _compare_same |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

