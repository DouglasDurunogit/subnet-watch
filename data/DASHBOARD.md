# Subnet watch — dashboard

_snapshot 2026-11-05T11:38:10Z · block 9439583 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 62 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 102 | `miner_burn` < 0.99 |
| Ranked | 102 | passed every gate |
| **Positive margin** | **62** | income beats machine cost |
| New events this window | 8 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 68 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 8 | `███` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 26 | `███████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn120 Affine | 74.6 | 2,967 | 2,967 = | rtx4090* | 10 | 10% |
| 2 | sn3 Teutonic | 73.2 | 1,939 | 3,886 | rtx4090* | 7 | 25% |
| 3 | sn97 Ingot | 72.5 | 1,580 | 1,580 = | rtx4090* | 5 | 20% |
| 4 | sn58 Attune | 68.6 | 497 | 800 | rtx4090* | 5 | 70% |
| 5 | sn56 Gradients | 68.5 | 478 | 5,141 | rtx4090* | 7 | 51% |
| 6 | sn103 Terza Inference | 68.2 | 434 | 1,308 | rtx4090* | 5 | 41% |
| 7 | sn41 Almanac | 67.5 | 7.59 | 130 | cpu-small | 176 | 7% |
| 8 | sn1 Apex | 67.4 | 342 | 819 | rtx4090* | 4 | 70% |
| 9 | sn102 ConnitoAI | 67.3 | 336 | 692 | rtx4090* | 9 | 25% |
| 10 | sn82 Noah | 66.5 | 387 | 454 | rtx4090* | 64 | 2% |
| 11 | sn107 Minos | 66.2 | 183 | 15,586 | cpu-small | 20 | 80% |
| 12 | sn70 Fugal | 65.6 | 198 | 492 | rtx4090* | 37 | 7% |
| 13 | sn15 ORO | 65.6 | 6.59 | 12,219 | cpu-small | 69 | 96% |
| 14 | sn53 engy | 65.4 | 188 | 3,091 | rtx4090 | 31 | 21% |
| 15 | sn67 Harnyx | 64.4 | 3.11 | 615 | cpu-small | 131 | 32% |
| 16 | sn38 ChronoLLM | 63.4 | 52.29 | 466 | cpu-small | 10 | 52% |
| 17 | sn66 conjectures | 63 | 91.38 | 191 | rtx4090* | 4 | 80% |
| 18 | sn124 Swarm | 62.9 | 99.03 | 1,661 | rtx4090* | 16 | 28% |
| 19 | sn62 Ridges | 61.9 | 65.25 | 1,215 | rtx4090* | 37 | 22% |
| 20 | sn55 NIOME | 61.2 | 53.20 | 453 | rtx4090* | 11 | 30% |

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
| dominated (60–90%) | 28 |
| captured (>90%) | 25 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 99 |
| README keywords (GUESS) | 11 |
| min_compute.yml (curated) | 9 |
| code-submission (validator runs it) | 8 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-11-05T11:38 | sn51 | RELEASE | sn51 released executor-v1.171 |
| 2026-11-05T11:38 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-5664 - [P0] Validator: reclaim a kill |
| 2026-11-05T11:38 | sn51 | README_TASK_DIFF | sn51 README task/scoring sections changed |
| 2026-11-05T11:38 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-11-05T11:38 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge pull request #1036 from leadpoet/op |
| 2026-11-05T11:38 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: fix(audit): refuse forced-draw drift with |
| 2026-11-05T11:38 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: A2: keep attempt 1's evaluation files so |
| 2026-11-05T11:38 | sn127 | BURN_DROP | sn127 burn fell 0.990 -> 0.872 - miners can earn again |
| 2026-11-05T03:46 | sn27 | RELEASE | sn27 released archive/worktrees-2026-11-04 |
| 2026-11-05T03:46 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Recover only the infrastructure-damaged N |
| 2026-11-05T03:46 | sn82 | SCORING_COMMIT | sn82 commit touches scoring: Merge pull request #6: Improve validator  |
| 2026-11-05T03:46 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Owner manifest migration: encode the Val |
| 2026-11-05T03:46 | sn126 | BURN_DROP | sn126 burn fell 1.000 -> 0.955 - miners can earn again |
| 2026-11-04T23:36 | sn12 | RELEASE | sn12 released sdk-v0.0.20: feat: local executor and local bind mount v |
| 2026-11-04T23:36 | sn58 | SCORING_COMMIT | sn58 commit touches scoring: feat(validator): only a permitted Hub acc |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

