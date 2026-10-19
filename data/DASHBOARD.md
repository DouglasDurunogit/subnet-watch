# Subnet watch — dashboard

_snapshot 2026-10-19T17:12:29Z · block 9318944 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 55 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 98 | `miner_burn` < 0.99 |
| Ranked | 98 | passed every gate |
| **Positive margin** | **55** | income beats machine cost |
| New events this window | 10 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 67 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 10 | `████` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 30 | `█████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn41 Almanac | 74.6 | 41.16 | 111 | cpu-small | 122 | 8% |
| 2 | sn3 Teutonic | 74.3 | 2,705 | 7,227 | rtx4090* | 5 | 40% |
| 3 | sn91 cascade | 72.4 | 594 | 1,584 | cpu-small | 5 | 52% |
| 4 | sn67 Harnyx | 69.4 | 10.58 | 265 | cpu-small | 163 | 11% |
| 5 | sn53 engy | 69.1 | 560 | 2,331 | rtx4090 | 24 | 16% |
| 6 | sn82 Noah | 69 | 722 | 755 | rtx4090* | 60 | 2% |
| 7 | sn1 Apex | 68.3 | 450 | 999 | rtx4090* | 5 | 55% |
| 8 | sn102 ConnitoAI | 67.9 | 399 | 1,302 | rtx4090* | 7 | 30% |
| 9 | sn23 Trishool | 67.6 | 239 | 239 = | cpu-small | 4 | 80% |
| 10 | sn107 Minos | 67.5 | 252 | 21,359 | cpu-small | 20 | 80% |
| 11 | sn15 ORO | 66.3 | 6.20 | 16,126 | cpu-small | 56 | 98% |
| 12 | sn120 Affine | 64.3 | 152 | 287 | rtx4090* | 237 | 1% |
| 13 | sn66 conjectures | 63.7 | 113 | 234 | rtx4090* | 4 | 80% |
| 14 | sn14 Cacheon | 63.6 | 111 | 4,325 | rtx4090* | 11 | 63% |
| 15 | sn55 NIOME | 62.3 | 73.41 | 604 | rtx4090* | 11 | 30% |
| 16 | sn97 Ingot | 61.5 | 2,019 | 2,019 = | rtx4090* | 5 | 20% |
| 17 | sn61 RedTeam | 61.5 | 60.59 | 110 | rtx4090* | 123 | 1% |
| 18 | sn92 REAX | 59.7 | 85.70 | 3,383 | rtx4090 | 225 | 11% |
| 19 | sn80 OpenRoboto | 59.6 | 1,145 | 2,706 | rtx4090* | 11 | 35% |
| 20 | sn81 Reliquary | 59.6 | 32.40 | 210 | rtx4090* | 8 | 88% |

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
| dominated (60–90%) | 27 |
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
| 2026-10-19T17:12 | sn7 | RELEASE | sn7 released release-20261019-165322 |
| 2026-10-19T17:12 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: feat(scoring): the pooled count score can |
| 2026-10-19T17:12 | sn22 | SCORING_COMMIT | sn22 commit touches scoring: fix(task-api): reference vectors finish a |
| 2026-10-19T17:12 | sn25 | RELEASE | sn25 released v2026.10.19-1076177550 |
| 2026-10-19T17:12 | sn28 | RELEASE | sn28 released v0.5.3-dev |
| 2026-10-19T17:12 | sn51 | RELEASE | sn51 released miner-v1.008 |
| 2026-10-19T17:12 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-4124 - [P2] validator: record EXECUTO |
| 2026-10-19T17:12 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-10-19T17:12 | sn82 | SCORING_COMMIT | sn82 commit touches scoring: Allow configured validator publishing ide |
| 2026-10-19T17:12 | sn90 | README_TASK_DIFF | sn90 README task/scoring sections changed |
| 2026-10-19T10:42 | sn25 | RELEASE | sn25 released v2026.10.19-1076002880 |
| 2026-10-19T10:42 | sn51 | RELEASE | sn51 released miner-v1.007 |
| 2026-10-19T10:42 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-2834 - [P2] shadow the verify agent o |
| 2026-10-19T10:42 | sn53 | SCORING_COMMIT | sn53 commit touches scoring: Merge pull request #56 from hanlinai/fix/ |
| 2026-10-19T10:42 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

