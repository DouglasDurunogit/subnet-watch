# Subnet watch — dashboard

_snapshot 2026-10-17T15:58:08Z · block 9304172 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 58 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 99 | `miner_burn` < 0.99 |
| Ranked | 99 | passed every gate |
| **Positive margin** | **58** | income beats machine cost |
| New events this window | 5 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 66 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 6 | `███` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 29 | `████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn41 Almanac | 76 | 59.19 | 98.67 | cpu-small | 120 | 6% |
| 2 | sn3 Teutonic | 74.6 | 2,902 | 2,902 = | rtx4090* | 5 | 40% |
| 3 | sn102 ConnitoAI | 70 | 731 | 1,656 | rtx4090* | 6 | 38% |
| 4 | sn53 engy | 69.3 | 593 | 2,465 | rtx4090 | 24 | 16% |
| 5 | sn91 cascade | 68.9 | 207 | 831 | cpu-small | 5 | 52% |
| 6 | sn1 Apex | 68.6 | 484 | 953 | rtx4090* | 5 | 54% |
| 7 | sn82 Noah | 68.1 | 647 | 647 = | rtx4090* | 64 | 2% |
| 8 | sn58 Attune | 67.8 | 393 | 634 | rtx4090* | 5 | 71% |
| 9 | sn67 Harnyx | 67.8 | 7.37 | 152 | cpu-small | 184 | 6% |
| 10 | sn107 Minos | 67.6 | 261 | 22,153 | cpu-small | 20 | 80% |
| 11 | sn15 ORO | 67.2 | 8.02 | 16.00 | cpu-small | 65 | 97% |
| 12 | sn4 Targon | 66.8 | 9,815 | 28,939 | rtx4090* | 5 | 70% |
| 13 | sn14 Cacheon | 66.5 | 264 | 1,839 | rtx4090* | 9 | 52% |
| 14 | sn120 Affine | 63.7 | 125 | 643 | rtx4090* | 178 | 2% |
| 15 | sn66 conjectures | 62.9 | 88.49 | 201 | rtx4090* | 4 | 84% |
| 16 | sn92 REAX | 62.2 | 93.33 | 3,044 | rtx4090 | 232 | 11% |
| 17 | sn97 Ingot | 61.5 | 2,026 | 2,026 = | rtx4090* | 4 | 40% |
| 18 | sn61 RedTeam | 61.4 | 57.03 | 96.09 | rtx4090* | 129 | 1% |
| 19 | sn28 SayGM | 58.5 | 25.73 | 2,102 | rtx4090* | 102 | 41% |
| 20 | sn81 Reliquary | 58.3 | 21.49 | 123 | rtx4090* | 18 | 81% |

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
| concentrated (30–60%) | 25 |
| dominated (60–90%) | 26 |
| captured (>90%) | 24 |

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
| 2026-10-17T15:58 | sn7 | RELEASE | sn7 released release-20261017-152034: Bound event ingest per pass and  |
| 2026-10-17T15:58 | sn28 | RELEASE | sn28 released v0.5.2 |
| 2026-10-17T15:58 | sn28 | SCORING_COMMIT | sn28 commit touches scoring: chore(release): promote gm-miner 0.5.2 (# |
| 2026-10-17T15:58 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-4601 - [P0] Validator: fail a node wh |
| 2026-10-17T15:58 | sn92 | RELEASE | sn92 released v1.2.0-rc8 |
| 2026-10-17T12:28 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: feat(scoring): absence charges stop once  |
| 2026-10-17T12:28 | sn25 | RELEASE | sn25 released v2026.10.17-1074370910 |
| 2026-10-17T12:28 | sn51 | RELEASE | sn51 released executor-v1.142 |
| 2026-10-17T12:28 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: Sysbox installer: show the verify contain |
| 2026-10-17T12:28 | sn92 | RELEASE | sn92 released v1.2.0-rc7.post4 |
| 2026-10-17T08:43 | sn15 | RELEASE | sn15 released v2.5.5: Bound validator reads of sandbox output files (# |
| 2026-10-17T08:43 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: Bound validator reads of sandbox output f |
| 2026-10-17T08:43 | sn25 | RELEASE | sn25 released v2026.10.16-1074191560 |
| 2026-10-17T08:43 | sn37 | SCORING_COMMIT | sn37 commit touches scoring: fix(miner): enable reviewed runtime479 fu |
| 2026-10-17T08:43 | sn37 | README_TASK_DIFF | sn37 README task/scoring sections changed |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

