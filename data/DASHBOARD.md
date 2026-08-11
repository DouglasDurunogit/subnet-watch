# Subnet watch — dashboard

_snapshot 2026-08-11T16:23:58Z · block 8822399 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 52 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 90 | `miner_burn` < 0.99 |
| Ranked | 90 | passed every gate |
| **Positive margin** | **52** | income beats machine cost |
| New events this window | 6 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 56 | `████████████████████████████` |
| 0–0.2 | 7 | `████` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 8 | `████` |
| 0.6–0.8 | 7 | `████` |
| 0.8–0.99 | 7 | `████` |
| ≥0.99 dead | 38 | `███████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 77.8 | 104 | 32,129 | cpu-small | 20 | 90% |
| 2 | sn76 Phylax | 76.5 | 63.86 | 192 | cpu-small | 10 | 34% |
| 3 | sn96 Verathos | 70.5 | 37.58 | 505 | rtx4090 | 42 | 42% |
| 4 | sn67 Harnyx | 70.5 | 13.81 | 800 | cpu-small | 150 | 21% |
| 5 | sn91 cascade | 70.1 | 774 | 2,628 | rtx4090* | 5 | 50% |
| 6 | sn62 Ridges | 68.9 | 532 | 1,926 | rtx4090* | 7 | 35% |
| 7 | sn41 Almanac | 68.9 | 10.31 | 24.18 | cpu-small | 68 | 73% |
| 8 | sn26 Perturb | 67.8 | 19.35 | 171 | rtx3060 | 11 | 50% |
| 9 | sn15 ORO | 67.8 | 10.13 | 21.65 | cpu-small | 88 | 92% |
| 10 | sn85 Vidaio | 67.6 | 361 | 503 | rtx4090* | 10 | 16% |
| 11 | sn21 AdTAO | 67.5 | 7.46 | 33.53 | cpu-small | 88 | 45% |
| 12 | sn56 Gradients | 66.6 | 271 | 980 | rtx4090* | 8 | 72% |
| 13 | sn100 BASE | 66.2 | 236 | 1,947 | rtx4090* | 6 | 50% |
| 14 | sn124 Swarm | 65.7 | 216 | 655 | rtx4090* | 23 | 11% |
| 15 | sn38 ChronoLLM | 64.6 | 161 | 3,514 | rtx4090* | 10 | 52% |
| 16 | sn80 OpenRoboto | 64.6 | 149 | 541 | rtx4090* | 4 | 91% |
| 17 | sn61 RedTeam | 62.5 | 77.54 | 325 | rtx4090* | 46 | 7% |
| 18 | sn28 gm | 61.2 | 54.09 | 2,929 | rtx4090* | 27 | 30% |
| 19 | sn51 lium.io | 59.4 | 38.24 | 2,901 | rtx4090* | 52 | 68% |
| 20 | sn2 DSperse | 59 | 27.11 | 82.95 | rtx4090* | 13 | 83% |

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
| concentrated (30–60%) | 20 |
| dominated (60–90%) | 18 |
| captured (>90%) | 26 |

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
| 2026-08-11T16:24 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Seed required miner in Git-tree rehearsal |
| 2026-08-11T16:24 | sn100 | RELEASE | sn100 released v3.3.18 — design tip-emit from latest scored round only |
| 2026-08-11T15:13 | sn1 | RELEASE | sn1 released v4.2.22 |
| 2026-08-11T15:13 | sn28 | RELEASE | sn28 released v0.4.2-dev |
| 2026-08-11T15:13 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: Improve Silver adjudication and scoring |
| 2026-08-11T15:13 | sn124 | SCORING_COMMIT | sn124 commit touches scoring: Merge per-process validator session and  |
| 2026-08-11T13:53 | sn28 | README_TASK_DIFF | sn28 README task/scoring sections changed |
| 2026-08-11T13:53 | sn85 | SCORING_COMMIT | sn85 commit touches scoring: optimise validator competition dataset pr |
| 2026-08-11T12:08 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: merge: daily model intake, multi-miner ex |
| 2026-08-11T12:08 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: Merge pull request #38 from conjectures-i |
| 2026-08-11T09:11 | sn85 | SCORING_COMMIT | sn85 commit touches scoring: isolate competition batches in separate m |
| 2026-08-11T09:11 | sn96 | RELEASE | sn96 released Verathos v0.1.35 — Concurrent Proof Serving |
| 2026-08-11T09:11 | sn96 | SCORING_COMMIT | sn96 commit touches scoring: fix: recover shared-checkout miner update |
| 2026-08-11T07:58 | sn61 | RELEASE | sn61 released 4.9.6 |
| 2026-08-11T07:58 | sn126 | README_TASK_DIFF | sn126 README task/scoring sections changed |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

