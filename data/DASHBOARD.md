# Subnet watch — dashboard

_snapshot 2026-11-11T00:36:45Z · block 9479471 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 60 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 100 | `miner_burn` < 0.99 |
| Ranked | 100 | passed every gate |
| **Positive margin** | **60** | income beats machine cost |
| New events this window | 7 | see ALARMS.md |

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
| 1 | sn120 Affine | 74.4 | 2,757 | 2,757 = | rtx4090* | 10 | 10% |
| 2 | sn3 Teutonic | 72.7 | 1,694 | 3,397 | rtx4090* | 7 | 25% |
| 3 | sn97 Ingot | 72.2 | 1,433 | 1,433 = | rtx4090* | 5 | 20% |
| 4 | sn41 Almanac | 70.3 | 14.37 | 161 | cpu-small | 160 | 3% |
| 5 | sn103 Terza Inference | 69.7 | 685 | 1,142 | rtx4090* | 4 | 42% |
| 6 | sn58 Attune | 69.5 | 643 | 1,034 | rtx4090* | 5 | 70% |
| 7 | sn56 Gradients | 69.3 | 606 | 4,667 | rtx4090* | 6 | 51% |
| 8 | sn1 Apex | 68.9 | 532 | 694 | rtx4090* | 4 | 59% |
| 9 | sn67 Harnyx | 68.7 | 8.16 | 139 | cpu-small | 137 | 8% |
| 10 | sn124 Swarm | 67.6 | 374 | 1,835 | rtx4090* | 10 | 32% |
| 11 | sn46 Instant | 67.5 | 135 | 219 | cpu-small | 10 | 45% |
| 12 | sn15 ORO | 66.1 | 6.27 | 13.70 | cpu-small | 74 | 95% |
| 13 | sn82 Noah | 65.8 | 290 | 377 | rtx4090* | 64 | 2% |
| 14 | sn53 engy | 65.1 | 172 | 2,669 | rtx4090 | 31 | 21% |
| 15 | sn14 Cacheon | 62.6 | 79.97 | 203 | rtx4090* | 4 | 95% |
| 16 | sn66 conjectures | 59.9 | 35.53 | 1,138 | rtx4090* | 5 | 81% |
| 17 | sn55 NIOME | 59.3 | 29.93 | 374 | rtx4090* | 11 | 30% |
| 18 | sn4 Targon | 58.4 | 11,684 | 22,815 | rtx4090* | 5 | 60% |
| 19 | sn111 Claims | 58.4 | 23.27 | 2,354 | rtx4090* | 6 | 90% |
| 20 | sn102 ConnitoAI | 57.6 | 636 | 636 = | rtx4090* | 4 | 25% |

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
| wide (<30%) | 29 |
| concentrated (30–60%) | 17 |
| dominated (60–90%) | 29 |
| captured (>90%) | 23 |

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
| 2026-11-11T00:37 | sn2 | SCORING_COMMIT | sn2 commit touches scoring: Merge pull request #1 from mybelovedstar12 |
| 2026-11-11T00:37 | sn17 | SCORING_COMMIT | sn17 commit touches scoring: Add validation worker with manual replays |
| 2026-11-11T00:37 | sn54 | SCORING_COMMIT | sn54 commit touches scoring: Validate validator requests and submissio |
| 2026-11-11T00:37 | sn70 | RELEASE | sn70 released Fugal Subnet v0.3.1 |
| 2026-11-11T00:37 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Reserve replay network budget after local |
| 2026-11-11T00:37 | sn108 | SCORING_COMMIT | sn108 commit touches scoring: Neuron 1.0.9: the validator stops an eva |
| 2026-11-11T00:37 | sn117 | RELEASE | sn117 released everycli v1.1.1 |
| 2026-11-10T20:02 | sn3 | SCORING_COMMIT | sn3 commit touches scoring: Align evaluation defaults and docs with ma |
| 2026-11-10T20:02 | sn12 | RELEASE | sn12 released miner-staging-2026-11-10-42883644919-432-1: feat: upgrad |
| 2026-11-10T20:02 | sn66 | RELEASE | sn66 released v2026.11.10.2 |
| 2026-11-10T20:02 | sn70 | SCORING_COMMIT | sn70 commit touches scoring: Merge pull request #188 from fugal-ai/doc |
| 2026-11-10T20:02 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Verify composed evidence prompts without  |
| 2026-11-10T20:02 | sn108 | SCORING_COMMIT | sn108 commit touches scoring: Neuron 1.0.7: miner_cli.py withdraw and  |
| 2026-11-10T20:02 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Updates: the lost-task re-queued uploads |
| 2026-11-10T20:02 | sn117 | RELEASE | sn117 released everycli v1.1.0 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

