# Subnet watch — dashboard

_snapshot 2026-11-13T07:23:00Z · block 9495903 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 62 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 101 | `miner_burn` < 0.99 |
| Ranked | 101 | passed every gate |
| **Positive margin** | **62** | income beats machine cost |
| New events this window | 5 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 69 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 7 | `███` |
| 0.4–0.6 | 2 | `█` |
| 0.6–0.8 | 11 | `████` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 27 | `███████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn42 CADmind | 82.2 | 274 | 274 = | cpu-small | 5 | 20% |
| 2 | sn120 Affine | 74.2 | 2,574 | 2,574 = | rtx4090* | 10 | 10% |
| 3 | sn3 Teutonic | 74 | 2,433 | 4,873 | rtx4090* | 4 | 40% |
| 4 | sn97 Ingot | 72.1 | 1,366 | 1,366 = | rtx4090* | 5 | 20% |
| 5 | sn34 Yugos | 69.9 | 735 | 6,310 | rtx4090* | 3 | 85% |
| 6 | sn41 Almanac | 69.4 | 11.53 | 139 | cpu-small | 158 | 2% |
| 7 | sn56 Gradients | 69.1 | 574 | 4,373 | rtx4090* | 6 | 50% |
| 8 | sn67 Harnyx | 68.3 | 7.64 | 131 | cpu-small | 133 | 8% |
| 9 | sn15 ORO | 66 | 6.56 | 10,478 | cpu-small | 71 | 95% |
| 10 | sn124 Swarm | 65.7 | 215 | 899 | rtx4090* | 10 | 31% |
| 11 | sn53 engy | 65 | 168 | 6,699 | rtx4090 | 23 | 40% |
| 12 | sn38 ChronoLLM | 63.5 | 51.90 | 357 | cpu-small | 9 | 52% |
| 13 | sn14 Cacheon | 62.5 | 78.01 | 199 | rtx4090* | 4 | 95% |
| 14 | sn121 sundae_bar | 61.6 | 819 | 819 = | cpu-small | 2 | 60% |
| 15 | sn111 Claims | 60.7 | 46.55 | 184 | rtx4090* | 4 | 88% |
| 16 | sn62 Ridges | 60.1 | 37.84 | 671 | rtx4090* | 44 | 15% |
| 17 | sn117 everyframe.studi | 59.6 | 33.03 | 348 | rtx4090* | 38 | 18% |
| 18 | sn60 Bitsec.ai | 59.2 | 402 | 620 | cpu-small | 3 | 50% |
| 19 | sn4 Targon | 58.2 | 10,930 | 20,816 | rtx4090* | 5 | 60% |
| 20 | sn58 Attune | 57.2 | 577 | 929 | rtx4090* | 5 | 70% |

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
| concentrated (30–60%) | 19 |
| dominated (60–90%) | 27 |
| captured (>90%) | 26 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 97 |
| README keywords (GUESS) | 12 |
| min_compute.yml (curated) | 10 |
| code-submission (validator runs it) | 8 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-11-13T07:23 | sn45 | SCORING_COMMIT | sn45 commit touches scoring: AlphaRidge 4.1.1: validator stability |
| 2026-11-13T07:23 | sn48 | README_TASK_DIFF | sn48 README task/scoring sections changed |
| 2026-11-13T07:23 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-6325 - [P0] Validator FIXED_RATIO fol |
| 2026-11-13T07:23 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: fix(admin): keep a job's counts for good  |
| 2026-11-13T07:23 | sn127 | RELEASE | sn127 released Release 3e2660e |
| 2026-11-13T00:38 | sn3 | SCORING_COMMIT | sn3 commit touches scoring: V3 validator preflight and weight publicat |
| 2026-11-13T00:38 | sn42 | BURN_DROP | sn42 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-11-13T00:38 | sn42 | RELEASE | sn42 released v0.6.6 |
| 2026-11-13T00:38 | sn45 | SCORING_COMMIT | sn45 commit touches scoring: AlphaRidge 4.1.0: improved breakthrough e |
| 2026-11-13T00:38 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: Validator: log dockerd's reason when dock |
| 2026-11-13T00:38 | sn89 | SCORING_COMMIT | sn89 commit touches scoring: Agent books: outside validators pay the a |
| 2026-11-13T00:38 | sn94 | SCORING_COMMIT | sn94 commit touches scoring: Fetch archived hotel bindings when verify |
| 2026-11-13T00:38 | sn127 | RELEASE | sn127 released Release ba66e7b |
| 2026-11-13T00:38 | sn127 | SCORING_COMMIT | sn127 commit touches scoring: Docs: what the soup round bank holds and |
| 2026-11-12T19:10 | sn34 | SCORING_COMMIT | sn34 commit touches scoring: Merge pull request #54 from BitMind-AI/fi |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

