# Subnet watch — dashboard

_snapshot 2026-08-20T19:54:55Z · block 8888243 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 56 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 91 | `miner_burn` < 0.99 |
| Ranked | 91 | passed every gate |
| **Positive margin** | **56** | income beats machine cost |
| New events this window | 1 | see ALARMS.md |

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
| 1 | sn76 Phylax | 76.7 | 70.01 | 124 | cpu-small | 13 | 20% |
| 2 | sn121 sundae_bar | 74.6 | 1,124 | 1,124 = | cpu-small | 2 | 60% |
| 3 | sn67 Harnyx | 72.1 | 21.07 | 280 | cpu-small | 177 | 8% |
| 4 | sn23 Trishool | 72 | 514 | 514 = | cpu-small | 2 | 80% |
| 5 | sn56 Gradients | 69.6 | 666 | 1,017 | rtx4090* | 5 | 72% |
| 6 | sn15 ORO | 69.6 | 18.87 | 18,443 | cpu-small | 82 | 92% |
| 7 | sn91 cascade | 69.3 | 602 | 2,435 | rtx4090* | 5 | 52% |
| 8 | sn1 Apex | 68.1 | 426 | 1,201 | rtx4090* | 5 | 53% |
| 9 | sn38 ChronoLLM | 67.6 | 153 | 3,248 | cpu-small | 10 | 52% |
| 10 | sn11 TrajectoryRL | 67.3 | 4,412 | 4,412 = | cpu-small | 1 | 100% |
| 11 | sn26 Perturb | 67.2 | 16.82 | 244 | rtx3060 | 10 | 70% |
| 12 | sn96 Verathos | 67.2 | 16.74 | 375 | rtx4090 | 96 | 40% |
| 13 | sn107 Minos | 65.5 | 154 | 37,747 | cpu-small | 20 | 89% |
| 14 | sn85 Vidaio | 64.5 | 144 | 412 | rtx4090* | 13 | 42% |
| 15 | sn108 Prometheon | 63.8 | 117 | 172 | rtx4090* | 7 | 66% |
| 16 | sn28 gm | 63.4 | 104 | 1,652 | rtx4090* | 53 | 15% |
| 17 | sn51 lium.io | 61.6 | 68.80 | 1,157 | rtx4090* | 46 | 82% |
| 18 | sn55 NIOME | 61.6 | 60.16 | 506 | rtx4090* | 11 | 29% |
| 19 | sn81 Reliquary | 61.5 | 57.29 | 187 | rtx4090* | 51 | 5% |
| 20 | sn60 Bitsec.ai | 61.2 | 732 | 1,025 | cpu-small | 3 | 50% |

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
| 2026-08-20T14:10 | sn28 | RELEASE | sn28 released v0.4.9 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

