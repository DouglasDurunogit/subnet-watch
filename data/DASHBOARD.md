# Subnet watch — dashboard

_snapshot 2026-10-16T18:46:09Z · block 9297812 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 58 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 99 | `miner_burn` < 0.99 |
| Ranked | 99 | passed every gate |
| **Positive margin** | **58** | income beats machine cost |
| New events this window | 7 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 67 | `████████████████████████████` |
| 0–0.2 | 4 | `██` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 7 | `███` |
| 0.6–0.8 | 10 | `████` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 29 | `████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn121 sundae_bar | 74.8 | 1,201 | 1,201 = | cpu-small | 2 | 60% |
| 2 | sn3 Teutonic | 74.6 | 2,961 | 2,961 = | rtx4090* | 5 | 40% |
| 3 | sn41 Almanac | 74.3 | 38.40 | 121 | cpu-small | 108 | 10% |
| 4 | sn53 engy | 69.4 | 617 | 2,564 | rtx4090 | 24 | 16% |
| 5 | sn91 cascade | 69.1 | 219 | 878 | cpu-small | 5 | 52% |
| 6 | sn67 Harnyx | 68.6 | 8.66 | 8.66 = | cpu-small | 229 | 15% |
| 7 | sn1 Apex | 68.5 | 468 | 1,106 | rtx4090* | 5 | 61% |
| 8 | sn58 Attune | 67.8 | 395 | 637 | rtx4090* | 5 | 71% |
| 9 | sn107 Minos | 67.8 | 269 | 22,842 | cpu-small | 20 | 80% |
| 10 | sn102 ConnitoAI | 67.3 | 327 | 1,785 | rtx4090* | 8 | 41% |
| 11 | sn79 MVTRX | 67.2 | 7.33 | 42.55 | cpu-small | 247 | 2% |
| 12 | sn14 Cacheon | 67.1 | 308 | 3,663 | rtx4090* | 9 | 52% |
| 13 | sn15 ORO | 66.6 | 8.11 | 16.69 | cpu-small | 66 | 97% |
| 14 | sn66 conjectures | 63.8 | 115 | 239 | rtx4090* | 4 | 80% |
| 15 | sn62 Ridges | 63.7 | 111 | 1,211 | rtx4090* | 38 | 17% |
| 16 | sn120 Affine | 62.7 | 94.15 | 945 | rtx4090* | 156 | 3% |
| 17 | sn28 SayGM | 62.6 | 83.95 | 2,180 | rtx4090* | 92 | 29% |
| 18 | sn92 REAX | 62.3 | 111 | 133 | rtx4090 | 225 | 1% |
| 19 | sn61 RedTeam | 61.2 | 53.60 | 83.28 | rtx4090* | 137 | 1% |
| 20 | sn81 Reliquary | 59 | 26.69 | 250 | rtx4090* | 16 | 73% |

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
| concentrated (30–60%) | 24 |
| dominated (60–90%) | 25 |
| captured (>90%) | 24 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 95 |
| README keywords (GUESS) | 13 |
| min_compute.yml (curated) | 10 |
| code-submission (validator runs it) | 9 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-10-16T18:46 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Allow selected frozen executions in isola |
| 2026-10-16T18:46 | sn92 | RELEASE | sn92 released v1.2.0-rc6 |
| 2026-10-16T18:46 | sn100 | BURN_DROP | sn100 burn fell 1.000 -> 0.705 - miners can earn again |
| 2026-10-16T18:46 | sn102 | SCORING_COMMIT | sn102 commit touches scoring: ✅ test(validator): after a skipped round |
| 2026-10-16T18:46 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: test(launchpad): bind retain policy fixt |
| 2026-10-16T18:46 | sn121 | SCORING_COMMIT | sn121 commit touches scoring: Update README for skill bundles, the lea |
| 2026-10-16T18:46 | sn121 | README_TASK_DIFF | sn121 README task/scoring sections changed |
| 2026-10-16T14:58 | sn1 | RELEASE | sn1 released v4.4.13 |
| 2026-10-16T14:58 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: scoring: an entry without a measurable ef |
| 2026-10-16T14:58 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-4123 - Validator: split build-log str |
| 2026-10-16T14:58 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-10-16T14:58 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Adopt qualified reward runtimes without r |
| 2026-10-16T14:58 | sn90 | SCORING_COMMIT | sn90 commit touches scoring: docs(subnet): README model lists + valida |
| 2026-10-16T14:58 | sn90 | README_TASK_DIFF | sn90 README task/scoring sections changed |
| 2026-10-16T14:58 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: engine track: protect pending challenger, |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

