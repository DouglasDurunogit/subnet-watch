# Subnet watch — dashboard

_snapshot 2026-11-25T23:11:44Z · block 9587019 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 49 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 103 | `miner_burn` < 0.99 |
| Ranked | 103 | passed every gate |
| **Positive margin** | **49** | income beats machine cost |
| New events this window | 9 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 71 | `████████████████████████████` |
| 0–0.2 | 6 | `██` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 7 | `███` |
| 0.8–0.99 | 10 | `████` |
| ≥0.99 dead | 25 | `██████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn42 CADmind | 81 | 204 | 204 = | cpu-small | 5 | 20% |
| 2 | sn120 Affine | 74.9 | 3,190 | 3,190 = | rtx4090* | 6 | 17% |
| 3 | sn3 Teutonic | 72.9 | 1,759 | 3,526 | rtx4090* | 4 | 40% |
| 4 | sn121 sundae_bar | 71.4 | 429 | 687 | cpu-small | 3 | 50% |
| 5 | sn53 engy | 69.4 | 625 | 3,182 | rtx4090 | 8 | 49% |
| 6 | sn67 Harnyx | 63.8 | 1.60 | 471 | cpu-small | 102 | 37% |
| 7 | sn66 conjectures | 62 | 68.01 | 840 | rtx4090* | 4 | 81% |
| 8 | sn58 Attune | 61.2 | 53.51 | 1,522 | rtx4090* | 57 | 30% |
| 9 | sn111 Claims | 59.8 | 34.93 | 143 | rtx4090* | 4 | 88% |
| 10 | sn127 Zils | 59.7 | 33.94 | 57.67 | rtx4090 | 7 | 80% |
| 11 | sn56 Gradients | 58.6 | 164 | 3,064 | a100-80 | 7 | 43% |
| 12 | sn25 UR | 57.8 | 18.85 | 26.87 | rtx4090* | 10 | 45% |
| 13 | sn28 SayGM | 57.4 | 19.57 | 2,081 | rtx4090* | 105 | 30% |
| 14 | sn102 ConnitoAI | 56.6 | 478 | 512 | rtx4090* | 4 | 26% |
| 15 | sn99 Axonry | 54.9 | 7,384 | 7,384 = | rtx4090* | 1 | 100% |
| 16 | sn38 ChronoLLM | 54.3 | 102 | 258 | cpu-small | 6 | 53% |
| 17 | sn124 Swarm | 54.2 | 237 | 1,052 | rtx4090* | 10 | 28% |
| 18 | sn46 Instant | 54.1 | 88.48 | 100 | cpu-small | 13 | 15% |
| 19 | sn107 Minos | 53.4 | 106 | 9,061 | cpu-small | 20 | 80% |
| 20 | sn15 ORO | 51.7 | 5.14 | 7,694 | cpu-small | 70 | 95% |

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
| concentrated (30–60%) | 22 |
| dominated (60–90%) | 24 |
| captured (>90%) | 28 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 98 |
| README keywords (GUESS) | 12 |
| min_compute.yml (curated) | 10 |
| code-submission (validator runs it) | 8 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-11-25T23:12 | sn39 | SCORING_COMMIT | sn39 commit touches scoring: state that spot fills count for the volum |
| 2026-11-25T23:12 | sn40 | BURN_DROP | sn40 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-11-25T23:12 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-6683 - [P0] Validator backup, restore |
| 2026-11-25T23:12 | sn53 | SCORING_COMMIT | sn53 commit touches scoring: Merge pull request #69 from hanlinai/feat |
| 2026-11-25T23:12 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: Activate staged experimental scientific  |
| 2026-11-25T23:12 | sn117 | RELEASE | sn117 released everycli v1.3.3 |
| 2026-11-25T23:12 | sn121 | BURN_DROP | sn121 burn fell 1.000 -> 0.500 - miners can earn again |
| 2026-11-25T23:12 | sn121 | README_TASK_DIFF | sn121 README task/scoring sections changed |
| 2026-11-25T23:12 | sn127 | RELEASE | sn127 released Release eb41ab3 |
| 2026-11-25T14:12 | sn12 | RELEASE | sn12 released validator-staging-2026-11-25-45557483497-637-1: feat: al |
| 2026-11-25T14:12 | sn22 | SCORING_COMMIT | sn22 commit touches scoring: fix(task-api): the signed log, anchors, v |
| 2026-11-25T14:12 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Merge docs/validator-data-grant-1125: the |
| 2026-11-25T14:12 | sn26 | SCORING_COMMIT | sn26 commit touches scoring: Report: round the displayed score |
| 2026-11-25T14:12 | sn28 | RELEASE | sn28 released v0.6.1 |
| 2026-11-25T14:12 | sn40 | SCORING_COMMIT | sn40 commit touches scoring: Merge pull request #20 from RalphLabsAI/f |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

