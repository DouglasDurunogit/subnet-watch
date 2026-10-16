# Subnet watch — dashboard

_snapshot 2026-10-16T10:10:18Z · block 9295233 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 61 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 101 | `miner_burn` < 0.99 |
| Ranked | 101 | passed every gate |
| **Positive margin** | **61** | income beats machine cost |
| New events this window | 6 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 67 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 6 | `███` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 9 | `████` |
| ≥0.99 dead | 27 | `███████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn3 Teutonic | 74.8 | 3,100 | 3,100 = | rtx4090* | 5 | 40% |
| 2 | sn41 Almanac | 74.2 | 37.94 | 119 | cpu-small | 108 | 15% |
| 3 | sn53 engy | 69.7 | 668 | 2,775 | rtx4090 | 24 | 16% |
| 4 | sn91 cascade | 69.3 | 234 | 940 | cpu-small | 5 | 52% |
| 5 | sn67 Harnyx | 68.8 | 9.16 | 9.16 = | cpu-small | 230 | 13% |
| 6 | sn58 Attune | 68.2 | 440 | 708 | rtx4090* | 5 | 71% |
| 7 | sn107 Minos | 68 | 286 | 24,296 | cpu-small | 20 | 80% |
| 8 | sn79 MVTRX | 67.9 | 8.02 | 33.01 | cpu-small | 249 | 1% |
| 9 | sn15 ORO | 67.6 | 8.94 | 17,682 | cpu-small | 66 | 97% |
| 10 | sn4 Targon | 67 | 10,412 | 30,697 | rtx4090* | 5 | 70% |
| 11 | sn7 Allways | 66 | 229 | 504 | rtx4090* | 7 | 27% |
| 12 | sn14 Cacheon | 65.4 | 187 | 3,850 | rtx4090* | 9 | 52% |
| 13 | sn62 Ridges | 64.1 | 126 | 1,275 | rtx4090* | 38 | 17% |
| 14 | sn66 conjectures | 64 | 124 | 256 | rtx4090* | 4 | 80% |
| 15 | sn92 REAX | 63.3 | 119 | 159 | rtx4090 | 229 | 1% |
| 16 | sn28 SayGM | 62.5 | 81.81 | 3,179 | rtx4090* | 94 | 20% |
| 17 | sn120 Affine | 62.1 | 85.23 | 603 | rtx4090* | 270 | 2% |
| 18 | sn61 RedTeam | 61.9 | 69.10 | 92.53 | rtx4090* | 125 | 1% |
| 19 | sn111 Claims | 59.7 | 35.21 | 3,098 | rtx4090* | 6 | 90% |
| 20 | sn81 Reliquary | 58.9 | 26.54 | 224 | rtx4090* | 14 | 83% |

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
| concentrated (30–60%) | 21 |
| dominated (60–90%) | 27 |
| captured (>90%) | 24 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 95 |
| README keywords (GUESS) | 13 |
| min_compute.yml (curated) | 10 |
| code-submission (validator runs it) | 9 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-10-16T10:10 | sn37 | BURN_DROP | sn37 burn fell 1.000 -> 0.713 - miners can earn again |
| 2026-10-16T10:10 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-4362 - [P3] Validator: remove setting |
| 2026-10-16T10:10 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge pull request #489 from leadpoet/fix |
| 2026-10-16T10:10 | sn76 | BURN_DROP | sn76 burn fell 0.999 -> 0.961 - miners can earn again |
| 2026-10-16T10:10 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Add read-only retained miner revision pre |
| 2026-10-16T10:10 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Merge pull request #1404 from carbonphys |
| 2026-10-16T05:47 | sn25 | RELEASE | sn25 released v2026.10.15-1073121200 |
| 2026-10-16T05:47 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-3980 - Validator: new loopback volume |
| 2026-10-16T05:47 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Verify failed fallback stays an infrastru |
| 2026-10-16T05:47 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Reuse verified semantics for authenticate |
| 2026-10-16T05:47 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: fix(corpus): serve signed jobs from the s |
| 2026-10-16T05:47 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: Pin the best-bench round in the receipt i |
| 2026-10-16T05:47 | sn94 | SCORING_COMMIT | sn94 commit touches scoring: Merge pull request #281 from cathedralai/ |
| 2026-10-16T05:47 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Merge pull request #1401 from carbonphys |
| 2026-10-16T00:49 | sn25 | RELEASE | sn25 released v2026.10.15-1073082520 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

