# Subnet watch — dashboard

_snapshot 2026-08-19T21:10:40Z · block 8881423 · run_status **ok**_

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
| New events this window | 8 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 61 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 8 | `████` |
| ≥0.99 dead | 36 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 76.7 | 67.44 | 120 | cpu-small | 13 | 20% |
| 2 | sn121 sundae_bar | 74.6 | 1,128 | 1,128 = | cpu-small | 2 | 60% |
| 3 | sn62 Ridges | 72.6 | 1,619 | 4,286 | rtx4090* | 3 | 59% |
| 4 | sn67 Harnyx | 72.4 | 23.22 | 310 | cpu-small | 147 | 9% |
| 5 | sn23 Trishool | 72 | 525 | 525 = | cpu-small | 2 | 80% |
| 6 | sn26 Perturb | 71 | 42.57 | 77.99 | rtx3060 | 10 | 70% |
| 7 | sn15 ORO | 69.8 | 16.52 | 15,845 | cpu-small | 84 | 92% |
| 8 | sn56 Gradients | 69.6 | 660 | 999 | rtx4090* | 5 | 72% |
| 9 | sn91 cascade | 69.2 | 582 | 2,353 | rtx4090* | 5 | 52% |
| 10 | sn38 ChronoLLM | 67.6 | 151 | 3,202 | cpu-small | 10 | 52% |
| 11 | sn96 Verathos | 66.5 | 14.14 | 352 | rtx4090 | 88 | 41% |
| 12 | sn41 Almanac | 66 | 5.31 | 32.55 | cpu-small | 74 | 82% |
| 13 | sn107 Minos | 64.4 | 121 | 36,044 | cpu-small | 20 | 90% |
| 14 | sn85 Vidaio | 64.1 | 127 | 223 | rtx4090* | 13 | 42% |
| 15 | sn81 Reliquary | 61.6 | 59.62 | 201 | rtx4090* | 54 | 5% |
| 16 | sn55 NIOME | 61.5 | 58.94 | 495 | rtx4090* | 11 | 29% |
| 17 | sn51 lium.io | 61.1 | 59.80 | 1,088 | rtx4090* | 51 | 76% |
| 18 | sn53 engy | 59.8 | 34.98 | 12,154 | rtx4090 | 144 | 63% |
| 19 | sn102 ConnitoAI | 59.6 | 1,158 | 1,930 | rtx4090* | 5 | 33% |
| 20 | sn28 gm | 59 | 28.70 | 1,585 | rtx4090* | 50 | 42% |

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
| concentrated (30–60%) | 19 |
| dominated (60–90%) | 19 |
| captured (>90%) | 28 |

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
| 2026-08-19T21:11 | sn10 | SCORING_COMMIT | sn10 commit touches scoring: feat(bench): harness round mode with a si |
| 2026-08-19T21:11 | sn38 | SCORING_COMMIT | sn38 commit touches scoring: Add multi-layer dedup and weighted leak e |
| 2026-08-19T20:41 | sn1 | RELEASE | sn1 released v4.3.5 |
| 2026-08-19T20:41 | sn89 | README_TASK_DIFF | sn89 README task/scoring sections changed |
| 2026-08-19T20:02 | sn25 | RELEASE | sn25 released v2026.8.19-1023689220 |
| 2026-08-19T20:02 | sn51 | RELEASE | sn51 released executor-v1.123 |
| 2026-08-19T20:02 | sn66 | README_TASK_DIFF | sn66 README task/scoring sections changed |
| 2026-08-19T20:02 | sn108 | SCORING_COMMIT | sn108 commit touches scoring: feat!: validators run miners' models; re |
| 2026-08-19T19:35 | sn46 | SCORING_COMMIT | sn46 commit touches scoring: Restore validator log visibility after th |
| 2026-08-19T18:50 | sn10 | README_TASK_DIFF | sn10 README task/scoring sections changed |
| 2026-08-19T18:50 | sn46 | SCORING_COMMIT | sn46 commit touches scoring: Merge pull request #21 from instant-subne |
| 2026-08-19T18:50 | sn90 | README_TASK_DIFF | sn90 README task/scoring sections changed |
| 2026-08-19T18:50 | sn103 | BURN_DROP | sn103 burn fell 1.000 -> 0.845 - miners can earn again |
| 2026-08-19T18:02 | sn1 | RELEASE | sn1 released v4.3.4 |
| 2026-08-19T16:56 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Retry pinned validator yum installs safel |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

