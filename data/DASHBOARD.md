# Subnet watch — dashboard

_snapshot 2026-10-22T13:13:21Z · block 9339268 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 58 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 96 | `miner_burn` < 0.99 |
| Ranked | 96 | passed every gate |
| **Positive margin** | **58** | income beats machine cost |
| New events this window | 8 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 67 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 6 | `███` |
| 0.6–0.8 | 10 | `████` |
| 0.8–0.99 | 3 | `█` |
| ≥0.99 dead | 32 | `█████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn3 Teutonic | 73.5 | 2,162 | 7,883 | rtx4090* | 5 | 45% |
| 2 | sn67 Harnyx | 73.2 | 27.95 | 264 | cpu-small | 46 | 11% |
| 3 | sn120 Affine | 71 | 1,014 | 2,994 | rtx4090* | 25 | 9% |
| 4 | sn91 cascade | 70.9 | 381 | 1,526 | cpu-small | 5 | 52% |
| 5 | sn1 Apex | 68.3 | 450 | 852 | rtx4090* | 5 | 55% |
| 6 | sn102 ConnitoAI | 68.1 | 417 | 858 | rtx4090* | 7 | 25% |
| 7 | sn82 Noah | 67.6 | 577 | 593 | rtx4090* | 62 | 2% |
| 8 | sn56 Gradients | 67.3 | 327 | 5,230 | rtx4090* | 9 | 46% |
| 9 | sn125 Refinery | 67.2 | 320 | 945 | rtx4090* | 4 | 50% |
| 10 | sn53 engy | 67.1 | 308 | 2,733 | rtx4090 | 36 | 11% |
| 11 | sn107 Minos | 67.1 | 228 | 19,220 | cpu-small | 20 | 80% |
| 12 | sn15 ORO | 66.1 | 8.63 | 14,666 | cpu-small | 75 | 95% |
| 13 | sn66 conjectures | 63.4 | 104 | 217 | rtx4090* | 4 | 80% |
| 14 | sn26 Perturb | 62.8 | 183 | 229 | rtx3060 | 4 | 60% |
| 15 | sn41 Almanac | 62.2 | 2.80 | 130 | cpu-small | 156 | 3% |
| 16 | sn55 NIOME | 61.9 | 64.66 | 539 | rtx4090* | 11 | 30% |
| 17 | sn23 Trishool | 61.7 | 849 | 849 = | cpu-small | 2 | 80% |
| 18 | sn117 everyframe.studi | 59.5 | 32.36 | 101 | rtx4090* | 8 | 82% |
| 19 | sn111 Claims | 59.3 | 30.69 | 2,777 | rtx4090* | 6 | 90% |
| 20 | sn80 OpenRoboto | 59 | 956 | 4,030 | rtx4090* | 11 | 25% |

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
| concentrated (30–60%) | 19 |
| dominated (60–90%) | 26 |
| captured (>90%) | 21 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 95 |
| README keywords (GUESS) | 13 |
| min_compute.yml (curated) | 10 |
| code-submission (validator runs it) | 9 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-10-22T13:13 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: Validator v3: world packs on oro-env-runt |
| 2026-10-22T13:13 | sn15 | README_TASK_DIFF | sn15 README task/scoring sections changed |
| 2026-10-22T13:13 | sn22 | SCORING_COMMIT | sn22 commit touches scoring: fix(validators): a pinned read refused af |
| 2026-10-22T13:13 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Merge pull request #15 from Ryanmello07/m |
| 2026-10-22T13:13 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-4817 - [P2] Validator: fresh-node gra |
| 2026-10-22T13:13 | sn56 | SCORING_COMMIT | sn56 commit touches scoring: Fix FP8 LoRA evaluation and Flux cache ar |
| 2026-10-22T13:13 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-10-22T13:13 | sn92 | RELEASE | sn92 released v1.2.0-rc11 |
| 2026-10-22T07:29 | sn28 | RELEASE | sn28 released v0.5.8 |
| 2026-10-22T07:29 | sn28 | SCORING_COMMIT | sn28 commit touches scoring: chore(release): gm-miner 0.5.8 (#343) |
| 2026-10-22T07:29 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-4954 - [P0] Validator: revert the alw |
| 2026-10-22T07:29 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-10-22T07:29 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Validate Arena round IDs before store fil |
| 2026-10-22T07:29 | sn78 | README_TASK_DIFF | sn78 README task/scoring sections changed |
| 2026-10-22T07:29 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: Merge pull request #383 from reliquadotai |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

