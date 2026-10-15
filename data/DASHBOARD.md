# Subnet watch — dashboard

_snapshot 2026-10-15T19:27:10Z · block 9290818 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 65 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 104 | `miner_burn` < 0.99 |
| Ranked | 104 | passed every gate |
| **Positive margin** | **65** | income beats machine cost |
| New events this window | 14 | see ALARMS.md |

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
| 1 | sn107 Minos | 81.9 | 280 | 23,740 | cpu-small | 20 | 80% |
| 2 | sn3 Teutonic | 74.7 | 3,017 | 8,058 | rtx4090* | 5 | 40% |
| 3 | sn102 ConnitoAI | 71.4 | 1,123 | 1,123 = | rtx4090* | 4 | 25% |
| 4 | sn41 Almanac | 71.2 | 18.35 | 145 | cpu-small | 119 | 3% |
| 5 | sn101 Tag101 | 69.8 | 12.12 | 12.89 | cpu-small | 241 | 0% |
| 6 | sn53 engy | 69.4 | 622 | 2,586 | rtx4090 | 24 | 16% |
| 7 | sn91 cascade | 69.3 | 234 | 938 | cpu-small | 5 | 52% |
| 8 | sn14 Cacheon | 68.2 | 430 | 5,476 | rtx4090* | 6 | 76% |
| 9 | sn67 Harnyx | 68.2 | 7.43 | 972 | cpu-small | 127 | 36% |
| 10 | sn58 Attune | 68 | 419 | 675 | rtx4090* | 5 | 71% |
| 11 | sn79 MVTRX | 67.5 | 7.58 | 31.91 | cpu-small | 247 | 1% |
| 12 | sn4 Targon | 66.9 | 10,111 | 29,811 | rtx4090* | 5 | 70% |
| 13 | sn7 Allways | 66.5 | 265 | 373 | rtx4090* | 7 | 20% |
| 14 | sn15 ORO | 66.3 | 7.53 | 15.51 | cpu-small | 61 | 97% |
| 15 | sn26 Perturb | 64.8 | 306 | 1,156 | rtx3060 | 4 | 59% |
| 16 | sn92 REAX | 64.6 | 156 | 273 | rtx4090 | 159 | 1% |
| 17 | sn28 SayGM | 64.4 | 142 | 2,881 | rtx4090* | 78 | 26% |
| 18 | sn62 Ridges | 64 | 123 | 1,242 | rtx4090* | 37 | 17% |
| 19 | sn66 conjectures | 63.9 | 120 | 247 | rtx4090* | 4 | 80% |
| 20 | sn120 Affine | 62.2 | 82.44 | 585 | rtx4090* | 270 | 2% |

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
| concentrated (30–60%) | 21 |
| dominated (60–90%) | 29 |
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
| 2026-10-15T19:27 | sn7 | RELEASE | sn7 released release-20261015-164605: Gate quotes and crown reconcile  |
| 2026-10-15T19:27 | sn9 | RELEASE | sn9 released v4.13.7 |
| 2026-10-15T19:27 | sn15 | RELEASE | sn15 released v2.5.3 |
| 2026-10-15T19:27 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Merge test/validator-crash-loop-root-caus |
| 2026-10-15T19:27 | sn28 | RELEASE | sn28 released v0.5.1-dev |
| 2026-10-15T19:27 | sn51 | RELEASE | sn51 released executor-v1.141 |
| 2026-10-15T19:27 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-4465 validator: fail an unrented node |
| 2026-10-15T19:27 | sn76 | BURN_DROP | sn76 burn fell 1.000 -> 0.979 - miners can earn again |
| 2026-10-15T19:27 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Reuse verified host and OCI identities du |
| 2026-10-15T19:27 | sn92 | RELEASE | sn92 released v1.2.0-rc3 |
| 2026-10-15T19:27 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: tiers: keep the per-miner tier-order rule |
| 2026-10-15T19:27 | sn116 | RELEASE | sn116 released Carbon worker images v4 |
| 2026-10-15T19:27 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Merge pull request #1383 from carbonphys |
| 2026-10-15T19:27 | sn122 | BURN_DROP | sn122 burn fell 1.000 -> 0.727 - miners can earn again |
| 2026-10-15T15:41 | sn3 | SCORING_COMMIT | sn3 commit touches scoring: Optimize evaluator dataset downloads with  |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

