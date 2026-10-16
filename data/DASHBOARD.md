# Subnet watch — dashboard

_snapshot 2026-10-16T14:57:55Z · block 9296671 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 60 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 100 | `miner_burn` < 0.99 |
| Ranked | 100 | passed every gate |
| **Positive margin** | **60** | income beats machine cost |
| New events this window | 11 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 68 | `████████████████████████████` |
| 0–0.2 | 6 | `██` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 11 | `█████` |
| 0.8–0.99 | 6 | `██` |
| ≥0.99 dead | 28 | `████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn3 Teutonic | 74.8 | 3,100 | 3,100 = | rtx4090* | 5 | 40% |
| 2 | sn41 Almanac | 74.3 | 38.32 | 121 | cpu-small | 108 | 14% |
| 3 | sn53 engy | 69.6 | 650 | 2,699 | rtx4090 | 24 | 16% |
| 4 | sn91 cascade | 69.2 | 229 | 918 | cpu-small | 5 | 52% |
| 5 | sn1 Apex | 68.7 | 503 | 915 | rtx4090* | 4 | 69% |
| 6 | sn67 Harnyx | 68.7 | 9.08 | 9.08 = | cpu-small | 230 | 14% |
| 7 | sn58 Attune | 68.3 | 454 | 732 | rtx4090* | 5 | 71% |
| 8 | sn79 MVTRX | 68.2 | 8.24 | 31.66 | cpu-small | 248 | 1% |
| 9 | sn107 Minos | 68 | 283 | 23,986 | cpu-small | 20 | 80% |
| 10 | sn15 ORO | 67.4 | 8.55 | 17.54 | cpu-small | 66 | 97% |
| 11 | sn14 Cacheon | 67.2 | 323 | 3,841 | rtx4090* | 9 | 52% |
| 12 | sn102 ConnitoAI | 67.1 | 316 | 1,582 | rtx4090* | 8 | 34% |
| 13 | sn4 Targon | 67 | 10,479 | 30,896 | rtx4090* | 5 | 70% |
| 14 | sn7 Allways | 65.2 | 182 | 282 | rtx4090* | 7 | 47% |
| 15 | sn66 conjectures | 64 | 122 | 237 | rtx4090* | 4 | 81% |
| 16 | sn62 Ridges | 63.8 | 117 | 1,272 | rtx4090* | 38 | 17% |
| 17 | sn92 REAX | 63.3 | 130 | 164 | rtx4090 | 218 | 1% |
| 18 | sn28 SayGM | 63.2 | 99.51 | 3,401 | rtx4090* | 85 | 24% |
| 19 | sn120 Affine | 62.3 | 85.85 | 607 | rtx4090* | 270 | 2% |
| 20 | sn61 RedTeam | 61.9 | 65.71 | 93.79 | rtx4090* | 125 | 1% |

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
| wide (<30%) | 26 |
| concentrated (30–60%) | 23 |
| dominated (60–90%) | 26 |
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
| 2026-10-16T14:58 | sn1 | RELEASE | sn1 released v4.4.13 |
| 2026-10-16T14:58 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: scoring: an entry without a measurable ef |
| 2026-10-16T14:58 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-4123 - Validator: split build-log str |
| 2026-10-16T14:58 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-10-16T14:58 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Adopt qualified reward runtimes without r |
| 2026-10-16T14:58 | sn90 | SCORING_COMMIT | sn90 commit touches scoring: docs(subnet): README model lists + valida |
| 2026-10-16T14:58 | sn90 | README_TASK_DIFF | sn90 README task/scoring sections changed |
| 2026-10-16T14:58 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: engine track: protect pending challenger, |
| 2026-10-16T14:58 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: fix(challenges): raise get_weights timeo |
| 2026-10-16T14:58 | sn114 | SCORING_COMMIT | sn114 commit touches scoring: update scoring.md docs |
| 2026-10-16T14:58 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Merge pull request #1405 from carbonphys |
| 2026-10-16T10:10 | sn37 | BURN_DROP | sn37 burn fell 1.000 -> 0.713 - miners can earn again |
| 2026-10-16T10:10 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-4362 - [P3] Validator: remove setting |
| 2026-10-16T10:10 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge pull request #489 from leadpoet/fix |
| 2026-10-16T10:10 | sn76 | BURN_DROP | sn76 burn fell 0.999 -> 0.961 - miners can earn again |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

