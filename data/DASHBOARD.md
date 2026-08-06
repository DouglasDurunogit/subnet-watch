# Subnet watch — dashboard

_snapshot 2026-08-06T14:54:40Z · block 8785953 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 58 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 90 | `miner_burn` < 0.99 |
| Ranked | 90 | passed every gate |
| **Positive margin** | **58** | income beats machine cost |
| New events this window | 3 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 56 | `████████████████████████████` |
| 0–0.2 | 4 | `██` |
| 0.2–0.4 | 3 | `██` |
| 0.4–0.6 | 10 | `█████` |
| 0.6–0.8 | 7 | `████` |
| 0.8–0.99 | 10 | `█████` |
| ≥0.99 dead | 38 | `███████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn11 TrajectoryRL | 79.8 | 5,356 | 5,356 = | cpu-small | 1 | 100% |
| 2 | sn76 Phylax | 77.7 | 86.65 | 435 | cpu-small | 10 | 29% |
| 3 | sn107 Minos | 77.1 | 89.23 | 27,673 | cpu-small | 19 | 90% |
| 4 | sn98 NeverPlayAlone | 75.9 | 1,685 | 1,685 = | cpu-small | 1 | 100% |
| 5 | sn60 Bitsec.ai | 75.5 | 1,456 | 1,456 = | cpu-small | 2 | 59% |
| 6 | sn67 Harnyx | 72.2 | 22.88 | 1,069 | cpu-small | 126 | 25% |
| 7 | sn96 Verathos | 71.7 | 50.03 | 172 | rtx4090 | 46 | 44% |
| 8 | sn114 SOMA | 71.6 | 1,182 | 4,412 | rtx4090* | 4 | 65% |
| 9 | sn62 Ridges | 68.9 | 537 | 1,945 | rtx4090* | 7 | 35% |
| 10 | sn91 cascade | 68.7 | 509 | 1,442 | rtx4090* | 5 | 52% |
| 11 | sn26 Perturb | 68.2 | 21.44 | 39.13 | rtx3060 | 11 | 50% |
| 12 | sn41 Almanac | 67.6 | 7.53 | 33.60 | cpu-small | 54 | 82% |
| 13 | sn15 ORO | 66.9 | 9.78 | 10,283 | cpu-small | 82 | 93% |
| 14 | sn74 Gittensor | 65.7 | 206 | 343 | rtx4090* | 9 | 18% |
| 15 | sn124 Swarm | 65.6 | 208 | 598 | rtx4090* | 23 | 10% |
| 16 | sn21 AdTAO | 65.5 | 4.91 | 22.61 | cpu-small | 142 | 45% |
| 17 | sn80 OpenRoboto | 63 | 91.26 | 340 | rtx4090* | 4 | 91% |
| 18 | sn61 RedTeam | 62.3 | 74.55 | 172 | rtx4090* | 38 | 6% |
| 19 | sn101 Tag101 | 59.8 | 0.11 | 0.68 | cpu-small | 244 | 90% |
| 20 | sn28 gm | 58 | 21.56 | 5,527 | rtx4090* | 19 | 60% |

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
| concentrated (30–60%) | 22 |
| dominated (60–90%) | 19 |
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
| 2026-08-06T14:55 | sn26 | SCORING_COMMIT | sn26 commit touches scoring: Merge pull request #45 from 0xsigurd/feat |
| 2026-08-06T14:55 | sn126 | SCORING_COMMIT | sn126 commit touches scoring: Reduce validator burn default to 30 perc |
| 2026-08-06T14:55 | sn126 | README_TASK_DIFF | sn126 README task/scoring sections changed |
| 2026-08-06T12:25 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-08-06T12:25 | sn100 | RELEASE | sn100 released v3.3.2 — miner HTML sandboxing + chain endpoint failove |
| 2026-08-06T12:25 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Document the RT-6 incident: sampler + re |
| 2026-08-06T10:19 | sn15 | RELEASE | sn15 released v1.2.6: docs(validator): correct stale weight-salt fallb |
| 2026-08-06T10:19 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: docs(validator): correct stale weight-sal |
| 2026-08-06T10:19 | sn100 | RELEASE | sn100 released v3.3.1 — prod trust-root roll + prism epoch-close emiss |
| 2026-08-06T10:19 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: fix(design): sandbox miner HTML viewer e |
| 2026-08-06T07:28 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Repair Research Lab verifier drift |
| 2026-08-06T07:28 | sn100 | RELEASE | sn100 released v3.3.1 — prod validator trust-root roll |
| 2026-08-06T07:28 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: chore(pins): promote prod validator to v |
| 2026-08-06T07:28 | sn100 | README_TASK_DIFF | sn100 README task/scoring sections changed |
| 2026-08-06T04:41 | sn2 | RELEASE | sn2 released 14.13.1 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

