# Subnet watch — dashboard

_snapshot 2026-08-12T17:44:34Z · block 8829994 · run_status **ok**_

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
| 0 (none) | 57 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 9 | `████` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 38 | `███████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn67 Harnyx | 71.5 | 17.98 | 748 | cpu-small | 131 | 20% |
| 2 | sn41 Almanac | 69.1 | 10.67 | 23.83 | cpu-small | 69 | 72% |
| 3 | sn62 Ridges | 69 | 547 | 1,980 | rtx4090* | 7 | 35% |
| 4 | sn56 Gradients | 68.9 | 535 | 980 | rtx4090* | 7 | 65% |
| 5 | sn26 Perturb | 67.7 | 18.96 | 34.99 | rtx3060 | 11 | 50% |
| 6 | sn21 AdTAO | 67.5 | 7.47 | 33.56 | cpu-small | 88 | 45% |
| 7 | sn11 TrajectoryRL | 67.1 | 4,216 | 4,216 = | cpu-small | 1 | 100% |
| 8 | sn15 ORO | 66.6 | 8.71 | 20.97 | cpu-small | 67 | 95% |
| 9 | sn38 ChronoLLM | 64.6 | 160 | 3,492 | rtx4090* | 10 | 52% |
| 10 | sn28 gm | 61.5 | 59.92 | 2,304 | rtx4090* | 31 | 23% |
| 11 | sn51 lium.io | 59.5 | 40.85 | 2,016 | rtx4090* | 47 | 77% |
| 12 | sn2 DSperse | 59.4 | 31.00 | 86.25 | rtx4090* | 14 | 83% |
| 13 | sn61 RedTeam | 58.2 | 20.88 | 1,641 | rtx4090* | 61 | 35% |
| 14 | sn6 Numinous | 56.3 | 15.81 | 477 | cpu-small | 20 | 26% |
| 15 | sn120 Affine | 54.7 | 6,949 | 6,949 = | rtx4090* | 5 | 20% |
| 16 | sn97 Albedo | 52.6 | 2,902 | 2,902 = | rtx4090* | 5 | 20% |
| 17 | sn90 KubeTEE | 52.1 | 2,266 | 2,266 = | rtx4090* | 2 | 87% |
| 18 | sn98 NeverPlayAlone | 51.4 | 1,741 | 1,741 = | rtx4090* | 1 | 100% |
| 19 | sn53 engy | 50.9 | 86.23 | 585 | rtx4090 | 144 | 11% |
| 20 | sn114 SOMA | 50.5 | 1,163 | 4,342 | rtx4090* | 4 | 65% |

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
| concentrated (30–60%) | 22 |
| dominated (60–90%) | 19 |
| captured (>90%) | 25 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 112 |
| code-submission (validator runs it) | 7 |
| min_compute.yml (curated) | 4 |
| README keywords (GUESS) | 4 |
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

