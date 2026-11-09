# Subnet watch — dashboard

_snapshot 2026-11-09T21:32:31Z · block 9471350 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 59 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 102 | `miner_burn` < 0.99 |
| Ranked | 102 | passed every gate |
| **Positive margin** | **59** | income beats machine cost |
| New events this window | 13 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 69 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 7 | `███` |
| 0.6–0.8 | 8 | `███` |
| 0.8–0.99 | 6 | `██` |
| ≥0.99 dead | 26 | `███████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn120 Affine | 74.5 | 2,802 | 2,802 = | rtx4090* | 10 | 10% |
| 2 | sn3 Teutonic | 72.8 | 1,734 | 3,477 | rtx4090* | 7 | 25% |
| 3 | sn41 Almanac | 70.9 | 16.50 | 171 | cpu-small | 167 | 2% |
| 4 | sn1 Apex | 69.5 | 634 | 765 | rtx4090* | 4 | 54% |
| 5 | sn58 Attune | 69.3 | 610 | 981 | rtx4090* | 5 | 70% |
| 6 | sn103 Terza Inference | 67.6 | 358 | 577 | rtx4090* | 5 | 37% |
| 7 | sn46 Instant | 67.6 | 143 | 180 | cpu-small | 9 | 48% |
| 8 | sn82 Noah | 66.1 | 302 | 387 | rtx4090* | 65 | 2% |
| 9 | sn15 ORO | 65.9 | 6.33 | 13.82 | cpu-small | 84 | 95% |
| 10 | sn53 engy | 65.2 | 178 | 2,757 | rtx4090 | 31 | 21% |
| 11 | sn67 Harnyx | 64.6 | 2.84 | 199 | cpu-small | 154 | 11% |
| 12 | sn121 sundae_bar | 61.4 | 774 | 774 = | cpu-small | 2 | 65% |
| 13 | sn60 Bitsec.ai | 60.9 | 663 | 663 = | cpu-small | 3 | 50% |
| 14 | sn55 NIOME | 60.6 | 44.17 | 385 | rtx4090* | 11 | 30% |
| 15 | sn4 Targon | 58.6 | 12,293 | 24,148 | rtx4090* | 5 | 61% |
| 16 | sn111 Claims | 58.5 | 24.56 | 2,450 | rtx4090* | 6 | 90% |
| 17 | sn66 conjectures | 58.3 | 21.76 | 142 | rtx4090* | 6 | 80% |
| 18 | sn102 ConnitoAI | 58.1 | 735 | 736 | rtx4090* | 4 | 25% |
| 19 | sn5 Hone | 57.8 | 23.21 | 49.46 | rtx4090* | 241 | 1% |
| 20 | sn70 Fugal | 57 | 16.38 | 37.98 | rtx4090* | 236 | 1% |

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
| wide (<30%) | 29 |
| concentrated (30–60%) | 20 |
| dominated (60–90%) | 24 |
| captured (>90%) | 27 |

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
| 2026-11-09T21:33 | sn28 | RELEASE | sn28 released v0.5.24 |
| 2026-11-09T21:33 | sn41 | SCORING_COMMIT | sn41 commit touches scoring: Using the validator gamma api call for th |
| 2026-11-09T21:33 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-6008 - [P0] validator: accept GB200 a |
| 2026-11-09T21:33 | sn56 | SCORING_COMMIT | sn56 commit touches scoring: Route multi-GPU tasks to SXM/NVLink train |
| 2026-11-09T21:33 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-11-09T21:33 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge pull request #1160 from leadpoet/fi |
| 2026-11-09T21:33 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Kit page Motor: Carbon Validator-Motor m |
| 2026-11-09T21:33 | sn117 | RELEASE | sn117 released everycli v1.0.0 |
| 2026-11-09T21:33 | sn117 | SCORING_COMMIT | sn117 commit touches scoring: test: verify Phala UI errors and await r |
| 2026-11-09T21:33 | sn117 | README_TASK_DIFF | sn117 README task/scoring sections changed |
| 2026-11-09T21:33 | sn121 | BURN_DROP | sn121 burn fell 1.000 -> 0.646 - miners can earn again |
| 2026-11-09T21:33 | sn127 | BURN_DROP | sn127 burn fell 1.000 -> 0.960 - miners can earn again |
| 2026-11-09T21:33 | sn127 | SCORING_COMMIT | sn127 commit touches scoring: Merge pull request #225 from ooo-hq/mine |
| 2026-11-09T11:22 | sn15 | RELEASE | sn15 released v3.0.8: feat(validator): report each episode's end reaso |
| 2026-11-09T11:22 | sn15 | README_TASK_DIFF | sn15 README task/scoring sections changed |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

