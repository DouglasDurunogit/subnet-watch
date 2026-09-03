# Subnet watch — dashboard

_snapshot 2026-09-03T15:14:48Z · block 8987639 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 58 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 94 | `miner_burn` < 0.99 |
| Ranked | 94 | passed every gate |
| **Positive margin** | **58** | income beats machine cost |
| New events this window | 2 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 59 | `████████████████████████████` |
| 0–0.2 | 12 | `██████` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 34 | `████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn92 MicroTensor | 80.9 | 199 | 545 | cpu-small | 9 | 26% |
| 2 | sn3 Teutonic | 75.5 | 3,771 | 3,771 = | rtx4090* | 5 | 20% |
| 3 | sn76 Phylax | 73.7 | 33.17 | 87.63 | cpu-small | 21 | 20% |
| 4 | sn23 Trishool | 72.1 | 531 | 531 = | cpu-small | 2 | 80% |
| 5 | sn91 cascade | 70.3 | 813 | 3,278 | rtx4090* | 5 | 52% |
| 6 | sn15 ORO | 69.7 | 21.54 | 42.99 | cpu-small | 74 | 93% |
| 7 | sn96 Verathos | 69.5 | 29.62 | 165 | rtx4090 | 77 | 41% |
| 8 | sn56 Gradients | 68.9 | 540 | 1,354 | rtx4090* | 5 | 74% |
| 9 | sn67 Harnyx | 68.9 | 9.32 | 9.32 = | cpu-small | 221 | 32% |
| 10 | sn111 Claims | 67.1 | 330 | 2,950 | rtx4090* | 5 | 70% |
| 11 | sn124 Swarm | 66.5 | 267 | 823 | rtx4090* | 25 | 11% |
| 12 | sn61 RedTeam | 65.2 | 175 | 248 | rtx4090* | 44 | 3% |
| 13 | sn79 MVTRX | 64.6 | 4.32 | 408 | cpu-small | 221 | 9% |
| 14 | sn60 Bitsec.ai | 63.9 | 1,601 | 1,601 = | cpu-small | 2 | 50% |
| 15 | sn65 True Performance | 62.1 | 78.97 | 166 | rtx4090* | 6 | 78% |
| 16 | sn74 Gittensor | 62 | 69.94 | 383 | rtx4090 | 11 | 64% |
| 17 | sn101 Tag101 | 61.5 | 0.55 | 0.68 | cpu-small | 244 | 90% |
| 18 | sn2 DSperse | 61 | 49.32 | 149 | rtx4090* | 7 | 82% |
| 19 | sn28 SayGM | 59.6 | 34.01 | 5,244 | rtx4090* | 40 | 38% |
| 20 | sn41 Almanac | 59.3 | 29.79 | 77.26 | cpu-small | 88 | 19% |

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
| concentrated (30–60%) | 19 |
| dominated (60–90%) | 19 |
| captured (>90%) | 27 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 99 |
| min_compute.yml (curated) | 11 |
| code-submission (validator runs it) | 10 |
| README keywords (GUESS) | 7 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-09-03T15:15 | sn1 | RELEASE | sn1 released v4.4.1 |
| 2026-09-03T15:15 | sn2 | RELEASE | sn2 released 14.14.2 |
| 2026-09-03T11:45 | sn1 | RELEASE | sn1 released v4.4.0 |
| 2026-09-03T11:45 | sn50 | SCORING_COMMIT | sn50 commit touches scoring: base miner: gzip-compress axon responses  |
| 2026-09-03T11:45 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: fix(relearn): pin proven CUDA scoring ev |
| 2026-09-03T06:32 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-09-03T06:32 | sn71 | BURN_DROP | sn71 burn fell 1.000 -> 0.974 - miners can earn again |
| 2026-09-03T06:32 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: ci: run the non-scoring tests on every pu |
| 2026-09-03T06:32 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: scoring: block-scheduled fresh-king margi |
| 2026-09-03T06:32 | sn91 | README_TASK_DIFF | sn91 README task/scoring sections changed |
| 2026-09-03T01:31 | sn105 | BURN_DROP | sn105 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-09-02T23:37 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Repair SOURCE_ADD provenance origin rewar |
| 2026-09-02T21:47 | sn2 | RELEASE | sn2 released 14.14.1 |
| 2026-09-02T21:47 | sn2 | SCORING_COMMIT | sn2 commit touches scoring: Resolve slow validator recovery after exte |
| 2026-09-02T21:47 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: feat(validator): reference partner valida |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

