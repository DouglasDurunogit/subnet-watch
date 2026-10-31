# Subnet watch — dashboard

_snapshot 2026-10-31T21:27:25Z · block 9406538 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 54 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 99 | `miner_burn` < 0.99 |
| Ranked | 99 | passed every gate |
| **Positive margin** | **54** | income beats machine cost |
| New events this window | 10 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 65 | `████████████████████████████` |
| 0–0.2 | 9 | `████` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 29 | `████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn120 Affine | 74.6 | 2,903 | 2,903 = | rtx4090* | 10 | 10% |
| 2 | sn3 Teutonic | 73.2 | 1,933 | 3,875 | rtx4090* | 7 | 25% |
| 3 | sn97 Ingot | 72.8 | 1,685 | 1,685 = | rtx4090* | 5 | 20% |
| 4 | sn103 Terza Inference | 70 | 731 | 1,913 | rtx4090* | 5 | 39% |
| 5 | sn53 engy | 67.9 | 399 | 2,153 | rtx4090 | 29 | 26% |
| 6 | sn1 Apex | 67.3 | 330 | 770 | rtx4090* | 5 | 65% |
| 7 | sn67 Harnyx | 67.3 | 6.02 | 476 | cpu-small | 140 | 24% |
| 8 | sn15 ORO | 66.7 | 6.50 | 12,183 | cpu-small | 74 | 96% |
| 9 | sn107 Minos | 65.7 | 166 | 14,107 | cpu-small | 20 | 80% |
| 10 | sn125 Refinery | 64.7 | 153 | 825 | rtx4090* | 4 | 50% |
| 11 | sn102 ConnitoAI | 64.6 | 147 | 1,174 | rtx4090* | 7 | 39% |
| 12 | sn124 Swarm | 63 | 102 | 2,074 | rtx4090* | 14 | 33% |
| 13 | sn62 Ridges | 61.5 | 59.00 | 2,142 | rtx4090* | 34 | 37% |
| 14 | sn117 everyframe.studi | 60.5 | 43.45 | 90.77 | rtx4090* | 7 | 89% |
| 15 | sn66 conjectures | 58.9 | 26.53 | 99.56 | rtx4090* | 7 | 84% |
| 16 | sn4 Targon | 58.4 | 11,539 | 25,835 | rtx4090* | 4 | 64% |
| 17 | sn91 cascade | 57.5 | 18.94 | 64.22 | rtx4090* | 6 | 95% |
| 18 | sn46 Instant | 57.4 | 233 | 251 | cpu-small | 6 | 40% |
| 19 | sn58 Attune | 57.1 | 558 | 898 | rtx4090* | 5 | 70% |
| 20 | sn56 Gradients | 56.6 | 473 | 1,289 | rtx4090* | 6 | 51% |

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
| wide (<30%) | 23 |
| concentrated (30–60%) | 23 |
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
| 2026-10-31T21:27 | sn1 | RELEASE | sn1 released v4.6.0 |
| 2026-10-31T21:27 | sn11 | RELEASE | sn11 released v0.7.6 |
| 2026-10-31T21:27 | sn11 | SCORING_COMMIT | sn11 commit touches scoring: chore(release): validator 0.7.6 for bound |
| 2026-10-31T21:27 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Merge feat/miner-pprof: opt-in pprof and  |
| 2026-10-31T21:27 | sn34 | SCORING_COMMIT | sn34 commit touches scoring: Batch frozen tasks with redundant sandbox |
| 2026-10-31T21:27 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Keep admission source review on verified  |
| 2026-10-31T21:27 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Rewards: testnet-winner-v5-launch resets |
| 2026-10-31T21:27 | sn117 | RELEASE | sn117 released everycli v0.8.3 |
| 2026-10-31T21:27 | sn117 | README_TASK_DIFF | sn117 README task/scoring sections changed |
| 2026-10-31T21:27 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: SN120 miner kit (miner/): everything a m |
| 2026-10-31T17:58 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: docs: the settling window is 2 days every |
| 2026-10-31T17:58 | sn21 | README_TASK_DIFF | sn21 README task/scoring sections changed |
| 2026-10-31T17:58 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Preserve verified training pairs from inc |
| 2026-10-31T17:58 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Miner client: every HTTP call to a door  |
| 2026-10-31T17:58 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: SN120 legacy removal docs: llms.txt (sit |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

