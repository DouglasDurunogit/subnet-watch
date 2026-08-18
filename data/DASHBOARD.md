# Subnet watch — dashboard

_snapshot 2026-08-18T09:45:33Z · block 8870797 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 50 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 90 | `miner_burn` < 0.99 |
| Ranked | 90 | passed every gate |
| **Positive margin** | **50** | income beats machine cost |
| New events this window | 2 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 63 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 3 | `█` |
| 0.4–0.6 | 7 | `███` |
| 0.6–0.8 | 6 | `███` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 38 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn41 Almanac | 83.3 | 366 | 1,041 | cpu-small | 5 | 37% |
| 2 | sn76 Phylax | 78.2 | 98.53 | 190 | cpu-small | 10 | 20% |
| 3 | sn67 Harnyx | 71.9 | 20.15 | 429 | cpu-small | 122 | 13% |
| 4 | sn26 Perturb | 70.7 | 39.59 | 72.68 | rtx3060 | 10 | 70% |
| 5 | sn1 Apex | 70.4 | 844 | 1,100 | rtx4090* | 4 | 52% |
| 6 | sn91 cascade | 68.8 | 515 | 2,084 | rtx4090* | 5 | 51% |
| 7 | sn62 Ridges | 68.4 | 456 | 2,114 | rtx4090* | 6 | 40% |
| 8 | sn56 Gradients | 67.8 | 383 | 936 | rtx4090* | 8 | 68% |
| 9 | sn21 AdTAO | 67.8 | 7.86 | 35.16 | cpu-small | 88 | 45% |
| 10 | sn38 ChronoLLM | 67.6 | 150 | 3,182 | cpu-small | 10 | 52% |
| 11 | sn96 Verathos | 67.5 | 17.97 | 382 | rtx4090 | 74 | 41% |
| 12 | sn15 ORO | 67.5 | 10.06 | 12,571 | cpu-small | 66 | 95% |
| 13 | sn11 TrajectoryRL | 67.1 | 4,130 | 4,130 = | cpu-small | 1 | 100% |
| 14 | sn124 Swarm | 66.1 | 240 | 729 | rtx4090* | 24 | 11% |
| 15 | sn28 gm | 64.4 | 143 | 2,563 | rtx4090* | 41 | 27% |
| 16 | sn107 Minos | 64.2 | 116 | 33,342 | cpu-small | 20 | 90% |
| 17 | sn85 Vidaio | 63.9 | 120 | 370 | rtx4090* | 13 | 42% |
| 18 | sn55 NIOME | 61.6 | 59.60 | 500 | rtx4090* | 11 | 29% |
| 19 | sn102 ConnitoAI | 59.1 | 1,000 | 1,695 | rtx4090* | 6 | 34% |
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
| wide (<30%) | 25 |
| concentrated (30–60%) | 21 |
| dominated (60–90%) | 16 |
| captured (>90%) | 27 |

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
| 2026-08-17T22:36 | sn62 | RELEASE | sn62 released v0.2.8 |
| 2026-08-17T21:09 | sn21 | RELEASE | sn21 released SN21 training bundle — 10,791 records, refreshed 2026-08 |
| 2026-08-17T19:36 | sn51 | RELEASE | sn51 released executor-v1.121 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

