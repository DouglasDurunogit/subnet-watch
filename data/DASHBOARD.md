# Subnet watch — dashboard

_snapshot 2026-10-18T05:48:50Z · block 9308326 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 56 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 99 | `miner_burn` < 0.99 |
| Ranked | 99 | passed every gate |
| **Positive margin** | **56** | income beats machine cost |
| New events this window | 6 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 67 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 6 | `███` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 29 | `████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn41 Almanac | 75.7 | 54.85 | 97.28 | cpu-small | 120 | 6% |
| 2 | sn3 Teutonic | 74.5 | 2,860 | 7,641 | rtx4090* | 5 | 40% |
| 3 | sn91 cascade | 71.2 | 411 | 1,646 | cpu-small | 5 | 52% |
| 4 | sn53 engy | 69.3 | 596 | 2,479 | rtx4090 | 24 | 16% |
| 5 | sn1 Apex | 68.4 | 465 | 874 | rtx4090* | 5 | 56% |
| 6 | sn102 ConnitoAI | 68.4 | 457 | 1,120 | rtx4090* | 7 | 26% |
| 7 | sn82 Noah | 68.1 | 629 | 629 = | rtx4090* | 64 | 2% |
| 8 | sn67 Harnyx | 67.9 | 7.25 | 150 | cpu-small | 188 | 6% |
| 9 | sn58 Attune | 67.8 | 389 | 628 | rtx4090* | 5 | 71% |
| 10 | sn107 Minos | 67.5 | 249 | 21,164 | cpu-small | 20 | 80% |
| 11 | sn15 ORO | 66.8 | 6.73 | 16,120 | cpu-small | 60 | 97% |
| 12 | sn14 Cacheon | 65.4 | 185 | 595 | rtx4090* | 9 | 53% |
| 13 | sn120 Affine | 64.6 | 167 | 428 | rtx4090* | 201 | 1% |
| 14 | sn66 conjectures | 63.7 | 113 | 235 | rtx4090* | 4 | 80% |
| 15 | sn97 Ingot | 61.5 | 2,036 | 2,036 = | rtx4090* | 5 | 20% |
| 16 | sn92 REAX | 61.5 | 100 | 3,482 | rtx4090 | 230 | 11% |
| 17 | sn61 RedTeam | 61.1 | 53.47 | 97.25 | rtx4090* | 132 | 1% |
| 18 | sn28 SayGM | 59 | 29.44 | 3,617 | rtx4090* | 104 | 25% |
| 19 | sn4 Targon | 57.8 | 9,746 | 28,734 | rtx4090* | 5 | 70% |
| 20 | sn23 Trishool | 57.5 | 238 | 238 = | cpu-small | 4 | 80% |

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
| concentrated (30–60%) | 20 |
| dominated (60–90%) | 26 |
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
| 2026-10-18T05:49 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: fix(validator): send sandbox_metadata whe |
| 2026-10-18T05:49 | sn25 | RELEASE | sn25 released v2026.10.17-1074871400 |
| 2026-10-18T05:49 | sn53 | SCORING_COMMIT | sn53 commit touches scoring: tee_miner: default to half the legs on th |
| 2026-10-18T05:49 | sn55 | SCORING_COMMIT | sn55 commit touches scoring: set weights using valid scores |
| 2026-10-18T05:49 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Prune superseded Deepline score billing h |
| 2026-10-18T05:49 | sn125 | README_TASK_DIFF | sn125 README task/scoring sections changed |
| 2026-10-18T00:59 | sn15 | RELEASE | sn15 released v2.5.6: Bound per-evaluation sandbox disk use |
| 2026-10-18T00:59 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: Bound per-evaluation sandbox disk use |
| 2026-10-17T23:04 | sn51 | RELEASE | sn51 released miner-v1.006 |
| 2026-10-17T23:04 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-4539 - Miner: a portal delete removes |
| 2026-10-17T23:04 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Recover historical reward coverage gaps f |
| 2026-10-17T20:51 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: Merge pull request #373 from TensorLink-A |
| 2026-10-17T18:25 | sn41 | SCORING_COMMIT | sn41 commit touches scoring: Merge pull request #59 from corvxai/vali_ |
| 2026-10-17T18:25 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Backport current reward coverage capture  |
| 2026-10-17T15:58 | sn7 | RELEASE | sn7 released release-20261017-152034: Bound event ingest per pass and  |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

