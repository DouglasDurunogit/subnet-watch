# Subnet watch — dashboard

_snapshot 2026-08-20T20:41:08Z · block 8888474 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 55 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 91 | `miner_burn` < 0.99 |
| Ranked | 91 | passed every gate |
| **Positive margin** | **55** | income beats machine cost |
| New events this window | 2 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 61 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 37 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 77 | 74.32 | 125 | cpu-small | 13 | 20% |
| 2 | sn67 Harnyx | 72.1 | 21.34 | 283 | cpu-small | 176 | 8% |
| 3 | sn23 Trishool | 72 | 516 | 516 = | cpu-small | 2 | 80% |
| 4 | sn15 ORO | 70.1 | 19.06 | 18,620 | cpu-small | 82 | 92% |
| 5 | sn56 Gradients | 69.7 | 670 | 1,023 | rtx4090* | 5 | 72% |
| 6 | sn91 cascade | 69.3 | 603 | 2,436 | rtx4090* | 5 | 52% |
| 7 | sn1 Apex | 68.1 | 426 | 1,206 | rtx4090* | 5 | 53% |
| 8 | sn38 ChronoLLM | 67.6 | 154 | 3,268 | cpu-small | 10 | 52% |
| 9 | sn11 TrajectoryRL | 67.3 | 4,439 | 4,439 = | cpu-small | 1 | 100% |
| 10 | sn26 Perturb | 67.2 | 16.93 | 246 | rtx3060 | 10 | 70% |
| 11 | sn96 Verathos | 67.1 | 16.26 | 370 | rtx4090 | 94 | 40% |
| 12 | sn107 Minos | 64.7 | 128 | 37,164 | cpu-small | 20 | 90% |
| 13 | sn85 Vidaio | 64.6 | 146 | 415 | rtx4090* | 13 | 42% |
| 14 | sn108 Prometheon | 63.8 | 118 | 174 | rtx4090* | 7 | 66% |
| 15 | sn28 gm | 63.4 | 104 | 1,656 | rtx4090* | 53 | 15% |
| 16 | sn55 NIOME | 61.7 | 62.15 | 520 | rtx4090* | 11 | 29% |
| 17 | sn51 lium.io | 61.5 | 65.58 | 1,173 | rtx4090* | 47 | 82% |
| 18 | sn81 Reliquary | 61.4 | 56.93 | 204 | rtx4090* | 50 | 5% |
| 19 | sn60 Bitsec.ai | 61.2 | 724 | 1,013 | cpu-small | 3 | 50% |
| 20 | sn102 ConnitoAI | 60.1 | 1,351 | 1,623 | rtx4090* | 5 | 28% |

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
| concentrated (30–60%) | 20 |
| dominated (60–90%) | 18 |
| captured (>90%) | 26 |

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
| 2026-08-20T20:41 | sn25 | RELEASE | sn25 released v2026.8.20-1024555910 |
| 2026-08-20T19:55 | sn18 | RELEASE | sn18 released Release 2.1.2 |
| 2026-08-20T18:15 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Repair release verifier test isolation |
| 2026-08-20T18:15 | sn89 | SCORING_COMMIT | sn89 commit touches scoring: HF: apply owner-hosted miner integrity ve |
| 2026-08-20T18:15 | sn121 | BURN_DROP | sn121 burn fell 1.000 -> 0.611 - miners can earn again |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

