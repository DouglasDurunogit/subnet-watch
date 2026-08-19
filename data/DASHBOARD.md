# Subnet watch — dashboard

_snapshot 2026-08-19T18:50:22Z · block 8880722 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 54 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 91 | `miner_burn` < 0.99 |
| Ranked | 91 | passed every gate |
| **Positive margin** | **54** | income beats machine cost |
| New events this window | 5 | see ALARMS.md |

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
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 37 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 76.6 | 65.07 | 115 | cpu-small | 13 | 20% |
| 2 | sn121 sundae_bar | 74.5 | 1,088 | 1,088 = | cpu-small | 2 | 60% |
| 3 | sn62 Ridges | 72.5 | 1,562 | 4,136 | rtx4090* | 3 | 59% |
| 4 | sn67 Harnyx | 72.3 | 22.48 | 301 | cpu-small | 147 | 9% |
| 5 | sn23 Trishool | 71.9 | 509 | 509 = | cpu-small | 2 | 80% |
| 6 | sn26 Perturb | 70.9 | 41.10 | 1,642 | rtx3060 | 10 | 70% |
| 7 | sn56 Gradients | 69.5 | 637 | 964 | rtx4090* | 5 | 72% |
| 8 | sn15 ORO | 69.4 | 16.00 | 15,376 | cpu-small | 84 | 92% |
| 9 | sn91 cascade | 69.1 | 576 | 2,328 | rtx4090* | 5 | 52% |
| 10 | sn38 ChronoLLM | 67.5 | 146 | 3,088 | cpu-small | 10 | 52% |
| 11 | sn96 Verathos | 66.7 | 14.96 | 347 | rtx4090 | 87 | 41% |
| 12 | sn41 Almanac | 65.9 | 5.14 | 31.37 | cpu-small | 74 | 82% |
| 13 | sn107 Minos | 64.5 | 126 | 35,000 | cpu-small | 20 | 90% |
| 14 | sn21 AdTAO | 64.3 | 3.66 | 746 | cpu-small | 16 | 37% |
| 15 | sn85 Vidaio | 64 | 122 | 253 | rtx4090* | 13 | 42% |
| 16 | sn28 gm | 62 | 69.92 | 1,194 | rtx4090* | 50 | 20% |
| 17 | sn51 lium.io | 61.4 | 63.51 | 988 | rtx4090* | 48 | 80% |
| 18 | sn55 NIOME | 61.4 | 56.90 | 480 | rtx4090* | 11 | 29% |
| 19 | sn81 Reliquary | 60.6 | 44.27 | 214 | rtx4090* | 57 | 6% |
| 20 | sn53 engy | 59.8 | 35.03 | 12,169 | rtx4090 | 144 | 63% |

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
| captured (>90%) | 27 |

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
| 2026-08-19T18:50 | sn10 | README_TASK_DIFF | sn10 README task/scoring sections changed |
| 2026-08-19T18:50 | sn46 | SCORING_COMMIT | sn46 commit touches scoring: Merge pull request #21 from instant-subne |
| 2026-08-19T18:50 | sn90 | README_TASK_DIFF | sn90 README task/scoring sections changed |
| 2026-08-19T18:50 | sn103 | BURN_DROP | sn103 burn fell 1.000 -> 0.845 - miners can earn again |
| 2026-08-19T18:02 | sn1 | RELEASE | sn1 released v4.3.4 |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

