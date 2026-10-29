# Subnet watch — dashboard

_snapshot 2026-10-29T13:29:41Z · block 9389749 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 57 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 97 | `miner_burn` < 0.99 |
| Ranked | 97 | passed every gate |
| **Positive margin** | **57** | income beats machine cost |
| New events this window | 15 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 66 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 31 | `█████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn120 Affine | 78.8 | 10,344 | 10,344 = | rtx4090* | 3 | 33% |
| 2 | sn3 Teutonic | 73.5 | 2,125 | 2,125 = | rtx4090* | 7 | 25% |
| 3 | sn97 Ingot | 73 | 1,797 | 1,797 = | rtx4090* | 5 | 20% |
| 4 | sn103 Terza Inference | 71.4 | 1,127 | 1,508 | rtx4090* | 5 | 32% |
| 5 | sn56 Gradients | 71.1 | 1,019 | 5,507 | rtx4090* | 6 | 51% |
| 6 | sn46 Instant | 70.1 | 296 | 329 | cpu-small | 5 | 44% |
| 7 | sn91 cascade | 69.5 | 632 | 1,699 | rtx4090* | 5 | 52% |
| 8 | sn60 Bitsec.ai | 69.4 | 241 | 241 = | cpu-small | 3 | 50% |
| 9 | sn53 engy | 68.4 | 454 | 2,445 | rtx4090 | 29 | 26% |
| 10 | sn1 Apex | 68.1 | 415 | 796 | rtx4090* | 5 | 60% |
| 11 | sn67 Harnyx | 67 | 6.06 | 551 | cpu-small | 130 | 26% |
| 12 | sn107 Minos | 66.2 | 185 | 15,690 | cpu-small | 20 | 80% |
| 13 | sn15 ORO | 66 | 7.28 | 13,718 | cpu-small | 67 | 96% |
| 14 | sn124 Swarm | 65.8 | 235 | 681 | rtx4090* | 25 | 10% |
| 15 | sn125 Refinery | 65.2 | 174 | 871 | rtx4090* | 4 | 50% |
| 16 | sn23 Trishool | 62.4 | 1,035 | 1,035 = | cpu-small | 2 | 80% |
| 17 | sn62 Ridges | 62.4 | 76.08 | 746 | rtx4090* | 44 | 15% |
| 18 | sn28 SayGM | 59.4 | 34.69 | 1,008 | rtx4090* | 147 | 37% |
| 19 | sn66 conjectures | 59 | 27.44 | 170 | rtx4090* | 7 | 80% |
| 20 | sn4 Targon | 58.1 | 10,684 | 30,648 | rtx4090* | 3 | 73% |

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
| wide (<30%) | 26 |
| concentrated (30–60%) | 24 |
| dominated (60–90%) | 22 |
| captured (>90%) | 24 |

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
| 2026-10-29T13:30 | sn28 | RELEASE | sn28 released v0.5.14 |
| 2026-10-29T13:30 | sn34 | SCORING_COMMIT | sn34 commit touches scoring: Bound symbolic math grading and preserve  |
| 2026-10-29T13:30 | sn51 | RELEASE | sn51 released executor-v1.163 |
| 2026-10-29T13:30 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-5295 - [P2] Rent survives a central-m |
| 2026-10-29T13:30 | sn66 | RELEASE | sn66 released deployed/dev |
| 2026-10-29T13:30 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-10-29T13:30 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Verify exact final capture after lost upl |
| 2026-10-29T13:30 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Drain evaluator status HTTP cleanup befor |
| 2026-10-29T13:30 | sn90 | RELEASE | sn90 released v1.3.2 |
| 2026-10-29T13:30 | sn90 | SCORING_COMMIT | sn90 commit touches scoring: feat(validation): remove the minimum node |
| 2026-10-29T13:30 | sn90 | README_TASK_DIFF | sn90 README task/scoring sections changed |
| 2026-10-29T13:30 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: Merge pull request #384 from TensorLink-A |
| 2026-10-29T13:30 | sn114 | SCORING_COMMIT | sn114 commit touches scoring: Show reset validations as pending |
| 2026-10-29T13:30 | sn124 | SCORING_COMMIT | sn124 commit touches scoring: Give the Sentinel test tasks the family' |
| 2026-10-29T13:30 | sn124 | README_TASK_DIFF | sn124 README task/scoring sections changed |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

