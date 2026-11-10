# Subnet watch — dashboard

_snapshot 2026-11-10T20:01:50Z · block 9478097 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 59 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 100 | `miner_burn` < 0.99 |
| Ranked | 100 | passed every gate |
| **Positive margin** | **59** | income beats machine cost |
| New events this window | 12 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 69 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 6 | `██` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 28 | `███████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn120 Affine | 74.4 | 2,737 | 2,737 = | rtx4090* | 10 | 10% |
| 2 | sn3 Teutonic | 72.7 | 1,699 | 3,406 | rtx4090* | 7 | 25% |
| 3 | sn97 Ingot | 72.2 | 1,425 | 1,425 = | rtx4090* | 5 | 20% |
| 4 | sn41 Almanac | 70.6 | 15.65 | 165 | cpu-small | 160 | 2% |
| 5 | sn103 Terza Inference | 70.3 | 822 | 984 | rtx4090* | 4 | 37% |
| 6 | sn34 Yugos | 70.1 | 773 | 6,629 | rtx4090* | 3 | 85% |
| 7 | sn58 Attune | 69.5 | 644 | 1,036 | rtx4090* | 5 | 70% |
| 8 | sn1 Apex | 69 | 543 | 704 | rtx4090* | 4 | 58% |
| 9 | sn67 Harnyx | 68.7 | 8.11 | 138 | cpu-small | 137 | 8% |
| 10 | sn56 Gradients | 68.3 | 439 | 4,642 | rtx4090* | 7 | 51% |
| 11 | sn124 Swarm | 67.6 | 370 | 1,814 | rtx4090* | 10 | 32% |
| 12 | sn46 Instant | 67.5 | 136 | 177 | cpu-small | 10 | 45% |
| 13 | sn82 Noah | 66.4 | 288 | 374 | rtx4090* | 65 | 2% |
| 14 | sn15 ORO | 65.9 | 6.26 | 13.67 | cpu-small | 74 | 95% |
| 15 | sn53 engy | 65 | 168 | 2,614 | rtx4090 | 31 | 21% |
| 16 | sn14 Cacheon | 62.5 | 79.41 | 202 | rtx4090* | 4 | 95% |
| 17 | sn121 sundae_bar | 61.7 | 849 | 849 = | cpu-small | 2 | 60% |
| 18 | sn117 everyframe.studi | 60.4 | 42.99 | 1,430 | rtx4090* | 27 | 43% |
| 19 | sn55 NIOME | 59.3 | 29.76 | 372 | rtx4090* | 11 | 30% |
| 20 | sn111 Claims | 58.4 | 23.43 | 2,367 | rtx4090* | 6 | 90% |

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
| wide (<30%) | 30 |
| concentrated (30–60%) | 17 |
| dominated (60–90%) | 27 |
| captured (>90%) | 24 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 99 |
| README keywords (GUESS) | 11 |
| min_compute.yml (curated) | 9 |
| code-submission (validator runs it) | 8 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-11-10T20:02 | sn3 | SCORING_COMMIT | sn3 commit touches scoring: Align evaluation defaults and docs with ma |
| 2026-11-10T20:02 | sn12 | RELEASE | sn12 released miner-staging-2026-11-10-42883644919-432-1: feat: upgrad |
| 2026-11-10T20:02 | sn66 | RELEASE | sn66 released v2026.11.10.2 |
| 2026-11-10T20:02 | sn70 | SCORING_COMMIT | sn70 commit touches scoring: Merge pull request #188 from fugal-ai/doc |
| 2026-11-10T20:02 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Verify composed evidence prompts without  |
| 2026-11-10T20:02 | sn108 | SCORING_COMMIT | sn108 commit touches scoring: Neuron 1.0.7: miner_cli.py withdraw and  |
| 2026-11-10T20:02 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Updates: the lost-task re-queued uploads |
| 2026-11-10T20:02 | sn117 | RELEASE | sn117 released everycli v1.1.0 |
| 2026-11-10T20:02 | sn117 | README_TASK_DIFF | sn117 README task/scoring sections changed |
| 2026-11-10T20:02 | sn124 | SCORING_COMMIT | sn124 commit touches scoring: Build test_RL tasks through the family r |
| 2026-11-10T20:02 | sn124 | README_TASK_DIFF | sn124 README task/scoring sections changed |
| 2026-11-10T20:02 | sn127 | SCORING_COMMIT | sn127 commit touches scoring: Merge pull request #233 from ooo-hq/open |
| 2026-11-10T12:31 | sn51 | RELEASE | sn51 released miner-v1.012 |
| 2026-11-10T12:31 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: Validator: judge a rented pod's ownership |
| 2026-11-10T12:31 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

