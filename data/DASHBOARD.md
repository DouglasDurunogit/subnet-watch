# Subnet watch — dashboard

_snapshot 2026-08-20T17:40:42Z · block 8887572 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 57 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 91 | `miner_burn` < 0.99 |
| Ranked | 91 | passed every gate |
| **Positive margin** | **57** | income beats machine cost |
| New events this window | 4 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 61 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 8 | `████` |
| ≥0.99 dead | 37 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 76.8 | 70.83 | 126 | cpu-small | 13 | 20% |
| 2 | sn67 Harnyx | 72.1 | 21.50 | 286 | cpu-small | 178 | 8% |
| 3 | sn23 Trishool | 72 | 523 | 523 = | cpu-small | 2 | 80% |
| 4 | sn15 ORO | 69.8 | 18.98 | 18,546 | cpu-small | 82 | 92% |
| 5 | sn56 Gradients | 69.7 | 679 | 1,035 | rtx4090* | 5 | 72% |
| 6 | sn1 Apex | 69.5 | 647 | 1,436 | rtx4090* | 4 | 53% |
| 7 | sn91 cascade | 69.3 | 611 | 2,470 | rtx4090* | 5 | 52% |
| 8 | sn38 ChronoLLM | 67.7 | 158 | 3,348 | cpu-small | 10 | 52% |
| 9 | sn11 TrajectoryRL | 67.3 | 4,492 | 4,492 = | cpu-small | 1 | 100% |
| 10 | sn26 Perturb | 67.3 | 17.26 | 249 | rtx3060 | 10 | 70% |
| 11 | sn96 Verathos | 66.8 | 15.24 | 369 | rtx4090 | 95 | 41% |
| 12 | sn85 Vidaio | 64.6 | 146 | 420 | rtx4090* | 13 | 42% |
| 13 | sn107 Minos | 64.6 | 127 | 39,106 | cpu-small | 20 | 90% |
| 14 | sn108 Prometheon | 63.8 | 118 | 174 | rtx4090* | 7 | 66% |
| 15 | sn28 gm | 63.3 | 103 | 932 | rtx4090* | 49 | 8% |
| 16 | sn60 Bitsec.ai | 62.4 | 1,027 | 1,027 = | cpu-small | 3 | 50% |
| 17 | sn81 Reliquary | 61.9 | 65.13 | 212 | rtx4090* | 52 | 5% |
| 18 | sn55 NIOME | 61.7 | 61.36 | 514 | rtx4090* | 11 | 29% |
| 19 | sn51 lium.io | 61.3 | 63.28 | 1,197 | rtx4090* | 47 | 82% |
| 20 | sn102 ConnitoAI | 60.5 | 1,508 | 1,510 | rtx4090* | 4 | 25% |

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
| concentrated (30–60%) | 20 |
| dominated (60–90%) | 18 |
| captured (>90%) | 27 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 101 |
| code-submission (validator runs it) | 10 |
| min_compute.yml (curated) | 10 |
| README keywords (GUESS) | 6 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-08-20T17:41 | sn25 | README_TASK_DIFF | sn25 README task/scoring sections changed |
| 2026-08-20T17:41 | sn33 | SCORING_COMMIT | sn33 commit touches scoring: Merge pull request #136 from afterpartyai |
| 2026-08-20T17:41 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: docs(validation): document resilient dia |
| 2026-08-20T17:01 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Bind local readiness verifier environment |
| 2026-08-20T16:17 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: docs: rich-era corrections in scoring arc |
| 2026-08-20T15:47 | sn10 | SCORING_COMMIT | sn10 commit touches scoring: fix(worker): pass leaders.last_score to r |
| 2026-08-20T15:47 | sn53 | SCORING_COMMIT | sn53 commit touches scoring: tee_miner: lift the 1 MiB websocket frame |
| 2026-08-20T15:47 | sn100 | RELEASE | sn100 released v3.3.27 |
| 2026-08-20T15:47 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: fix(design-challenge): drop crate_name s |
| 2026-08-20T14:10 | sn10 | SCORING_COMMIT | sn10 commit touches scoring: feat(api): public read API for rounds, le |
| 2026-08-20T14:10 | sn28 | RELEASE | sn28 released v0.4.9 |
| 2026-08-20T14:10 | sn89 | SCORING_COMMIT | sn89 commit touches scoring: README: a validator needs NO market-data  |
| 2026-08-20T13:27 | sn66 | RELEASE | sn66 released Payment and IAM update |
| 2026-08-20T12:15 | sn28 | RELEASE | sn28 released v0.4.9-dev |
| 2026-08-20T11:38 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: docs: point miners at rich training v2 an |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

