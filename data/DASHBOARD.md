# Subnet watch — dashboard

_snapshot 2026-11-10T12:30:49Z · block 9475842 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 60 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 101 | `miner_burn` < 0.99 |
| Ranked | 101 | passed every gate |
| **Positive margin** | **60** | income beats machine cost |
| New events this window | 4 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 70 | `████████████████████████████` |
| 0–0.2 | 6 | `██` |
| 0.2–0.4 | 6 | `██` |
| 0.4–0.6 | 6 | `██` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 27 | `███████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn120 Affine | 74.4 | 2,761 | 2,761 = | rtx4090* | 10 | 10% |
| 2 | sn3 Teutonic | 72.8 | 1,722 | 3,367 | rtx4090* | 7 | 25% |
| 3 | sn41 Almanac | 70.6 | 15.69 | 159 | cpu-small | 160 | 3% |
| 4 | sn34 Yugos | 70.1 | 781 | 6,697 | rtx4090* | 3 | 85% |
| 5 | sn58 Attune | 69.4 | 634 | 1,019 | rtx4090* | 5 | 70% |
| 6 | sn1 Apex | 69.1 | 573 | 736 | rtx4090* | 4 | 57% |
| 7 | sn67 Harnyx | 68.7 | 8.22 | 140 | cpu-small | 137 | 8% |
| 8 | sn56 Gradients | 68.3 | 445 | 4,698 | rtx4090* | 7 | 51% |
| 9 | sn103 Terza Inference | 67.7 | 377 | 588 | rtx4090* | 5 | 42% |
| 10 | sn46 Instant | 67.4 | 134 | 173 | cpu-small | 9 | 47% |
| 11 | sn82 Noah | 66.3 | 291 | 379 | rtx4090* | 65 | 2% |
| 12 | sn53 engy | 65.2 | 178 | 2,752 | rtx4090 | 31 | 21% |
| 13 | sn15 ORO | 65.2 | 6.51 | 14.01 | cpu-small | 72 | 96% |
| 14 | sn14 Cacheon | 64.5 | 142 | 5,718 | rtx4090* | 4 | 95% |
| 15 | sn121 sundae_bar | 61.8 | 858 | 858 = | cpu-small | 2 | 60% |
| 16 | sn55 NIOME | 60.5 | 42.92 | 375 | rtx4090* | 11 | 30% |
| 17 | sn4 Targon | 58.4 | 11,585 | 23,324 | rtx4090* | 5 | 61% |
| 18 | sn111 Claims | 58.4 | 23.69 | 2,386 | rtx4090* | 6 | 90% |
| 19 | sn66 conjectures | 58.2 | 21.21 | 139 | rtx4090* | 7 | 80% |
| 20 | sn5 Hone | 57.7 | 22.73 | 48.72 | rtx4090* | 241 | 1% |

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
| wide (<30%) | 30 |
| concentrated (30–60%) | 17 |
| dominated (60–90%) | 28 |
| captured (>90%) | 23 |

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
| 2026-11-10T12:31 | sn51 | RELEASE | sn51 released miner-v1.012 |
| 2026-11-10T12:31 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: Validator: judge a rented pod's ownership |
| 2026-11-10T12:31 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-11-10T12:31 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Require visible source excerpts for citat |
| 2026-11-10T03:50 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: docs: tag oroagents.com links in the mine |
| 2026-11-10T03:50 | sn36 | SCORING_COMMIT | sn36 commit touches scoring: Validator: GPUs with a UUID nvidia-smi wo |
| 2026-11-10T03:50 | sn51 | RELEASE | sn51 released executor-v1.173 |
| 2026-11-10T03:50 | sn66 | RELEASE | sn66 released v2026.11.10 |
| 2026-11-10T03:50 | sn70 | RELEASE | sn70 released build-v2026.11.10: Merge pull request #185 from fugal-ai |
| 2026-11-10T03:50 | sn70 | SCORING_COMMIT | sn70 commit touches scoring: validator: only a head hash can count as  |
| 2026-11-10T03:50 | sn70 | README_TASK_DIFF | sn70 README task/scoring sections changed |
| 2026-11-10T03:50 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Keep historical publication proofs on the |
| 2026-11-10T03:50 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: fix(validator): keep private-eval checkpo |
| 2026-11-10T03:50 | sn127 | SCORING_COMMIT | sn127 commit touches scoring: Merge pull request #229 from ooo-hq/docs |
| 2026-11-10T03:50 | sn127 | README_TASK_DIFF | sn127 README task/scoring sections changed |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

