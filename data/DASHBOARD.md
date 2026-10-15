# Subnet watch — dashboard

_snapshot 2026-10-15T15:40:28Z · block 9289684 · run_status **ok**_

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
| New events this window | 12 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 68 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 10 | `████` |
| 0.8–0.99 | 9 | `████` |
| ≥0.99 dead | 27 | `███████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 81.9 | 279 | 23,649 | cpu-small | 20 | 80% |
| 2 | sn3 Teutonic | 74.6 | 2,926 | 7,816 | rtx4090* | 5 | 40% |
| 3 | sn102 ConnitoAI | 71.3 | 1,105 | 1,105 = | rtx4090* | 4 | 25% |
| 4 | sn41 Almanac | 71.2 | 18.12 | 143 | cpu-small | 117 | 3% |
| 5 | sn101 Tag101 | 69.8 | 12.09 | 13.03 | cpu-small | 242 | 0% |
| 6 | sn53 engy | 69.5 | 632 | 2,628 | rtx4090 | 24 | 16% |
| 7 | sn91 cascade | 69.2 | 224 | 900 | cpu-small | 5 | 52% |
| 8 | sn58 Attune | 68.2 | 440 | 709 | rtx4090* | 5 | 71% |
| 9 | sn14 Cacheon | 68.1 | 419 | 5,344 | rtx4090* | 6 | 76% |
| 10 | sn67 Harnyx | 67.9 | 7.32 | 959 | cpu-small | 127 | 36% |
| 11 | sn4 Targon | 66.8 | 9,790 | 28,864 | rtx4090* | 5 | 70% |
| 12 | sn79 MVTRX | 66.8 | 7.47 | 29.24 | cpu-small | 245 | 1% |
| 13 | sn15 ORO | 66.5 | 7.33 | 15.12 | cpu-small | 61 | 97% |
| 14 | sn7 Allways | 66.1 | 234 | 323 | rtx4090* | 8 | 20% |
| 15 | sn92 REAX | 65.5 | 226 | 830 | rtx4090 | 85 | 3% |
| 16 | sn62 Ridges | 64 | 123 | 1,239 | rtx4090* | 37 | 17% |
| 17 | sn66 conjectures | 63.9 | 118 | 244 | rtx4090* | 4 | 80% |
| 18 | sn28 SayGM | 63.5 | 107 | 3,511 | rtx4090* | 76 | 26% |
| 19 | sn120 Affine | 62.2 | 81.81 | 581 | rtx4090* | 270 | 2% |
| 20 | sn61 RedTeam | 61.8 | 65.12 | 84.95 | rtx4090* | 125 | 1% |

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
| wide (<30%) | 27 |
| concentrated (30–60%) | 18 |
| dominated (60–90%) | 31 |
| captured (>90%) | 23 |

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
| 2026-10-15T15:41 | sn3 | SCORING_COMMIT | sn3 commit touches scoring: Optimize evaluator dataset downloads with  |
| 2026-10-15T15:41 | sn10 | SCORING_COMMIT | sn10 commit touches scoring: fix(score): charge short completions at f |
| 2026-10-15T15:41 | sn18 | SCORING_COMMIT | sn18 commit touches scoring: change reward function to win rate (#92) |
| 2026-10-15T15:41 | sn25 | RELEASE | sn25 released v2026.10.15-1072765730 |
| 2026-10-15T15:41 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Merge v2/cheaper-validator-production-tes |
| 2026-10-15T15:41 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge pull request #461: broker diagnosti |
| 2026-10-15T15:41 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Reuse parsed packages across independentl |
| 2026-10-15T15:41 | sn92 | RELEASE | sn92 released v1.2.0-rc2 |
| 2026-10-15T15:41 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: tests: tier/split tests keep synthetic tr |
| 2026-10-15T15:41 | sn102 | RELEASE | sn102 released v0.7.0 |
| 2026-10-15T15:41 | sn102 | SCORING_COMMIT | sn102 commit touches scoring: 📝 docs(miner-faq): base usage varies a l |
| 2026-10-15T15:41 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Merge pull request #1377 from carbonphys |
| 2026-10-15T11:20 | sn3 | SCORING_COMMIT | sn3 commit touches scoring: Optimize evaluator model loading by broadc |
| 2026-10-15T11:20 | sn14 | SCORING_COMMIT | sn14 commit touches scoring: Resume checkpointed evaluations across GP |
| 2026-10-15T11:20 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Verify the begun intent before the receip |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

