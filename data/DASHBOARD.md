# Subnet watch — dashboard

_snapshot 2026-08-02T12:34:32Z · block 8756463 · run_status **ok**_

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
| New events this window | 3 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 58 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 8 | `████` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 11 | `█████` |
| ≥0.99 dead | 31 | `███████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn23 Trishool | 85.1 | 575 | 575 = | cpu-small | 5 | 20% |
| 2 | sn107 Minos | 77.3 | 93.91 | 26,867 | cpu-small | 19 | 89% |
| 3 | sn98 NeverPlayAlone | 76 | 1,710 | 1,710 = | cpu-small | 1 | 100% |
| 4 | sn76 Phylax | 75.8 | 1,634 | 1,634 = | cpu-small | 1 | 100% |
| 5 | sn67 Harnyx | 73.4 | 29.02 | 861 | cpu-small | 124 | 19% |
| 6 | sn62 Ridges | 71.2 | 1,056 | 4,860 | rtx4090* | 6 | 57% |
| 7 | sn56 Gradients | 69.6 | 654 | 1,217 | rtx4090* | 6 | 64% |
| 8 | sn26 Perturb | 68.9 | 25.48 | 195 | rtx3060 | 11 | 50% |
| 9 | sn15 ORO | 68.9 | 11.22 | 10,129 | cpu-small | 91 | 91% |
| 10 | sn85 Vidaio | 68.8 | 520 | 532 | rtx4090* | 10 | 18% |
| 11 | sn74 Gittensor | 66.4 | 253 | 331 | rtx4090* | 7 | 22% |
| 12 | sn124 Swarm | 66 | 230 | 684 | rtx4090* | 20 | 12% |
| 13 | sn38 ChronoLLM | 63.1 | 106 | 1,542 | rtx4090* | 10 | 52% |
| 14 | sn53 engy | 63.1 | 93.61 | 2,350 | rtx4090 | 34 | 13% |
| 15 | sn71 Leadpoet | 63.1 | 93.09 | 141 | rtx4090* | 9 | 70% |
| 16 | sn28 gm | 61.8 | 64.68 | 2,768 | rtx4090* | 14 | 57% |
| 17 | sn61 RedTeam | 58.3 | 22.06 | 91.37 | rtx4090* | 94 | 3% |
| 18 | sn9 iota | 56.2 | 12,994 | 12,994 = | rtx4090* | 3 | 65% |
| 19 | sn102 ConnitoAI | 54.8 | 7.13 | 2,934 | rtx4090* | 6 | 73% |
| 20 | sn51 lium.io | 53.1 | 9.95 | 7,452 | rtx4090* | 43 | 41% |

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
| dominated (60–90%) | 24 |
| captured (>90%) | 26 |

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
| 2026-08-02T01:17 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Recycle scoring workers at baseline check |
| 2026-08-02T01:17 | sn97 | SCORING_COMMIT | sn97 commit touches scoring: feat: Added display overall score + margi |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

