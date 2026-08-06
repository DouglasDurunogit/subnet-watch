# Subnet watch — dashboard

_snapshot 2026-08-06T07:27:59Z · block 8783720 · run_status **ok**_

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
| 0.6–0.8 | 6 | `███` |
| 0.8–0.99 | 12 | `██████` |
| ≥0.99 dead | 38 | `███████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 77.9 | 91.11 | 457 | cpu-small | 10 | 29% |
| 2 | sn107 Minos | 77.5 | 98.00 | 28,190 | cpu-small | 20 | 90% |
| 3 | sn60 Bitsec.ai | 77 | 2,280 | 2,280 = | cpu-small | 2 | 90% |
| 4 | sn67 Harnyx | 72.5 | 23.84 | 1,112 | cpu-small | 126 | 25% |
| 5 | sn91 cascade | 70.1 | 757 | 3,054 | rtx4090* | 5 | 52% |
| 6 | sn114 SOMA | 69.7 | 670 | 1,688 | rtx4090* | 4 | 65% |
| 7 | sn62 Ridges | 69.4 | 622 | 2,556 | rtx4090* | 7 | 35% |
| 8 | sn96 Verathos | 68.6 | 23.62 | 153 | rtx4090 | 76 | 43% |
| 9 | sn26 Perturb | 68.5 | 22.85 | 924 | rtx3060 | 11 | 51% |
| 10 | sn15 ORO | 67.8 | 10.27 | 10,501 | cpu-small | 81 | 93% |
| 11 | sn41 Almanac | 67.5 | 7.38 | 30.96 | cpu-small | 54 | 83% |
| 12 | sn74 Gittensor | 66.3 | 248 | 381 | rtx4090* | 9 | 18% |
| 13 | sn124 Swarm | 65.8 | 220 | 631 | rtx4090* | 23 | 10% |
| 14 | sn21 AdTAO | 65.7 | 4.90 | 22.55 | cpu-small | 142 | 45% |
| 15 | sn38 ChronoLLM | 65.5 | 204 | 3,431 | rtx4090* | 10 | 52% |
| 16 | sn80 OpenRoboto | 62.1 | 70.47 | 267 | rtx4090* | 4 | 91% |
| 17 | sn61 RedTeam | 62 | 67.26 | 173 | rtx4090* | 40 | 5% |
| 18 | sn101 Tag101 | 59.6 | 0.08 | 0.62 | cpu-small | 244 | 90% |
| 19 | sn28 gm | 58.8 | 27.44 | 6,663 | rtx4090* | 17 | 72% |
| 20 | sn2 DSperse | 58.7 | 24.52 | 99.32 | rtx4090* | 12 | 83% |

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
| 2026-08-05T22:45 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: feat(validator): epoch-pinned weights onl |
| 2026-08-05T21:45 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: Merge pull request #6 from ippcteam/docs/ |
| 2026-08-05T21:45 | sn21 | README_TASK_DIFF | sn21 README task/scoring sections changed |
| 2026-08-05T21:45 | sn62 | RELEASE | sn62 released v0.2.6 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

