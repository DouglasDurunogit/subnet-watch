# Subnet watch — dashboard

_snapshot 2026-08-12T15:28:56Z · block 8829315 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 55 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 91 | `miner_burn` < 0.99 |
| Ranked | 91 | passed every gate |
| **Positive margin** | **55** | income beats machine cost |
| New events this window | 1 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 55 | `████████████████████████████` |
| 0–0.2 | 7 | `████` |
| 0.2–0.4 | 5 | `███` |
| 0.4–0.6 | 9 | `█████` |
| 0.6–0.8 | 9 | `█████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 37 | `███████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 78 | 111 | 31,146 | cpu-small | 20 | 90% |
| 2 | sn98 NeverPlayAlone | 76.1 | 1,743 | 1,743 = | cpu-small | 1 | 100% |
| 3 | sn76 Phylax | 74.6 | 39.48 | 189 | cpu-small | 10 | 34% |
| 4 | sn114 SOMA | 71.5 | 1,146 | 4,280 | rtx4090* | 4 | 65% |
| 5 | sn67 Harnyx | 71.4 | 17.67 | 736 | cpu-small | 131 | 20% |
| 6 | sn91 cascade | 70.1 | 756 | 2,592 | rtx4090* | 5 | 50% |
| 7 | sn96 Verathos | 69.3 | 27.78 | 290 | rtx4090 | 65 | 41% |
| 8 | sn62 Ridges | 69 | 545 | 1,974 | rtx4090* | 7 | 35% |
| 9 | sn41 Almanac | 69 | 10.41 | 22.94 | cpu-small | 69 | 72% |
| 10 | sn56 Gradients | 68.9 | 533 | 977 | rtx4090* | 7 | 64% |
| 11 | sn100 BASE | 68.4 | 460 | 1,863 | rtx4090* | 5 | 50% |
| 12 | sn26 Perturb | 67.8 | 19.11 | 36.21 | rtx3060 | 11 | 50% |
| 13 | sn21 AdTAO | 67.5 | 7.45 | 33.48 | cpu-small | 88 | 45% |
| 14 | sn15 ORO | 67.2 | 9.41 | 12,505 | cpu-small | 65 | 95% |
| 15 | sn11 TrajectoryRL | 67.1 | 4,203 | 4,203 = | cpu-small | 1 | 100% |
| 16 | sn85 Vidaio | 66.7 | 278 | 438 | rtx4090* | 10 | 17% |
| 17 | sn124 Swarm | 65.8 | 219 | 665 | rtx4090* | 23 | 11% |
| 18 | sn38 ChronoLLM | 64.6 | 159 | 3,482 | rtx4090* | 10 | 52% |
| 19 | sn80 OpenRoboto | 64.6 | 145 | 607 | rtx4090* | 4 | 91% |
| 20 | sn28 gm | 63.7 | 115 | 2,500 | rtx4090* | 27 | 25% |

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
| 2026-08-12T15:29 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: Add validator cost profile |
| 2026-08-12T14:09 | sn28 | RELEASE | sn28 released v0.4.4 |
| 2026-08-12T14:09 | sn28 | SCORING_COMMIT | sn28 commit touches scoring: Release gm-miner v0.4.4 |
| 2026-08-12T14:09 | sn56 | SCORING_COMMIT | sn56 commit touches scoring: Oversample 2026+ models into one R1 and o |
| 2026-08-12T14:09 | sn96 | RELEASE | sn96 released Verathos v0.1.37 — Scoring Integrity and Fairness |
| 2026-08-12T14:09 | sn96 | SCORING_COMMIT | sn96 commit touches scoring: fix: correct validator scoring inputs |
| 2026-08-12T14:09 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: publish bench rollout records: per-task  |
| 2026-08-12T14:09 | sn126 | README_TASK_DIFF | sn126 README task/scoring sections changed |
| 2026-08-12T12:34 | sn28 | RELEASE | sn28 released v0.4.4-dev |
| 2026-08-12T12:34 | sn28 | SCORING_COMMIT | sn28 commit touches scoring: Document miner model sourcing options |
| 2026-08-12T12:34 | sn28 | README_TASK_DIFF | sn28 README task/scoring sections changed |
| 2026-08-12T12:34 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-08-12T12:34 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: rollouts: recover 7k terminal_lego tasks |
| 2026-08-12T11:33 | sn51 | RELEASE | sn51 released executor-v1.117 |
| 2026-08-12T10:34 | sn85 | SCORING_COMMIT | sn85 commit touches scoring: add audio validation for competitions (#1 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

