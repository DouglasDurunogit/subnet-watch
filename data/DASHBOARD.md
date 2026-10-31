# Subnet watch — dashboard

_snapshot 2026-10-31T06:56:03Z · block 9402181 · run_status **ok**_

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
| New events this window | 8 | see ALARMS.md |

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
| 0.6–0.8 | 10 | `████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 28 | `████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn120 Affine | 74.5 | 2,880 | 2,880 = | rtx4090* | 10 | 10% |
| 2 | sn3 Teutonic | 73.2 | 1,928 | 3,864 | rtx4090* | 7 | 25% |
| 3 | sn97 Ingot | 72.8 | 1,684 | 1,684 = | rtx4090* | 5 | 20% |
| 4 | sn103 Terza Inference | 71.2 | 1,050 | 1,958 | rtx4090* | 4 | 42% |
| 5 | sn60 Bitsec.ai | 69.4 | 241 | 241 = | cpu-small | 3 | 50% |
| 6 | sn53 engy | 67.9 | 394 | 2,128 | rtx4090 | 29 | 26% |
| 7 | sn1 Apex | 67.6 | 357 | 826 | rtx4090* | 5 | 62% |
| 8 | sn67 Harnyx | 67.6 | 6.88 | 362 | cpu-small | 136 | 18% |
| 9 | sn15 ORO | 66.7 | 6.68 | 12,471 | cpu-small | 74 | 96% |
| 10 | sn107 Minos | 65.7 | 166 | 14,110 | cpu-small | 20 | 80% |
| 11 | sn125 Refinery | 64.7 | 152 | 819 | rtx4090* | 4 | 50% |
| 12 | sn102 ConnitoAI | 64.5 | 143 | 714 | rtx4090* | 9 | 25% |
| 13 | sn124 Swarm | 61.7 | 70.12 | 2,811 | rtx4090* | 12 | 45% |
| 14 | sn62 Ridges | 61.1 | 52.01 | 3,017 | rtx4090* | 32 | 52% |
| 15 | sn66 conjectures | 58.8 | 25.48 | 160 | rtx4090* | 7 | 80% |
| 16 | sn4 Targon | 58.4 | 11,421 | 25,577 | rtx4090* | 4 | 64% |
| 17 | sn56 Gradients | 57.5 | 626 | 5,148 | rtx4090* | 6 | 51% |
| 18 | sn91 cascade | 57.5 | 18.94 | 64.23 | rtx4090* | 6 | 95% |
| 19 | sn58 Attune | 57.1 | 556 | 895 | rtx4090* | 5 | 70% |
| 20 | sn117 everyframe.studi | 56.9 | 14.83 | 191 | rtx4090* | 6 | 84% |

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
| wide (<30%) | 24 |
| concentrated (30–60%) | 22 |
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
| 2026-10-31T06:56 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Record the census fix deployment in taskw |
| 2026-10-31T06:56 | sn34 | SCORING_COMMIT | sn34 commit touches scoring: fix: score empty stopped ArenaHard answer |
| 2026-10-31T06:56 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-5457 - [P0] Validator: GPU drop repor |
| 2026-10-31T06:56 | sn62 | RELEASE | sn62 released v0.3.16 |
| 2026-10-31T06:56 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Keep validator checkout warnings out of u |
| 2026-10-31T06:56 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: King leg: channel floor by ref, ignore th |
| 2026-10-31T06:56 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Record five owner decisions given in the |
| 2026-10-31T06:56 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: SN120 free-file protocol: miners upload  |
| 2026-10-31T00:56 | sn25 | RELEASE | sn25 released v2026.10.30-1086064830 |
| 2026-10-31T00:56 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Add quality-gated CPU efficiency rewards  |
| 2026-10-31T00:56 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: bench data: a completion marker only for  |
| 2026-10-31T00:56 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: MINING: help contact is the owner's Tele |
| 2026-10-30T21:08 | sn15 | RELEASE | sn15 released v3.0.6: fix(validator): keep sandbox output from blockin |
| 2026-10-30T21:08 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: fix(validator): keep sandbox output from  |
| 2026-10-30T21:08 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Require verified empty EMA prior for head |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

