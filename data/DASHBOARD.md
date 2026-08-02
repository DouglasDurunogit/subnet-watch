# Subnet watch — dashboard

_snapshot 2026-08-02T14:17:02Z · block 8756976 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 57 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 97 | `miner_burn` < 0.99 |
| Ranked | 97 | passed every gate |
| **Positive margin** | **57** | income beats machine cost |
| New events this window | 0 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 58 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 6 | `███` |
| 0.6–0.8 | 11 | `█████` |
| 0.8–0.99 | 10 | `█████` |
| ≥0.99 dead | 31 | `███████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 77.1 | 88.89 | 26,492 | cpu-small | 20 | 89% |
| 2 | sn98 NeverPlayAlone | 76 | 1,713 | 1,713 = | cpu-small | 1 | 100% |
| 3 | sn76 Phylax | 75.8 | 1,637 | 1,637 = | cpu-small | 1 | 100% |
| 4 | sn67 Harnyx | 73.3 | 29.05 | 860 | cpu-small | 125 | 19% |
| 5 | sn23 Trishool | 72.3 | 576 | 576 = | cpu-small | 5 | 20% |
| 6 | sn62 Ridges | 71.2 | 1,047 | 4,822 | rtx4090* | 6 | 57% |
| 7 | sn102 ConnitoAI | 69.9 | 715 | 1,438 | rtx4090* | 5 | 37% |
| 8 | sn56 Gradients | 69.6 | 655 | 1,218 | rtx4090* | 6 | 64% |
| 9 | sn26 Perturb | 68.9 | 25.51 | 195 | rtx3060 | 11 | 50% |
| 10 | sn15 ORO | 68.7 | 11.37 | 10,239 | cpu-small | 92 | 91% |
| 11 | sn85 Vidaio | 68.6 | 485 | 485 = | rtx4090* | 10 | 16% |
| 12 | sn74 Gittensor | 66.4 | 253 | 333 | rtx4090* | 7 | 21% |
| 13 | sn124 Swarm | 65.9 | 229 | 680 | rtx4090* | 20 | 12% |
| 14 | sn38 ChronoLLM | 63.1 | 105 | 1,531 | rtx4090* | 10 | 52% |
| 15 | sn71 Leadpoet | 63.1 | 92.75 | 140 | rtx4090* | 9 | 70% |
| 16 | sn53 engy | 63 | 92.11 | 2,316 | rtx4090 | 34 | 13% |
| 17 | sn28 gm | 62 | 69.31 | 2,412 | rtx4090* | 13 | 61% |
| 18 | sn61 RedTeam | 58.4 | 22.14 | 91.57 | rtx4090* | 94 | 3% |
| 19 | sn9 iota | 56.2 | 12,964 | 12,964 = | rtx4090* | 3 | 65% |
| 20 | sn90 KubeTEE AI Facto | 52.8 | 3,061 | 3,061 = | rtx4090* | 2 | 76% |

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
| concentrated (30–60%) | 19 |
| dominated (60–90%) | 25 |
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

