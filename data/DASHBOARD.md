# Subnet watch — dashboard

_snapshot 2026-09-21T19:39:59Z · block 9118095 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 57 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 96 | `miner_burn` < 0.99 |
| Ranked | 96 | passed every gate |
| **Positive margin** | **57** | income beats machine cost |
| New events this window | 16 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 62 | `████████████████████████████` |
| 0–0.2 | 12 | `█████` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 7 | `███` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 32 | `██████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn4 Targon | 78.3 | 8,776 | 24,632 | rtx4090* | 6 | 53% |
| 2 | sn3 Teutonic | 76.7 | 5,551 | 5,551 = | rtx4090* | 5 | 20% |
| 3 | sn91 cascade | 72.1 | 532 | 1,419 | cpu-small | 5 | 52% |
| 4 | sn102 ConnitoAI | 71.5 | 1,158 | 1,264 | rtx4090* | 5 | 26% |
| 5 | sn107 Minos | 69 | 361 | 30,669 | cpu-small | 20 | 80% |
| 6 | sn26 Perturb | 68.8 | 25.53 | 296 | rtx3060 | 10 | 70% |
| 7 | sn67 Harnyx | 68.6 | 9.00 | 1,226 | cpu-small | 142 | 36% |
| 8 | sn15 ORO | 67.5 | 9.56 | 19.12 | cpu-small | 55 | 97% |
| 9 | sn124 Swarm | 66.9 | 310 | 984 | rtx4090* | 25 | 11% |
| 10 | sn38 ChronoLLM | 66.8 | 126 | 1,112 | cpu-small | 10 | 52% |
| 11 | sn111 Claims | 66.6 | 285 | 2,945 | rtx4090* | 5 | 73% |
| 12 | sn14 Cacheon | 65.8 | 213 | 2,209 | rtx4090* | 16 | 29% |
| 13 | sn62 Ridges | 62.4 | 75.30 | 2,709 | rtx4090* | 19 | 30% |
| 14 | sn28 SayGM | 62.2 | 74.27 | 1,605 | rtx4090* | 71 | 13% |
| 15 | sn74 Gittensor | 60 | 39.95 | 299 | rtx4090* | 13 | 61% |
| 16 | sn51 lium.io | 59.7 | 44.15 | 1,629 | rtx4090* | 69 | 81% |
| 17 | sn81 Reliquary | 59 | 27.39 | 97.95 | rtx4090* | 23 | 84% |
| 18 | sn61 RedTeam | 58.8 | 25.38 | 871 | rtx4090* | 128 | 9% |
| 19 | sn80 OpenRoboto | 57.1 | 555 | 1,963 | rtx4090* | 5 | 43% |
| 20 | sn9 iota | 56.1 | 12,251 | 12,251 = | rtx4090* | 3 | 56% |

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
| concentrated (30–60%) | 26 |
| dominated (60–90%) | 19 |
| captured (>90%) | 24 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 98 |
| README keywords (GUESS) | 10 |
| min_compute.yml (curated) | 10 |
| code-submission (validator runs it) | 9 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-09-21T19:40 | sn10 | BURN_DROP | sn10 burn fell 1.000 -> 0.810 - miners can earn again |
| 2026-09-21T19:40 | sn10 | SCORING_COMMIT | sn10 commit touches scoring: fix(bench): validate both baselines befor |
| 2026-09-21T19:40 | sn14 | SCORING_COMMIT | sn14 commit touches scoring: Merge pull request #120 from latent-to/re |
| 2026-09-21T19:40 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: fix(validator): fail fast on invalid pref |
| 2026-09-21T19:40 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: verify: the grouping recheck narrows to t |
| 2026-09-21T19:40 | sn26 | SCORING_COMMIT | sn26 commit touches scoring: feat: report model evaluations in the tra |
| 2026-09-21T19:40 | sn26 | README_TASK_DIFF | sn26 README task/scoring sections changed |
| 2026-09-21T19:40 | sn28 | RELEASE | sn28 released v0.4.20 |
| 2026-09-21T19:40 | sn28 | SCORING_COMMIT | sn28 commit touches scoring: chore(release): promote gm-miner 0.4.20 |
| 2026-09-21T19:40 | sn33 | SCORING_COMMIT | sn33 commit touches scoring: Merge pull request #137 from afterpartyai |
| 2026-09-21T19:40 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: docs: use validators consistently in setu |
| 2026-09-21T19:40 | sn71 | README_TASK_DIFF | sn71 README task/scoring sections changed |
| 2026-09-21T19:40 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Validate continuous intake status and rea |
| 2026-09-21T19:40 | sn102 | RELEASE | sn102 released v0.6.3 |
| 2026-09-21T19:40 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: eval_client/validator: upstream 5xx / tr |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

