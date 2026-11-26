# Subnet watch — dashboard

_snapshot 2026-11-26T05:17:10Z · block 9588847 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 54 of 129

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 129 | everything on chain |
| Pays miners at all | 103 | `miner_burn` < 0.99 |
| Ranked | 103 | passed every gate |
| **Positive margin** | **54** | income beats machine cost |
| New events this window | 10 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 73 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 7 | `███` |
| 0.8–0.99 | 9 | `███` |
| ≥0.99 dead | 26 | `██████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn42 CADmind | 81.1 | 207 | 207 = | cpu-small | 5 | 20% |
| 2 | sn120 Affine | 74.4 | 2,781 | 2,781 = | rtx4090* | 7 | 14% |
| 3 | sn3 Teutonic | 72.9 | 1,791 | 3,590 | rtx4090* | 4 | 40% |
| 4 | sn121 sundae_bar | 71.4 | 432 | 688 | cpu-small | 3 | 51% |
| 5 | sn53 engy | 69.5 | 642 | 3,266 | rtx4090 | 8 | 49% |
| 6 | sn67 Harnyx | 62.9 | 1.11 | 502 | cpu-small | 103 | 39% |
| 7 | sn66 conjectures | 61.9 | 65.78 | 855 | rtx4090* | 4 | 81% |
| 8 | sn58 Attune | 61.1 | 53.25 | 1,516 | rtx4090* | 57 | 30% |
| 9 | sn111 Claims | 59.8 | 35.69 | 145 | rtx4090* | 4 | 88% |
| 10 | sn56 Gradients | 58.6 | 167 | 3,120 | a100-80 | 7 | 43% |
| 11 | sn127 Zils | 58.6 | 23.64 | 58.17 | rtx4090 | 6 | 85% |
| 12 | sn34 Yugos | 57.5 | 623 | 5,358 | rtx4090* | 3 | 85% |
| 13 | sn102 ConnitoAI | 56.7 | 487 | 521 | rtx4090* | 4 | 26% |
| 14 | sn28 SayGM | 55.2 | 10.91 | 2,834 | rtx4090* | 108 | 27% |
| 15 | sn116 Carbon | 55.1 | 8,018 | 8,018 = | rtx4090* | 1 | 100% |
| 16 | sn99 Axonry | 54.8 | 7,096 | 7,096 = | rtx4090* | 1 | 100% |
| 17 | sn1 Apex | 54.7 | 272 | 545 | rtx4090* | 4 | 67% |
| 18 | sn117 everyframe.studi | 54.5 | 7.13 | 1,150 | rtx4090* | 31 | 48% |
| 19 | sn38 ChronoLLM | 54.3 | 103 | 263 | cpu-small | 6 | 53% |
| 20 | sn46 Instant | 53.8 | 79.66 | 86.24 | cpu-small | 15 | 15% |

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
| concentrated (30–60%) | 23 |
| dominated (60–90%) | 24 |
| captured (>90%) | 27 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 99 |
| README keywords (GUESS) | 12 |
| min_compute.yml (curated) | 10 |
| code-submission (validator runs it) | 8 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-11-26T05:17 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Merge miner-update-sn-feed: miner self-up |
| 2026-11-26T05:17 | sn30 | SCORING_COMMIT | sn30 commit touches scoring: feat(scoring): weight 30d EMAs by maturit |
| 2026-11-26T05:17 | sn51 | RELEASE | sn51 released executor-v1.199 |
| 2026-11-26T05:17 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-7109 - [P4] Validator stale-container |
| 2026-11-26T05:17 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-11-26T05:17 | sn70 | SCORING_COMMIT | sn70 commit touches scoring: Merge pull request #218 from fugal-ai/ops |
| 2026-11-26T05:17 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge pull request #1378 from leadpoet/fe |
| 2026-11-26T05:17 | sn82 | SCORING_COMMIT | sn82 commit touches scoring: Use live runtime metadata for miner repor |
| 2026-11-26T05:17 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: feat(pool): pool_d takes lane A's selecti |
| 2026-11-26T05:17 | sn129 | NEW_SUBNET | NEW SUBNET sn129 "va" first seen |
| 2026-11-25T23:12 | sn39 | SCORING_COMMIT | sn39 commit touches scoring: state that spot fills count for the volum |
| 2026-11-25T23:12 | sn40 | BURN_DROP | sn40 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-11-25T23:12 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-6683 - [P0] Validator backup, restore |
| 2026-11-25T23:12 | sn53 | SCORING_COMMIT | sn53 commit touches scoring: Merge pull request #69 from hanlinai/feat |
| 2026-11-25T23:12 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: Activate staged experimental scientific  |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

