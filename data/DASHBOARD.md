# Subnet watch — dashboard

_snapshot 2026-08-19T16:55:35Z · block 8880148 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 57 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 92 | `miner_burn` < 0.99 |
| Ranked | 92 | passed every gate |
| **Positive margin** | **57** | income beats machine cost |
| New events this window | 3 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 62 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 36 | `████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 76.5 | 64.47 | 115 | cpu-small | 13 | 20% |
| 2 | sn121 sundae_bar | 74.5 | 1,086 | 1,086 = | cpu-small | 2 | 60% |
| 3 | sn62 Ridges | 72.5 | 1,567 | 4,149 | rtx4090* | 3 | 59% |
| 4 | sn67 Harnyx | 72.3 | 22.29 | 298 | cpu-small | 147 | 9% |
| 5 | sn23 Trishool | 71.9 | 511 | 511 = | cpu-small | 2 | 80% |
| 6 | sn26 Perturb | 71.7 | 50.80 | 1,639 | rtx3060 | 10 | 70% |
| 7 | sn15 ORO | 69.8 | 15.94 | 15,473 | cpu-small | 83 | 92% |
| 8 | sn56 Gradients | 69.5 | 637 | 962 | rtx4090* | 5 | 72% |
| 9 | sn91 cascade | 69.1 | 576 | 2,327 | rtx4090* | 5 | 52% |
| 10 | sn38 ChronoLLM | 67.5 | 145 | 3,083 | cpu-small | 10 | 52% |
| 11 | sn11 TrajectoryRL | 67.1 | 4,229 | 4,229 = | cpu-small | 1 | 100% |
| 12 | sn96 Verathos | 66.6 | 14.38 | 346 | rtx4090 | 89 | 41% |
| 13 | sn41 Almanac | 66 | 5.26 | 35.73 | cpu-small | 74 | 82% |
| 14 | sn107 Minos | 64.4 | 121 | 35,790 | cpu-small | 20 | 90% |
| 15 | sn21 AdTAO | 64.3 | 3.68 | 744 | cpu-small | 16 | 37% |
| 16 | sn85 Vidaio | 64.2 | 130 | 187 | rtx4090* | 13 | 42% |
| 17 | sn28 gm | 62.5 | 80.31 | 1,029 | rtx4090* | 48 | 15% |
| 18 | sn55 NIOME | 61.4 | 56.68 | 478 | rtx4090* | 11 | 29% |
| 19 | sn51 lium.io | 61.3 | 62.26 | 967 | rtx4090* | 51 | 80% |
| 20 | sn81 Reliquary | 61.2 | 53.02 | 205 | rtx4090* | 52 | 5% |

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
| wide (<30%) | 26 |
| concentrated (30–60%) | 17 |
| dominated (60–90%) | 19 |
| captured (>90%) | 29 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 101 |
| code-submission (validator runs it) | 10 |
| min_compute.yml (curated) | 10 |
| README keywords (GUESS) | 6 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-08-19T16:56 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Retry pinned validator yum installs safel |
| 2026-08-19T16:12 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: feat(scoring): bound eligible claims and |
| 2026-08-19T15:42 | sn108 | SCORING_COMMIT | sn108 commit touches scoring: feat(miner): refuse an architecture the  |
| 2026-08-19T14:49 | sn108 | SCORING_COMMIT | sn108 commit touches scoring: docs(miner): say which architectures the |
| 2026-08-19T13:56 | sn14 | RELEASE | sn14 released v2.1.0 |
| 2026-08-19T13:56 | sn28 | RELEASE | sn28 released v0.4.8 |
| 2026-08-19T13:56 | sn28 | SCORING_COMMIT | sn28 commit touches scoring: Release gm-miner v0.4.8 |
| 2026-08-19T13:56 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: Merge pull request #184 from reliquadotai |
| 2026-08-19T13:56 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: Cut the validator guide to specs and step |
| 2026-08-19T11:36 | sn23 | BURN_DROP | sn23 burn fell 1.000 -> 0.847 - miners can earn again |
| 2026-08-19T11:36 | sn51 | RELEASE | sn51 released executor-v1.122 |
| 2026-08-19T11:36 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Preserve validator app modes in restart r |
| 2026-08-19T11:36 | sn108 | SCORING_COMMIT | sn108 commit touches scoring: feat(scoring): burn 40%, pay 40% for dat |
| 2026-08-19T10:54 | sn28 | RELEASE | sn28 released v0.4.8-dev |
| 2026-08-19T10:54 | sn28 | SCORING_COMMIT | sn28 commit touches scoring: Expand verified NEAR model coverage |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

