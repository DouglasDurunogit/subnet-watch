# Subnet watch — dashboard

_snapshot 2026-11-20T11:26:20Z · block 9547512 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 55 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 106 | `miner_burn` < 0.99 |
| Ranked | 106 | passed every gate |
| **Positive margin** | **55** | income beats machine cost |
| New events this window | 10 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 70 | `████████████████████████████` |
| 0–0.2 | 6 | `██` |
| 0.2–0.4 | 6 | `██` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 10 | `████` |
| 0.8–0.99 | 9 | `████` |
| ≥0.99 dead | 22 | `█████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn42 CADmind | 81.5 | 229 | 229 = | cpu-small | 5 | 20% |
| 2 | sn3 Teutonic | 73.5 | 2,098 | 4,095 | rtx4090* | 4 | 39% |
| 3 | sn67 Harnyx | 66.5 | 4.60 | 4.60 = | cpu-small | 229 | 6% |
| 4 | sn56 Gradients | 66.1 | 229 | 3,787 | rtx4090* | 7 | 49% |
| 5 | sn15 ORO | 65.3 | 5.36 | 8,589 | cpu-small | 73 | 95% |
| 6 | sn124 Swarm | 65.2 | 185 | 668 | rtx4090* | 11 | 30% |
| 7 | sn66 conjectures | 64.8 | 155 | 940 | rtx4090* | 3 | 81% |
| 8 | sn53 engy | 64.3 | 133 | 10,911 | rtx4090 | 20 | 61% |
| 9 | sn120 Affine | 61.7 | 2,157 | 2,157 = | rtx4090* | 10 | 10% |
| 10 | sn60 Bitsec.ai | 60.6 | 600 | 600 = | cpu-small | 3 | 50% |
| 11 | sn62 Ridges | 60.3 | 40.75 | 496 | rtx4090* | 45 | 12% |
| 12 | sn111 Claims | 60.1 | 38.60 | 156 | rtx4090* | 4 | 88% |
| 13 | sn97 Ingot | 59.5 | 1,122 | 1,122 = | rtx4090* | 4 | 40% |
| 14 | sn102 ConnitoAI | 57.5 | 613 | 628 | rtx4090* | 4 | 26% |
| 15 | sn1 Apex | 56.9 | 518 | 585 | rtx4090* | 4 | 56% |
| 16 | sn5 Hone | 56.8 | 17.88 | 39.32 | rtx4090* | 239 | 1% |
| 17 | sn28 SayGM | 55.8 | 12.90 | 3,089 | rtx4090* | 125 | 19% |
| 18 | sn4 Targon | 55.5 | 4,903 | 19,513 | rtx4090* | 5 | 66% |
| 19 | sn46 Instant | 55.3 | 126 | 160 | cpu-small | 9 | 23% |
| 20 | sn107 Minos | 54.8 | 147 | 11,448 | cpu-small | 20 | 79% |

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
| concentrated (30–60%) | 21 |
| dominated (60–90%) | 30 |
| captured (>90%) | 24 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 98 |
| README keywords (GUESS) | 12 |
| min_compute.yml (curated) | 10 |
| code-submission (validator runs it) | 8 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-11-20T11:26 | sn25 | RELEASE | sn25 released v2026.11.19-1103608200 |
| 2026-11-20T11:26 | sn51 | RELEASE | sn51 released executor-v1.192 |
| 2026-11-20T11:26 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-6666 - [P1] Executor trusts the valid |
| 2026-11-20T11:26 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-11-20T11:26 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Record reviewed scorer changes in protect |
| 2026-11-20T11:26 | sn84 | BURN_DROP | sn84 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-11-20T11:26 | sn94 | README_TASK_DIFF | sn94 README task/scoring sections changed |
| 2026-11-20T11:26 | sn99 | SCORING_COMMIT | sn99 commit touches scoring: Validator loop: tempo read once, one try  |
| 2026-11-20T11:26 | sn99 | README_TASK_DIFF | sn99 README task/scoring sections changed |
| 2026-11-20T11:26 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: L2 FULL RED (release g9334la/lb): the 6  |
| 2026-11-20T03:04 | sn2 | BURN_DROP | sn2 burn fell 1.000 -> 0.936 - miners can earn again |
| 2026-11-20T03:04 | sn53 | SCORING_COMMIT | sn53 commit touches scoring: Merge pull request #65 from hanlinai/feat |
| 2026-11-20T03:04 | sn99 | SCORING_COMMIT | sn99 commit touches scoring: A candidate is evaluated on the machine a |
| 2026-11-20T03:04 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Box loss: a live DOWN mark stays DOWN on |
| 2026-11-19T21:51 | sn3 | SCORING_COMMIT | sn3 commit touches scoring: Retry incomplete R2 reads and prefetch eva |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

