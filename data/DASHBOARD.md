# Subnet watch — dashboard

_snapshot 2026-11-09T11:21:47Z · block 9468297 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 60 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 99 | `miner_burn` < 0.99 |
| Ranked | 99 | passed every gate |
| **Positive margin** | **60** | income beats machine cost |
| New events this window | 11 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 68 | `████████████████████████████` |
| 0–0.2 | 8 | `███` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 7 | `███` |
| 0.6–0.8 | 8 | `███` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 29 | `████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn120 Affine | 74.4 | 2,742 | 2,742 = | rtx4090* | 10 | 10% |
| 2 | sn3 Teutonic | 72.8 | 1,709 | 3,427 | rtx4090* | 7 | 25% |
| 3 | sn14 Cacheon | 72.8 | 1,709 | 4,106 | rtx4090* | 3 | 68% |
| 4 | sn56 Gradients | 70.6 | 882 | 4,779 | rtx4090* | 5 | 52% |
| 5 | sn41 Almanac | 70.4 | 14.70 | 159 | cpu-small | 170 | 2% |
| 6 | sn1 Apex | 69.6 | 656 | 712 | rtx4090* | 4 | 56% |
| 7 | sn36 Weir | 69.2 | 584 | 654 | rtx4090* | 8 | 24% |
| 8 | sn58 Attune | 68.9 | 540 | 869 | rtx4090* | 5 | 70% |
| 9 | sn46 Instant | 67.8 | 148 | 181 | cpu-small | 9 | 46% |
| 10 | sn103 Terza Inference | 67.5 | 354 | 354 = | rtx4090* | 5 | 45% |
| 11 | sn82 Noah | 66.7 | 312 | 400 | rtx4090* | 65 | 2% |
| 12 | sn15 ORO | 66 | 6.18 | 13.52 | cpu-small | 84 | 95% |
| 13 | sn53 engy | 65.2 | 178 | 2,758 | rtx4090 | 31 | 21% |
| 14 | sn67 Harnyx | 64.5 | 2.79 | 196 | cpu-small | 149 | 11% |
| 15 | sn38 ChronoLLM | 62.5 | 41.75 | 374 | cpu-small | 10 | 52% |
| 16 | sn60 Bitsec.ai | 61.1 | 704 | 704 = | cpu-small | 3 | 50% |
| 17 | sn66 conjectures | 61.1 | 50.68 | 139 | rtx4090* | 5 | 80% |
| 18 | sn55 NIOME | 60.7 | 45.21 | 393 | rtx4090* | 11 | 30% |
| 19 | sn111 Claims | 58.5 | 23.91 | 2,401 | rtx4090* | 6 | 90% |
| 20 | sn102 ConnitoAI | 58 | 728 | 728 | rtx4090* | 4 | 25% |

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
| concentrated (30–60%) | 19 |
| dominated (60–90%) | 26 |
| captured (>90%) | 24 |

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
| 2026-11-09T11:22 | sn15 | RELEASE | sn15 released v3.0.8: feat(validator): report each episode's end reaso |
| 2026-11-09T11:22 | sn15 | README_TASK_DIFF | sn15 README task/scoring sections changed |
| 2026-11-09T11:22 | sn51 | RELEASE | sn51 released watchtower-v1.2.1: DAH-5942 - docker_build.sh: optional  |
| 2026-11-09T11:22 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-5917 - [P2] Miner releases: create th |
| 2026-11-09T11:22 | sn53 | SCORING_COMMIT | sn53 commit touches scoring: tee_miner: read KV load from sglang /v1/l |
| 2026-11-09T11:22 | sn66 | RELEASE | sn66 released v2026.11.09 |
| 2026-11-09T11:22 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-11-09T11:22 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Allow the fixed reward clock failure labe |
| 2026-11-09T11:22 | sn97 | SCORING_COMMIT | sn97 commit touches scoring: fix(miner): Fixed ty format |
| 2026-11-09T11:22 | sn108 | SCORING_COMMIT | sn108 commit touches scoring: Neuron 1.0.5: a validator updated mid-ev |
| 2026-11-09T11:22 | sn127 | SCORING_COMMIT | sn127 commit touches scoring: Merge pull request #222 from ooo-hq/mine |
| 2026-11-09T02:52 | sn34 | SCORING_COMMIT | sn34 commit touches scoring: Remove grader versions from prepared task |
| 2026-11-09T02:52 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge pull request #1136 from leadpoet/fi |
| 2026-11-09T02:52 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Door chain reader: an uncollected SDK se |
| 2026-11-08T23:11 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: feat(validator): report each episode's en |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

