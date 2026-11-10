# Subnet watch — dashboard

_snapshot 2026-11-10T03:50:32Z · block 9473240 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 63 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 101 | `miner_burn` < 0.99 |
| Ranked | 101 | passed every gate |
| **Positive margin** | **63** | income beats machine cost |
| New events this window | 11 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 69 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 7 | `███` |
| 0.6–0.8 | 8 | `███` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 27 | `███████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn120 Affine | 74.4 | 2,771 | 2,771 = | rtx4090* | 10 | 10% |
| 2 | sn3 Teutonic | 72.8 | 1,717 | 3,442 | rtx4090* | 7 | 25% |
| 3 | sn97 Ingot | 72.3 | 1,451 | 1,451 = | rtx4090* | 5 | 20% |
| 4 | sn34 Yugos | 70.2 | 786 | 6,739 | rtx4090* | 3 | 85% |
| 5 | sn58 Attune | 69.6 | 653 | 942 | rtx4090* | 5 | 71% |
| 6 | sn41 Almanac | 69.5 | 11.90 | 161 | cpu-small | 164 | 3% |
| 7 | sn1 Apex | 69.3 | 605 | 769 | rtx4090* | 4 | 55% |
| 8 | sn103 Terza Inference | 67.9 | 397 | 645 | rtx4090* | 5 | 38% |
| 9 | sn46 Instant | 67.4 | 135 | 204 | cpu-small | 9 | 46% |
| 10 | sn82 Noah | 66.2 | 294 | 383 | rtx4090* | 65 | 2% |
| 11 | sn15 ORO | 66.2 | 6.29 | 13.76 | cpu-small | 84 | 95% |
| 12 | sn53 engy | 65.2 | 176 | 2,724 | rtx4090 | 31 | 21% |
| 13 | sn14 Cacheon | 64.5 | 143 | 5,756 | rtx4090* | 4 | 95% |
| 14 | sn67 Harnyx | 64.1 | 2.79 | 196 | cpu-small | 155 | 11% |
| 15 | sn121 sundae_bar | 61.8 | 863 | 863 = | cpu-small | 2 | 60% |
| 16 | sn60 Bitsec.ai | 60.8 | 644 | 644 = | cpu-small | 3 | 50% |
| 17 | sn55 NIOME | 59.4 | 30.28 | 249 | rtx4090* | 11 | 30% |
| 18 | sn4 Targon | 58.5 | 11,931 | 24,020 | rtx4090* | 5 | 61% |
| 19 | sn111 Claims | 58.5 | 24.24 | 2,425 | rtx4090* | 6 | 90% |
| 20 | sn66 conjectures | 58.4 | 22.65 | 85.96 | rtx4090* | 7 | 84% |

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
| concentrated (30–60%) | 20 |
| dominated (60–90%) | 23 |
| captured (>90%) | 26 |

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
| 2026-11-10T03:50 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: docs: tag oroagents.com links in the mine |
| 2026-11-10T03:50 | sn36 | SCORING_COMMIT | sn36 commit touches scoring: Validator: GPUs with a UUID nvidia-smi wo |
| 2026-11-10T03:50 | sn51 | RELEASE | sn51 released executor-v1.173 |
| 2026-11-10T03:50 | sn66 | RELEASE | sn66 released v2026.11.10 |
| 2026-11-10T03:50 | sn70 | RELEASE | sn70 released build-v2026.11.10: Merge pull request #185 from fugal-ai |
| 2026-11-10T03:50 | sn70 | SCORING_COMMIT | sn70 commit touches scoring: validator: only a head hash can count as  |
| 2026-11-10T03:50 | sn70 | README_TASK_DIFF | sn70 README task/scoring sections changed |
| 2026-11-10T03:50 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Keep historical publication proofs on the |
| 2026-11-10T03:50 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: fix(validator): keep private-eval checkpo |
| 2026-11-10T03:50 | sn127 | SCORING_COMMIT | sn127 commit touches scoring: Merge pull request #229 from ooo-hq/docs |
| 2026-11-10T03:50 | sn127 | README_TASK_DIFF | sn127 README task/scoring sections changed |
| 2026-11-09T21:33 | sn28 | RELEASE | sn28 released v0.5.24 |
| 2026-11-09T21:33 | sn41 | SCORING_COMMIT | sn41 commit touches scoring: Using the validator gamma api call for th |
| 2026-11-09T21:33 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-6008 - [P0] validator: accept GB200 a |
| 2026-11-09T21:33 | sn56 | SCORING_COMMIT | sn56 commit touches scoring: Route multi-GPU tasks to SXM/NVLink train |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

