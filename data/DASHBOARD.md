# Subnet watch — dashboard

_snapshot 2026-08-12T21:58:09Z · block 8831262 · run_status **ok**_

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
| New events this window | 0 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 56 | `████████████████████████████` |
| 0–0.2 | 8 | `████` |
| 0.2–0.4 | 2 | `█` |
| 0.4–0.6 | 9 | `████` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 7 | `████` |
| ≥0.99 dead | 38 | `███████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 77.6 | 101 | 31,271 | cpu-small | 20 | 90% |
| 2 | sn76 Phylax | 76.3 | 61.22 | 186 | cpu-small | 10 | 34% |
| 3 | sn67 Harnyx | 71.4 | 17.89 | 745 | cpu-small | 131 | 20% |
| 4 | sn96 Verathos | 70.7 | 39.05 | 394 | rtx4090 | 51 | 42% |
| 5 | sn91 cascade | 70.1 | 760 | 2,621 | rtx4090* | 5 | 50% |
| 6 | sn114 SOMA | 69.7 | 670 | 4,398 | rtx4090* | 4 | 65% |
| 7 | sn41 Almanac | 69.1 | 10.59 | 29.69 | cpu-small | 68 | 72% |
| 8 | sn62 Ridges | 69 | 544 | 1,969 | rtx4090* | 7 | 35% |
| 9 | sn56 Gradients | 68.9 | 531 | 975 | rtx4090* | 7 | 65% |
| 10 | sn100 BASE | 68.3 | 451 | 1,828 | rtx4090* | 5 | 50% |
| 11 | sn26 Perturb | 67.8 | 19.26 | 36.56 | rtx3060 | 11 | 50% |
| 12 | sn21 AdTAO | 67.5 | 7.47 | 33.56 | cpu-small | 88 | 45% |
| 13 | sn11 TrajectoryRL | 67.1 | 4,175 | 4,175 = | cpu-small | 1 | 100% |
| 14 | sn15 ORO | 67 | 8.97 | 12,187 | cpu-small | 69 | 94% |
| 15 | sn124 Swarm | 65.8 | 219 | 667 | rtx4090* | 23 | 11% |
| 16 | sn80 OpenRoboto | 65 | 164 | 596 | rtx4090* | 4 | 91% |
| 17 | sn38 ChronoLLM | 64.6 | 160 | 3,493 | rtx4090* | 10 | 52% |
| 18 | sn85 Vidaio | 64.2 | 129 | 441 | rtx4090* | 10 | 20% |
| 19 | sn28 gm | 62.8 | 88.61 | 2,668 | rtx4090* | 30 | 27% |
| 20 | sn51 lium.io | 60.4 | 49.83 | 2,256 | rtx4090* | 46 | 71% |

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
| concentrated (30–60%) | 23 |
| dominated (60–90%) | 17 |
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
| 2026-08-12T18:40 | sn54 | SCORING_COMMIT | sn54 commit touches scoring: update miner screen reply readme |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

