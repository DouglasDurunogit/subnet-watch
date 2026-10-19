# Subnet watch — dashboard

_snapshot 2026-10-19T10:42:00Z · block 9316992 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 56 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 99 | `miner_burn` < 0.99 |
| Ranked | 99 | passed every gate |
| **Positive margin** | **56** | income beats machine cost |
| New events this window | 9 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 66 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 6 | `███` |
| 0.6–0.8 | 10 | `████` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 29 | `████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn41 Almanac | 76.4 | 64.30 | 110 | cpu-small | 120 | 8% |
| 2 | sn3 Teutonic | 74.4 | 2,780 | 7,428 | rtx4090* | 5 | 40% |
| 3 | sn91 cascade | 72.5 | 604 | 1,613 | cpu-small | 5 | 52% |
| 4 | sn102 ConnitoAI | 69.8 | 695 | 1,261 | rtx4090* | 6 | 29% |
| 5 | sn67 Harnyx | 69.4 | 10.70 | 268 | cpu-small | 161 | 11% |
| 6 | sn53 engy | 69.1 | 572 | 2,379 | rtx4090 | 24 | 16% |
| 7 | sn82 Noah | 68.9 | 722 | 755 | rtx4090* | 60 | 2% |
| 8 | sn1 Apex | 68.5 | 468 | 746 | rtx4090* | 5 | 59% |
| 9 | sn107 Minos | 67.4 | 246 | 20,922 | cpu-small | 20 | 80% |
| 10 | sn15 ORO | 65.4 | 6.36 | 16,214 | cpu-small | 55 | 98% |
| 11 | sn120 Affine | 64.5 | 168 | 299 | rtx4090* | 229 | 1% |
| 12 | sn14 Cacheon | 64.3 | 136 | 3,830 | rtx4090* | 11 | 55% |
| 13 | sn66 conjectures | 63.7 | 112 | 233 | rtx4090* | 4 | 80% |
| 14 | sn97 Ingot | 61.5 | 2,015 | 2,015 = | rtx4090* | 5 | 20% |
| 15 | sn55 NIOME | 61.5 | 58.86 | 495 | rtx4090* | 11 | 30% |
| 16 | sn61 RedTeam | 61.4 | 60.65 | 110 | rtx4090* | 120 | 1% |
| 17 | sn92 REAX | 60.7 | 85.82 | 3,481 | rtx4090 | 243 | 11% |
| 18 | sn49 Nepher Robotics | 59.7 | 1,192 | 3,886 | rtx4090* | 4 | 68% |
| 19 | sn80 OpenRoboto | 59.6 | 1,168 | 2,760 | rtx4090* | 11 | 35% |
| 20 | sn81 Reliquary | 59.6 | 32.32 | 154 | rtx4090* | 8 | 90% |

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
| wide (<30%) | 28 |
| concentrated (30–60%) | 19 |
| dominated (60–90%) | 28 |
| captured (>90%) | 23 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 95 |
| README keywords (GUESS) | 13 |
| min_compute.yml (curated) | 10 |
| code-submission (validator runs it) | 9 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-10-19T10:42 | sn25 | RELEASE | sn25 released v2026.10.19-1076002880 |
| 2026-10-19T10:42 | sn51 | RELEASE | sn51 released miner-v1.007 |
| 2026-10-19T10:42 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-2834 - [P2] shadow the verify agent o |
| 2026-10-19T10:42 | sn53 | SCORING_COMMIT | sn53 commit touches scoring: Merge pull request #56 from hanlinai/fix/ |
| 2026-10-19T10:42 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-10-19T10:42 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Preserve first-party funding context thro |
| 2026-10-19T10:42 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Merge pull request #315 from Umi-BitSign/ |
| 2026-10-19T10:42 | sn92 | RELEASE | sn92 released v1.2.0-rc9.post3 |
| 2026-10-19T10:42 | sn122 | BURN_DROP | sn122 burn fell 1.000 -> 0.700 - miners can earn again |
| 2026-10-19T05:03 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: feat(executor): the scored run can wait f |
| 2026-10-19T05:03 | sn25 | RELEASE | sn25 released v2026.10.18-1075707760 |
| 2026-10-19T05:03 | sn51 | RELEASE | sn51 released executor-v1.143 |
| 2026-10-19T05:03 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-3980 - Validator: customer create rem |
| 2026-10-19T05:03 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Resolve verified LinkedIn company redirec |
| 2026-10-19T05:03 | sn89 | README_TASK_DIFF | sn89 README task/scoring sections changed |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

