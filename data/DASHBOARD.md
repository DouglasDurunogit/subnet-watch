# Subnet watch — dashboard

_snapshot 2026-10-21T01:02:11Z · block 9328470 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 56 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 97 | `miner_burn` < 0.99 |
| Ranked | 97 | passed every gate |
| **Positive margin** | **56** | income beats machine cost |
| New events this window | 4 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 67 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 3 | `█` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 11 | `█████` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 31 | `█████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn114 SOMA | 81.5 | 8,820 | 13,230 | cpu-small | 2 | 75% |
| 2 | sn120 Affine | 75 | 3,324 | 5,899 | rtx4090* | 10 | 17% |
| 3 | sn121 sundae_bar | 74.7 | 1,179 | 1,179 = | cpu-small | 2 | 60% |
| 4 | sn3 Teutonic | 74.4 | 2,767 | 7,391 | rtx4090* | 5 | 40% |
| 5 | sn97 Ingot | 73.4 | 2,062 | 2,062 = | rtx4090* | 5 | 20% |
| 6 | sn102 ConnitoAI | 71.2 | 1,069 | 1,069 | rtx4090* | 4 | 25% |
| 7 | sn67 Harnyx | 71.1 | 16.27 | 231 | cpu-small | 137 | 9% |
| 8 | sn91 cascade | 71 | 392 | 1,570 | cpu-small | 5 | 52% |
| 9 | sn53 engy | 69 | 557 | 2,318 | rtx4090 | 24 | 16% |
| 10 | sn82 Noah | 68.7 | 659 | 677 | rtx4090* | 60 | 2% |
| 11 | sn1 Apex | 68.5 | 476 | 1,021 | rtx4090* | 5 | 56% |
| 12 | sn23 Trishool | 67.6 | 237 | 237 = | cpu-small | 4 | 80% |
| 13 | sn107 Minos | 67.5 | 255 | 21,612 | cpu-small | 20 | 80% |
| 14 | sn15 ORO | 66.8 | 7.08 | 15,979 | cpu-small | 66 | 97% |
| 15 | sn14 Cacheon | 65.1 | 170 | 4,393 | rtx4090* | 11 | 63% |
| 16 | sn66 conjectures | 63.8 | 115 | 239 | rtx4090* | 4 | 80% |
| 17 | sn55 NIOME | 62 | 67.92 | 563 | rtx4090* | 11 | 30% |
| 18 | sn81 Reliquary | 60.9 | 48.46 | 217 | rtx4090* | 14 | 76% |
| 19 | sn111 Claims | 59.5 | 32.86 | 2,932 | rtx4090* | 6 | 90% |
| 20 | sn80 OpenRoboto | 58.9 | 946 | 3,780 | rtx4090* | 11 | 35% |

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
| dominated (60–90%) | 28 |
| captured (>90%) | 21 |

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
| 2026-10-21T01:02 | sn25 | RELEASE | sn25 released v2026.10.20-1077406510 |
| 2026-10-21T01:02 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Evaluate Arena claim admission lazily in  |
| 2026-10-21T01:02 | sn92 | RELEASE | sn92 released v1.2.0-rc9.post7 |
| 2026-10-21T01:02 | sn120 | BURN_DROP | sn120 burn fell 1.000 -> 0.100 - miners can earn again |
| 2026-10-20T22:43 | sn5 | SCORING_COMMIT | sn5 commit touches scoring: Keep validator connections alive while min |
| 2026-10-20T22:43 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Bound composed scorer image tags without  |
| 2026-10-20T22:43 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: Merge invalidated export filtering (#365) |
| 2026-10-20T19:28 | sn48 | BURN_DROP | sn48 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-10-20T19:28 | sn66 | RELEASE | sn66 released deployed/dev: Merge pull request #143 from conjectures-i |
| 2026-10-20T19:28 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: Merge pull request #139 from conjectures- |
| 2026-10-20T19:28 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Refresh persisted Arena model scores befo |
| 2026-10-20T19:28 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: ci: replace obsolete validator check runs |
| 2026-10-20T19:28 | sn92 | RELEASE | sn92 released v1.2.0-rc9.post6 |
| 2026-10-20T15:16 | sn3 | SCORING_COMMIT | sn3 commit touches scoring: Sample evaluation sequences from at least  |
| 2026-10-20T15:16 | sn25 | RELEASE | sn25 released v2026.10.20-1077000950 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

