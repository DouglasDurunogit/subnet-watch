# Subnet watch — dashboard

_snapshot 2026-08-18T12:03:51Z · block 8871489 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 51 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 90 | `miner_burn` < 0.99 |
| Ranked | 90 | passed every gate |
| **Positive margin** | **51** | income beats machine cost |
| New events this window | 3 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 62 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 7 | `███` |
| 0.6–0.8 | 6 | `███` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 38 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 78.2 | 98.03 | 189 | cpu-small | 10 | 20% |
| 2 | sn67 Harnyx | 71.9 | 20.12 | 428 | cpu-small | 127 | 13% |
| 3 | sn26 Perturb | 70.7 | 39.38 | 72.30 | rtx3060 | 10 | 70% |
| 4 | sn1 Apex | 70.4 | 838 | 1,093 | rtx4090* | 4 | 52% |
| 5 | sn41 Almanac | 69.2 | 10.87 | 50.12 | cpu-small | 74 | 67% |
| 6 | sn91 cascade | 68.8 | 523 | 2,118 | rtx4090* | 5 | 51% |
| 7 | sn62 Ridges | 68.4 | 454 | 2,104 | rtx4090* | 6 | 40% |
| 8 | sn96 Verathos | 67.9 | 19.73 | 385 | rtx4090 | 66 | 41% |
| 9 | sn56 Gradients | 67.8 | 380 | 931 | rtx4090* | 8 | 68% |
| 10 | sn21 AdTAO | 67.8 | 7.82 | 34.99 | cpu-small | 88 | 45% |
| 11 | sn38 ChronoLLM | 67.6 | 149 | 3,168 | cpu-small | 10 | 52% |
| 12 | sn15 ORO | 67.5 | 10.33 | 12,516 | cpu-small | 67 | 95% |
| 13 | sn11 TrajectoryRL | 67.1 | 4,124 | 4,124 = | cpu-small | 1 | 100% |
| 14 | sn124 Swarm | 66.1 | 241 | 722 | rtx4090* | 24 | 11% |
| 15 | sn107 Minos | 64.3 | 116 | 33,061 | cpu-small | 20 | 90% |
| 16 | sn85 Vidaio | 63.6 | 110 | 370 | rtx4090* | 13 | 42% |
| 17 | sn28 gm | 63.4 | 105 | 2,232 | rtx4090* | 41 | 24% |
| 18 | sn55 NIOME | 61.6 | 59.10 | 497 | rtx4090* | 11 | 29% |
| 19 | sn102 ConnitoAI | 59.6 | 1,174 | 1,309 | rtx4090* | 5 | 26% |
| 20 | sn60 Bitsec.ai | 59 | 372 | 372 = | cpu-small | 3 | 50% |

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
| concentrated (30–60%) | 18 |
| dominated (60–90%) | 16 |
| captured (>90%) | 28 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 102 |
| code-submission (validator runs it) | 10 |
| min_compute.yml (curated) | 9 |
| README keywords (GUESS) | 6 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-08-18T12:04 | sn10 | README_TASK_DIFF | sn10 README task/scoring sections changed |
| 2026-08-18T10:55 | sn65 | SCORING_COMMIT | sn65 commit touches scoring: Merge pull request #4 from taofu-labs/doc |
| 2026-08-18T10:55 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-08-18T09:46 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-08-18T08:51 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-2702: verify GPU persistence mode aft |
| 2026-08-18T07:14 | sn85 | SCORING_COMMIT | sn85 commit touches scoring: debug VBR scoring in compression competit |
| 2026-08-18T07:14 | sn89 | SCORING_COMMIT | sn89 commit touches scoring: hf board: keep a re-rolled miner's retire |
| 2026-08-18T05:02 | sn91 | README_TASK_DIFF | sn91 README task/scoring sections changed |
| 2026-08-18T04:21 | sn91 | RELEASE | sn91 released pre-decay-wsd-contract |
| 2026-08-18T04:21 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: audit fixes + miner CLI: warm-start init  |
| 2026-08-18T02:44 | sn15 | RELEASE | sn15 released v1.2.7 |
| 2026-08-18T01:47 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Repair semantic gate verification fixture |
| 2026-08-18T00:01 | sn56 | SCORING_COMMIT | sn56 commit touches scoring: Fix re-finalize crowning the re-evaluated |
| 2026-08-17T23:02 | sn14 | RELEASE | sn14 released v2-finite-debt-preextraction: Pre-extraction snapshot of |
| 2026-08-17T22:36 | sn54 | SCORING_COMMIT | sn54 commit touches scoring: updating miner info |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

