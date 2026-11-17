# Subnet watch — dashboard

_snapshot 2026-11-17T00:21:44Z · block 9522596 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 59 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 101 | `miner_burn` < 0.99 |
| Ranked | 101 | passed every gate |
| **Positive margin** | **59** | income beats machine cost |
| New events this window | 13 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 69 | `████████████████████████████` |
| 0–0.2 | 4 | `██` |
| 0.2–0.4 | 7 | `███` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 8 | `███` |
| ≥0.99 dead | 27 | `███████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn42 CADmind | 81.6 | 238 | 238 = | cpu-small | 5 | 20% |
| 2 | sn3 Teutonic | 73.6 | 2,205 | 4,306 | rtx4090* | 4 | 39% |
| 3 | sn14 Cacheon | 70.9 | 975 | 2,503 | rtx4090* | 5 | 50% |
| 4 | sn34 Yugos | 69.6 | 664 | 5,704 | rtx4090* | 3 | 85% |
| 5 | sn41 Almanac | 68.9 | 10.21 | 118 | cpu-small | 156 | 9% |
| 6 | sn58 Attune | 68.7 | 512 | 824 | rtx4090* | 5 | 70% |
| 7 | sn70 Fugal | 66.7 | 279 | 2,436 | rtx4090* | 3 | 85% |
| 8 | sn124 Swarm | 66.5 | 266 | 1,439 | rtx4090* | 10 | 31% |
| 9 | sn56 Gradients | 66.1 | 233 | 3,879 | rtx4090* | 8 | 49% |
| 10 | sn15 ORO | 65.9 | 5.54 | 11.76 | cpu-small | 72 | 95% |
| 11 | sn53 engy | 65.3 | 182 | 7,239 | rtx4090 | 23 | 40% |
| 12 | sn67 Harnyx | 65.1 | 2.88 | 172 | cpu-small | 148 | 12% |
| 13 | sn24 ms.computer | 63.3 | 102 | 338 | rtx4090* | 45 | 7% |
| 14 | sn120 Affine | 61.8 | 2,279 | 2,279 = | rtx4090* | 10 | 10% |
| 15 | sn38 ChronoLLM | 61.7 | 33.31 | 301 | cpu-small | 10 | 52% |
| 16 | sn111 Claims | 60.2 | 39.68 | 159 | rtx4090* | 4 | 88% |
| 17 | sn97 Ingot | 59.7 | 1,179 | 1,179 = | rtx4090* | 5 | 20% |
| 18 | sn62 Ridges | 59.5 | 31.83 | 595 | rtx4090* | 44 | 15% |
| 19 | sn4 Targon | 57.6 | 9,127 | 19,574 | rtx4090* | 5 | 62% |
| 20 | sn5 Hone | 56.5 | 18.32 | 40.29 | rtx4090* | 241 | 1% |

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
| wide (<30%) | 27 |
| concentrated (30–60%) | 23 |
| dominated (60–90%) | 27 |
| captured (>90%) | 23 |

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
| 2026-11-17T00:22 | sn15 | RELEASE | sn15 released v3.0.9: fix(sandbox): isolate each task in a run from th |
| 2026-11-17T00:22 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: fix(sandbox): isolate each task in a run  |
| 2026-11-17T00:22 | sn25 | RELEASE | sn25 released v2026.11.16-1100716180 |
| 2026-11-17T00:22 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Merge fix/validator-upload-encoding-1116: |
| 2026-11-17T00:22 | sn41 | SCORING_COMMIT | sn41 commit touches scoring: Document the one-agent-per-hotkey upload  |
| 2026-11-17T00:22 | sn42 | RELEASE | sn42 released v0.6.19 |
| 2026-11-17T00:22 | sn42 | SCORING_COMMIT | sn42 commit touches scoring: desk: a sweep of a miner's grants is job- |
| 2026-11-17T00:22 | sn62 | SCORING_COMMIT | sn62 commit touches scoring: add more validation |
| 2026-11-17T00:22 | sn66 | RELEASE | sn66 released v2026.11.16.4 |
| 2026-11-17T00:22 | sn70 | RELEASE | sn70 released build-v3rc1-2026.11.17: v3: pin the embeddings file (EMB |
| 2026-11-17T00:22 | sn94 | SCORING_COMMIT | sn94 commit touches scoring: Add miner hotel offer signer to room-kit  |
| 2026-11-17T00:22 | sn127 | RELEASE | sn127 released Release 9bd0c63 |
| 2026-11-17T00:22 | sn127 | SCORING_COMMIT | sn127 commit touches scoring: Weekly judge: left-out bodies, scores fr |
| 2026-11-16T16:14 | sn3 | SCORING_COMMIT | sn3 commit touches scoring: Stream Horizon scoring during packed-text  |
| 2026-11-16T16:14 | sn25 | RELEASE | sn25 released v2026.11.16-1100273030 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

