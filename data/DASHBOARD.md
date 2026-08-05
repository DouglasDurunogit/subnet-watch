# Subnet watch — dashboard

_snapshot 2026-08-05T18:45:06Z · block 8779905 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 55 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 91 | `miner_burn` < 0.99 |
| Ranked | 91 | passed every gate |
| **Positive margin** | **55** | income beats machine cost |
| New events this window | 3 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 55 | `████████████████████████████` |
| 0–0.2 | 7 | `████` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 8 | `████` |
| 0.6–0.8 | 7 | `████` |
| 0.8–0.99 | 10 | `█████` |
| ≥0.99 dead | 37 | `███████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 82.5 | 293 | 527 | cpu-small | 4 | 35% |
| 2 | sn107 Minos | 77.8 | 110 | 28,496 | cpu-small | 20 | 90% |
| 3 | sn60 Bitsec.ai | 76.9 | 2,233 | 2,233 = | cpu-small | 2 | 90% |
| 4 | sn98 NeverPlayAlone | 76 | 1,704 | 1,704 = | cpu-small | 1 | 100% |
| 5 | sn114 SOMA | 72.7 | 1,651 | 4,307 | rtx4090* | 3 | 65% |
| 6 | sn67 Harnyx | 72.3 | 22.68 | 971 | cpu-small | 155 | 22% |
| 7 | sn91 cascade | 70.1 | 775 | 3,127 | rtx4090* | 5 | 52% |
| 8 | sn62 Ridges | 69.5 | 632 | 2,597 | rtx4090* | 7 | 35% |
| 9 | sn102 ConnitoAI | 69 | 550 | 1,792 | rtx4090* | 7 | 28% |
| 10 | sn26 Perturb | 68.8 | 24.94 | 202 | rtx3060 | 11 | 50% |
| 11 | sn41 Almanac | 68.4 | 8.99 | 66.42 | cpu-small | 60 | 78% |
| 12 | sn96 Verathos | 67 | 15.69 | 80.42 | rtx4090 | 126 | 41% |
| 13 | sn15 ORO | 66.9 | 8.56 | 19.17 | cpu-small | 76 | 93% |
| 14 | sn74 Gittensor | 66.3 | 246 | 256 | rtx4090* | 9 | 18% |
| 15 | sn124 Swarm | 65.8 | 220 | 631 | rtx4090* | 23 | 10% |
| 16 | sn38 ChronoLLM | 65.7 | 217 | 3,645 | rtx4090* | 10 | 52% |
| 17 | sn21 AdTAO | 65.6 | 4.78 | 22.06 | cpu-small | 142 | 45% |
| 18 | sn80 OpenRoboto | 62.2 | 71.10 | 270 | rtx4090* | 4 | 91% |
| 19 | sn61 RedTeam | 61.9 | 65.21 | 168 | rtx4090* | 40 | 5% |
| 20 | sn101 Tag101 | 59.8 | 0.10 | 0.72 | cpu-small | 243 | 90% |

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
| wide (<30%) | 22 |
| concentrated (30–60%) | 21 |
| dominated (60–90%) | 21 |
| captured (>90%) | 26 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 104 |
| code-submission (validator runs it) | 9 |
| min_compute.yml (curated) | 9 |
| README keywords (GUESS) | 5 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-08-05T18:45 | sn36 | BURN_DROP | sn36 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-08-05T18:45 | sn96 | RELEASE | sn96 released v0.1.26 - Gleipnir Proof Protocol v3 |
| 2026-08-05T18:45 | sn96 | SCORING_COMMIT | sn96 commit touches scoring: fix: serialize validator block dispatch |
| 2026-08-05T16:50 | sn21 | README_TASK_DIFF | sn21 README task/scoring sections changed |
| 2026-08-05T16:50 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: Merge pull request #24 from conjectures-i |
| 2026-08-05T14:53 | sn21 | RELEASE | sn21 released SN21 training bundle |
| 2026-08-05T14:53 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: docs: resolve the first-basket date ambig |
| 2026-08-05T14:53 | sn21 | README_TASK_DIFF | sn21 README task/scoring sections changed |
| 2026-08-05T14:53 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: Merge pull request #23 from conjectures-i |
| 2026-08-05T14:53 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Disclose the serving stack so miners can |
| 2026-08-05T12:15 | sn12 | RELEASE | sn12 released miner-staging-2026-08-05-31002481795-421-1: fix: replace |
| 2026-08-05T12:15 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: feat(verifiability): W1+W3 — miners can n |
| 2026-08-05T12:15 | sn21 | README_TASK_DIFF | sn21 README task/scoring sections changed |
| 2026-08-05T12:15 | sn61 | RELEASE | sn61 released 4.9.0 |
| 2026-08-05T12:15 | sn61 | SCORING_COMMIT | sn61 commit touches scoring: fix: uncomment validation for miner conta |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

