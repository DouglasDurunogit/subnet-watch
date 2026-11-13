# Subnet watch — dashboard

_snapshot 2026-11-13T00:37:39Z · block 9493876 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 63 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 102 | `miner_burn` < 0.99 |
| Ranked | 102 | passed every gate |
| **Positive margin** | **63** | income beats machine cost |
| New events this window | 9 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 69 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 6 | `██` |
| 0.4–0.6 | 2 | `█` |
| 0.6–0.8 | 10 | `████` |
| 0.8–0.99 | 8 | `███` |
| ≥0.99 dead | 26 | `███████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn42 CADmind | 82.4 | 287 | 287 = | cpu-small | 5 | 20% |
| 2 | sn120 Affine | 74.2 | 2,577 | 2,577 = | rtx4090* | 10 | 10% |
| 3 | sn3 Teutonic | 72.4 | 1,525 | 3,058 | rtx4090* | 7 | 25% |
| 4 | sn97 Ingot | 72.1 | 1,370 | 1,370 = | rtx4090* | 5 | 20% |
| 5 | sn34 Yugos | 69.9 | 736 | 6,321 | rtx4090* | 3 | 85% |
| 6 | sn41 Almanac | 69.4 | 11.71 | 162 | cpu-small | 157 | 3% |
| 7 | sn56 Gradients | 69.1 | 573 | 4,413 | rtx4090* | 6 | 50% |
| 8 | sn67 Harnyx | 68.4 | 7.67 | 131 | cpu-small | 132 | 8% |
| 9 | sn15 ORO | 66.8 | 7.13 | 10,493 | cpu-small | 77 | 95% |
| 10 | sn124 Swarm | 66.3 | 254 | 1,759 | rtx4090* | 10 | 31% |
| 11 | sn53 engy | 64.9 | 163 | 6,727 | rtx4090 | 23 | 40% |
| 12 | sn38 ChronoLLM | 63.5 | 52.03 | 358 | cpu-small | 9 | 52% |
| 13 | sn14 Cacheon | 62.5 | 78.08 | 199 | rtx4090* | 4 | 95% |
| 14 | sn127 Zils | 62.4 | 75.61 | 75.61 = | rtx4090* | 4 | 88% |
| 15 | sn121 sundae_bar | 61.6 | 821 | 821 = | cpu-small | 2 | 60% |
| 16 | sn111 Claims | 60.8 | 47.33 | 186 | rtx4090* | 4 | 88% |
| 17 | sn62 Ridges | 60.2 | 39.24 | 831 | rtx4090* | 43 | 18% |
| 18 | sn60 Bitsec.ai | 59.3 | 403 | 622 | cpu-small | 3 | 50% |
| 19 | sn117 everyframe.studi | 58.4 | 23.30 | 202 | rtx4090* | 33 | 41% |
| 20 | sn4 Targon | 58.2 | 10,958 | 20,895 | rtx4090* | 5 | 60% |

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
| concentrated (30–60%) | 21 |
| dominated (60–90%) | 28 |
| captured (>90%) | 25 |

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
| 2026-11-12T19:10 | sn36 | SCORING_COMMIT | sn36 commit touches scoring: Publish miner agent and simplify connecti |
| 2026-11-12T19:10 | sn51 | RELEASE | sn51 released executor-v1.181 |
| 2026-11-12T19:10 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-4889 - [P0] validator: a foreign GPU  |
| 2026-11-12T19:10 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-11-12T19:10 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: docs: runner keys do not expire; to chang |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

