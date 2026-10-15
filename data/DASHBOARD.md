# Subnet watch — dashboard

_snapshot 2026-10-15T11:20:08Z · block 9288382 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 58 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 100 | `miner_burn` < 0.99 |
| Ranked | 100 | passed every gate |
| **Positive margin** | **58** | income beats machine cost |
| New events this window | 9 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 67 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 10 | `████` |
| 0.8–0.99 | 9 | `████` |
| ≥0.99 dead | 28 | `████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 81.7 | 266 | 22,600 | cpu-small | 20 | 80% |
| 2 | sn96 Verathos | 73.4 | 77.39 | 128 | rtx4090 | 7 | 86% |
| 3 | sn41 Almanac | 71.1 | 17.67 | 140 | cpu-small | 119 | 3% |
| 4 | sn101 Tag101 | 69.8 | 11.76 | 12.72 | cpu-small | 246 | 0% |
| 5 | sn53 engy | 69.3 | 602 | 2,503 | rtx4090 | 24 | 16% |
| 6 | sn91 cascade | 69.2 | 226 | 907 | cpu-small | 5 | 52% |
| 7 | sn14 Cacheon | 68.3 | 452 | 633 | rtx4090* | 5 | 76% |
| 8 | sn58 Attune | 68.2 | 446 | 718 | rtx4090* | 5 | 71% |
| 9 | sn67 Harnyx | 68 | 6.97 | 920 | cpu-small | 127 | 36% |
| 10 | sn4 Targon | 66.6 | 9,342 | 27,545 | rtx4090* | 5 | 70% |
| 11 | sn79 MVTRX | 66.6 | 6.19 | 34.06 | cpu-small | 244 | 2% |
| 12 | sn15 ORO | 66.4 | 7.05 | 15,730 | cpu-small | 60 | 97% |
| 13 | sn7 Allways | 65.6 | 200 | 290 | rtx4090* | 9 | 18% |
| 14 | sn62 Ridges | 63.8 | 117 | 1,187 | rtx4090* | 37 | 17% |
| 15 | sn66 conjectures | 62.9 | 87.21 | 199 | rtx4090* | 4 | 84% |
| 16 | sn28 SayGM | 62.5 | 81.79 | 1,855 | rtx4090* | 73 | 34% |
| 17 | sn120 Affine | 61.8 | 77.94 | 555 | rtx4090* | 270 | 2% |
| 18 | sn61 RedTeam | 61.6 | 63.25 | 82.93 | rtx4090* | 126 | 1% |
| 19 | sn102 ConnitoAI | 59.4 | 1,091 | 1,091 = | rtx4090* | 4 | 25% |
| 20 | sn111 Claims | 59.3 | 31.40 | 2,826 | rtx4090* | 6 | 90% |

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
| concentrated (30–60%) | 20 |
| dominated (60–90%) | 30 |
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
| 2026-10-15T11:20 | sn3 | SCORING_COMMIT | sn3 commit touches scoring: Optimize evaluator model loading by broadc |
| 2026-10-15T11:20 | sn14 | SCORING_COMMIT | sn14 commit touches scoring: Resume checkpointed evaluations across GP |
| 2026-10-15T11:20 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Verify the begun intent before the receip |
| 2026-10-15T11:20 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: validator: name the reason when a rented  |
| 2026-10-15T11:20 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-10-15T11:20 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Preserve nested history profile aliases w |
| 2026-10-15T11:20 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: test(corpus): the signed-sandbox restart  |
| 2026-10-15T11:20 | sn89 | SCORING_COMMIT | sn89 commit touches scoring: HF warmup dust: not-yet-eligible HF miner |
| 2026-10-15T11:20 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Expose battery scorer initializer closur |
| 2026-10-15T05:51 | sn15 | RELEASE | sn15 released v2.5.2 |
| 2026-10-15T05:51 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: Treat a miner's OpenRouter credit 402 as  |
| 2026-10-15T05:51 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Update the SN25 timeline with the validat |
| 2026-10-15T05:51 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-4071 - [P1] validator: SCORING_EXCLUD |
| 2026-10-15T05:51 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-10-15T05:51 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Merge pull request #266 from Umi-BitSign/ |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

