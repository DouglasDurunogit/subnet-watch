# Subnet watch — dashboard

_snapshot 2026-10-20T22:43:14Z · block 9327798 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 54 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 96 | `miner_burn` < 0.99 |
| Ranked | 96 | passed every gate |
| **Positive margin** | **54** | income beats machine cost |
| New events this window | 3 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 66 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 3 | `█` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 11 | `█████` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 32 | `██████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn114 SOMA | 81.5 | 8,751 | 13,127 | cpu-small | 2 | 75% |
| 2 | sn121 sundae_bar | 74.8 | 1,188 | 1,188 = | cpu-small | 2 | 60% |
| 3 | sn3 Teutonic | 74.4 | 2,786 | 7,443 | rtx4090* | 5 | 40% |
| 4 | sn97 Ingot | 73.5 | 2,093 | 2,093 = | rtx4090* | 5 | 20% |
| 5 | sn91 cascade | 71.1 | 398 | 1,595 | cpu-small | 5 | 52% |
| 6 | sn67 Harnyx | 71.1 | 16.42 | 233 | cpu-small | 137 | 9% |
| 7 | sn102 ConnitoAI | 69.1 | 573 | 1,929 | rtx4090* | 6 | 45% |
| 8 | sn53 engy | 69 | 558 | 2,319 | rtx4090 | 24 | 16% |
| 9 | sn82 Noah | 68.7 | 663 | 680 | rtx4090* | 60 | 2% |
| 10 | sn1 Apex | 68.6 | 486 | 1,021 | rtx4090* | 5 | 55% |
| 11 | sn23 Trishool | 67.6 | 238 | 238 = | cpu-small | 4 | 80% |
| 12 | sn107 Minos | 67.5 | 251 | 21,320 | cpu-small | 20 | 80% |
| 13 | sn15 ORO | 67 | 7.14 | 16,088 | cpu-small | 66 | 97% |
| 14 | sn14 Cacheon | 65.1 | 171 | 4,430 | rtx4090* | 11 | 63% |
| 15 | sn66 conjectures | 63.8 | 117 | 242 | rtx4090* | 4 | 80% |
| 16 | sn55 NIOME | 62.1 | 69.40 | 574 | rtx4090* | 11 | 30% |
| 17 | sn92 REAX | 60.7 | 82.64 | 2,978 | rtx4090 | 243 | 11% |
| 18 | sn111 Claims | 59.5 | 33.15 | 2,953 | rtx4090* | 6 | 90% |
| 19 | sn80 OpenRoboto | 58.9 | 949 | 3,794 | rtx4090* | 11 | 35% |
| 20 | sn81 Reliquary | 58.9 | 26.19 | 254 | rtx4090* | 12 | 75% |

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
| wide (<30%) | 24 |
| concentrated (30–60%) | 22 |
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
| 2026-10-20T15:16 | sn28 | RELEASE | sn28 released v0.5.5 |
| 2026-10-20T15:16 | sn28 | SCORING_COMMIT | sn28 commit touches scoring: chore(release): gm-miner 0.5.5 (#335) |
| 2026-10-20T15:16 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-4481 - [P1] Validator says the miner  |
| 2026-10-20T15:16 | sn66 | RELEASE | sn66 released deployed/dev: Merge pull request #141 from conjectures-i |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

