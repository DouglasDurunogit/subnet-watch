# Subnet watch — dashboard

_snapshot 2026-11-17T08:16:06Z · block 9524968 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 60 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 101 | `miner_burn` < 0.99 |
| Ranked | 101 | passed every gate |
| **Positive margin** | **60** | income beats machine cost |
| New events this window | 11 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 68 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 6 | `██` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 10 | `████` |
| 0.8–0.99 | 8 | `███` |
| ≥0.99 dead | 27 | `███████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn42 CADmind | 81.6 | 237 | 237 = | cpu-small | 5 | 20% |
| 2 | sn3 Teutonic | 73.6 | 2,200 | 4,408 | rtx4090* | 4 | 40% |
| 3 | sn58 Attune | 68.5 | 485 | 781 | rtx4090* | 5 | 70% |
| 4 | sn56 Gradients | 67.8 | 381 | 3,913 | rtx4090* | 7 | 49% |
| 5 | sn70 Fugal | 66.9 | 290 | 2,529 | rtx4090* | 3 | 85% |
| 6 | sn14 Cacheon | 66.6 | 272 | 1,695 | rtx4090* | 5 | 50% |
| 7 | sn124 Swarm | 66.4 | 261 | 1,416 | rtx4090* | 10 | 31% |
| 8 | sn67 Harnyx | 65.9 | 3.77 | 180 | cpu-small | 138 | 13% |
| 9 | sn15 ORO | 65.8 | 5.88 | 9,135 | cpu-small | 69 | 95% |
| 10 | sn53 engy | 65.6 | 197 | 7,823 | rtx4090 | 23 | 40% |
| 11 | sn120 Affine | 61.9 | 2,290 | 2,290 = | rtx4090* | 10 | 10% |
| 12 | sn38 ChronoLLM | 61.7 | 33.56 | 302 | cpu-small | 10 | 52% |
| 13 | sn111 Claims | 60.2 | 40.10 | 161 | rtx4090* | 4 | 88% |
| 14 | sn24 ms.computer | 60.1 | 38.98 | 164 | rtx4090* | 90 | 3% |
| 15 | sn97 Ingot | 59.7 | 1,181 | 1,181 = | rtx4090* | 5 | 20% |
| 16 | sn62 Ridges | 59.6 | 32.15 | 600 | rtx4090* | 44 | 15% |
| 17 | sn4 Targon | 57.6 | 9,158 | 19,666 | rtx4090* | 5 | 62% |
| 18 | sn102 ConnitoAI | 57.5 | 625 | 626 | rtx4090* | 4 | 25% |
| 19 | sn5 Hone | 56.7 | 18.31 | 40.64 | rtx4090* | 242 | 1% |
| 20 | sn66 conjectures | 56.5 | 12.45 | 1,020 | rtx4090* | 8 | 82% |

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
| concentrated (30–60%) | 23 |
| dominated (60–90%) | 27 |
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
| 2026-11-17T08:16 | sn25 | RELEASE | sn25 released v2026.11.16-1101008320 |
| 2026-11-17T08:16 | sn42 | RELEASE | sn42 released v0.6.20 |
| 2026-11-17T08:16 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-6257 - [P2] Validator: avoid a host i |
| 2026-11-17T08:16 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-11-17T08:16 | sn70 | RELEASE | sn70 released SUPERSEDED: use image-v2026.11.17b |
| 2026-11-17T08:16 | sn70 | SCORING_COMMIT | sn70 commit touches scoring: validator: the collateral startup probe o |
| 2026-11-17T08:16 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Keep unvalidated paragraph replies out of |
| 2026-11-17T08:16 | sn76 | RELEASE | sn76 released Ormas subnet SDK 0.0.4 |
| 2026-11-17T08:16 | sn76 | README_TASK_DIFF | sn76 README task/scoring sections changed |
| 2026-11-17T08:16 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: validator: keep bench-sweep evidence; wei |
| 2026-11-17T08:16 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: Compress controller evaluation transport |
| 2026-11-17T00:22 | sn15 | RELEASE | sn15 released v3.0.9: fix(sandbox): isolate each task in a run from th |
| 2026-11-17T00:22 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: fix(sandbox): isolate each task in a run  |
| 2026-11-17T00:22 | sn25 | RELEASE | sn25 released v2026.11.16-1100716180 |
| 2026-11-17T00:22 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Merge fix/validator-upload-encoding-1116: |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

