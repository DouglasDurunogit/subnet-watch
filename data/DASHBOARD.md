# Subnet watch — dashboard

_snapshot 2026-08-12T16:39:35Z · block 8829669 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 52 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 89 | `miner_burn` < 0.99 |
| Ranked | 89 | passed every gate |
| **Positive margin** | **52** | income beats machine cost |
| New events this window | 1 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 55 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 9 | `█████` |
| 0.6–0.8 | 9 | `█████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 39 | `████████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn120 Affine | 54.8 | 7,158 | 7,158 = | rtx4090* | 5 | 21% |
| 2 | sn97 Albedo | 52.6 | 2,894 | 2,894 = | rtx4090* | 5 | 20% |
| 3 | sn90 KubeTEE | 52 | 2,190 | 2,190 = | rtx4090* | 2 | 87% |
| 4 | sn98 NeverPlayAlone | 51.4 | 1,737 | 1,737 = | rtx4090* | 1 | 100% |
| 5 | sn114 SOMA | 50.4 | 1,149 | 4,289 | rtx4090* | 4 | 65% |
| 6 | sn1 Apex | 50.1 | 990 | 1,482 | rtx4090* | 3 | 58% |
| 7 | sn91 cascade | 49.5 | 755 | 2,586 | rtx4090* | 5 | 50% |
| 8 | sn62 Ridges | 48.7 | 546 | 1,975 | rtx4090* | 7 | 35% |
| 9 | sn56 Gradients | 48.6 | 534 | 978 | rtx4090* | 7 | 64% |
| 10 | sn100 BASE | 48.3 | 460 | 1,864 | rtx4090* | 5 | 50% |
| 11 | sn85 Vidaio | 47.3 | 307 | 487 | rtx4090* | 10 | 16% |
| 12 | sn124 Swarm | 46.4 | 219 | 665 | rtx4090* | 23 | 11% |
| 13 | sn38 ChronoLLM | 45.6 | 159 | 3,483 | rtx4090* | 10 | 52% |
| 14 | sn11 TrajectoryRL | 45.1 | 4,199 | 4,199 = | rtx4090* | 1 | 100% |
| 15 | sn28 gm | 45.1 | 121 | 2,428 | rtx4090* | 27 | 24% |
| 16 | sn80 OpenRoboto | 44.5 | 90.71 | 607 | rtx4090* | 4 | 92% |
| 17 | sn107 Minos | 44.3 | 100 | 31,151 | rtx4090* | 20 | 90% |
| 18 | sn51 lium.io | 42.1 | 40.74 | 1,996 | rtx4090* | 49 | 76% |
| 19 | sn76 Phylax | 42 | 31.42 | 178 | rtx4090* | 10 | 34% |
| 20 | sn2 DSperse | 42 | 30.91 | 86.05 | rtx4090* | 14 | 83% |

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
| captured (>90%) | 24 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 128 |

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

