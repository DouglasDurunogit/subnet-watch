# Subnet watch — dashboard

_snapshot 2026-09-03T11:44:52Z · block 8986589 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 58 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 95 | `miner_burn` < 0.99 |
| Ranked | 95 | passed every gate |
| **Positive margin** | **58** | income beats machine cost |
| New events this window | 3 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 60 | `████████████████████████████` |
| 0–0.2 | 12 | `██████` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 33 | `███████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn92 MicroTensor | 80.9 | 198 | 542 | cpu-small | 9 | 26% |
| 2 | sn76 Phylax | 73.7 | 33.38 | 88.22 | cpu-small | 21 | 20% |
| 3 | sn23 Trishool | 72 | 525 | 525 = | cpu-small | 2 | 80% |
| 4 | sn102 ConnitoAI | 71.3 | 1,097 | 1,925 | rtx4090* | 5 | 34% |
| 5 | sn15 ORO | 70.5 | 21.75 | 21,424 | cpu-small | 74 | 93% |
| 6 | sn91 cascade | 70.3 | 807 | 3,253 | rtx4090* | 5 | 52% |
| 7 | sn96 Verathos | 69.3 | 28.06 | 175 | rtx4090 | 78 | 41% |
| 8 | sn56 Gradients | 68.9 | 533 | 1,339 | rtx4090* | 5 | 74% |
| 9 | sn67 Harnyx | 68.7 | 9.19 | 9.19 = | cpu-small | 220 | 33% |
| 10 | sn111 Claims | 67.1 | 329 | 2,939 | rtx4090* | 5 | 70% |
| 11 | sn124 Swarm | 66.4 | 262 | 809 | rtx4090* | 25 | 11% |
| 12 | sn61 RedTeam | 65.1 | 170 | 240 | rtx4090* | 44 | 3% |
| 13 | sn79 MVTRX | 64.5 | 4.10 | 405 | cpu-small | 222 | 9% |
| 14 | sn60 Bitsec.ai | 63.7 | 1,536 | 1,536 = | cpu-small | 2 | 50% |
| 15 | sn65 True Performance | 62.5 | 88.32 | 185 | rtx4090* | 6 | 75% |
| 16 | sn55 NIOME | 62.5 | 78.28 | 641 | rtx4090* | 11 | 29% |
| 17 | sn74 Gittensor | 61.8 | 67.74 | 370 | rtx4090 | 11 | 65% |
| 18 | sn101 Tag101 | 61.4 | 0.53 | 0.79 | cpu-small | 242 | 90% |
| 19 | sn2 DSperse | 61.2 | 52.63 | 136 | rtx4090* | 7 | 82% |
| 20 | sn28 SayGM | 60.1 | 40.24 | 5,987 | rtx4090* | 41 | 44% |

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
| wide (<30%) | 25 |
| concentrated (30–60%) | 20 |
| dominated (60–90%) | 21 |
| captured (>90%) | 26 |

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
| 2026-09-02T21:47 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Revalidate topology for each release plan |
| 2026-09-02T18:51 | sn13 | RELEASE | sn13 released Release v1.18.72 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

