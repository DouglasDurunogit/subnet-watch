# Subnet watch — dashboard

_snapshot 2026-08-19T11:35:43Z · block 8878548 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 51 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 91 | `miner_burn` < 0.99 |
| Ranked | 91 | passed every gate |
| **Positive margin** | **51** | income beats machine cost |
| New events this window | 8 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 62 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 6 | `███` |
| 0.8–0.99 | 8 | `████` |
| ≥0.99 dead | 37 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 77.6 | 85.19 | 161 | cpu-small | 10 | 24% |
| 2 | sn107 Minos | 73.3 | 1,011 | 7,770 | cpu-small | 19 | 21% |
| 3 | sn67 Harnyx | 72.1 | 21.59 | 289 | cpu-small | 147 | 9% |
| 4 | sn23 Trishool | 71 | 387 | 387 = | cpu-small | 2 | 85% |
| 5 | sn26 Perturb | 70.7 | 39.60 | 1,586 | rtx3060 | 10 | 70% |
| 6 | sn1 Apex | 70 | 747 | 1,015 | rtx4090* | 4 | 56% |
| 7 | sn15 ORO | 69.5 | 15.08 | 14,950 | cpu-small | 81 | 92% |
| 8 | sn56 Gradients | 69.4 | 617 | 930 | rtx4090* | 5 | 72% |
| 9 | sn91 cascade | 69.2 | 591 | 2,387 | rtx4090* | 5 | 52% |
| 10 | sn38 ChronoLLM | 67.4 | 142 | 3,016 | cpu-small | 10 | 52% |
| 11 | sn11 TrajectoryRL | 67 | 4,079 | 4,079 = | cpu-small | 1 | 100% |
| 12 | sn41 Almanac | 65.8 | 5.05 | 27.40 | cpu-small | 76 | 82% |
| 13 | sn96 Verathos | 65.7 | 11.64 | 292 | rtx4090 | 93 | 41% |
| 14 | sn21 AdTAO | 64.1 | 3.50 | 720 | cpu-small | 16 | 37% |
| 15 | sn85 Vidaio | 63.8 | 118 | 183 | rtx4090* | 13 | 42% |
| 16 | sn81 Reliquary | 62 | 68.44 | 243 | rtx4090* | 49 | 6% |
| 17 | sn55 NIOME | 61.4 | 55.76 | 472 | rtx4090* | 11 | 29% |
| 18 | sn28 gm | 60.7 | 47.11 | 2,339 | rtx4090* | 44 | 24% |
| 19 | sn102 ConnitoAI | 60.1 | 1,326 | 1,327 | rtx4090* | 4 | 25% |
| 20 | sn53 engy | 60 | 37.06 | 10,901 | rtx4090 | 144 | 58% |

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
| wide (<30%) | 28 |
| concentrated (30–60%) | 17 |
| dominated (60–90%) | 16 |
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
| 2026-08-19T11:36 | sn23 | BURN_DROP | sn23 burn fell 1.000 -> 0.847 - miners can earn again |
| 2026-08-19T11:36 | sn51 | RELEASE | sn51 released executor-v1.122 |
| 2026-08-19T11:36 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Preserve validator app modes in restart r |
| 2026-08-19T11:36 | sn108 | SCORING_COMMIT | sn108 commit touches scoring: feat(scoring): burn 40%, pay 40% for dat |
| 2026-08-19T10:54 | sn28 | RELEASE | sn28 released v0.4.8-dev |
| 2026-08-19T10:54 | sn28 | SCORING_COMMIT | sn28 commit touches scoring: Expand verified NEAR model coverage |
| 2026-08-19T10:54 | sn44 | SCORING_COMMIT | sn44 commit touches scoring: Merge pull request #53 from score-technol |
| 2026-08-19T10:54 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-2703: withhold unrented incentive whe |
| 2026-08-19T10:13 | sn14 | SCORING_COMMIT | sn14 commit touches scoring: Burn a departed claimant's share to the v |
| 2026-08-19T09:46 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: Report an abstained row when a track has  |
| 2026-08-19T08:52 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Use verified local rehearsal base |
| 2026-08-19T08:52 | sn97 | SCORING_COMMIT | sn97 commit touches scoring: feat: score looped trajectories 0 without |
| 2026-08-19T08:02 | sn62 | BURN_DROP | sn62 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-08-19T08:02 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: Declare pynacl for token verification |
| 2026-08-19T07:15 | sn100 | RELEASE | sn100 released v3.3.25: fix(prism): stop control-plane OOM restarts |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

