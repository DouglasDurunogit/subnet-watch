# Subnet watch — dashboard

_snapshot 2026-11-18T16:38:51Z · block 9534682 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 58 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 102 | `miner_burn` < 0.99 |
| Ranked | 102 | passed every gate |
| **Positive margin** | **58** | income beats machine cost |
| New events this window | 11 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 69 | `████████████████████████████` |
| 0–0.2 | 6 | `██` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 6 | `██` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 26 | `███████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn42 CADmind | 81.5 | 232 | 232 = | cpu-small | 5 | 20% |
| 2 | sn58 Attune | 68.1 | 419 | 675 | rtx4090* | 5 | 70% |
| 3 | sn56 Gradients | 67.7 | 376 | 3,856 | rtx4090* | 7 | 49% |
| 4 | sn14 Cacheon | 66.6 | 267 | 2,481 | rtx4090* | 5 | 50% |
| 5 | sn67 Harnyx | 66.5 | 4.42 | 4.42 = | cpu-small | 228 | 12% |
| 6 | sn124 Swarm | 65.5 | 202 | 847 | rtx4090* | 11 | 30% |
| 7 | sn53 engy | 64.8 | 157 | 12,756 | rtx4090 | 20 | 61% |
| 8 | sn15 ORO | 64.4 | 5.66 | 8,789 | cpu-small | 75 | 95% |
| 9 | sn120 Affine | 61.7 | 2,197 | 2,197 = | rtx4090* | 10 | 10% |
| 10 | sn38 ChronoLLM | 61.6 | 32.66 | 294 | cpu-small | 10 | 52% |
| 11 | sn60 Bitsec.ai | 60.5 | 593 | 593 = | cpu-small | 3 | 50% |
| 12 | sn111 Claims | 60.1 | 39.31 | 158 | rtx4090* | 4 | 88% |
| 13 | sn62 Ridges | 60.1 | 38.33 | 471 | rtx4090* | 45 | 12% |
| 14 | sn97 Ingot | 59.6 | 1,149 | 1,149 = | rtx4090* | 5 | 20% |
| 15 | sn4 Targon | 57.5 | 8,838 | 18,978 | rtx4090* | 5 | 62% |
| 16 | sn102 ConnitoAI | 57.5 | 622 | 626 | rtx4090* | 4 | 25% |
| 17 | sn5 Hone | 56.9 | 17.80 | 39.60 | rtx4090* | 243 | 1% |
| 18 | sn66 conjectures | 56.4 | 11.81 | 982 | rtx4090* | 8 | 81% |
| 19 | sn46 Instant | 55.5 | 132 | 153 | cpu-small | 9 | 21% |
| 20 | sn107 Minos | 55.1 | 155 | 12,079 | cpu-small | 20 | 79% |

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
| concentrated (30–60%) | 20 |
| dominated (60–90%) | 25 |
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
| 2026-11-18T16:39 | sn12 | RELEASE | sn12 released validator-staging-2026-11-18-44297690409-632-1: feat: mi |
| 2026-11-18T16:39 | sn12 | SCORING_COMMIT | sn12 commit touches scoring: feat: log validator ignored commitments ( |
| 2026-11-18T16:39 | sn25 | RELEASE | sn25 released v2026.11.18-1101975730 |
| 2026-11-18T16:39 | sn42 | RELEASE | sn42 released v0.6.22 |
| 2026-11-18T16:39 | sn42 | SCORING_COMMIT | sn42 commit touches scoring: v0.6.22: the reference miner checks watt  |
| 2026-11-18T16:39 | sn51 | RELEASE | sn51 released executor-v1.190 |
| 2026-11-18T16:39 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-6546 - [P2] Validator: an unread pod  |
| 2026-11-18T16:39 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-11-18T16:39 | sn90 | RELEASE | sn90 released v1.4.3 |
| 2026-11-18T16:39 | sn90 | SCORING_COMMIT | sn90 commit touches scoring: fix(subnet): score only worker nodes |
| 2026-11-18T16:39 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: Score audited Bronze source faults witho |
| 2026-11-18T07:14 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-6566 - [P0] Validator writes the need |
| 2026-11-18T07:14 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-11-18T07:14 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: fix(rl): a pod's link reaches its task's  |
| 2026-11-18T07:14 | sn127 | RELEASE | sn127 released Release b5a248c |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

