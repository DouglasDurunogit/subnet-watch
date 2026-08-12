# Subnet watch — dashboard

_snapshot 2026-08-12T18:40:22Z · block 8830273 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 55 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 90 | `miner_burn` < 0.99 |
| Ranked | 90 | passed every gate |
| **Positive margin** | **55** | income beats machine cost |
| New events this window | 1 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 57 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 3 | `█` |
| 0.4–0.6 | 9 | `████` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 38 | `███████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 78 | 111 | 31,080 | cpu-small | 20 | 89% |
| 2 | sn76 Phylax | 76.4 | 62.35 | 189 | cpu-small | 10 | 34% |
| 3 | sn98 NeverPlayAlone | 76.1 | 1,750 | 1,750 = | cpu-small | 1 | 100% |
| 4 | sn114 SOMA | 71.5 | 1,165 | 4,349 | rtx4090* | 4 | 65% |
| 5 | sn67 Harnyx | 71.4 | 17.99 | 749 | cpu-small | 131 | 20% |
| 6 | sn91 cascade | 70.1 | 766 | 2,624 | rtx4090* | 5 | 50% |
| 7 | sn96 Verathos | 69.3 | 28.14 | 323 | rtx4090 | 60 | 42% |
| 8 | sn41 Almanac | 69.1 | 10.68 | 23.85 | cpu-small | 69 | 72% |
| 9 | sn62 Ridges | 69 | 548 | 1,981 | rtx4090* | 7 | 35% |
| 10 | sn56 Gradients | 68.9 | 535 | 981 | rtx4090* | 7 | 65% |
| 11 | sn100 BASE | 68.4 | 465 | 1,886 | rtx4090* | 5 | 50% |
| 12 | sn26 Perturb | 67.9 | 19.64 | 172 | rtx3060 | 11 | 51% |
| 13 | sn21 AdTAO | 67.6 | 7.50 | 33.68 | cpu-small | 88 | 45% |
| 14 | sn11 TrajectoryRL | 67.1 | 4,220 | 4,220 = | cpu-small | 1 | 100% |
| 15 | sn15 ORO | 66.2 | 8.77 | 20.88 | cpu-small | 68 | 94% |
| 16 | sn124 Swarm | 65.8 | 220 | 667 | rtx4090* | 23 | 11% |
| 17 | sn80 OpenRoboto | 65 | 168 | 610 | rtx4090* | 4 | 91% |
| 18 | sn38 ChronoLLM | 64.6 | 161 | 3,523 | rtx4090* | 10 | 52% |
| 19 | sn85 Vidaio | 64.1 | 125 | 480 | rtx4090* | 10 | 17% |
| 20 | sn28 gm | 61.4 | 58.03 | 2,742 | rtx4090* | 32 | 28% |

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
| concentrated (30–60%) | 21 |
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

