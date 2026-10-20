# Subnet watch — dashboard

_snapshot 2026-10-20T15:15:50Z · block 9325561 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 54 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 98 | `miner_burn` < 0.99 |
| Ranked | 98 | passed every gate |
| **Positive margin** | **54** | income beats machine cost |
| New events this window | 9 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 66 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 3 | `█` |
| 0.4–0.6 | 6 | `███` |
| 0.6–0.8 | 10 | `████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 30 | `█████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn3 Teutonic | 74.3 | 2,717 | 7,258 | rtx4090* | 5 | 40% |
| 2 | sn97 Ingot | 73.4 | 2,051 | 2,051 = | rtx4090* | 5 | 20% |
| 3 | sn91 cascade | 71 | 392 | 1,572 | cpu-small | 5 | 52% |
| 4 | sn67 Harnyx | 71 | 16.05 | 228 | cpu-small | 136 | 9% |
| 5 | sn53 engy | 69 | 549 | 2,285 | rtx4090 | 24 | 16% |
| 6 | sn82 Noah | 68.7 | 661 | 679 | rtx4090* | 60 | 2% |
| 7 | sn1 Apex | 68.3 | 452 | 888 | rtx4090* | 5 | 58% |
| 8 | sn107 Minos | 67.6 | 258 | 21,890 | cpu-small | 20 | 80% |
| 9 | sn23 Trishool | 67.5 | 233 | 233 = | cpu-small | 4 | 80% |
| 10 | sn15 ORO | 65.1 | 6.99 | 15,785 | cpu-small | 66 | 97% |
| 11 | sn14 Cacheon | 65 | 167 | 4,317 | rtx4090* | 11 | 63% |
| 12 | sn120 Affine | 63.8 | 130 | 243 | rtx4090* | 269 | 1% |
| 13 | sn66 conjectures | 63.7 | 114 | 235 | rtx4090* | 4 | 80% |
| 14 | sn55 NIOME | 62.2 | 71.52 | 590 | rtx4090* | 11 | 30% |
| 15 | sn61 RedTeam | 61.8 | 64.11 | 133 | rtx4090* | 121 | 2% |
| 16 | sn111 Claims | 59.5 | 32.44 | 2,902 | rtx4090* | 6 | 90% |
| 17 | sn7 Allways | 59.3 | 33.65 | 103 | rtx4090* | 6 | 71% |
| 18 | sn81 Reliquary | 59.1 | 27.49 | 296 | rtx4090* | 11 | 80% |
| 19 | sn80 OpenRoboto | 58.9 | 941 | 3,761 | rtx4090* | 11 | 35% |
| 20 | sn4 Targon | 57.9 | 9,968 | 29,386 | rtx4090* | 5 | 70% |

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
| wide (<30%) | 29 |
| concentrated (30–60%) | 19 |
| dominated (60–90%) | 27 |
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
| 2026-10-20T15:16 | sn3 | SCORING_COMMIT | sn3 commit touches scoring: Sample evaluation sequences from at least  |
| 2026-10-20T15:16 | sn25 | RELEASE | sn25 released v2026.10.20-1077000950 |
| 2026-10-20T15:16 | sn28 | RELEASE | sn28 released v0.5.5 |
| 2026-10-20T15:16 | sn28 | SCORING_COMMIT | sn28 commit touches scoring: chore(release): gm-miner 0.5.5 (#335) |
| 2026-10-20T15:16 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-4481 - [P1] Validator says the miner  |
| 2026-10-20T15:16 | sn66 | RELEASE | sn66 released deployed/dev: Merge pull request #141 from conjectures-i |
| 2026-10-20T15:16 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-10-20T15:16 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Recover abandoned scorer-image setup thro |
| 2026-10-20T15:16 | sn97 | SCORING_COMMIT | sn97 commit touches scoring: fix: show diverged challengers as < −50%  |
| 2026-10-20T10:18 | sn25 | RELEASE | sn25 released v2026.10.20-1076869840 |
| 2026-10-20T10:18 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-4622 - [P1] Validator: report rented  |
| 2026-10-20T10:18 | sn66 | RELEASE | sn66 released deployed/dev: Merge pull request #139 from conjectures-i |
| 2026-10-20T10:18 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-10-20T10:18 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Reuse validated company authority for con |
| 2026-10-20T10:18 | sn127 | SCORING_COMMIT | sn127 commit touches scoring: Merge pull request #1 from astridintelli |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

