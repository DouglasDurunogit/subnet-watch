# Subnet watch — dashboard

_snapshot 2026-08-17T15:48:40Z · block 8865413 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 51 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 91 | `miner_burn` < 0.99 |
| Ranked | 91 | passed every gate |
| **Positive margin** | **51** | income beats machine cost |
| New events this window | 1 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 62 | `████████████████████████████` |
| 0–0.2 | 4 | `██` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 7 | `███` |
| 0.6–0.8 | 7 | `███` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 37 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn26 Perturb | 72 | 55.11 | 1,623 | rtx3060 | 10 | 70% |
| 2 | sn67 Harnyx | 72 | 20.39 | 382 | cpu-small | 129 | 11% |
| 3 | sn91 cascade | 69.1 | 564 | 2,282 | rtx4090* | 5 | 51% |
| 4 | sn15 ORO | 67.9 | 10.94 | 12,459 | cpu-small | 66 | 94% |
| 5 | sn96 Verathos | 67.8 | 19.20 | 508 | rtx4090 | 69 | 41% |
| 6 | sn21 AdTAO | 67.7 | 7.67 | 34.36 | cpu-small | 88 | 45% |
| 7 | sn38 ChronoLLM | 66.1 | 102 | 1,388 | cpu-small | 10 | 52% |
| 8 | sn124 Swarm | 65.9 | 226 | 507 | rtx4090* | 24 | 11% |
| 9 | sn107 Minos | 64.4 | 121 | 33,857 | cpu-small | 20 | 90% |
| 10 | sn2 DSperse | 62.8 | 86.66 | 135 | rtx4090* | 5 | 82% |
| 11 | sn55 NIOME | 61.6 | 58.93 | 495 | rtx4090* | 11 | 29% |
| 12 | sn102 ConnitoAI | 57.6 | 635 | 1,239 | rtx4090* | 7 | 25% |
| 13 | sn61 RedTeam | 57.4 | 16.34 | 400 | rtx4090* | 82 | 10% |
| 14 | sn51 lium.io | 57.3 | 23.00 | 2,549 | rtx4090* | 56 | 79% |
| 15 | sn28 gm | 55.9 | 11.83 | 419 | rtx4090* | 39 | 83% |
| 16 | sn68 NOVA | 55.1 | 8,069 | 8,069 = | rtx4090* | 1 | 100% |
| 17 | sn120 Affine | 54.6 | 6,606 | 6,606 = | rtx4090* | 5 | 20% |
| 18 | sn93 Bitcast | 54.3 | 237 | 528 | rtx4090* | 4 | 84% |
| 19 | sn80 OpenRoboto | 53.2 | 173 | 626 | rtx4090* | 4 | 91% |
| 20 | sn97 Albedo | 52.6 | 2,824 | 2,824 = | rtx4090* | 5 | 20% |

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
| concentrated (30–60%) | 18 |
| dominated (60–90%) | 20 |
| captured (>90%) | 26 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 113 |
| code-submission (validator runs it) | 5 |
| README keywords (GUESS) | 5 |
| min_compute.yml (curated) | 4 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-08-17T15:52 | sn121 | BURN_DROP | sn121 burn fell 1.000 -> 0.620 - miners can earn again |
| 2026-08-17T13:03 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: feat: add adaptive miner selection and r |
| 2026-08-17T13:03 | sn114 | SCORING_COMMIT | sn114 commit touches scoring: hotfix(scoring): exclude comp 112 stage  |
| 2026-08-17T11:12 | sn85 | SCORING_COMMIT | sn85 commit touches scoring: treat miner sandbox raised error as miner |
| 2026-08-17T10:46 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-08-17T10:46 | sn85 | SCORING_COMMIT | sn85 commit touches scoring: ensure comp scoring worker can access Mod |
| 2026-08-17T10:46 | sn114 | SCORING_COMMIT | sn114 commit touches scoring: perf(validator): reduce validator write  |
| 2026-08-17T09:54 | sn10 | SCORING_COMMIT | sn10 commit touches scoring: feat(bench): score the full workload trac |
| 2026-08-17T08:59 | sn85 | SCORING_COMMIT | sn85 commit touches scoring: reinvite miners rejected with flag INVITA |
| 2026-08-17T08:07 | sn51 | RELEASE | sn51 released executor-v1.120 |
| 2026-08-17T08:07 | sn75 | SCORING_COMMIT | sn75 commit touches scoring: feat(compute-scoring): root-settable dedi |
| 2026-08-17T06:00 | sn2 | BURN_DROP | sn2 burn fell 1.000 -> 0.823 - miners can earn again |
| 2026-08-17T06:00 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Refresh provider failures during recovery |
| 2026-08-17T01:52 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Bound validator worker startup verificati |
| 2026-08-16T17:31 | sn100 | RELEASE | sn100 released v3.3.24 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

