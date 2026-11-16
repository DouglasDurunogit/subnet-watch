# Subnet watch — dashboard

_snapshot 2026-11-16T16:14:28Z · block 9520160 · run_status **ok**_

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
| New events this window | 11 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 69 | `████████████████████████████` |
| 0–0.2 | 3 | `█` |
| 0.2–0.4 | 7 | `███` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 8 | `███` |
| 0.8–0.99 | 8 | `███` |
| ≥0.99 dead | 28 | `███████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn42 CADmind | 81.6 | 235 | 235 = | cpu-small | 5 | 20% |
| 2 | sn58 Attune | 69 | 550 | 884 | rtx4090* | 5 | 70% |
| 3 | sn41 Almanac | 68.9 | 10.22 | 118 | cpu-small | 156 | 2% |
| 4 | sn14 Cacheon | 68.4 | 460 | 2,464 | rtx4090* | 5 | 50% |
| 5 | sn70 Fugal | 66.8 | 288 | 2,509 | rtx4090* | 3 | 85% |
| 6 | sn24 ms.computer | 65.3 | 183 | 796 | rtx4090* | 23 | 15% |
| 7 | sn124 Swarm | 65 | 176 | 741 | rtx4090* | 10 | 31% |
| 8 | sn15 ORO | 65 | 5.56 | 11.81 | cpu-small | 74 | 95% |
| 9 | sn53 engy | 64.9 | 163 | 5,449 | rtx4090 | 23 | 40% |
| 10 | sn67 Harnyx | 64.8 | 2.80 | 169 | cpu-small | 142 | 12% |
| 11 | sn38 ChronoLLM | 62.8 | 43.04 | 297 | cpu-small | 9 | 52% |
| 12 | sn120 Affine | 61.8 | 2,247 | 2,247 = | rtx4090* | 10 | 10% |
| 13 | sn60 Bitsec.ai | 60.3 | 554 | 554 = | cpu-small | 3 | 50% |
| 14 | sn111 Claims | 60.1 | 39.15 | 158 | rtx4090* | 4 | 88% |
| 15 | sn97 Ingot | 59.6 | 1,155 | 1,155 = | rtx4090* | 5 | 20% |
| 16 | sn62 Ridges | 59.5 | 31.33 | 588 | rtx4090* | 44 | 15% |
| 17 | sn4 Targon | 57.5 | 8,966 | 19,229 | rtx4090* | 5 | 62% |
| 18 | sn102 ConnitoAI | 57.2 | 562 | 562 | rtx4090* | 4 | 25% |
| 19 | sn5 Hone | 56.6 | 18.00 | 39.41 | rtx4090* | 241 | 1% |
| 20 | sn66 conjectures | 56.4 | 12.07 | 1,024 | rtx4090* | 7 | 84% |

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
| dominated (60–90%) | 24 |
| captured (>90%) | 25 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 99 |
| README keywords (GUESS) | 11 |
| min_compute.yml (curated) | 10 |
| code-submission (validator runs it) | 8 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-11-16T16:14 | sn3 | SCORING_COMMIT | sn3 commit touches scoring: Stream Horizon scoring during packed-text  |
| 2026-11-16T16:14 | sn25 | RELEASE | sn25 released v2026.11.16-1100273030 |
| 2026-11-16T16:14 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Merge fix/validator-nonce-wait-1116: the  |
| 2026-11-16T16:14 | sn42 | RELEASE | sn42 released v0.6.18 |
| 2026-11-16T16:14 | sn42 | SCORING_COMMIT | sn42 commit touches scoring: reference miner: a brief that asks for no |
| 2026-11-16T16:14 | sn42 | README_TASK_DIFF | sn42 README task/scoring sections changed |
| 2026-11-16T16:14 | sn51 | RELEASE | sn51 released executor-v1.184 |
| 2026-11-16T16:14 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: Validator: quote executor-reported paths  |
| 2026-11-16T16:14 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-11-16T16:14 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Assert exact judgment binding in score pr |
| 2026-11-16T16:14 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: Verify carried-forward scoring revisions |
| 2026-11-16T06:16 | sn24 | RELEASE | sn24 released v0.2.1 |
| 2026-11-16T06:16 | sn25 | RELEASE | sn25 released v2026.11.15-1100072900 |
| 2026-11-16T06:16 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Merge release/validator-1115-transient-wa |
| 2026-11-16T06:16 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-6295 - [P0] Validator: a node on anot |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

