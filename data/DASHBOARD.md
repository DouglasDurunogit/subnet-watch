# Subnet watch — dashboard

_snapshot 2026-10-20T19:27:53Z · block 9326821 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 57 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 99 | `miner_burn` < 0.99 |
| Ranked | 99 | passed every gate |
| **Positive margin** | **57** | income beats machine cost |
| New events this window | 6 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 69 | `████████████████████████████` |
| 0–0.2 | 6 | `██` |
| 0.2–0.4 | 3 | `█` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 11 | `████` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 29 | `████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn121 sundae_bar | 74.7 | 1,164 | 1,164 = | cpu-small | 2 | 60% |
| 2 | sn3 Teutonic | 74.3 | 2,729 | 7,292 | rtx4090* | 5 | 40% |
| 3 | sn97 Ingot | 73.4 | 2,052 | 2,052 = | rtx4090* | 5 | 20% |
| 4 | sn67 Harnyx | 71.1 | 16.06 | 228 | cpu-small | 137 | 9% |
| 5 | sn91 cascade | 71 | 392 | 1,571 | cpu-small | 5 | 52% |
| 6 | sn102 ConnitoAI | 69.1 | 560 | 1,883 | rtx4090* | 6 | 45% |
| 7 | sn53 engy | 69 | 547 | 2,277 | rtx4090 | 24 | 16% |
| 8 | sn82 Noah | 68.7 | 654 | 672 | rtx4090* | 60 | 2% |
| 9 | sn1 Apex | 68.5 | 478 | 1,012 | rtx4090* | 5 | 55% |
| 10 | sn23 Trishool | 67.5 | 234 | 234 = | cpu-small | 4 | 80% |
| 11 | sn107 Minos | 67.4 | 245 | 20,872 | cpu-small | 20 | 80% |
| 12 | sn15 ORO | 66 | 6.98 | 15,771 | cpu-small | 66 | 97% |
| 13 | sn14 Cacheon | 65 | 167 | 4,333 | rtx4090* | 11 | 63% |
| 14 | sn120 Affine | 63.9 | 134 | 250 | rtx4090* | 269 | 1% |
| 15 | sn66 conjectures | 63.7 | 114 | 222 | rtx4090* | 4 | 81% |
| 16 | sn55 NIOME | 62 | 68.29 | 566 | rtx4090* | 11 | 30% |
| 17 | sn81 Reliquary | 61.1 | 51.28 | 267 | rtx4090* | 11 | 76% |
| 18 | sn111 Claims | 59.5 | 32.32 | 2,893 | rtx4090* | 6 | 90% |
| 19 | sn80 OpenRoboto | 58.9 | 928 | 3,709 | rtx4090* | 11 | 35% |
| 20 | sn92 REAX | 58.8 | 74.84 | 3,168 | rtx4090 | 245 | 11% |

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
| wide (<30%) | 25 |
| concentrated (30–60%) | 22 |
| dominated (60–90%) | 28 |
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
| 2026-10-20T15:16 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-10-20T15:16 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Recover abandoned scorer-image setup thro |
| 2026-10-20T15:16 | sn97 | SCORING_COMMIT | sn97 commit touches scoring: fix: show diverged challengers as < −50%  |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

