# Subnet watch — dashboard

_snapshot 2026-07-29T01:13:04Z · block 8724270 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 0 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 93 | `miner_burn` < 0.99 |
| Ranked | 93 | passed every gate |
| **Positive margin** | **0** | income beats machine cost |
| New events this window | 5 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 57 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 8 | `████` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 8 | `████` |
| ≥0.99 dead | 35 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 50 | n/a | n/a | cpu-small | 1 | 100% |
| 2 | sn67 Harnyx | 50 | n/a | n/a | cpu-small | 60 | 19% |
| 3 | sn98 NeverPlayAlone | 50 | n/a | n/a | cpu-small | 1 | 100% |
| 4 | sn15 ORO | 50 | n/a | n/a | cpu-small | 83 | 93% |
| 5 | sn71 Leadpoet | 39.3 | n/a | n/a | rtx4090* | 47 | 30% |
| 6 | sn85 Vidaio | 39.3 | n/a | n/a | rtx4090* | 10 | 17% |
| 7 | sn102 ConnitoAI | 39.3 | n/a | n/a | rtx4090* | 9 | 36% |
| 8 | sn56 Gradients | 39.3 | n/a | n/a | rtx4090* | 6 | 61% |
| 9 | sn13 Data Universe | 39.3 | n/a | n/a | rtx4090* | 236 | 69% |
| 10 | sn89 InfiniteQuant | 39.3 | n/a | n/a | rtx4090* | 36 | 44% |
| 11 | sn28 gm | 39.3 | n/a | n/a | rtx4090* | 10 | 56% |
| 12 | sn74 Gittensor | 39.3 | n/a | n/a | rtx4090* | 55 | 45% |
| 13 | sn7 Allways | 39.3 | n/a | n/a | rtx4090* | 11 | 54% |
| 14 | sn103 Djinn | 39.3 | n/a | n/a | rtx4090* | 250 | 80% |
| 15 | sn124 Swarm | 39.3 | n/a | n/a | rtx4090* | 16 | 13% |
| 16 | sn86 kaunan | 27.8 | n/a | n/a | rtx4090* | 1 | n/a |
| 17 | sn90 KubeTEE AI Facto | 27.8 | n/a | n/a | rtx4090* | 1 | n/a |
| 18 | sn60 Bitsec.ai | 15 | n/a | n/a | cpu-small | 2 | 51% |
| 19 | sn101 Tag101 | 15 | n/a | n/a | cpu-small | 249 | 1% |
| 20 | sn11 TrajectoryRL | 15 | n/a | n/a | cpu-small | 1 | 100% |

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
| concentrated (30–60%) | 23 |
| dominated (60–90%) | 17 |
| captured (>90%) | 26 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 107 |
| min_compute.yml (curated) | 9 |
| code-submission (validator runs it) | 8 |
| README keywords (GUESS) | 3 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-07-29T01:13 | sn7 | RELEASE | sn7 released release-20260728-234943 |
| 2026-07-29T01:13 | sn7 | SCORING_COMMIT | sn7 commit touches scoring: Verify TAO transfers by settlement rather  |
| 2026-07-29T01:13 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-07-29T01:13 | sn67 | README_TASK_DIFF | sn67 README task/scoring sections changed |
| 2026-07-29T01:13 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: feat(agent-challenge): remove Phala TEE  |
| 2026-07-28T22:44 | sn13 | SCORING_COMMIT | sn13 commit touches scoring: fix(od): treat scraper ERRORS as "no evid |
| 2026-07-28T22:44 | sn46 | BURN_DROP | sn46 burn fell 1.000 -> 0.760 - miners can earn again |
| 2026-07-28T22:44 | sn56 | SCORING_COMMIT | sn56 commit touches scoring: fix(validator): read the dynamic emission |
| 2026-07-28T22:44 | sn74 | RELEASE | sn74 released release-20260728-214235 |
| 2026-07-28T21:37 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: feat(agent-challenge): NO_PHALA host pip |
| 2026-07-28T21:37 | sn103 | RELEASE | sn103 released v2004: validator: default settle gate budget to 1024 |
| 2026-07-28T21:37 | sn103 | SCORING_COMMIT | sn103 commit touches scoring: validator: default settle gate budget to |
| 2026-07-28T20:08 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: feat(validator): warn on startup when hos |
| 2026-07-28T20:08 | sn62 | BURN_DROP | sn62 burn fell 1.000 -> 0.038 - miners can earn again |
| 2026-07-28T20:08 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: Let the sandboxed agent write its workspa |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

