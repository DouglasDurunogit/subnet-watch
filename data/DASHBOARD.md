# Subnet watch — dashboard

_snapshot 2026-08-02T09:45:40Z · block 8755619 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 54 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 96 | `miner_burn` < 0.99 |
| Ranked | 96 | passed every gate |
| **Positive margin** | **54** | income beats machine cost |
| New events this window | 1 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 57 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 7 | `███` |
| 0.6–0.8 | 11 | `█████` |
| 0.8–0.99 | 10 | `█████` |
| ≥0.99 dead | 32 | `████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn23 Trishool | 85.1 | 578 | 578 = | cpu-small | 5 | 20% |
| 2 | sn107 Minos | 77.3 | 92.85 | 27,099 | cpu-small | 20 | 90% |
| 3 | sn67 Harnyx | 73.4 | 29.17 | 863 | cpu-small | 122 | 19% |
| 4 | sn62 Ridges | 71.2 | 1,063 | 4,893 | rtx4090* | 6 | 57% |
| 5 | sn102 ConnitoAI | 71 | 989 | 994 | rtx4090* | 4 | 25% |
| 6 | sn56 Gradients | 69.6 | 658 | 1,223 | rtx4090* | 6 | 64% |
| 7 | sn26 Perturb | 68.8 | 24.78 | 203 | rtx3060 | 11 | 50% |
| 8 | sn15 ORO | 68.6 | 11.31 | 10,208 | cpu-small | 90 | 91% |
| 9 | sn85 Vidaio | 67.4 | 339 | 589 | rtx4090* | 10 | 19% |
| 10 | sn74 Gittensor | 66.5 | 267 | 312 | rtx4090* | 7 | 23% |
| 11 | sn124 Swarm | 66 | 232 | 691 | rtx4090* | 20 | 12% |
| 12 | sn38 ChronoLLM | 63.2 | 107 | 1,557 | rtx4090* | 10 | 52% |
| 13 | sn53 engy | 63.1 | 93.90 | 2,357 | rtx4090 | 34 | 13% |
| 14 | sn71 Leadpoet | 63.1 | 92.92 | 140 | rtx4090* | 9 | 70% |
| 15 | sn61 RedTeam | 58.3 | 21.90 | 92.16 | rtx4090* | 96 | 3% |
| 16 | sn9 iota | 56.2 | 13,013 | 13,013 = | rtx4090* | 3 | 65% |
| 17 | sn28 gm | 55.7 | 11.21 | 2,554 | rtx4090* | 15 | 61% |
| 18 | sn97 Albedo | 52.8 | 3,065 | 3,065 = | rtx4090* | 5 | 20% |
| 19 | sn90 KubeTEE AI Facto | 52.7 | 3,015 | 3,015 = | rtx4090* | 2 | 77% |
| 20 | sn51 lium.io | 52.2 | 8.59 | 7,583 | rtx4090* | 45 | 40% |

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
| concentrated (30–60%) | 19 |
| dominated (60–90%) | 25 |
| captured (>90%) | 25 |

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
| 2026-08-01T23:28 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Protect validator settlement constants |
| 2026-08-01T21:07 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Fix baseline replay and compact weight va |
| 2026-08-01T21:07 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: Wire production Silver run metadata into |
| 2026-08-01T20:01 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Refresh validator ancestry workflow manif |
| 2026-08-01T17:45 | sn99 | BURN_DROP | sn99 burn fell 1.000 -> 0.000 - miners can earn again |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

