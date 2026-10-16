# Subnet watch — dashboard

_snapshot 2026-10-16T00:49:00Z · block 9292427 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 61 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 102 | `miner_burn` < 0.99 |
| Ranked | 102 | passed every gate |
| **Positive margin** | **61** | income beats machine cost |
| New events this window | 4 | see ALARMS.md |

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
| 0.6–0.8 | 11 | `█████` |
| 0.8–0.99 | 9 | `████` |
| ≥0.99 dead | 26 | `███████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 81.9 | 280 | 23,786 | cpu-small | 20 | 80% |
| 2 | sn3 Teutonic | 74.7 | 3,036 | 8,111 | rtx4090* | 5 | 40% |
| 3 | sn41 Almanac | 71.3 | 18.60 | 146 | cpu-small | 107 | 6% |
| 4 | sn101 Tag101 | 69.7 | 11.88 | 13.21 | cpu-small | 244 | 0% |
| 5 | sn53 engy | 69.5 | 644 | 2,677 | rtx4090 | 24 | 16% |
| 6 | sn91 cascade | 69.3 | 231 | 927 | cpu-small | 5 | 52% |
| 7 | sn102 ConnitoAI | 68.2 | 434 | 1,266 | rtx4090* | 7 | 28% |
| 8 | sn67 Harnyx | 68.2 | 7.45 | 975 | cpu-small | 127 | 36% |
| 9 | sn58 Attune | 67.9 | 399 | 541 | rtx4090* | 5 | 74% |
| 10 | sn79 MVTRX | 67.3 | 7.44 | 31.25 | cpu-small | 247 | 1% |
| 11 | sn15 ORO | 67.2 | 7.76 | 15.69 | cpu-small | 62 | 97% |
| 12 | sn4 Targon | 66.9 | 10,111 | 29,811 | rtx4090* | 5 | 70% |
| 13 | sn7 Allways | 65.6 | 219 | 404 | rtx4090* | 7 | 23% |
| 14 | sn14 Cacheon | 65.2 | 174 | 4,607 | rtx4090* | 8 | 63% |
| 15 | sn66 conjectures | 63.9 | 120 | 249 | rtx4090* | 4 | 80% |
| 16 | sn62 Ridges | 63.8 | 115 | 1,250 | rtx4090* | 37 | 17% |
| 17 | sn92 REAX | 63.5 | 124 | 203 | rtx4090 | 234 | 1% |
| 18 | sn120 Affine | 62.2 | 83.09 | 589 | rtx4090* | 270 | 2% |
| 19 | sn61 RedTeam | 61.8 | 65.70 | 87.92 | rtx4090* | 125 | 1% |
| 20 | sn28 SayGM | 61.8 | 65.24 | 2,618 | rtx4090* | 81 | 35% |

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
| concentrated (30–60%) | 20 |
| dominated (60–90%) | 30 |
| captured (>90%) | 25 |

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
| 2026-10-16T00:49 | sn25 | RELEASE | sn25 released v2026.10.15-1073082520 |
| 2026-10-16T00:49 | sn37 | SCORING_COMMIT | sn37 commit touches scoring: fix(miner): support reviewed mainnet runt |
| 2026-10-16T00:49 | sn37 | README_TASK_DIFF | sn37 README task/scoring sections changed |
| 2026-10-16T00:49 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Merge pull request #1393 from carbonphys |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

