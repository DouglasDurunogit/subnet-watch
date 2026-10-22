# Subnet watch — dashboard

_snapshot 2026-10-22T01:56:46Z · block 9335885 · run_status **ok**_

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
| New events this window | 4 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 65 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 7 | `███` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 32 | `██████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn3 Teutonic | 74.4 | 2,805 | 7,319 | rtx4090* | 5 | 41% |
| 2 | sn120 Affine | 73.9 | 2,404 | 11,912 | rtx4090* | 10 | 35% |
| 3 | sn91 cascade | 71.1 | 398 | 1,596 | cpu-small | 5 | 52% |
| 4 | sn102 ConnitoAI | 70.2 | 797 | 1,309 | rtx4090* | 5 | 33% |
| 5 | sn1 Apex | 68.5 | 480 | 934 | rtx4090* | 5 | 58% |
| 6 | sn67 Harnyx | 68.2 | 7.97 | 229 | cpu-small | 147 | 9% |
| 7 | sn82 Noah | 67.6 | 597 | 627 | rtx4090* | 62 | 2% |
| 8 | sn125 Refinery | 67.3 | 332 | 979 | rtx4090* | 4 | 50% |
| 9 | sn107 Minos | 67.2 | 235 | 19,962 | cpu-small | 20 | 80% |
| 10 | sn53 engy | 67.1 | 314 | 2,574 | rtx4090 | 36 | 11% |
| 11 | sn15 ORO | 66.8 | 7.64 | 15,366 | cpu-small | 64 | 97% |
| 12 | sn66 conjectures | 63.6 | 109 | 225 | rtx4090* | 4 | 80% |
| 13 | sn26 Perturb | 62.9 | 188 | 236 | rtx3060 | 4 | 60% |
| 14 | sn55 NIOME | 62 | 66.80 | 555 | rtx4090* | 11 | 30% |
| 15 | sn23 Trishool | 61.7 | 847 | 847 = | cpu-small | 2 | 80% |
| 16 | sn111 Claims | 59.4 | 32.17 | 2,883 | rtx4090* | 6 | 90% |
| 17 | sn92 REAX | 59.2 | 79.92 | 2,601 | rtx4090 | 236 | 10% |
| 18 | sn81 Reliquary | 59.2 | 28.75 | 99.03 | rtx4090* | 4 | 95% |
| 19 | sn80 OpenRoboto | 59.1 | 1,012 | 4,262 | rtx4090* | 11 | 25% |
| 20 | sn46 Instant | 59 | 376 | 414 | cpu-small | 7 | 16% |

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
| captured (>90%) | 22 |

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
| 2026-10-22T01:57 | sn2 | SCORING_COMMIT | sn2 commit touches scoring: Add finalized-chain observer for validator |
| 2026-10-22T01:57 | sn25 | RELEASE | sn25 released v2026.10.21-1078274420 |
| 2026-10-22T01:57 | sn117 | RELEASE | sn117 released everycli v0.7.0 |
| 2026-10-22T01:57 | sn117 | SCORING_COMMIT | sn117 commit touches scoring: test: record final v0.6.3 offline update |
| 2026-10-21T23:30 | sn10 | BURN_DROP | sn10 burn fell 1.000 -> 0.571 - miners can earn again |
| 2026-10-21T23:30 | sn25 | RELEASE | sn25 released v2026.10.21-1078195620 |
| 2026-10-21T23:30 | sn28 | RELEASE | sn28 released v0.5.7 |
| 2026-10-21T23:30 | sn28 | SCORING_COMMIT | sn28 commit touches scoring: chore(release): gm-miner 0.5.7 (#340) |
| 2026-10-21T23:30 | sn71 | BURN_DROP | sn71 burn fell 1.000 -> 0.700 - miners can earn again |
| 2026-10-21T23:30 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Keep restored-score exclusions visible wi |
| 2026-10-21T23:30 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Merge pull request #343 from Umi-BitSign/ |
| 2026-10-21T23:30 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: fix: verify evaluation image against supp |
| 2026-10-21T20:17 | sn7 | RELEASE | sn7 released release-20261021-195318: Scale the miner pool by recent s |
| 2026-10-21T20:17 | sn7 | SCORING_COMMIT | sn7 commit touches scoring: Scale the miner pool by recent swap fees ( |
| 2026-10-21T20:17 | sn28 | RELEASE | sn28 released v0.5.6-dev |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

