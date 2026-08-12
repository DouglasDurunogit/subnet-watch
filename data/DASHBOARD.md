# Subnet watch — dashboard

_snapshot 2026-08-12T14:08:46Z · block 8828915 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 54 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 91 | `miner_burn` < 0.99 |
| Ranked | 91 | passed every gate |
| **Positive margin** | **54** | income beats machine cost |
| New events this window | 7 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 55 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 9 | `█████` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 7 | `████` |
| ≥0.99 dead | 37 | `███████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 77.9 | 107 | 31,335 | cpu-small | 20 | 90% |
| 2 | sn98 NeverPlayAlone | 76.1 | 1,748 | 1,748 = | cpu-small | 1 | 100% |
| 3 | sn76 Phylax | 74.6 | 39.79 | 191 | cpu-small | 10 | 34% |
| 4 | sn114 SOMA | 71.5 | 1,157 | 4,321 | rtx4090* | 4 | 65% |
| 5 | sn67 Harnyx | 71.4 | 17.87 | 744 | cpu-small | 131 | 20% |
| 6 | sn91 cascade | 70.1 | 771 | 2,640 | rtx4090* | 5 | 50% |
| 7 | sn62 Ridges | 69 | 547 | 1,980 | rtx4090* | 7 | 35% |
| 8 | sn41 Almanac | 69 | 10.45 | 23.20 | cpu-small | 69 | 72% |
| 9 | sn56 Gradients | 68.9 | 535 | 980 | rtx4090* | 7 | 64% |
| 10 | sn96 Verathos | 68.9 | 25.11 | 321 | rtx4090 | 73 | 41% |
| 11 | sn100 BASE | 68.5 | 470 | 1,903 | rtx4090* | 5 | 50% |
| 12 | sn26 Perturb | 67.8 | 19.25 | 36.55 | rtx3060 | 11 | 50% |
| 13 | sn21 AdTAO | 67.6 | 7.49 | 33.62 | cpu-small | 88 | 45% |
| 14 | sn15 ORO | 67.5 | 9.47 | 12,587 | cpu-small | 65 | 95% |
| 15 | sn124 Swarm | 65.8 | 220 | 667 | rtx4090* | 23 | 11% |
| 16 | sn38 ChronoLLM | 64.6 | 160 | 3,498 | rtx4090* | 10 | 52% |
| 17 | sn85 Vidaio | 64.2 | 132 | 440 | rtx4090* | 10 | 18% |
| 18 | sn28 gm | 63.8 | 117 | 3,042 | rtx4090* | 27 | 30% |
| 19 | sn80 OpenRoboto | 62.8 | 86.73 | 586 | rtx4090* | 4 | 92% |
| 20 | sn102 ConnitoAI | 60.1 | 1,333 | 1,789 | rtx4090* | 5 | 29% |

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
| dominated (60–90%) | 18 |
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
| 2026-08-12T10:34 | sn100 | RELEASE | sn100 released v3.3.21 — Prism Lium single-GPU hard-reject (#129) |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

