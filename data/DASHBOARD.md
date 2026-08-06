# Subnet watch — dashboard

_snapshot 2026-08-06T10:18:41Z · block 8784573 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 54 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 90 | `miner_burn` < 0.99 |
| Ranked | 90 | passed every gate |
| **Positive margin** | **54** | income beats machine cost |
| New events this window | 4 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 56 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 3 | `██` |
| 0.4–0.6 | 8 | `████` |
| 0.6–0.8 | 7 | `████` |
| 0.8–0.99 | 11 | `██████` |
| ≥0.99 dead | 38 | `███████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 77.7 | 88.43 | 444 | cpu-small | 10 | 29% |
| 2 | sn107 Minos | 77.5 | 100.00 | 27,870 | cpu-small | 20 | 90% |
| 3 | sn60 Bitsec.ai | 76.9 | 2,266 | 2,266 = | cpu-small | 2 | 90% |
| 4 | sn67 Harnyx | 72.4 | 23.43 | 1,094 | cpu-small | 126 | 25% |
| 5 | sn102 ConnitoAI | 71.5 | 1,146 | 1,506 | rtx4090* | 6 | 28% |
| 6 | sn91 cascade | 70.1 | 760 | 3,065 | rtx4090* | 5 | 52% |
| 7 | sn114 SOMA | 69.6 | 661 | 1,666 | rtx4090* | 4 | 65% |
| 8 | sn62 Ridges | 69 | 544 | 1,969 | rtx4090* | 7 | 35% |
| 9 | sn26 Perturb | 68.4 | 22.18 | 907 | rtx3060 | 11 | 51% |
| 10 | sn15 ORO | 68 | 9.92 | 10,338 | cpu-small | 81 | 93% |
| 11 | sn96 Verathos | 67.4 | 17.50 | 129 | rtx4090 | 85 | 43% |
| 12 | sn41 Almanac | 67.4 | 7.10 | 63.85 | cpu-small | 52 | 82% |
| 13 | sn74 Gittensor | 66.1 | 232 | 386 | rtx4090* | 9 | 18% |
| 14 | sn124 Swarm | 65.7 | 214 | 614 | rtx4090* | 23 | 10% |
| 15 | sn21 AdTAO | 65.7 | 4.91 | 22.59 | cpu-small | 142 | 45% |
| 16 | sn80 OpenRoboto | 62.2 | 70.71 | 268 | rtx4090* | 4 | 91% |
| 17 | sn61 RedTeam | 61.9 | 66.03 | 170 | rtx4090* | 40 | 5% |
| 18 | sn101 Tag101 | 59.1 | 0.07 | 0.67 | cpu-small | 242 | 90% |
| 19 | sn28 gm | 56.9 | 15.51 | 6,357 | rtx4090* | 19 | 69% |
| 20 | sn56 Gradients | 56.4 | 452 | 953 | rtx4090* | 7 | 70% |

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
| concentrated (30–60%) | 17 |
| dominated (60–90%) | 22 |
| captured (>90%) | 25 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 104 |
| code-submission (validator runs it) | 9 |
| min_compute.yml (curated) | 9 |
| README keywords (GUESS) | 5 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-08-06T10:19 | sn15 | RELEASE | sn15 released v1.2.6: docs(validator): correct stale weight-salt fallb |
| 2026-08-06T10:19 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: docs(validator): correct stale weight-sal |
| 2026-08-06T10:19 | sn100 | RELEASE | sn100 released v3.3.1 — prod trust-root roll + prism epoch-close emiss |
| 2026-08-06T10:19 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: fix(design): sandbox miner HTML viewer e |
| 2026-08-06T07:28 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Repair Research Lab verifier drift |
| 2026-08-06T07:28 | sn100 | RELEASE | sn100 released v3.3.1 — prod validator trust-root roll |
| 2026-08-06T07:28 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: chore(pins): promote prod validator to v |
| 2026-08-06T07:28 | sn100 | README_TASK_DIFF | sn100 README task/scoring sections changed |
| 2026-08-06T04:41 | sn2 | RELEASE | sn2 released 14.13.1 |
| 2026-08-06T04:41 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: Merge pull request #28 from conjectures-i |
| 2026-08-06T04:41 | sn66 | README_TASK_DIFF | sn66 README task/scoring sections changed |
| 2026-08-06T04:41 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Honor scoring maintenance between rebench |
| 2026-08-06T04:41 | sn74 | RELEASE | sn74 released release-20260806-043739 |
| 2026-08-06T04:41 | sn74 | SCORING_COMMIT | sn74 commit touches scoring: sparkinfer-k3: 3x faster time-decay for m |
| 2026-08-05T22:45 | sn2 | RELEASE | sn2 released 14.13.0 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

