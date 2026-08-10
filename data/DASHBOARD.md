# Subnet watch — dashboard

_snapshot 2026-08-10T16:22:23Z · block 8815191 · run_status **ok**_

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
| 0.2–0.4 | 7 | `████` |
| 0.4–0.6 | 8 | `████` |
| 0.6–0.8 | 9 | `█████` |
| 0.8–0.99 | 7 | `████` |
| ≥0.99 dead | 38 | `███████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 78.2 | 114 | 32,773 | cpu-small | 20 | 90% |
| 2 | sn76 Phylax | 76.8 | 69.14 | 208 | cpu-small | 10 | 33% |
| 3 | sn21 AdTAO | 76.4 | 64.32 | 261 | cpu-small | 16 | 30% |
| 4 | sn67 Harnyx | 71.3 | 17.22 | 747 | cpu-small | 129 | 19% |
| 5 | sn91 cascade | 70.3 | 804 | 2,749 | rtx4090* | 5 | 50% |
| 6 | sn96 Verathos | 69.9 | 32.17 | 459 | rtx4090 | 47 | 42% |
| 7 | sn41 Almanac | 69.2 | 11.04 | 34.64 | cpu-small | 69 | 70% |
| 8 | sn62 Ridges | 69 | 545 | 1,973 | rtx4090* | 7 | 35% |
| 9 | sn26 Perturb | 68.1 | 20.88 | 849 | rtx3060 | 11 | 51% |
| 10 | sn11 TrajectoryRL | 67.4 | 4,536 | 4,536 = | cpu-small | 1 | 100% |
| 11 | sn15 ORO | 67 | 9.72 | 19.85 | cpu-small | 80 | 93% |
| 12 | sn124 Swarm | 65.8 | 217 | 664 | rtx4090* | 23 | 11% |
| 13 | sn38 ChronoLLM | 65.6 | 214 | 3,591 | rtx4090* | 10 | 52% |
| 14 | sn80 OpenRoboto | 64.5 | 144 | 525 | rtx4090* | 4 | 91% |
| 15 | sn28 gm | 64.4 | 141 | 4,309 | rtx4090* | 22 | 42% |
| 16 | sn61 RedTeam | 63.3 | 101 | 425 | rtx4090* | 45 | 8% |
| 17 | sn100 BASE | 63.3 | 100 | 317 | rtx4090* | 8 | 50% |
| 18 | sn51 lium.io | 58.8 | 32.90 | 4,494 | rtx4090* | 50 | 55% |
| 19 | sn6 Numinous | 58.1 | 23.89 | 468 | cpu-small | 18 | 26% |
| 20 | sn85 Vidaio | 56.9 | 519 | 664 | rtx4090* | 10 | 21% |

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
| concentrated (30–60%) | 25 |
| dominated (60–90%) | 18 |
| captured (>90%) | 24 |

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
| 2026-08-10T16:22 | sn2 | RELEASE | sn2 released 14.13.2 |
| 2026-08-10T16:22 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Reason v3: single-term scoring fork (wei |
| 2026-08-10T15:13 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: Merge pull request #36 from conjectures-i |
| 2026-08-10T15:13 | sn107 | README_TASK_DIFF | sn107 README task/scoring sections changed |
| 2026-08-10T13:54 | sn51 | RELEASE | sn51 released executor-v1.116 |
| 2026-08-10T13:54 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: Merge pull request #35 from conjectures-i |
| 2026-08-10T13:54 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-08-10T13:54 | sn75 | SCORING_COMMIT | sn75 commit touches scoring: Merge pull request #36 from thenervelab/f |
| 2026-08-10T13:54 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Raise duel max_model_len to 65k and stop |
| 2026-08-10T13:54 | sn124 | SCORING_COMMIT | sn124 commit touches scoring: Report seed scores under the epoch that  |
| 2026-08-10T12:08 | sn89 | SCORING_COMMIT | sn89 commit touches scoring: hf: import time — hf_scoring_config() rai |
| 2026-08-10T09:57 | sn56 | SCORING_COMMIT | sn56 commit touches scoring: Fix degenerate-dataset filter for DPO bos |
| 2026-08-10T08:13 | sn61 | RELEASE | sn61 released 4.9.4 |
| 2026-08-10T08:13 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Gate daily scoring and autoresearch readi |
| 2026-08-10T08:13 | sn96 | RELEASE | sn96 released Verathos v0.1.34 — Reliable Miner Updates |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

