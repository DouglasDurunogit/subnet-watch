# Subnet watch — dashboard

_snapshot 2026-11-03T09:27:09Z · block 9424531 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 57 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 101 | `miner_burn` < 0.99 |
| Ranked | 101 | passed every gate |
| **Positive margin** | **57** | income beats machine cost |
| New events this window | 8 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 67 | `████████████████████████████` |
| 0–0.2 | 8 | `███` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 27 | `███████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn120 Affine | 74.2 | 2,601 | 5,211 | rtx4090* | 10 | 19% |
| 2 | sn3 Teutonic | 73 | 1,826 | 3,660 | rtx4090* | 7 | 25% |
| 3 | sn97 Ingot | 72.4 | 1,528 | 1,528 = | rtx4090* | 5 | 20% |
| 4 | sn67 Harnyx | 69.6 | 11.50 | 171 | cpu-small | 129 | 9% |
| 5 | sn103 Terza Inference | 68.4 | 460 | 1,238 | rtx4090* | 5 | 34% |
| 6 | sn53 engy | 67.6 | 362 | 1,966 | rtx4090 | 29 | 26% |
| 7 | sn1 Apex | 67.3 | 330 | 777 | rtx4090* | 4 | 68% |
| 8 | sn56 Gradients | 65.9 | 219 | 4,852 | rtx4090* | 8 | 51% |
| 9 | sn107 Minos | 65.7 | 164 | 13,939 | cpu-small | 20 | 80% |
| 10 | sn15 ORO | 65.6 | 6.28 | 11,081 | cpu-small | 75 | 95% |
| 11 | sn38 ChronoLLM | 63.7 | 54.89 | 489 | cpu-small | 10 | 52% |
| 12 | sn102 ConnitoAI | 63 | 93.24 | 1,446 | rtx4090* | 10 | 41% |
| 13 | sn124 Swarm | 62.1 | 78.39 | 1,786 | rtx4090* | 15 | 31% |
| 14 | sn121 sundae_bar | 61.9 | 893 | 893 = | cpu-small | 2 | 60% |
| 15 | sn62 Ridges | 61.5 | 58.11 | 1,379 | rtx4090* | 36 | 25% |
| 16 | sn117 everyframe.studi | 60.6 | 44.75 | 133 | rtx4090* | 11 | 85% |
| 17 | sn60 Bitsec.ai | 59.9 | 483 | 744 | cpu-small | 3 | 50% |
| 18 | sn66 conjectures | 58.5 | 23.37 | 150 | rtx4090* | 6 | 80% |
| 19 | sn80 OpenRoboto | 57.3 | 575 | 1,120 | rtx4090* | 12 | 17% |
| 20 | sn58 Attune | 56.4 | 451 | 726 | rtx4090* | 5 | 70% |

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
| wide (<30%) | 30 |
| concentrated (30–60%) | 19 |
| dominated (60–90%) | 25 |
| captured (>90%) | 24 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 99 |
| README keywords (GUESS) | 11 |
| min_compute.yml (curated) | 9 |
| code-submission (validator runs it) | 8 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-11-03T09:27 | sn24 | BURN_DROP | sn24 burn fell 1.000 -> 0.031 - miners can earn again |
| 2026-11-03T09:27 | sn51 | RELEASE | sn51 released lium-protocol-v2.4.0 |
| 2026-11-03T09:27 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-5372 - [P1] VerifyX: fail a node whos |
| 2026-11-03T09:27 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Hold November 3 scoring until improved ve |
| 2026-11-03T09:27 | sn76 | BURN_DROP | sn76 burn fell 0.997 -> 0.972 - miners can earn again |
| 2026-11-03T09:27 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: Merge pull request #445 from reliquadotai |
| 2026-11-03T09:27 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: fix(money): miner spend per RENT, not per |
| 2026-11-03T09:27 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Crown origin rebind tests: the cancel re |
| 2026-11-03T01:50 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Document audited evaluator recovery metad |
| 2026-11-03T01:50 | sn34 | SCORING_COMMIT | sn34 commit touches scoring: docs: use pack versions in miner scoring  |
| 2026-11-03T01:50 | sn48 | README_TASK_DIFF | sn48 README task/scoring sections changed |
| 2026-11-03T01:50 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: feat(funding): miner-set total budget per |
| 2026-11-03T01:50 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Crown re-measure tests: the fake adapter |
| 2026-11-03T01:50 | sn117 | RELEASE | sn117 released everycli v0.9.2 |
| 2026-11-03T01:50 | sn117 | README_TASK_DIFF | sn117 README task/scoring sections changed |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

