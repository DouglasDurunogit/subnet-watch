# Subnet watch — dashboard

_snapshot 2026-10-08T14:58:11Z · block 9239078 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 61 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 101 | `miner_burn` < 0.99 |
| Ranked | 101 | passed every gate |
| **Positive margin** | **61** | income beats machine cost |
| New events this window | 10 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 68 | `████████████████████████████` |
| 0–0.2 | 6 | `██` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 6 | `██` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 8 | `███` |
| ≥0.99 dead | 27 | `███████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn3 Teutonic | 74.9 | 3,189 | 6,385 | rtx4090* | 5 | 30% |
| 2 | sn91 cascade | 72.1 | 542 | 2,169 | cpu-small | 5 | 52% |
| 3 | sn38 ChronoLLM | 69.8 | 285 | 1,939 | cpu-small | 9 | 52% |
| 4 | sn80 OpenRoboto | 69.3 | 594 | 3,110 | rtx4090* | 7 | 35% |
| 5 | sn1 Apex | 68.7 | 502 | 882 | rtx4090* | 4 | 73% |
| 6 | sn46 Instant | 68.7 | 196 | 238 | cpu-small | 9 | 45% |
| 7 | sn67 Harnyx | 68.6 | 8.31 | 1,001 | cpu-small | 136 | 35% |
| 8 | sn15 ORO | 67.2 | 8.54 | 19,003 | cpu-small | 57 | 97% |
| 9 | sn4 Targon | 66.9 | 10,097 | 29,764 | rtx4090* | 5 | 70% |
| 10 | sn26 Perturb | 66.4 | 252 | 420 | rtx3060 | 4 | 60% |
| 11 | sn62 Ridges | 63.7 | 113 | 1,379 | rtx4090* | 34 | 17% |
| 12 | sn120 Affine | 62.5 | 146 | 334 | rtx4090* | 243 | 1% |
| 13 | sn65 True Performance | 62.5 | 82.24 | 173 | rtx4090* | 6 | 75% |
| 14 | sn61 RedTeam | 62.5 | 81.61 | 116 | rtx4090* | 125 | 1% |
| 15 | sn28 SayGM | 61.9 | 68.11 | 2,415 | rtx4090* | 64 | 23% |
| 16 | sn53 engy | 60.3 | 1,408 | 4,654 | rtx4090 | 18 | 17% |
| 17 | sn23 Trishool | 59.5 | 435 | 435 = | cpu-small | 3 | 80% |
| 18 | sn41 Almanac | 58.7 | 26.02 | 115 | cpu-small | 139 | 2% |
| 19 | sn14 Cacheon | 58 | 20.08 | 1,718 | rtx4090* | 7 | 69% |
| 20 | sn111 Claims | 57.9 | 20.66 | 244 | rtx4090* | 6 | 90% |

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
| wide (<30%) | 22 |
| concentrated (30–60%) | 23 |
| dominated (60–90%) | 29 |
| captured (>90%) | 24 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 96 |
| README keywords (GUESS) | 12 |
| min_compute.yml (curated) | 10 |
| code-submission (validator runs it) | 9 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-10-08T14:58 | sn3 | SCORING_COMMIT | sn3 commit touches scoring: Add competition dataset panel and update e |
| 2026-10-08T14:58 | sn15 | RELEASE | sn15 released v2.4.0: Prepare runtime 3.5 validator and practice deliv |
| 2026-10-08T14:58 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: Prepare runtime 3.5 validator and practic |
| 2026-10-08T14:58 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: fix(scoring): copy groups agree on one ea |
| 2026-10-08T14:58 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-4001 - validator: shadow never delays |
| 2026-10-08T14:58 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge PR #276: verify judging through the |
| 2026-10-08T14:58 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: docs(corpus): the open route and the agen |
| 2026-10-08T14:58 | sn116 | RELEASE | sn116 released worker-images-v2 |
| 2026-10-08T14:58 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Merge pull request #815 from carbonphysi |
| 2026-10-08T14:58 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Keep learner startup independent of an u |
| 2026-10-08T07:46 | sn25 | BURN_DROP | sn25 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-10-08T07:46 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Merge runtime upgrade tolerance for the p |
| 2026-10-08T07:46 | sn51 | RELEASE | sn51 released executor-v1.138 |
| 2026-10-08T07:46 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: validator: remove the failed container be |
| 2026-10-08T07:46 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge remote-tracking branch 'origin/main |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

