# Subnet watch — dashboard

_snapshot 2026-11-01T18:52:45Z · block 9412964 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 57 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 98 | `miner_burn` < 0.99 |
| Ranked | 98 | passed every gate |
| **Positive margin** | **57** | income beats machine cost |
| New events this window | 2 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 65 | `████████████████████████████` |
| 0–0.2 | 8 | `███` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 30 | `█████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn120 Affine | 74.5 | 2,853 | 2,853 = | rtx4090* | 10 | 10% |
| 2 | sn3 Teutonic | 73.1 | 1,902 | 3,812 | rtx4090* | 7 | 25% |
| 3 | sn97 Ingot | 72.6 | 1,628 | 1,628 = | rtx4090* | 5 | 20% |
| 4 | sn103 Terza Inference | 69.9 | 711 | 1,863 | rtx4090* | 5 | 38% |
| 5 | sn14 Cacheon | 69.6 | 648 | 5,488 | rtx4090* | 3 | 84% |
| 6 | sn60 Bitsec.ai | 69.3 | 229 | 229 = | cpu-small | 3 | 50% |
| 7 | sn53 engy | 67.8 | 385 | 2,076 | rtx4090 | 29 | 26% |
| 8 | sn67 Harnyx | 66.8 | 5.45 | 464 | cpu-small | 148 | 24% |
| 9 | sn1 Apex | 66.6 | 268 | 835 | rtx4090* | 5 | 67% |
| 10 | sn15 ORO | 66.2 | 6.70 | 13.42 | cpu-small | 74 | 96% |
| 11 | sn107 Minos | 65.7 | 162 | 13,836 | cpu-small | 20 | 80% |
| 12 | sn102 ConnitoAI | 64.6 | 146 | 1,077 | rtx4090* | 8 | 35% |
| 13 | sn125 Refinery | 64.2 | 129 | 798 | rtx4090* | 4 | 50% |
| 14 | sn124 Swarm | 63 | 100 | 1,870 | rtx4090* | 15 | 31% |
| 15 | sn62 Ridges | 61.7 | 61.06 | 1,440 | rtx4090* | 36 | 25% |
| 16 | sn66 conjectures | 58.7 | 24.65 | 156 | rtx4090* | 6 | 81% |
| 17 | sn4 Targon | 58.4 | 11,556 | 25,874 | rtx4090* | 4 | 64% |
| 18 | sn91 cascade | 57.6 | 19.42 | 65.50 | rtx4090* | 6 | 95% |
| 19 | sn58 Attune | 56.8 | 505 | 814 | rtx4090* | 5 | 70% |
| 20 | sn56 Gradients | 56.6 | 468 | 1,275 | rtx4090* | 6 | 51% |

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
| concentrated (30–60%) | 19 |
| dominated (60–90%) | 24 |
| captured (>90%) | 26 |

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
| 2026-11-01T18:53 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: GPU receipt worker: the per-task run dir |
| 2026-11-01T18:53 | sn117 | RELEASE | sn117 released everycli v0.8.4 |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

