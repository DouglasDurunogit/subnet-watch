# Subnet watch — dashboard

_snapshot 2026-07-29T14:59:44Z · block 8728401 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 54 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 92 | `miner_burn` < 0.99 |
| Ranked | 92 | passed every gate |
| **Positive margin** | **54** | income beats machine cost |
| New events this window | 7 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 59 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 7 | `███` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 36 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn23 Trishool | 85.2 | 583 | 583 = | cpu-small | 5 | 20% |
| 2 | sn76 Phylax | 80.9 | 199 | 332 | cpu-small | 4 | 60% |
| 3 | sn98 NeverPlayAlone | 76.1 | 1,746 | 1,746 = | cpu-small | 1 | 100% |
| 4 | sn56 Gradients | 69.1 | 573 | 1,401 | rtx4090* | 6 | 62% |
| 5 | sn67 Harnyx | 68.5 | 8.51 | 995 | cpu-small | 114 | 21% |
| 6 | sn15 ORO | 68.4 | 11.39 | 11,692 | cpu-small | 76 | 93% |
| 7 | sn124 Swarm | 67.6 | 364 | 741 | rtx4090* | 16 | 13% |
| 8 | sn28 gm | 66.7 | 274 | 2,823 | rtx4090* | 7 | 48% |
| 9 | sn101 Tag101 | 65.2 | 3.11 | 65.11 | cpu-small | 244 | 2% |
| 10 | sn85 Vidaio | 65 | 167 | 539 | rtx4090* | 10 | 17% |
| 11 | sn71 Leadpoet | 63.1 | 92.66 | 370 | rtx4090* | 6 | 71% |
| 12 | sn53 engy | 63 | 91.60 | 2,125 | rtx4090 | 34 | 13% |
| 13 | sn61 RedTeam | 58.3 | 22.01 | 151 | rtx4090* | 82 | 5% |
| 14 | sn51 lium.io | 56 | 17.49 | 3,095 | rtx4090* | 38 | 66% |
| 15 | sn102 ConnitoAI | 53.7 | 4.76 | 1,018 | rtx4090* | 9 | 27% |
| 16 | sn7 Allways | 51.2 | 1,568 | 1,568 = | rtx4090* | 2 | 78% |
| 17 | sn120 Affine | 47.5 | 6,429 | 6,429 = | rtx4090* | 5 | 20% |
| 18 | sn4 Targon | 47.3 | 6,134 | 10,131 | rtx4090* | 8 | 31% |
| 19 | sn60 Bitsec.ai | 44.5 | 1,006 | 1,006 = | cpu-small | 2 | 51% |
| 20 | sn93 Bitcast | 43.3 | 55.33 | 55.33 = | rtx4090* | 2 | 98% |

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
| concentrated (30–60%) | 19 |
| dominated (60–90%) | 22 |
| captured (>90%) | 22 |

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
| 2026-07-29T15:00 | sn23 | SCORING_COMMIT | sn23 commit touches scoring: Add universal template support for miners |
| 2026-07-29T15:00 | sn23 | README_TASK_DIFF | sn23 README task/scoring sections changed |
| 2026-07-29T15:00 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-2527, exclude idle filler ports from  |
| 2026-07-29T15:00 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-07-29T15:00 | sn67 | README_TASK_DIFF | sn67 README task/scoring sections changed |
| 2026-07-29T15:00 | sn93 | SCORING_COMMIT | sn93 commit touches scoring: fix: deploy workflows not updating ECS se |
| 2026-07-29T15:00 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: fix(agent-challenge): allow PyPI index f |
| 2026-07-29T12:28 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Cap champion lifetime rewards |
| 2026-07-29T12:28 | sn93 | SCORING_COMMIT | sn93 commit touches scoring: feat: Double product placement reward pay |
| 2026-07-29T10:20 | sn8 | SCORING_COMMIT | sn8 commit touches scoring: Full miner payouts (#862) |
| 2026-07-29T10:20 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-2520, review fixes: guard the scoring |
| 2026-07-29T10:20 | sn53 | SCORING_COMMIT | sn53 commit touches scoring: Merge pull request #29 from hanlinai/docs |
| 2026-07-29T10:20 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: fix(proxy+agent-challenge): unblock mine |
| 2026-07-29T07:34 | sn7 | BURN_DROP | sn7 burn fell 1.000 -> 0.317 - miners can earn again |
| 2026-07-29T07:34 | sn61 | RELEASE | sn61 released 4.8.1 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

