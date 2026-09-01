# Subnet watch — dashboard

_snapshot 2026-09-01T10:31:24Z · block 8971824 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 58 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 94 | `miner_burn` < 0.99 |
| Ranked | 94 | passed every gate |
| **Positive margin** | **58** | income beats machine cost |
| New events this window | 4 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 65 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 8 | `███` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 34 | `███████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn92 MicroTensor | 81.2 | 218 | 2,124 | cpu-small | 9 | 60% |
| 2 | sn3 Teutonic | 75.5 | 3,761 | 3,761 = | rtx4090* | 5 | 20% |
| 3 | sn76 Phylax | 74.8 | 43.64 | 92.33 | cpu-small | 21 | 20% |
| 4 | sn67 Harnyx | 72.4 | 22.97 | 1,178 | cpu-small | 121 | 32% |
| 5 | sn15 ORO | 71.4 | 26.11 | 21,583 | cpu-small | 63 | 94% |
| 6 | sn91 cascade | 69.9 | 722 | 2,914 | rtx4090* | 5 | 52% |
| 7 | sn96 Verathos | 69.1 | 26.79 | 148 | rtx4090 | 79 | 43% |
| 8 | sn56 Gradients | 67.7 | 378 | 1,043 | rtx4090* | 7 | 71% |
| 9 | sn111 Claims | 67.1 | 327 | 2,925 | rtx4090* | 5 | 70% |
| 10 | sn124 Swarm | 66.5 | 268 | 869 | rtx4090* | 25 | 11% |
| 11 | sn61 RedTeam | 64.9 | 162 | 238 | rtx4090* | 48 | 3% |
| 12 | sn21 AdTAO | 64.5 | 4.04 | 106 | cpu-small | 14 | 45% |
| 13 | sn81 Reliquary | 64.4 | 138 | 248 | rtx4090* | 34 | 6% |
| 14 | sn107 Minos | 64.4 | 123 | 37,328 | cpu-small | 20 | 90% |
| 15 | sn60 Bitsec.ai | 64.3 | 1,808 | 1,808 = | cpu-small | 2 | 50% |
| 16 | sn79 MVTRX | 64.1 | 4.18 | 390 | cpu-small | 227 | 9% |
| 17 | sn54 Yanez | 63.5 | 5.29 | 942 | a4000 | 97 | 35% |
| 18 | sn55 NIOME | 62.5 | 78.55 | 643 | rtx4090* | 11 | 29% |
| 19 | sn101 Tag101 | 61.9 | 0.69 | 0.96 | cpu-small | 240 | 90% |
| 20 | sn28 gm | 61.6 | 61.18 | 4,859 | rtx4090* | 41 | 40% |

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
| wide (<30%) | 23 |
| concentrated (30–60%) | 19 |
| dominated (60–90%) | 21 |
| captured (>90%) | 28 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 101 |
| code-submission (validator runs it) | 10 |
| min_compute.yml (curated) | 10 |
| README keywords (GUESS) | 6 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-09-01T10:31 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Verify carried conviction under its sourc |
| 2026-09-01T10:31 | sn63 | SCORING_COMMIT | sn63 commit touches scoring: Support multiple validations on single va |
| 2026-09-01T10:31 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-09-01T10:31 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: feat(selection): harden adaptive miner s |
| 2026-09-01T05:44 | sn80 | README_TASK_DIFF | sn80 README task/scoring sections changed |
| 2026-09-01T00:34 | sn25 | RELEASE | sn25 released v2026.8.31-1034210530 |
| 2026-09-01T00:34 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Batch carried fleet refresh verification |
| 2026-08-31T20:48 | sn15 | RELEASE | sn15 released v1.2.12 |
| 2026-08-31T20:48 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: fix(validator): don't fail runs on incomp |
| 2026-08-31T20:48 | sn38 | SCORING_COMMIT | sn38 commit touches scoring: Update validator image to the latest vers |
| 2026-08-31T20:48 | sn38 | README_TASK_DIFF | sn38 README task/scoring sections changed |
| 2026-08-31T20:48 | sn50 | RELEASE | sn50 released v1.12.0 |
| 2026-08-31T20:48 | sn92 | RELEASE | sn92 released v0.3.0 |
| 2026-08-31T20:48 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: Grant the validator container the capabil |
| 2026-08-31T20:48 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: feat(selection): diversify adaptive mine |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

