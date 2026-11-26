# Subnet watch — dashboard

_snapshot 2026-11-26T15:34:13Z · block 9591932 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 56 of 129

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 129 | everything on chain |
| Pays miners at all | 105 | `miner_burn` < 0.99 |
| Ranked | 105 | passed every gate |
| **Positive margin** | **56** | income beats machine cost |
| New events this window | 11 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 73 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 7 | `███` |
| 0.8–0.99 | 10 | `████` |
| ≥0.99 dead | 24 | `█████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn42 CADmind | 80.8 | 192 | 192 = | cpu-small | 5 | 20% |
| 2 | sn120 Affine | 74.9 | 3,178 | 3,178 = | rtx4090* | 6 | 17% |
| 3 | sn3 Teutonic | 72.9 | 1,757 | 3,522 | rtx4090* | 4 | 40% |
| 4 | sn53 engy | 72.1 | 1,402 | 3,315 | rtx4090 | 8 | 49% |
| 5 | sn121 sundae_bar | 71.3 | 426 | 681 | cpu-small | 3 | 50% |
| 6 | sn67 Harnyx | 62.8 | 1.07 | 493 | cpu-small | 103 | 39% |
| 7 | sn66 conjectures | 62 | 67.28 | 832 | rtx4090* | 4 | 81% |
| 8 | sn28 SayGM | 61.7 | 65.40 | 1,415 | rtx4090* | 108 | 19% |
| 9 | sn54 Yanez | 61.5 | 2,029 | 2,029 = | a4000 | 2 | 96% |
| 10 | sn58 Attune | 61.1 | 51.78 | 1,479 | rtx4090* | 57 | 30% |
| 11 | sn111 Claims | 59.7 | 34.62 | 142 | rtx4090* | 4 | 88% |
| 12 | sn56 Gradients | 58.6 | 163 | 3,058 | a100-80 | 7 | 43% |
| 13 | sn127 Zils | 58.4 | 22.58 | 43.13 | rtx4090 | 6 | 88% |
| 14 | sn25 UR | 57.8 | 18.77 | 27.77 | rtx4090* | 10 | 45% |
| 15 | sn34 Yugos | 57.4 | 612 | 5,261 | rtx4090* | 3 | 85% |
| 16 | sn102 ConnitoAI | 56.7 | 482 | 482 = | rtx4090* | 4 | 25% |
| 17 | sn116 Carbon | 55 | 7,785 | 7,785 = | rtx4090* | 1 | 100% |
| 18 | sn99 Axonry | 55 | 7,726 | 7,726 = | rtx4090* | 1 | 100% |
| 19 | sn1 Apex | 54.5 | 254 | 510 | rtx4090* | 4 | 69% |
| 20 | sn38 ChronoLLM | 54.3 | 101 | 258 | cpu-small | 6 | 53% |

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
| concentrated (30–60%) | 24 |
| dominated (60–90%) | 25 |
| captured (>90%) | 28 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 98 |
| README keywords (GUESS) | 12 |
| min_compute.yml (curated) | 11 |
| code-submission (validator runs it) | 8 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-11-26T15:34 | sn14 | SCORING_COMMIT | sn14 commit touches scoring: Start the scored span at the cold-round r |
| 2026-11-26T15:34 | sn42 | RELEASE | sn42 released v0.6.27 |
| 2026-11-26T15:34 | sn42 | SCORING_COMMIT | sn42 commit touches scoring: miners: work an improvement job; the prac |
| 2026-11-26T15:34 | sn42 | README_TASK_DIFF | sn42 README task/scoring sections changed |
| 2026-11-26T15:34 | sn51 | RELEASE | sn51 released executor-v1.201 |
| 2026-11-26T15:34 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-7044 - [P4] Validation: a node is lis |
| 2026-11-26T15:34 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-11-26T15:34 | sn70 | BURN_DROP | sn70 burn fell 1.000 -> 0.500 - miners can earn again |
| 2026-11-26T15:34 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: Merge pull request #583 from reliquadotai |
| 2026-11-26T15:34 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: fix(trainer): lane B judge + merge scores |
| 2026-11-26T15:34 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: An overlay dispatch for a Challenge the  |
| 2026-11-26T05:17 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Merge miner-update-sn-feed: miner self-up |
| 2026-11-26T05:17 | sn30 | SCORING_COMMIT | sn30 commit touches scoring: feat(scoring): weight 30d EMAs by maturit |
| 2026-11-26T05:17 | sn51 | RELEASE | sn51 released executor-v1.199 |
| 2026-11-26T05:17 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-7109 - [P4] Validator stale-container |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

