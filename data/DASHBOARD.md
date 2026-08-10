# Subnet watch — dashboard

_snapshot 2026-08-10T15:12:52Z · block 8814843 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 56 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 89 | `miner_burn` < 0.99 |
| Ranked | 89 | passed every gate |
| **Positive margin** | **56** | income beats machine cost |
| New events this window | 2 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 54 | `████████████████████████████` |
| 0–0.2 | 5 | `███` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 8 | `████` |
| 0.6–0.8 | 9 | `█████` |
| 0.8–0.99 | 7 | `████` |
| ≥0.99 dead | 39 | `████████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 78 | 109 | 32,746 | cpu-small | 20 | 90% |
| 2 | sn76 Phylax | 76.8 | 69.15 | 208 | cpu-small | 10 | 33% |
| 3 | sn21 AdTAO | 76.4 | 64.37 | 261 | cpu-small | 16 | 30% |
| 4 | sn67 Harnyx | 71.2 | 17.42 | 755 | cpu-small | 129 | 19% |
| 5 | sn91 cascade | 70.1 | 764 | 2,617 | rtx4090* | 5 | 50% |
| 6 | sn96 Verathos | 69.4 | 28.47 | 304 | rtx4090 | 57 | 42% |
| 7 | sn41 Almanac | 69.2 | 11.07 | 34.68 | cpu-small | 69 | 70% |
| 8 | sn62 Ridges | 69 | 546 | 1,976 | rtx4090* | 7 | 35% |
| 9 | sn26 Perturb | 68.2 | 21.16 | 859 | rtx3060 | 11 | 51% |
| 10 | sn11 TrajectoryRL | 67.4 | 4,556 | 4,556 = | cpu-small | 1 | 100% |
| 11 | sn15 ORO | 66.5 | 9.71 | 19.83 | cpu-small | 80 | 93% |
| 12 | sn28 gm | 66.4 | 254 | 4,166 | rtx4090* | 25 | 42% |
| 13 | sn124 Swarm | 65.8 | 220 | 673 | rtx4090* | 23 | 11% |
| 14 | sn38 ChronoLLM | 65.7 | 215 | 3,609 | rtx4090* | 10 | 52% |
| 15 | sn80 OpenRoboto | 64.4 | 138 | 505 | rtx4090* | 4 | 91% |
| 16 | sn100 BASE | 63.3 | 101 | 318 | rtx4090* | 8 | 50% |
| 17 | sn61 RedTeam | 63.3 | 99.18 | 412 | rtx4090* | 45 | 8% |
| 18 | sn51 lium.io | 58.1 | 28.07 | 2,967 | rtx4090* | 50 | 58% |
| 19 | sn6 Numinous | 58 | 23.13 | 454 | cpu-small | 18 | 26% |
| 20 | sn85 Vidaio | 55.6 | 349 | 605 | rtx4090* | 10 | 19% |

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
| captured (>90%) | 23 |

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
| 2026-08-10T08:13 | sn96 | SCORING_COMMIT | sn96 commit touches scoring: fix: resume deferred miner updates at idl |
| 2026-08-10T06:20 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: miner: `cascade duel` — full settled-roun |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

