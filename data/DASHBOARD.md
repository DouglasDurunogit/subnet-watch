# Subnet watch — dashboard

_snapshot 2026-10-27T18:23:27Z · block 9376818 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 56 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 97 | `miner_burn` < 0.99 |
| Ranked | 97 | passed every gate |
| **Positive margin** | **56** | income beats machine cost |
| New events this window | 8 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 65 | `████████████████████████████` |
| 0–0.2 | 8 | `███` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 7 | `███` |
| 0.6–0.8 | 7 | `███` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 31 | `█████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn3 Teutonic | 73.5 | 2,135 | 4,277 | rtx4090* | 7 | 25% |
| 2 | sn97 Ingot | 73.1 | 1,896 | 1,896 = | rtx4090* | 5 | 20% |
| 3 | sn60 Bitsec.ai | 69.9 | 275 | 275 = | cpu-small | 3 | 50% |
| 4 | sn1 Apex | 67.9 | 401 | 907 | rtx4090* | 5 | 57% |
| 5 | sn67 Harnyx | 67.6 | 6.67 | 386 | cpu-small | 136 | 18% |
| 6 | sn56 Gradients | 67.3 | 336 | 5,528 | rtx4090* | 7 | 51% |
| 7 | sn46 Instant | 66.8 | 111 | 329 | cpu-small | 8 | 44% |
| 8 | sn107 Minos | 66.7 | 210 | 18,044 | cpu-small | 20 | 80% |
| 9 | sn120 Affine | 66.6 | 288 | 1,177 | rtx4090* | 109 | 4% |
| 10 | sn125 Refinery | 65.8 | 209 | 865 | rtx4090* | 4 | 50% |
| 11 | sn66 conjectures | 63.4 | 101 | 211 | rtx4090* | 4 | 80% |
| 12 | sn15 ORO | 63.3 | 6.68 | 14.34 | cpu-small | 67 | 97% |
| 13 | sn28 SayGM | 62.8 | 87.24 | 1,357 | rtx4090* | 139 | 6% |
| 14 | sn62 Ridges | 62.6 | 80.81 | 901 | rtx4090* | 44 | 15% |
| 15 | sn23 Trishool | 62.5 | 1,063 | 1,063 = | cpu-small | 2 | 80% |
| 16 | sn34 Yugos | 59.1 | 1,019 | 8,725 | rtx4090* | 3 | 85% |
| 17 | sn111 Claims | 58.9 | 27.28 | 2,654 | rtx4090* | 6 | 90% |
| 18 | sn78 Umi | 58.8 | 32.37 | 514 | rtx4090* | 21 | 30% |
| 19 | sn102 ConnitoAI | 57.7 | 668 | 1,119 | rtx4090* | 6 | 33% |
| 20 | sn58 Attune | 57.4 | 605 | 974 | rtx4090* | 5 | 70% |

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
| concentrated (30–60%) | 23 |
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
| 2026-10-27T18:24 | sn9 | RELEASE | sn9 released v4.13.10 |
| 2026-10-27T18:24 | sn25 | RELEASE | sn25 released v2026.10.27-1083160450 |
| 2026-10-27T18:24 | sn33 | SCORING_COMMIT | sn33 commit touches scoring: Enable 25% burn and shuffle task dispatch |
| 2026-10-27T18:24 | sn50 | SCORING_COMMIT | sn50 commit touches scoring: fix(validator): resync the metagraph afte |
| 2026-10-27T18:24 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Record verified SSM cutover and permanent |
| 2026-10-27T18:24 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Cap C7+ evaluation sources and preserve h |
| 2026-10-27T18:24 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: fix(rl-async): never charge miners for th |
| 2026-10-27T18:24 | sn89 | SCORING_COMMIT | sn89 commit touches scoring: Signals entity accounts: hosted miners as |
| 2026-10-27T12:46 | sn1 | RELEASE | sn1 released v4.5.0 |
| 2026-10-27T12:46 | sn2 | SCORING_COMMIT | sn2 commit touches scoring: Gate unverified miner scores and refresh n |
| 2026-10-27T12:46 | sn2 | README_TASK_DIFF | sn2 README task/scoring sections changed |
| 2026-10-27T12:46 | sn3 | SCORING_COMMIT | sn3 commit touches scoring: Show per-category losses in evaluation his |
| 2026-10-27T12:46 | sn25 | RELEASE | sn25 released v2026.10.26-1082839840 |
| 2026-10-27T12:46 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-5235 - [P0] Validator: publish a node |
| 2026-10-27T12:46 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

