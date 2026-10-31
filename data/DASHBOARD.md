# Subnet watch — dashboard

_snapshot 2026-10-31T13:35:35Z · block 9404179 · run_status **ok**_

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
| New events this window | 4 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 66 | `████████████████████████████` |
| 0–0.2 | 8 | `███` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 11 | `█████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 27 | `███████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn120 Affine | 74.5 | 2,869 | 2,869 = | rtx4090* | 10 | 10% |
| 2 | sn3 Teutonic | 73.2 | 1,920 | 3,848 | rtx4090* | 7 | 25% |
| 3 | sn97 Ingot | 72.7 | 1,673 | 1,673 = | rtx4090* | 5 | 20% |
| 4 | sn103 Terza Inference | 70.3 | 799 | 2,090 | rtx4090* | 5 | 41% |
| 5 | sn60 Bitsec.ai | 69.4 | 239 | 239 = | cpu-small | 3 | 50% |
| 6 | sn53 engy | 67.8 | 388 | 2,095 | rtx4090 | 29 | 26% |
| 7 | sn1 Apex | 67.4 | 341 | 792 | rtx4090* | 5 | 63% |
| 8 | sn67 Harnyx | 67.2 | 6.06 | 479 | cpu-small | 132 | 24% |
| 9 | sn15 ORO | 66.5 | 6.64 | 12,412 | cpu-small | 74 | 96% |
| 10 | sn107 Minos | 65.7 | 165 | 14,057 | cpu-small | 20 | 80% |
| 11 | sn125 Refinery | 64.7 | 150 | 814 | rtx4090* | 4 | 50% |
| 12 | sn102 ConnitoAI | 64.5 | 144 | 831 | rtx4090* | 9 | 28% |
| 13 | sn124 Swarm | 62.9 | 99.18 | 2,009 | rtx4090* | 14 | 33% |
| 14 | sn117 everyframe.studi | 62.4 | 77.50 | 301 | rtx4090* | 7 | 79% |
| 15 | sn62 Ridges | 61.2 | 53.49 | 2,497 | rtx4090* | 33 | 43% |
| 16 | sn66 conjectures | 58.7 | 24.98 | 158 | rtx4090* | 7 | 80% |
| 17 | sn4 Targon | 58.3 | 11,358 | 25,430 | rtx4090* | 4 | 64% |
| 18 | sn91 cascade | 57.6 | 19.33 | 65.26 | rtx4090* | 6 | 95% |
| 19 | sn56 Gradients | 57.5 | 626 | 5,150 | rtx4090* | 6 | 51% |
| 20 | sn58 Attune | 57.1 | 553 | 889 | rtx4090* | 5 | 70% |

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
| dominated (60–90%) | 24 |
| captured (>90%) | 28 |

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
| 2026-10-31T13:35 | sn14 | SCORING_COMMIT | sn14 commit touches scoring: Pay no first PASS under the reward margin |
| 2026-10-31T13:35 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-10-31T13:35 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: Merge pull request #393 from TensorLink-A |
| 2026-10-31T13:35 | sn108 | SCORING_COMMIT | sn108 commit touches scoring: Between quests the validator checks its  |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

