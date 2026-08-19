# Subnet watch — dashboard

_snapshot 2026-08-19T14:48:43Z · block 8879513 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 54 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 92 | `miner_burn` < 0.99 |
| Ranked | 92 | passed every gate |
| **Positive margin** | **54** | income beats machine cost |
| New events this window | 6 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 62 | `████████████████████████████` |
| 0–0.2 | 4 | `██` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 36 | `████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 76.3 | 61.24 | 114 | cpu-small | 13 | 20% |
| 2 | sn121 sundae_bar | 74.4 | 1,059 | 1,059 = | cpu-small | 2 | 60% |
| 3 | sn62 Ridges | 72.4 | 1,531 | 4,054 | rtx4090* | 3 | 60% |
| 4 | sn26 Perturb | 72.3 | 58.99 | 1,598 | rtx3060 | 10 | 70% |
| 5 | sn67 Harnyx | 72.1 | 21.77 | 292 | cpu-small | 147 | 9% |
| 6 | sn23 Trishool | 71.9 | 501 | 501 = | cpu-small | 2 | 80% |
| 7 | sn56 Gradients | 69.4 | 621 | 938 | rtx4090* | 5 | 72% |
| 8 | sn91 cascade | 69.1 | 564 | 2,281 | rtx4090* | 5 | 52% |
| 9 | sn15 ORO | 68.7 | 15.30 | 15,022 | cpu-small | 82 | 92% |
| 10 | sn38 ChronoLLM | 67.4 | 142 | 3,021 | cpu-small | 10 | 52% |
| 11 | sn11 TrajectoryRL | 67 | 4,108 | 4,108 = | cpu-small | 1 | 100% |
| 12 | sn96 Verathos | 66.5 | 14.18 | 335 | rtx4090 | 84 | 41% |
| 13 | sn41 Almanac | 65.9 | 5.10 | 34.81 | cpu-small | 75 | 82% |
| 14 | sn21 AdTAO | 65.1 | 4.32 | 679 | cpu-small | 16 | 35% |
| 15 | sn85 Vidaio | 63.9 | 119 | 182 | rtx4090* | 13 | 42% |
| 16 | sn107 Minos | 63.9 | 114 | 33,679 | cpu-small | 20 | 90% |
| 17 | sn81 Reliquary | 61.4 | 55.93 | 212 | rtx4090* | 50 | 6% |
| 18 | sn55 NIOME | 61.3 | 55.27 | 461 | rtx4090* | 11 | 29% |
| 19 | sn51 lium.io | 60 | 43.85 | 1,049 | rtx4090* | 55 | 79% |
| 20 | sn53 engy | 59.8 | 34.07 | 11,899 | rtx4090 | 144 | 63% |

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
| concentrated (30–60%) | 18 |
| dominated (60–90%) | 18 |
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
| 2026-08-19T10:54 | sn44 | SCORING_COMMIT | sn44 commit touches scoring: Merge pull request #53 from score-technol |
| 2026-08-19T10:54 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-2703: withhold unrented incentive whe |
| 2026-08-19T10:13 | sn14 | SCORING_COMMIT | sn14 commit touches scoring: Burn a departed claimant's share to the v |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

