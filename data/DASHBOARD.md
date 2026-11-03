# Subnet watch — dashboard

_snapshot 2026-11-03T17:16:32Z · block 9426877 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 58 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 99 | `miner_burn` < 0.99 |
| Ranked | 99 | passed every gate |
| **Positive margin** | **58** | income beats machine cost |
| New events this window | 19 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 66 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 7 | `███` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 29 | `████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn120 Affine | 74.3 | 2,661 | 5,329 | rtx4090* | 10 | 19% |
| 2 | sn97 Ingot | 72.6 | 1,588 | 1,588 = | rtx4090* | 5 | 20% |
| 3 | sn34 Yugos | 70.2 | 804 | 6,895 | rtx4090* | 3 | 85% |
| 4 | sn103 Terza Inference | 69.6 | 653 | 1,449 | rtx4090* | 5 | 38% |
| 5 | sn14 Cacheon | 69.5 | 632 | 5,149 | rtx4090* | 3 | 80% |
| 6 | sn53 engy | 67.7 | 370 | 2,011 | rtx4090 | 29 | 26% |
| 7 | sn67 Harnyx | 67.3 | 6.31 | 80.43 | cpu-small | 139 | 8% |
| 8 | sn1 Apex | 67.2 | 326 | 803 | rtx4090* | 4 | 68% |
| 9 | sn56 Gradients | 66.8 | 283 | 4,985 | rtx4090* | 7 | 51% |
| 10 | sn107 Minos | 66 | 177 | 15,062 | cpu-small | 20 | 80% |
| 11 | sn102 ConnitoAI | 65.6 | 202 | 1,884 | rtx4090* | 5 | 53% |
| 12 | sn15 ORO | 65.6 | 6.54 | 13.33 | cpu-small | 76 | 95% |
| 13 | sn38 ChronoLLM | 63.6 | 53.91 | 481 | cpu-small | 10 | 52% |
| 14 | sn124 Swarm | 62.1 | 80.41 | 1,828 | rtx4090* | 15 | 31% |
| 15 | sn121 sundae_bar | 62 | 911 | 911 = | cpu-small | 2 | 60% |
| 16 | sn62 Ridges | 61.6 | 59.42 | 1,406 | rtx4090* | 36 | 25% |
| 17 | sn117 everyframe.studi | 61.4 | 57.51 | 102 | rtx4090* | 13 | 80% |
| 18 | sn3 Teutonic | 61.2 | 1,859 | 3,727 | rtx4090* | 7 | 25% |
| 19 | sn60 Bitsec.ai | 60 | 499 | 769 | cpu-small | 3 | 50% |
| 20 | sn80 OpenRoboto | 58.7 | 893 | 1,277 | rtx4090* | 12 | 15% |

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
| concentrated (30–60%) | 19 |
| dominated (60–90%) | 28 |
| captured (>90%) | 22 |

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
| 2026-11-03T17:17 | sn1 | RELEASE | sn1 released v4.6.3 |
| 2026-11-03T17:17 | sn21 | RELEASE | sn21 released SN21 training data v6 (windows 15 Aug - 20 Sep 2026) |
| 2026-11-03T17:17 | sn28 | README_TASK_DIFF | sn28 README task/scoring sections changed |
| 2026-11-03T17:17 | sn51 | RELEASE | sn51 released miner-v1.011 |
| 2026-11-03T17:17 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-5118 - [P1] Validator: flatten a many |
| 2026-11-03T17:17 | sn66 | RELEASE | sn66 released v2026.11.03 |
| 2026-11-03T17:17 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: fix: preserve the task-pool retirement ac |
| 2026-11-03T17:17 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-11-03T17:17 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Clarify both host validators required for |
| 2026-11-03T17:17 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: Retain comparison cells for independent e |
| 2026-11-03T17:17 | sn90 | RELEASE | sn90 released v1.3.4 |
| 2026-11-03T17:17 | sn90 | SCORING_COMMIT | sn90 commit touches scoring: fix(validator): gate scoring on node hear |
| 2026-11-03T17:17 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: perf(validator): stream private-eval fore |
| 2026-11-03T17:17 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: Match competition validation to mainnet  |
| 2026-11-03T17:17 | sn114 | SCORING_COMMIT | sn114 commit touches scoring: Show reset validations as pending |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

