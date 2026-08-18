# Subnet watch — dashboard

_snapshot 2026-08-18T01:47:13Z · block 8868406 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 52 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 91 | `miner_burn` < 0.99 |
| Ranked | 91 | passed every gate |
| **Positive margin** | **52** | income beats machine cost |
| New events this window | 1 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 62 | `████████████████████████████` |
| 0–0.2 | 4 | `██` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 7 | `███` |
| 0.6–0.8 | 6 | `███` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 37 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 78.2 | 100 | 194 | cpu-small | 10 | 20% |
| 2 | sn67 Harnyx | 71.8 | 19.84 | 372 | cpu-small | 129 | 11% |
| 3 | sn26 Perturb | 70.8 | 40.08 | 73.55 | rtx3060 | 10 | 70% |
| 4 | sn1 Apex | 70.6 | 885 | 1,064 | rtx4090* | 4 | 52% |
| 5 | sn41 Almanac | 68.9 | 10.17 | 48.08 | cpu-small | 76 | 69% |
| 6 | sn91 cascade | 68.8 | 519 | 2,099 | rtx4090* | 5 | 51% |
| 7 | sn62 Ridges | 68.5 | 467 | 2,164 | rtx4090* | 6 | 40% |
| 8 | sn96 Verathos | 68.1 | 20.80 | 507 | rtx4090 | 71 | 41% |
| 9 | sn56 Gradients | 67.9 | 390 | 950 | rtx4090* | 8 | 68% |
| 10 | sn21 AdTAO | 67.8 | 7.94 | 35.49 | cpu-small | 88 | 45% |
| 11 | sn38 ChronoLLM | 67.6 | 150 | 3,174 | cpu-small | 10 | 52% |
| 12 | sn15 ORO | 67.6 | 10.27 | 20.52 | cpu-small | 66 | 94% |
| 13 | sn11 TrajectoryRL | 67 | 4,118 | 4,118 = | cpu-small | 1 | 100% |
| 14 | sn124 Swarm | 65.9 | 223 | 491 | rtx4090* | 24 | 11% |
| 15 | sn107 Minos | 64.1 | 116 | 33,948 | cpu-small | 20 | 90% |
| 16 | sn98 NeverPlayAlone | 64 | 1,680 | 1,680 = | cpu-small | 1 | 100% |
| 17 | sn85 Vidaio | 64 | 123 | 1,309 | rtx4090* | 13 | 42% |
| 18 | sn55 NIOME | 61.6 | 59.90 | 503 | rtx4090* | 11 | 29% |
| 19 | sn28 gm | 61.3 | 56.80 | 2,592 | rtx4090* | 41 | 27% |
| 20 | sn60 Bitsec.ai | 58.9 | 368 | 368 = | cpu-small | 3 | 50% |

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
| concentrated (30–60%) | 20 |
| dominated (60–90%) | 19 |
| captured (>90%) | 26 |

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
| 2026-08-18T01:47 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Repair semantic gate verification fixture |
| 2026-08-18T00:01 | sn56 | SCORING_COMMIT | sn56 commit touches scoring: Fix re-finalize crowning the re-evaluated |
| 2026-08-17T23:02 | sn14 | RELEASE | sn14 released v2-finite-debt-preextraction: Pre-extraction snapshot of |
| 2026-08-17T22:36 | sn54 | SCORING_COMMIT | sn54 commit touches scoring: updating miner info |
| 2026-08-17T22:36 | sn62 | RELEASE | sn62 released v0.2.8 |
| 2026-08-17T21:09 | sn21 | RELEASE | sn21 released SN21 training bundle — 10,791 records, refreshed 2026-08 |
| 2026-08-17T19:36 | sn51 | RELEASE | sn51 released executor-v1.121 |
| 2026-08-17T19:36 | sn65 | SCORING_COMMIT | sn65 commit touches scoring: Merge pull request #3 from taofu-labs/val |
| 2026-08-17T18:54 | sn21 | RELEASE | sn21 released SN21 training bundle (1977 records, refreshed 2026-08-17 |
| 2026-08-17T17:55 | sn123 | README_TASK_DIFF | sn123 README task/scoring sections changed |
| 2026-08-17T16:41 | sn10 | SCORING_COMMIT | sn10 commit touches scoring: feat: better miner commit patch logs (#83 |
| 2026-08-17T15:52 | sn121 | BURN_DROP | sn121 burn fell 1.000 -> 0.620 - miners can earn again |
| 2026-08-17T13:03 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: feat: add adaptive miner selection and r |
| 2026-08-17T13:03 | sn114 | SCORING_COMMIT | sn114 commit touches scoring: hotfix(scoring): exclude comp 112 stage  |
| 2026-08-17T11:12 | sn85 | SCORING_COMMIT | sn85 commit touches scoring: treat miner sandbox raised error as miner |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

