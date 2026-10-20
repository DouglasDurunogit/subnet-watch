# Subnet watch — dashboard

_snapshot 2026-10-20T10:17:46Z · block 9324071 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 55 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 100 | `miner_burn` < 0.99 |
| Ranked | 100 | passed every gate |
| **Positive margin** | **55** | income beats machine cost |
| New events this window | 6 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 67 | `████████████████████████████` |
| 0–0.2 | 8 | `███` |
| 0.2–0.4 | 3 | `█` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 8 | `███` |
| ≥0.99 dead | 28 | `████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn3 Teutonic | 74.2 | 2,648 | 7,075 | rtx4090* | 5 | 40% |
| 2 | sn91 cascade | 71 | 389 | 1,558 | cpu-small | 5 | 52% |
| 3 | sn67 Harnyx | 70.4 | 13.98 | 40.73 | cpu-small | 128 | 16% |
| 4 | sn102 ConnitoAI | 69.2 | 577 | 1,778 | rtx4090* | 6 | 42% |
| 5 | sn53 engy | 69 | 547 | 2,278 | rtx4090 | 24 | 16% |
| 6 | sn82 Noah | 68.6 | 653 | 671 | rtx4090* | 60 | 2% |
| 7 | sn1 Apex | 68.2 | 437 | 910 | rtx4090* | 5 | 57% |
| 8 | sn107 Minos | 67.5 | 254 | 21,548 | cpu-small | 20 | 80% |
| 9 | sn23 Trishool | 67.4 | 227 | 227 = | cpu-small | 4 | 80% |
| 10 | sn15 ORO | 66.4 | 6.76 | 15,346 | cpu-small | 66 | 97% |
| 11 | sn7 Allways | 66.2 | 248 | 481 | rtx4090* | 5 | 46% |
| 12 | sn120 Affine | 63.9 | 131 | 267 | rtx4090* | 259 | 1% |
| 13 | sn66 conjectures | 63.7 | 111 | 231 | rtx4090* | 4 | 80% |
| 14 | sn14 Cacheon | 63.5 | 108 | 864 | rtx4090* | 11 | 63% |
| 15 | sn55 NIOME | 62.2 | 72.01 | 594 | rtx4090* | 11 | 30% |
| 16 | sn61 RedTeam | 61.5 | 61.34 | 111 | rtx4090* | 121 | 1% |
| 17 | sn97 Ingot | 61.4 | 2,007 | 2,007 = | rtx4090* | 5 | 20% |
| 18 | sn92 REAX | 61.4 | 81.10 | 2,994 | rtx4090 | 250 | 11% |
| 19 | sn54 Yanez | 60.6 | 2.04 | 14.64 | a4000 | 174 | 39% |
| 20 | sn80 OpenRoboto | 59.4 | 1,082 | 2,557 | rtx4090* | 11 | 35% |

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
| 2026-10-20T10:18 | sn25 | RELEASE | sn25 released v2026.10.20-1076869840 |
| 2026-10-20T10:18 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-4622 - [P1] Validator: report rented  |
| 2026-10-20T10:18 | sn66 | RELEASE | sn66 released deployed/dev: Merge pull request #139 from conjectures-i |
| 2026-10-20T10:18 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-10-20T10:18 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Reuse validated company authority for con |
| 2026-10-20T10:18 | sn127 | SCORING_COMMIT | sn127 commit touches scoring: Merge pull request #1 from astridintelli |
| 2026-10-20T05:24 | sn37 | SCORING_COMMIT | sn37 commit touches scoring: fix(miner): admit reviewed runtime481 fun |
| 2026-10-20T05:24 | sn37 | README_TASK_DIFF | sn37 README task/scoring sections changed |
| 2026-10-20T05:24 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge pull request #583 from leadpoet/aud |
| 2026-10-20T05:24 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: fix(validator): a task on Qwen3.5's text- |
| 2026-10-20T00:43 | sn22 | SCORING_COMMIT | sn22 commit touches scoring: fix(validators): embed checks wait up to  |
| 2026-10-20T00:43 | sn28 | RELEASE | sn28 released v0.5.4 |
| 2026-10-20T00:43 | sn28 | SCORING_COMMIT | sn28 commit touches scoring: chore(release): promote gm-miner 0.5.4 (# |
| 2026-10-20T00:43 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Regenerate protected scorer manifest from |
| 2026-10-20T00:43 | sn76 | BURN_DROP | sn76 burn fell 1.000 -> 0.989 - miners can earn again |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

