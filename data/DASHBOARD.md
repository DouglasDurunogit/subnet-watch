# Subnet watch — dashboard

_snapshot 2026-08-02T15:36:49Z · block 8757375 · run_status **ok**_

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
| New events this window | 2 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 57 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 8 | `████` |
| 0.6–0.8 | 10 | `█████` |
| 0.8–0.99 | 9 | `████` |
| ≥0.99 dead | 33 | `████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 77 | 87.39 | 26,242 | cpu-small | 20 | 89% |
| 2 | sn98 NeverPlayAlone | 76 | 1,714 | 1,714 = | cpu-small | 1 | 100% |
| 3 | sn76 Phylax | 75.9 | 1,645 | 1,645 = | cpu-small | 1 | 100% |
| 4 | sn67 Harnyx | 73.3 | 28.88 | 855 | cpu-small | 125 | 19% |
| 5 | sn23 Trishool | 72.3 | 576 | 576 = | cpu-small | 5 | 20% |
| 6 | sn62 Ridges | 71.1 | 1,036 | 4,771 | rtx4090* | 6 | 57% |
| 7 | sn56 Gradients | 69.6 | 655 | 1,218 | rtx4090* | 6 | 64% |
| 8 | sn26 Perturb | 68.9 | 24.94 | 198 | rtx3060 | 11 | 50% |
| 9 | sn15 ORO | 68.8 | 11.35 | 10,286 | cpu-small | 93 | 91% |
| 10 | sn85 Vidaio | 68.6 | 490 | 536 | rtx4090* | 10 | 18% |
| 11 | sn74 Gittensor | 66.4 | 258 | 334 | rtx4090* | 7 | 21% |
| 12 | sn124 Swarm | 65.9 | 229 | 681 | rtx4090* | 20 | 12% |
| 13 | sn28 gm | 63.9 | 120 | 2,805 | rtx4090* | 12 | 55% |
| 14 | sn38 ChronoLLM | 63.1 | 104 | 1,513 | rtx4090* | 10 | 52% |
| 15 | sn53 engy | 63.1 | 92.92 | 2,335 | rtx4090 | 34 | 13% |
| 16 | sn71 Leadpoet | 63 | 91.72 | 139 | rtx4090* | 9 | 70% |
| 17 | sn61 RedTeam | 58.5 | 22.77 | 92.66 | rtx4090* | 93 | 3% |
| 18 | sn102 ConnitoAI | 55.7 | 9.58 | 1,530 | rtx4090* | 9 | 39% |
| 19 | sn9 iota | 55.1 | 8,011 | 8,011 = | rtx4090* | 3 | 56% |
| 20 | sn51 lium.io | 53.3 | 10.32 | 7,876 | rtx4090* | 42 | 41% |

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
| concentrated (30–60%) | 21 |
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
| 2026-08-02T04:52 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Preserve scoring state across gateway res |
| 2026-08-02T04:52 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: Harden scoring inputs and screening |
| 2026-08-02T04:52 | sn111 | README_TASK_DIFF | sn111 README task/scoring sections changed |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

