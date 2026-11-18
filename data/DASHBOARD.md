# Subnet watch — dashboard

_snapshot 2026-11-18T23:09:42Z · block 9536636 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 54 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 102 | `miner_burn` < 0.99 |
| Ranked | 102 | passed every gate |
| **Positive margin** | **54** | income beats machine cost |
| New events this window | 7 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 69 | `████████████████████████████` |
| 0–0.2 | 8 | `███` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 26 | `███████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn42 CADmind | 81.5 | 232 | 232 = | cpu-small | 5 | 20% |
| 2 | sn3 Teutonic | 73.5 | 2,117 | 4,242 | rtx4090* | 4 | 40% |
| 3 | sn58 Attune | 68.1 | 423 | 681 | rtx4090* | 5 | 70% |
| 4 | sn56 Gradients | 67.7 | 378 | 3,870 | rtx4090* | 7 | 49% |
| 5 | sn67 Harnyx | 66.6 | 4.55 | 4.55 = | cpu-small | 213 | 17% |
| 6 | sn15 ORO | 66.1 | 5.68 | 8,900 | cpu-small | 76 | 95% |
| 7 | sn53 engy | 64.7 | 153 | 12,473 | rtx4090 | 20 | 61% |
| 8 | sn124 Swarm | 62.9 | 97.06 | 682 | rtx4090* | 13 | 30% |
| 9 | sn14 Cacheon | 62.7 | 83.13 | 4,138 | rtx4090* | 5 | 83% |
| 10 | sn120 Affine | 61.7 | 2,193 | 2,193 = | rtx4090* | 10 | 10% |
| 11 | sn38 ChronoLLM | 61.6 | 32.77 | 295 | cpu-small | 10 | 52% |
| 12 | sn60 Bitsec.ai | 60.5 | 582 | 582 = | cpu-small | 3 | 50% |
| 13 | sn111 Claims | 60.2 | 39.49 | 159 | rtx4090* | 4 | 88% |
| 14 | sn62 Ridges | 60.1 | 38.20 | 470 | rtx4090* | 45 | 12% |
| 15 | sn97 Ingot | 59.6 | 1,153 | 1,153 = | rtx4090* | 5 | 20% |
| 16 | sn102 ConnitoAI | 57.5 | 624 | 628 | rtx4090* | 4 | 25% |
| 17 | sn4 Targon | 57.3 | 8,309 | 20,139 | rtx4090* | 5 | 66% |
| 18 | sn5 Hone | 57.1 | 17.93 | 39.74 | rtx4090* | 242 | 1% |
| 19 | sn66 conjectures | 56.4 | 11.90 | 988 | rtx4090* | 8 | 81% |
| 20 | sn46 Instant | 55.6 | 139 | 167 | cpu-small | 9 | 18% |

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
| concentrated (30–60%) | 18 |
| dominated (60–90%) | 27 |
| captured (>90%) | 27 |

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
| 2026-11-18T23:10 | sn62 | RELEASE | sn62 released v0.3.18 |
| 2026-11-18T23:10 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Allow audited published judgment recovery |
| 2026-11-18T23:10 | sn93 | SCORING_COMMIT | sn93 commit touches scoring: feat(validator): score briefs with allowe |
| 2026-11-18T23:10 | sn99 | README_TASK_DIFF | sn99 README task/scoring sections changed |
| 2026-11-18T23:10 | sn109 | BURN_DROP | sn109 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-11-18T23:10 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Auto retry: a spent cap (3 per failure c |
| 2026-11-18T23:10 | sn124 | SCORING_COMMIT | sn124 commit touches scoring: Merge pull request #246 from swarm-subne |
| 2026-11-18T16:39 | sn12 | RELEASE | sn12 released validator-staging-2026-11-18-44297690409-632-1: feat: mi |
| 2026-11-18T16:39 | sn12 | SCORING_COMMIT | sn12 commit touches scoring: feat: log validator ignored commitments ( |
| 2026-11-18T16:39 | sn25 | RELEASE | sn25 released v2026.11.18-1101975730 |
| 2026-11-18T16:39 | sn42 | RELEASE | sn42 released v0.6.22 |
| 2026-11-18T16:39 | sn42 | SCORING_COMMIT | sn42 commit touches scoring: v0.6.22: the reference miner checks watt  |
| 2026-11-18T16:39 | sn51 | RELEASE | sn51 released executor-v1.190 |
| 2026-11-18T16:39 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-6546 - [P2] Validator: an unread pod  |
| 2026-11-18T16:39 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

