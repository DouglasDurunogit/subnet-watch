# Subnet watch — dashboard

_snapshot 2026-11-02T01:54:52Z · block 9415072 · run_status **ok**_

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
| New events this window | 2 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 67 | `████████████████████████████` |
| 0–0.2 | 8 | `███` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 29 | `████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn104 TAOstatus | 77.2 | 2,492 | 2,492 = | cpu-small | 1 | 100% |
| 2 | sn120 Affine | 74.5 | 2,857 | 2,857 = | rtx4090* | 10 | 10% |
| 3 | sn3 Teutonic | 73.1 | 1,908 | 3,824 | rtx4090* | 7 | 25% |
| 4 | sn97 Ingot | 72.6 | 1,627 | 1,627 = | rtx4090* | 5 | 20% |
| 5 | sn60 Bitsec.ai | 71.8 | 493 | 760 | cpu-small | 3 | 50% |
| 6 | sn103 Terza Inference | 69.8 | 697 | 1,826 | rtx4090* | 5 | 37% |
| 7 | sn14 Cacheon | 69.6 | 648 | 5,490 | rtx4090* | 3 | 84% |
| 8 | sn1 Apex | 68 | 404 | 799 | rtx4090* | 5 | 65% |
| 9 | sn53 engy | 67.8 | 383 | 2,075 | rtx4090 | 29 | 26% |
| 10 | sn15 ORO | 66.9 | 6.71 | 12,048 | cpu-small | 75 | 96% |
| 11 | sn67 Harnyx | 66.8 | 5.45 | 464 | cpu-small | 152 | 24% |
| 12 | sn107 Minos | 65.7 | 164 | 13,925 | cpu-small | 20 | 80% |
| 13 | sn102 ConnitoAI | 64.6 | 148 | 898 | rtx4090* | 12 | 29% |
| 14 | sn125 Refinery | 64.2 | 129 | 798 | rtx4090* | 4 | 50% |
| 15 | sn124 Swarm | 62.9 | 97.65 | 1,865 | rtx4090* | 15 | 31% |
| 16 | sn62 Ridges | 61.7 | 61.23 | 1,444 | rtx4090* | 36 | 25% |
| 17 | sn66 conjectures | 58.7 | 24.61 | 145 | rtx4090* | 6 | 81% |
| 18 | sn4 Targon | 58.4 | 11,519 | 25,790 | rtx4090* | 4 | 64% |
| 19 | sn91 cascade | 57.6 | 19.29 | 65.13 | rtx4090* | 6 | 95% |
| 20 | sn58 Attune | 56.8 | 511 | 823 | rtx4090* | 5 | 70% |

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
| 2026-11-02T01:55 | sn117 | RELEASE | sn117 released Merge pull request #57: everycli v0.8.7 UI reliability |
| 2026-11-02T01:55 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: bench site: Avg is the first score colum |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

