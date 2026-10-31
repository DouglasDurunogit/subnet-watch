# Subnet watch — dashboard

_snapshot 2026-10-31T17:57:39Z · block 9405489 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 55 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 99 | `miner_burn` < 0.99 |
| Ranked | 99 | passed every gate |
| **Positive margin** | **55** | income beats machine cost |
| New events this window | 5 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 66 | `████████████████████████████` |
| 0–0.2 | 8 | `███` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 29 | `████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn120 Affine | 74.6 | 2,913 | 2,913 = | rtx4090* | 10 | 10% |
| 2 | sn3 Teutonic | 73.2 | 1,945 | 3,898 | rtx4090* | 7 | 25% |
| 3 | sn97 Ingot | 72.8 | 1,693 | 1,693 = | rtx4090* | 5 | 20% |
| 4 | sn103 Terza Inference | 70 | 738 | 1,931 | rtx4090* | 5 | 38% |
| 5 | sn60 Bitsec.ai | 69.3 | 232 | 232 = | cpu-small | 3 | 50% |
| 6 | sn53 engy | 67.9 | 398 | 2,147 | rtx4090 | 29 | 26% |
| 7 | sn1 Apex | 67.4 | 337 | 786 | rtx4090* | 5 | 64% |
| 8 | sn67 Harnyx | 67.2 | 6.08 | 479 | cpu-small | 139 | 24% |
| 9 | sn107 Minos | 65.8 | 167 | 14,196 | cpu-small | 20 | 80% |
| 10 | sn15 ORO | 65.4 | 6.64 | 14.07 | cpu-small | 74 | 96% |
| 11 | sn125 Refinery | 64.7 | 153 | 826 | rtx4090* | 4 | 50% |
| 12 | sn102 ConnitoAI | 64.5 | 145 | 765 | rtx4090* | 10 | 25% |
| 13 | sn124 Swarm | 63 | 100 | 2,048 | rtx4090* | 14 | 33% |
| 14 | sn62 Ridges | 61.2 | 54.28 | 2,528 | rtx4090* | 33 | 43% |
| 15 | sn117 everyframe.studi | 59.9 | 37.11 | 197 | rtx4090* | 7 | 87% |
| 16 | sn66 conjectures | 58.6 | 23.78 | 163 | rtx4090* | 7 | 82% |
| 17 | sn4 Targon | 58.4 | 11,516 | 25,784 | rtx4090* | 4 | 64% |
| 18 | sn91 cascade | 57.7 | 19.96 | 66.94 | rtx4090* | 6 | 95% |
| 19 | sn56 Gradients | 57.6 | 634 | 5,211 | rtx4090* | 6 | 51% |
| 20 | sn58 Attune | 57.1 | 561 | 903 | rtx4090* | 5 | 70% |

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
| concentrated (30–60%) | 22 |
| dominated (60–90%) | 23 |
| captured (>90%) | 27 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 100 |
| README keywords (GUESS) | 10 |
| min_compute.yml (curated) | 9 |
| code-submission (validator runs it) | 8 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-10-31T17:58 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: docs: the settling window is 2 days every |
| 2026-10-31T17:58 | sn21 | README_TASK_DIFF | sn21 README task/scoring sections changed |
| 2026-10-31T17:58 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Preserve verified training pairs from inc |
| 2026-10-31T17:58 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Miner client: every HTTP call to a door  |
| 2026-10-31T17:58 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: SN120 legacy removal docs: llms.txt (sit |
| 2026-10-31T13:35 | sn14 | SCORING_COMMIT | sn14 commit touches scoring: Pay no first PASS under the reward margin |
| 2026-10-31T13:35 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-10-31T13:35 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: Merge pull request #393 from TensorLink-A |
| 2026-10-31T13:35 | sn108 | SCORING_COMMIT | sn108 commit touches scoring: Between quests the validator checks its  |
| 2026-10-31T06:56 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Record the census fix deployment in taskw |
| 2026-10-31T06:56 | sn34 | SCORING_COMMIT | sn34 commit touches scoring: fix: score empty stopped ArenaHard answer |
| 2026-10-31T06:56 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-5457 - [P0] Validator: GPU drop repor |
| 2026-10-31T06:56 | sn62 | RELEASE | sn62 released v0.3.16 |
| 2026-10-31T06:56 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Keep validator checkout warnings out of u |
| 2026-10-31T06:56 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: King leg: channel floor by ref, ignore th |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

