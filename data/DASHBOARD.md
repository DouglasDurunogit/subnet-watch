# Subnet watch — dashboard

_snapshot 2026-10-15T22:38:45Z · block 9291775 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 64 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 104 | `miner_burn` < 0.99 |
| Ranked | 104 | passed every gate |
| **Positive margin** | **64** | income beats machine cost |
| New events this window | 9 | see ALARMS.md |

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
| 0.6–0.8 | 12 | `█████` |
| 0.8–0.99 | 10 | `████` |
| ≥0.99 dead | 24 | `██████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 81.8 | 274 | 23,745 | cpu-small | 20 | 80% |
| 2 | sn3 Teutonic | 74.7 | 3,013 | 8,049 | rtx4090* | 5 | 40% |
| 3 | sn41 Almanac | 71.2 | 18.30 | 144 | cpu-small | 107 | 6% |
| 4 | sn101 Tag101 | 69.8 | 11.89 | 12.93 | cpu-small | 244 | 0% |
| 5 | sn53 engy | 69.5 | 637 | 2,647 | rtx4090 | 24 | 16% |
| 6 | sn91 cascade | 69.3 | 233 | 936 | cpu-small | 5 | 52% |
| 7 | sn102 ConnitoAI | 68.5 | 475 | 1,338 | rtx4090* | 7 | 30% |
| 8 | sn58 Attune | 68.1 | 424 | 683 | rtx4090* | 5 | 71% |
| 9 | sn14 Cacheon | 68.1 | 417 | 674 | rtx4090* | 6 | 76% |
| 10 | sn67 Harnyx | 68.1 | 7.38 | 967 | cpu-small | 127 | 36% |
| 11 | sn79 MVTRX | 67.6 | 7.66 | 30.99 | cpu-small | 247 | 1% |
| 12 | sn15 ORO | 67.3 | 7.68 | 15.53 | cpu-small | 62 | 97% |
| 13 | sn4 Targon | 66.9 | 10,044 | 29,615 | rtx4090* | 5 | 70% |
| 14 | sn7 Allways | 65.3 | 190 | 401 | rtx4090* | 7 | 22% |
| 15 | sn26 Perturb | 64.8 | 303 | 1,153 | rtx3060 | 4 | 59% |
| 16 | sn28 SayGM | 64.3 | 136 | 3,368 | rtx4090* | 71 | 19% |
| 17 | sn66 conjectures | 63.9 | 119 | 247 | rtx4090* | 4 | 80% |
| 18 | sn92 REAX | 63.7 | 125 | 248 | rtx4090 | 236 | 1% |
| 19 | sn62 Ridges | 63.7 | 114 | 1,239 | rtx4090* | 37 | 17% |
| 20 | sn120 Affine | 62.2 | 82.31 | 584 | rtx4090* | 270 | 2% |

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
| wide (<30%) | 27 |
| concentrated (30–60%) | 20 |
| dominated (60–90%) | 30 |
| captured (>90%) | 26 |

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
| 2026-10-15T22:39 | sn7 | RELEASE | sn7 released release-20261015-220818: Quote the min for alpha pairs fr |
| 2026-10-15T22:39 | sn7 | SCORING_COMMIT | sn7 commit touches scoring: Quote /rate from held miner states and a l |
| 2026-10-15T22:39 | sn25 | RELEASE | sn25 released v2026.10.15-1072937160 |
| 2026-10-15T22:39 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Fix Arena progression lock order and clos |
| 2026-10-15T22:39 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Overlap retained history loading with bou |
| 2026-10-15T22:39 | sn92 | RELEASE | sn92 released v1.2.0-rc4 |
| 2026-10-15T22:39 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: probe: open each UID's window at the vali |
| 2026-10-15T22:39 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Verify persisted contract record through |
| 2026-10-15T22:39 | sn117 | RELEASE | sn117 released everycli v0.5.7 |
| 2026-10-15T19:27 | sn7 | RELEASE | sn7 released release-20261015-164605: Gate quotes and crown reconcile  |
| 2026-10-15T19:27 | sn9 | RELEASE | sn9 released v4.13.7 |
| 2026-10-15T19:27 | sn15 | RELEASE | sn15 released v2.5.3 |
| 2026-10-15T19:27 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Merge test/validator-crash-loop-root-caus |
| 2026-10-15T19:27 | sn28 | RELEASE | sn28 released v0.5.1-dev |
| 2026-10-15T19:27 | sn51 | RELEASE | sn51 released executor-v1.141 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

