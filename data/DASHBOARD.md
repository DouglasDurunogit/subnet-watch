# Subnet watch — dashboard

_snapshot 2026-08-24T17:41:49Z · block 8916378 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 51 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 89 | `miner_burn` < 0.99 |
| Ranked | 89 | passed every gate |
| **Positive margin** | **51** | income beats machine cost |
| New events this window | 4 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 60 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 7 | `███` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 39 | `██████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn11 TrajectoryRL | 79.5 | 4,903 | 4,903 = | cpu-small | 1 | 100% |
| 2 | sn76 Phylax | 79.3 | 134 | 200 | cpu-small | 13 | 20% |
| 3 | sn3 Teutonic | 76 | 4,391 | 4,391 = | rtx4090* | 5 | 20% |
| 4 | sn62 Ridges | 72.4 | 1,508 | 3,082 | rtx4090* | 6 | 39% |
| 5 | sn23 Trishool | 72.1 | 544 | 544 = | cpu-small | 2 | 80% |
| 6 | sn67 Harnyx | 71.7 | 19.07 | 164 | cpu-small | 179 | 4% |
| 7 | sn15 ORO | 71.5 | 26.83 | 45.73 | cpu-small | 81 | 93% |
| 8 | sn91 cascade | 68.9 | 533 | 1,434 | rtx4090* | 5 | 52% |
| 9 | sn1 Apex | 68.6 | 489 | 1,304 | rtx4090* | 5 | 53% |
| 10 | sn96 Verathos | 68.6 | 24.45 | 214 | rtx4090 | 86 | 41% |
| 11 | sn26 Perturb | 67.7 | 18.96 | 270 | rtx3060 | 10 | 70% |
| 12 | sn124 Swarm | 66.7 | 290 | 2,525 | rtx4090* | 21 | 30% |
| 13 | sn38 ChronoLLM | 66.6 | 117 | 1,604 | cpu-small | 10 | 52% |
| 14 | sn107 Minos | 65 | 140 | 44,125 | cpu-small | 20 | 90% |
| 15 | sn85 Vidaio | 64.8 | 156 | 431 | rtx4090* | 13 | 42% |
| 16 | sn98 NeverPlayAlone | 64.7 | 2,037 | 2,037 = | cpu-small | 1 | 100% |
| 17 | sn81 Reliquary | 64.1 | 125 | 402 | rtx4090* | 36 | 9% |
| 18 | sn60 Bitsec.ai | 64 | 1,664 | 1,664 = | cpu-small | 2 | 50% |
| 19 | sn108 Prometheon | 63.6 | 112 | 124 | rtx4090* | 9 | 66% |
| 20 | sn53 engy | 60 | 37.00 | 315 | rtx4090 | 144 | 63% |

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
| wide (<30%) | 24 |
| concentrated (30–60%) | 20 |
| dominated (60–90%) | 18 |
| captured (>90%) | 25 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 101 |
| code-submission (validator runs it) | 10 |
| min_compute.yml (curated) | 10 |
| README keywords (GUESS) | 6 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-08-24T17:42 | sn124 | SCORING_COMMIT | sn124 commit touches scoring: Rename the office challenge family to cf |
| 2026-08-24T17:42 | sn124 | README_TASK_DIFF | sn124 README task/scoring sections changed |
| 2026-08-24T16:53 | sn11 | RELEASE | sn11 released v0.6.34 |
| 2026-08-24T16:53 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: docs(rewards): leaderboard vs chain timin |
| 2026-08-24T16:05 | sn25 | RELEASE | sn25 released v2026.8.24-1027859650 |
| 2026-08-24T15:24 | sn3 | SCORING_COMMIT | sn3 commit touches scoring: Show provisional LCB during evaluations |
| 2026-08-24T15:24 | sn7 | RELEASE | sn7 released release-20260824-151246: Bump allways to 3.3.0 (#705) |
| 2026-08-24T15:24 | sn10 | SCORING_COMMIT | sn10 commit touches scoring: fix(miner): match fee-path test to the si |
| 2026-08-24T14:27 | sn11 | RELEASE | sn11 released v0.6.33 |
| 2026-08-24T13:30 | sn3 | SCORING_COMMIT | sn3 commit touches scoring: Enforce miner upload size limit |
| 2026-08-24T13:30 | sn89 | SCORING_COMMIT | sn89 commit touches scoring: HF scoreboard: pick the tick dir by newes |
| 2026-08-24T12:16 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-08-24T11:01 | sn3 | SCORING_COMMIT | sn3 commit touches scoring: Update evaluation dataset size to 2000 for |
| 2026-08-24T11:01 | sn53 | SCORING_COMMIT | sn53 commit touches scoring: tee_miner: log the WebSocket close code,  |
| 2026-08-24T11:01 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: fix(miner): accept monitoring task metada |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

