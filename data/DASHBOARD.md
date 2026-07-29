# Subnet watch — dashboard

_snapshot 2026-07-29T04:44:02Z · block 8725325 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 49 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 92 | `miner_burn` < 0.99 |
| Ranked | 92 | passed every gate |
| **Positive margin** | **49** | income beats machine cost |
| New events this window | 3 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 58 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 6 | `███` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 8 | `████` |
| ≥0.99 dead | 36 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn98 NeverPlayAlone | 76.1 | 1,740 | 1,740 = | cpu-small | 1 | 100% |
| 2 | sn56 Gradients | 69.1 | 574 | 1,450 | rtx4090* | 6 | 62% |
| 3 | sn67 Harnyx | 68.5 | 8.32 | 977 | cpu-small | 99 | 21% |
| 4 | sn15 ORO | 67.9 | 10.04 | 19.45 | cpu-small | 84 | 93% |
| 5 | sn101 Tag101 | 67.5 | 6.26 | 36.96 | cpu-small | 243 | 1% |
| 6 | sn124 Swarm | 67.4 | 346 | 703 | rtx4090* | 16 | 13% |
| 7 | sn85 Vidaio | 67.3 | 334 | 574 | rtx4090* | 10 | 19% |
| 8 | sn28 gm | 57 | 16.15 | 1,724 | rtx4090* | 10 | 67% |
| 9 | sn102 ConnitoAI | 56 | 10.49 | 945 | rtx4090* | 9 | 26% |
| 10 | sn23 Trishool | 52.2 | 986 | 986 = | cpu-small | 3 | 33% |
| 11 | sn76 Phylax | 50 | n/a | n/a | cpu-small | 1 | 100% |
| 12 | sn120 Affine | 47.5 | 6,480 | 6,480 = | rtx4090* | 5 | 20% |
| 13 | sn4 Targon | 47.2 | 5,960 | 9,844 | rtx4090* | 8 | 31% |
| 14 | sn60 Bitsec.ai | 44.3 | 969 | 969 = | cpu-small | 2 | 51% |
| 15 | sn107 Minos | 42.8 | 104 | 30,916 | cpu-small | 20 | 90% |
| 16 | sn1 Apex | 41.3 | 1,004 | 1,799 | rtx4090* | 5 | 40% |
| 17 | sn71 Leadpoet | 39.3 | -0.16 | 375 | rtx4090* | 24 | 35% |
| 18 | sn13 Data Universe | 39.3 | -2.71 | 2.50 | rtx4090* | 233 | 69% |
| 19 | sn74 Gittensor | 39.3 | -3.88 | 264 | rtx4090* | 56 | 46% |
| 20 | sn103 Djinn | 39.3 | -7.36 | -7.28 | rtx4090* | 250 | 80% |

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
| dominated (60–90%) | 18 |
| captured (>90%) | 27 |

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
| 2026-07-29T04:44 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: Create a writable state directory in the  |
| 2026-07-29T04:44 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: fix(master): allowlist public FE agent-c |
| 2026-07-29T04:44 | sn101 | SCORING_COMMIT | sn101 commit touches scoring: Penalize incomplete tag submissions in m |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

