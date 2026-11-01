# Subnet watch — dashboard

_snapshot 2026-11-01T13:50:24Z · block 9411453 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 57 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 99 | `miner_burn` < 0.99 |
| Ranked | 99 | passed every gate |
| **Positive margin** | **57** | income beats machine cost |
| New events this window | 7 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 65 | `████████████████████████████` |
| 0–0.2 | 8 | `███` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 6 | `███` |
| 0.6–0.8 | 8 | `███` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 29 | `████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn120 Affine | 74.6 | 2,903 | 2,903 = | rtx4090* | 10 | 10% |
| 2 | sn3 Teutonic | 73.2 | 1,928 | 3,865 | rtx4090* | 7 | 25% |
| 3 | sn97 Ingot | 72.7 | 1,663 | 1,663 = | rtx4090* | 5 | 20% |
| 4 | sn103 Terza Inference | 69.9 | 717 | 1,876 | rtx4090* | 5 | 38% |
| 5 | sn60 Bitsec.ai | 69.3 | 233 | 233 = | cpu-small | 3 | 50% |
| 6 | sn53 engy | 67.9 | 396 | 2,134 | rtx4090 | 29 | 26% |
| 7 | sn1 Apex | 67 | 300 | 712 | rtx4090* | 5 | 68% |
| 8 | sn15 ORO | 67 | 6.87 | 12,148 | cpu-small | 74 | 96% |
| 9 | sn67 Harnyx | 66.7 | 5.54 | 472 | cpu-small | 148 | 24% |
| 10 | sn107 Minos | 65.7 | 165 | 14,046 | cpu-small | 20 | 80% |
| 11 | sn102 ConnitoAI | 64.5 | 146 | 793 | rtx4090* | 11 | 26% |
| 12 | sn125 Refinery | 64.2 | 131 | 810 | rtx4090* | 4 | 50% |
| 13 | sn124 Swarm | 63 | 102 | 1,896 | rtx4090* | 15 | 31% |
| 14 | sn62 Ridges | 61.7 | 62.12 | 1,462 | rtx4090* | 36 | 25% |
| 15 | sn66 conjectures | 61.5 | 58.02 | 191 | rtx4090* | 4 | 80% |
| 16 | sn4 Targon | 58.5 | 11,774 | 26,361 | rtx4090* | 4 | 64% |
| 17 | sn91 cascade | 57.6 | 19.46 | 65.60 | rtx4090* | 6 | 95% |
| 18 | sn58 Attune | 57 | 543 | 873 | rtx4090* | 5 | 70% |
| 19 | sn46 Instant | 56.8 | 194 | 211 | cpu-small | 7 | 40% |
| 20 | sn56 Gradients | 56.6 | 477 | 1,300 | rtx4090* | 6 | 51% |

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
| concentrated (30–60%) | 20 |
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
| 2026-11-01T13:50 | sn9 | RELEASE | sn9 released v4.14.0 |
| 2026-11-01T13:50 | sn28 | RELEASE | sn28 released v0.5.17-dev |
| 2026-11-01T13:50 | sn76 | BURN_DROP | sn76 burn fell 0.991 -> 0.990 - miners can earn again |
| 2026-11-01T13:50 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: Merge pull request #409 from TensorLink-A |
| 2026-11-01T13:50 | sn94 | SCORING_COMMIT | sn94 commit touches scoring: Remove stale miner box runbook and seedbo |
| 2026-11-01T13:50 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: MINING.md: practice time limit wording p |
| 2026-11-01T13:50 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: bench tools: per-task MATH-500 cross-che |
| 2026-11-01T06:44 | sn11 | RELEASE | sn11 released v0.7.7 |
| 2026-11-01T06:44 | sn11 | SCORING_COMMIT | sn11 commit touches scoring: [coding-agent] bump validator version to  |
| 2026-11-01T06:44 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: Merge pull request #435 from reliquadotai |
| 2026-11-01T00:27 | sn15 | RELEASE | sn15 released v3.0.7 |
| 2026-11-01T00:27 | sn66 | RELEASE | sn66 released v2026.10.31.2 |
| 2026-10-31T21:27 | sn1 | RELEASE | sn1 released v4.6.0 |
| 2026-10-31T21:27 | sn11 | RELEASE | sn11 released v0.7.6 |
| 2026-10-31T21:27 | sn11 | SCORING_COMMIT | sn11 commit touches scoring: chore(release): validator 0.7.6 for bound |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

