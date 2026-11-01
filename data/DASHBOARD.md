# Subnet watch — dashboard

_snapshot 2026-11-01T22:44:48Z · block 9414125 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 55 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 98 | `miner_burn` < 0.99 |
| Ranked | 98 | passed every gate |
| **Positive margin** | **55** | income beats machine cost |
| New events this window | 3 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 67 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 30 | `█████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn120 Affine | 74.5 | 2,842 | 2,842 = | rtx4090* | 10 | 10% |
| 2 | sn3 Teutonic | 73.1 | 1,893 | 3,795 | rtx4090* | 7 | 25% |
| 3 | sn97 Ingot | 72.6 | 1,620 | 1,620 = | rtx4090* | 5 | 20% |
| 4 | sn60 Bitsec.ai | 71.8 | 492 | 758 | cpu-small | 3 | 50% |
| 5 | sn103 Terza Inference | 70.1 | 763 | 1,996 | rtx4090* | 5 | 41% |
| 6 | sn14 Cacheon | 69.5 | 645 | 5,463 | rtx4090* | 3 | 84% |
| 7 | sn1 Apex | 68 | 406 | 803 | rtx4090* | 5 | 65% |
| 8 | sn53 engy | 67.8 | 381 | 2,061 | rtx4090 | 29 | 26% |
| 9 | sn15 ORO | 66.8 | 6.62 | 13.46 | cpu-small | 75 | 96% |
| 10 | sn67 Harnyx | 66.8 | 5.42 | 463 | cpu-small | 152 | 24% |
| 11 | sn107 Minos | 65.6 | 162 | 13,775 | cpu-small | 20 | 80% |
| 12 | sn102 ConnitoAI | 64.5 | 145 | 1,165 | rtx4090* | 6 | 38% |
| 13 | sn125 Refinery | 64.1 | 128 | 795 | rtx4090* | 4 | 50% |
| 14 | sn124 Swarm | 62.9 | 97.43 | 1,861 | rtx4090* | 15 | 31% |
| 15 | sn62 Ridges | 61.7 | 60.95 | 1,438 | rtx4090* | 36 | 25% |
| 16 | sn66 conjectures | 58.7 | 24.27 | 154 | rtx4090* | 6 | 80% |
| 17 | sn4 Targon | 58.4 | 11,428 | 25,588 | rtx4090* | 4 | 64% |
| 18 | sn91 cascade | 57.6 | 19.28 | 65.11 | rtx4090* | 6 | 95% |
| 19 | sn58 Attune | 56.8 | 510 | 821 | rtx4090* | 5 | 70% |
| 20 | sn56 Gradients | 56.6 | 467 | 1,272 | rtx4090* | 6 | 51% |

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
| concentrated (30–60%) | 18 |
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
| 2026-11-01T22:45 | sn11 | SCORING_COMMIT | sn11 commit touches scoring: [coding-agent] remove automatic alpha bur |
| 2026-11-01T22:45 | sn28 | RELEASE | sn28 released v0.5.18 |
| 2026-11-01T22:45 | sn117 | RELEASE | sn117 released everycli v0.8.6 |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

