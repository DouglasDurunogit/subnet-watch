# Subnet watch — dashboard

_snapshot 2026-10-16T05:47:18Z · block 9293918 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 59 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 99 | `miner_burn` < 0.99 |
| Ranked | 99 | passed every gate |
| **Positive margin** | **59** | income beats machine cost |
| New events this window | 8 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 68 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 8 | `███` |
| ≥0.99 dead | 29 | `████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 82 | 287 | 24,357 | cpu-small | 20 | 80% |
| 2 | sn3 Teutonic | 74.8 | 3,075 | 8,213 | rtx4090* | 5 | 40% |
| 3 | sn41 Almanac | 74.4 | 39.95 | 126 | cpu-small | 106 | 14% |
| 4 | sn101 Tag101 | 69.8 | 11.97 | 13.27 | cpu-small | 244 | 0% |
| 5 | sn53 engy | 69.6 | 658 | 2,731 | rtx4090 | 24 | 16% |
| 6 | sn91 cascade | 69.3 | 235 | 942 | cpu-small | 5 | 52% |
| 7 | sn67 Harnyx | 68.8 | 9.03 | 9.98 | cpu-small | 232 | 13% |
| 8 | sn58 Attune | 68.2 | 439 | 707 | rtx4090* | 5 | 71% |
| 9 | sn15 ORO | 67.8 | 9.28 | 17,532 | cpu-small | 65 | 97% |
| 10 | sn79 MVTRX | 67.2 | 7.48 | 31.30 | cpu-small | 242 | 1% |
| 11 | sn4 Targon | 66.9 | 10,252 | 30,225 | rtx4090* | 5 | 70% |
| 12 | sn7 Allways | 65.8 | 219 | 420 | rtx4090* | 7 | 23% |
| 13 | sn14 Cacheon | 65.2 | 175 | 3,255 | rtx4090* | 9 | 44% |
| 14 | sn62 Ridges | 64.1 | 126 | 1,268 | rtx4090* | 38 | 18% |
| 15 | sn66 conjectures | 64 | 122 | 252 | rtx4090* | 4 | 80% |
| 16 | sn92 REAX | 63.6 | 121 | 183 | rtx4090 | 232 | 1% |
| 17 | sn28 SayGM | 62.8 | 89.01 | 3,489 | rtx4090* | 78 | 24% |
| 18 | sn120 Affine | 62.3 | 84.32 | 597 | rtx4090* | 270 | 2% |
| 19 | sn61 RedTeam | 62 | 68.53 | 91.66 | rtx4090* | 125 | 1% |
| 20 | sn111 Claims | 59.7 | 34.27 | 3,080 | rtx4090* | 6 | 90% |

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
| concentrated (30–60%) | 19 |
| dominated (60–90%) | 28 |
| captured (>90%) | 23 |

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
| 2026-10-16T05:47 | sn25 | RELEASE | sn25 released v2026.10.15-1073121200 |
| 2026-10-16T05:47 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-3980 - Validator: new loopback volume |
| 2026-10-16T05:47 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Verify failed fallback stays an infrastru |
| 2026-10-16T05:47 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Reuse verified semantics for authenticate |
| 2026-10-16T05:47 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: fix(corpus): serve signed jobs from the s |
| 2026-10-16T05:47 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: Pin the best-bench round in the receipt i |
| 2026-10-16T05:47 | sn94 | SCORING_COMMIT | sn94 commit touches scoring: Merge pull request #281 from cathedralai/ |
| 2026-10-16T05:47 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Merge pull request #1401 from carbonphys |
| 2026-10-16T00:49 | sn25 | RELEASE | sn25 released v2026.10.15-1073082520 |
| 2026-10-16T00:49 | sn37 | SCORING_COMMIT | sn37 commit touches scoring: fix(miner): support reviewed mainnet runt |
| 2026-10-16T00:49 | sn37 | README_TASK_DIFF | sn37 README task/scoring sections changed |
| 2026-10-16T00:49 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Merge pull request #1393 from carbonphys |
| 2026-10-15T22:39 | sn7 | RELEASE | sn7 released release-20261015-220818: Quote the min for alpha pairs fr |
| 2026-10-15T22:39 | sn7 | SCORING_COMMIT | sn7 commit touches scoring: Quote /rate from held miner states and a l |
| 2026-10-15T22:39 | sn25 | RELEASE | sn25 released v2026.10.15-1072937160 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

