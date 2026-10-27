# Subnet watch — dashboard

_snapshot 2026-10-27T06:46:16Z · block 9373332 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 54 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 97 | `miner_burn` < 0.99 |
| Ranked | 97 | passed every gate |
| **Positive margin** | **54** | income beats machine cost |
| New events this window | 8 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 64 | `████████████████████████████` |
| 0–0.2 | 9 | `████` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 8 | `████` |
| 0.6–0.8 | 7 | `███` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 31 | `██████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn3 Teutonic | 73.4 | 2,083 | 4,175 | rtx4090* | 7 | 25% |
| 2 | sn97 Ingot | 72.9 | 1,779 | 1,779 = | rtx4090* | 5 | 20% |
| 3 | sn60 Bitsec.ai | 70 | 283 | 283 = | cpu-small | 3 | 50% |
| 4 | sn1 Apex | 68.1 | 421 | 845 | rtx4090* | 5 | 56% |
| 5 | sn46 Instant | 68.1 | 162 | 195 | cpu-small | 8 | 44% |
| 6 | sn67 Harnyx | 67.8 | 7.32 | 376 | cpu-small | 119 | 18% |
| 7 | sn56 Gradients | 67.3 | 331 | 5,458 | rtx4090* | 7 | 51% |
| 8 | sn120 Affine | 66.8 | 308 | 1,099 | rtx4090* | 105 | 4% |
| 9 | sn107 Minos | 66.7 | 207 | 17,546 | cpu-small | 20 | 80% |
| 10 | sn125 Refinery | 65.7 | 206 | 852 | rtx4090* | 4 | 50% |
| 11 | sn15 ORO | 65.5 | 6.50 | 13.99 | cpu-small | 67 | 97% |
| 12 | sn66 conjectures | 63.3 | 99.52 | 207 | rtx4090* | 4 | 80% |
| 13 | sn62 Ridges | 62.6 | 80.06 | 894 | rtx4090* | 44 | 15% |
| 14 | sn111 Claims | 58.9 | 27.01 | 2,633 | rtx4090* | 6 | 90% |
| 15 | sn28 SayGM | 58.3 | 23.69 | 1,570 | rtx4090* | 139 | 36% |
| 16 | sn5 Hone | 57.6 | 28.70 | 37.89 | rtx4090* | 242 | 1% |
| 17 | sn58 Attune | 57.4 | 608 | 978 | rtx4090* | 5 | 70% |
| 18 | sn49 Nepher Robotics | 56.3 | 439 | 3,124 | rtx4090* | 5 | 69% |
| 19 | sn92 REAX | 55.8 | 21.58 | 2,254 | rtx4090 | 235 | 14% |
| 20 | sn9 iota | 55.7 | 10,496 | 10,496 = | rtx4090* | 2 | 60% |

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
| concentrated (30–60%) | 24 |
| dominated (60–90%) | 22 |
| captured (>90%) | 23 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 98 |
| README keywords (GUESS) | 12 |
| min_compute.yml (curated) | 9 |
| code-submission (validator runs it) | 8 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-10-27T06:46 | sn2 | SCORING_COMMIT | sn2 commit touches scoring: Score finalized epoch snapshots and log un |
| 2026-10-27T06:46 | sn2 | README_TASK_DIFF | sn2 README task/scoring sections changed |
| 2026-10-27T06:46 | sn15 | RELEASE | sn15 released v3.0.5: fix(validator): policy_view.max_steps is the tas |
| 2026-10-27T06:46 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: fix(validator): policy_view.max_steps is  |
| 2026-10-27T06:46 | sn73 | BURN_DROP | sn73 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-10-27T06:46 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: docs: sync worker CONTRACT.md (relay spen |
| 2026-10-27T06:46 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Merge pull request #445 from Umi-BitSign/ |
| 2026-10-27T06:46 | sn123 | README_TASK_DIFF | sn123 README task/scoring sections changed |
| 2026-10-27T01:27 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Record the authorized evidence-verificati |
| 2026-10-27T01:27 | sn76 | BURN_DROP | sn76 burn fell 0.998 -> 0.978 - miners can earn again |
| 2026-10-27T01:27 | sn94 | SCORING_COMMIT | sn94 commit touches scoring: Accept a list of AMD ARK pins in the brok |
| 2026-10-27T01:27 | sn123 | README_TASK_DIFF | sn123 README task/scoring sections changed |
| 2026-10-27T01:27 | sn125 | README_TASK_DIFF | sn125 README task/scoring sections changed |
| 2026-10-26T21:56 | sn2 | SCORING_COMMIT | sn2 commit touches scoring: Document live Finney burn validator status |
| 2026-10-26T21:56 | sn2 | README_TASK_DIFF | sn2 README task/scoring sections changed |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

