# Subnet watch — dashboard

_snapshot 2026-07-29T10:20:30Z · block 8727005 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 51 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 93 | `miner_burn` < 0.99 |
| Ranked | 93 | passed every gate |
| **Positive margin** | **51** | income beats machine cost |
| New events this window | 4 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 59 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 6 | `███` |
| 0.6–0.8 | 10 | `█████` |
| 0.8–0.99 | 8 | `████` |
| ≥0.99 dead | 35 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 81 | 202 | 339 | cpu-small | 4 | 60% |
| 2 | sn56 Gradients | 69.2 | 582 | 1,444 | rtx4090* | 6 | 62% |
| 3 | sn15 ORO | 68.7 | 11.79 | 12,070 | cpu-small | 76 | 93% |
| 4 | sn85 Vidaio | 68.5 | 474 | 517 | rtx4090* | 10 | 17% |
| 5 | sn67 Harnyx | 68.5 | 8.48 | 992 | cpu-small | 108 | 21% |
| 6 | sn124 Swarm | 67.4 | 354 | 719 | rtx4090* | 16 | 13% |
| 7 | sn28 gm | 66.4 | 258 | 1,801 | rtx4090* | 7 | 63% |
| 8 | sn101 Tag101 | 65.9 | 3.99 | 57.78 | cpu-small | 242 | 2% |
| 9 | sn53 engy | 62.4 | 77.15 | 2,303 | rtx4090 | 45 | 13% |
| 10 | sn71 Leadpoet | 61.4 | 56.93 | 271 | rtx4090* | 6 | 70% |
| 11 | sn61 RedTeam | 58.5 | 23.15 | 155 | rtx4090* | 82 | 5% |
| 12 | sn51 lium.io | 55.3 | 15.07 | 3,150 | rtx4090* | 38 | 66% |
| 13 | sn102 ConnitoAI | 55.1 | 7.65 | 986 | rtx4090* | 9 | 26% |
| 14 | sn7 Allways | 51.8 | 2,061 | 2,061 = | rtx4090* | 1 | 100% |
| 15 | sn23 Trishool | 50.2 | 593 | 593 = | cpu-small | 5 | 20% |
| 16 | sn98 NeverPlayAlone | 50 | n/a | n/a | cpu-small | 1 | 100% |
| 17 | sn120 Affine | 47.6 | 6,655 | 6,655 = | rtx4090* | 5 | 20% |
| 18 | sn4 Targon | 47.4 | 6,216 | 10,267 | rtx4090* | 8 | 31% |
| 19 | sn60 Bitsec.ai | 44.5 | 1,001 | 1,001 = | cpu-small | 2 | 51% |
| 20 | sn107 Minos | 43.3 | 118 | 35,003 | cpu-small | 20 | 90% |

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
| concentrated (30–60%) | 19 |
| dominated (60–90%) | 19 |
| captured (>90%) | 27 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 106 |
| min_compute.yml (curated) | 9 |
| code-submission (validator runs it) | 8 |
| README keywords (GUESS) | 4 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-07-29T10:20 | sn8 | SCORING_COMMIT | sn8 commit touches scoring: Full miner payouts (#862) |
| 2026-07-29T10:20 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-2520, review fixes: guard the scoring |
| 2026-07-29T10:20 | sn53 | SCORING_COMMIT | sn53 commit touches scoring: Merge pull request #29 from hanlinai/docs |
| 2026-07-29T10:20 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: fix(proxy+agent-challenge): unblock mine |
| 2026-07-29T07:34 | sn7 | BURN_DROP | sn7 burn fell 1.000 -> 0.317 - miners can earn again |
| 2026-07-29T07:34 | sn61 | RELEASE | sn61 released 4.8.1 |
| 2026-07-29T07:34 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Preserve live validator runtime during re |
| 2026-07-29T07:34 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: fix(agent-challenge): copy golden digest |
| 2026-07-29T04:44 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: Create a writable state directory in the  |
| 2026-07-29T04:44 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: fix(master): allowlist public FE agent-c |
| 2026-07-29T04:44 | sn101 | SCORING_COMMIT | sn101 commit touches scoring: Penalize incomplete tag submissions in m |
| 2026-07-29T01:13 | sn7 | RELEASE | sn7 released release-20260728-234943 |
| 2026-07-29T01:13 | sn7 | SCORING_COMMIT | sn7 commit touches scoring: Verify TAO transfers by settlement rather  |
| 2026-07-29T01:13 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-07-29T01:13 | sn67 | README_TASK_DIFF | sn67 README task/scoring sections changed |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

