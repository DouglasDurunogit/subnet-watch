# Subnet watch — dashboard

_snapshot 2026-08-20T19:10:08Z · block 8888019 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 57 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 92 | `miner_burn` < 0.99 |
| Ranked | 92 | passed every gate |
| **Positive margin** | **57** | income beats machine cost |
| New events this window | 3 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 61 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 10 | `█████` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 36 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 76.8 | 70.30 | 125 | cpu-small | 13 | 20% |
| 2 | sn121 sundae_bar | 74.5 | 1,106 | 1,106 = | cpu-small | 2 | 61% |
| 3 | sn67 Harnyx | 72.1 | 21.18 | 282 | cpu-small | 178 | 8% |
| 4 | sn23 Trishool | 72 | 516 | 516 = | cpu-small | 2 | 80% |
| 5 | sn56 Gradients | 69.7 | 669 | 1,021 | rtx4090* | 5 | 72% |
| 6 | sn91 cascade | 69.3 | 605 | 2,443 | rtx4090* | 5 | 52% |
| 7 | sn15 ORO | 69.2 | 19.01 | 18,573 | cpu-small | 82 | 92% |
| 8 | sn1 Apex | 68.2 | 430 | 1,198 | rtx4090* | 5 | 53% |
| 9 | sn38 ChronoLLM | 67.7 | 155 | 3,283 | cpu-small | 10 | 52% |
| 10 | sn11 TrajectoryRL | 67.3 | 4,432 | 4,432 = | cpu-small | 1 | 100% |
| 11 | sn26 Perturb | 67.3 | 16.99 | 245 | rtx3060 | 10 | 70% |
| 12 | sn96 Verathos | 67.1 | 16.24 | 378 | rtx4090 | 95 | 41% |
| 13 | sn107 Minos | 65.4 | 151 | 38,028 | cpu-small | 20 | 89% |
| 14 | sn85 Vidaio | 64.2 | 133 | 414 | rtx4090* | 13 | 42% |
| 15 | sn108 Prometheon | 63.8 | 117 | 173 | rtx4090* | 7 | 66% |
| 16 | sn28 gm | 63.4 | 106 | 1,267 | rtx4090* | 51 | 11% |
| 17 | sn60 Bitsec.ai | 62.4 | 1,018 | 1,018 = | cpu-small | 3 | 50% |
| 18 | sn81 Reliquary | 62.2 | 70.97 | 203 | rtx4090* | 51 | 5% |
| 19 | sn51 lium.io | 62 | 75.76 | 1,157 | rtx4090* | 45 | 82% |
| 20 | sn55 NIOME | 61.7 | 61.02 | 511 | rtx4090* | 11 | 29% |

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
| concentrated (30–60%) | 19 |
| dominated (60–90%) | 21 |
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
| 2026-08-20T14:10 | sn28 | RELEASE | sn28 released v0.4.9 |
| 2026-08-20T14:10 | sn89 | SCORING_COMMIT | sn89 commit touches scoring: README: a validator needs NO market-data  |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

