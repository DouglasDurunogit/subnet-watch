# Subnet watch — dashboard

_snapshot 2026-08-10T20:25:39Z · block 8816407 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 56 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 90 | `miner_burn` < 0.99 |
| Ranked | 90 | passed every gate |
| **Positive margin** | **56** | income beats machine cost |
| New events this window | 4 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 55 | `████████████████████████████` |
| 0–0.2 | 4 | `██` |
| 0.2–0.4 | 5 | `███` |
| 0.4–0.6 | 9 | `█████` |
| 0.6–0.8 | 10 | `█████` |
| 0.8–0.99 | 7 | `████` |
| ≥0.99 dead | 38 | `███████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 78.1 | 114 | 32,837 | cpu-small | 20 | 90% |
| 2 | sn76 Phylax | 76.8 | 68.88 | 208 | cpu-small | 10 | 33% |
| 3 | sn67 Harnyx | 71.3 | 17.15 | 744 | cpu-small | 129 | 19% |
| 4 | sn96 Verathos | 70.6 | 38.28 | 400 | rtx4090 | 46 | 42% |
| 5 | sn91 cascade | 70.5 | 868 | 2,694 | rtx4090* | 5 | 49% |
| 6 | sn41 Almanac | 69.2 | 11.05 | 34.49 | cpu-small | 69 | 70% |
| 7 | sn62 Ridges | 69 | 543 | 1,964 | rtx4090* | 7 | 35% |
| 8 | sn26 Perturb | 68 | 20.46 | 177 | rtx3060 | 11 | 50% |
| 9 | sn15 ORO | 67.7 | 9.97 | 20.34 | cpu-small | 80 | 93% |
| 10 | sn28 gm | 67.3 | 331 | 1,316 | rtx4090* | 27 | 15% |
| 11 | sn21 AdTAO | 66.2 | 5.51 | 25.96 | cpu-small | 118 | 45% |
| 12 | sn38 ChronoLLM | 65.7 | 216 | 3,634 | rtx4090* | 10 | 52% |
| 13 | sn124 Swarm | 65.7 | 216 | 661 | rtx4090* | 23 | 11% |
| 14 | sn80 OpenRoboto | 64.8 | 156 | 566 | rtx4090* | 4 | 91% |
| 15 | sn100 BASE | 64.8 | 155 | 337 | rtx4090* | 7 | 44% |
| 16 | sn61 RedTeam | 62.8 | 84.84 | 344 | rtx4090* | 47 | 6% |
| 17 | sn2 DSperse | 60.7 | 45.12 | 210 | rtx4090* | 6 | 83% |
| 18 | sn51 lium.io | 58.7 | 32.58 | 2,342 | rtx4090* | 48 | 68% |
| 19 | sn6 Numinous | 58.1 | 23.74 | 465 | cpu-small | 18 | 26% |
| 20 | sn85 Vidaio | 55.8 | 375 | 573 | rtx4090* | 10 | 19% |

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
| concentrated (30–60%) | 22 |
| dominated (60–90%) | 20 |
| captured (>90%) | 25 |

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
| 2026-08-10T20:26 | sn2 | RELEASE | sn2 released 14.13.3 |
| 2026-08-10T20:26 | sn100 | RELEASE | sn100 released v3.3.16 — design emit cold-start + permanent seal-sync  |
| 2026-08-10T19:31 | sn97 | SCORING_COMMIT | sn97 commit touches scoring: feat: add discarded questions to scoring  |
| 2026-08-10T19:31 | sn100 | RELEASE | sn100 released v3.3.15 — seal epoch sync + Prism submitter WTA |
| 2026-08-10T18:24 | sn103 | BURN_DROP | sn103 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-08-10T17:25 | sn104 | SCORING_COMMIT | sn104 commit touches scoring: fix validator weight-setting reliability |
| 2026-08-10T16:22 | sn2 | RELEASE | sn2 released 14.13.2 |
| 2026-08-10T16:22 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Reason v3: single-term scoring fork (wei |
| 2026-08-10T15:13 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: Merge pull request #36 from conjectures-i |
| 2026-08-10T15:13 | sn107 | README_TASK_DIFF | sn107 README task/scoring sections changed |
| 2026-08-10T13:54 | sn51 | RELEASE | sn51 released executor-v1.116 |
| 2026-08-10T13:54 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: Merge pull request #35 from conjectures-i |
| 2026-08-10T13:54 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-08-10T13:54 | sn75 | SCORING_COMMIT | sn75 commit touches scoring: Merge pull request #36 from thenervelab/f |
| 2026-08-10T13:54 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Raise duel max_model_len to 65k and stop |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

