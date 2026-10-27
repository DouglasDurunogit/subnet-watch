# Subnet watch — dashboard

_snapshot 2026-10-27T12:46:06Z · block 9375131 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 54 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 97 | `miner_burn` < 0.99 |
| Ranked | 97 | passed every gate |
| **Positive margin** | **54** | income beats machine cost |
| New events this window | 11 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 64 | `████████████████████████████` |
| 0–0.2 | 9 | `████` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 6 | `███` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 31 | `██████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn3 Teutonic | 73.5 | 2,121 | 4,251 | rtx4090* | 7 | 25% |
| 2 | sn97 Ingot | 73 | 1,795 | 1,795 = | rtx4090* | 5 | 20% |
| 3 | sn60 Bitsec.ai | 69.8 | 269 | 269 = | cpu-small | 3 | 50% |
| 4 | sn46 Instant | 69.5 | 246 | 277 | cpu-small | 6 | 44% |
| 5 | sn1 Apex | 68 | 413 | 826 | rtx4090* | 5 | 58% |
| 6 | sn107 Minos | 67.4 | 243 | 16,996 | cpu-small | 20 | 77% |
| 7 | sn67 Harnyx | 67.4 | 6.64 | 385 | cpu-small | 133 | 18% |
| 8 | sn56 Gradients | 67.3 | 334 | 5,503 | rtx4090* | 7 | 51% |
| 9 | sn120 Affine | 66.6 | 297 | 1,058 | rtx4090* | 105 | 3% |
| 10 | sn125 Refinery | 65.8 | 208 | 861 | rtx4090* | 4 | 50% |
| 11 | sn15 ORO | 65.6 | 6.63 | 14.25 | cpu-small | 67 | 97% |
| 12 | sn66 conjectures | 63.3 | 101 | 209 | rtx4090* | 4 | 80% |
| 13 | sn62 Ridges | 62.6 | 81.01 | 903 | rtx4090* | 44 | 15% |
| 14 | sn28 SayGM | 62.2 | 73.48 | 1,898 | rtx4090* | 136 | 10% |
| 15 | sn34 Yugos | 59.1 | 1,017 | 8,708 | rtx4090* | 3 | 85% |
| 16 | sn78 Umi | 58.5 | 30.11 | 485 | rtx4090* | 21 | 30% |
| 17 | sn49 Nepher Robotics | 57.7 | 668 | 3,146 | rtx4090* | 5 | 69% |
| 18 | sn58 Attune | 57.4 | 606 | 975 | rtx4090* | 5 | 70% |
| 19 | sn5 Hone | 57.3 | 28.66 | 37.68 | rtx4090* | 242 | 1% |
| 20 | sn111 Claims | 57.3 | 16.83 | 2,659 | rtx4090* | 7 | 90% |

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
| wide (<30%) | 28 |
| concentrated (30–60%) | 21 |
| dominated (60–90%) | 23 |
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
| 2026-10-27T12:46 | sn1 | RELEASE | sn1 released v4.5.0 |
| 2026-10-27T12:46 | sn2 | SCORING_COMMIT | sn2 commit touches scoring: Gate unverified miner scores and refresh n |
| 2026-10-27T12:46 | sn2 | README_TASK_DIFF | sn2 README task/scoring sections changed |
| 2026-10-27T12:46 | sn3 | SCORING_COMMIT | sn3 commit touches scoring: Show per-category losses in evaluation his |
| 2026-10-27T12:46 | sn25 | RELEASE | sn25 released v2026.10.26-1082839840 |
| 2026-10-27T12:46 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-5235 - [P0] Validator: publish a node |
| 2026-10-27T12:46 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-10-27T12:46 | sn75 | RELEASE | sn75 released Runtime 92023 |
| 2026-10-27T12:46 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Cap retained reward coverage at native su |
| 2026-10-27T12:46 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: Report static-guard rejections from verif |
| 2026-10-27T12:46 | sn91 | README_TASK_DIFF | sn91 README task/scoring sections changed |
| 2026-10-27T06:46 | sn2 | SCORING_COMMIT | sn2 commit touches scoring: Score finalized epoch snapshots and log un |
| 2026-10-27T06:46 | sn2 | README_TASK_DIFF | sn2 README task/scoring sections changed |
| 2026-10-27T06:46 | sn15 | RELEASE | sn15 released v3.0.5: fix(validator): policy_view.max_steps is the tas |
| 2026-10-27T06:46 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: fix(validator): policy_view.max_steps is  |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

