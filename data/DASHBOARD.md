# Subnet watch — dashboard

_snapshot 2026-10-03T05:10:55Z · block 9200141 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 58 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 98 | `miner_burn` < 0.99 |
| Ranked | 98 | passed every gate |
| **Positive margin** | **58** | income beats machine cost |
| New events this window | 3 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 67 | `████████████████████████████` |
| 0–0.2 | 8 | `███` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 7 | `███` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 30 | `█████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn41 Almanac | 74.7 | 43.05 | 124 | cpu-small | 123 | 2% |
| 2 | sn23 Trishool | 73.8 | 897 | 897 = | cpu-small | 2 | 80% |
| 3 | sn91 cascade | 72.7 | 638 | 2,554 | cpu-small | 5 | 52% |
| 4 | sn53 engy | 71.9 | 1,319 | 3,620 | rtx4090 | 14 | 22% |
| 5 | sn46 Instant | 70.2 | 308 | 365 | cpu-small | 6 | 49% |
| 6 | sn1 Apex | 69.8 | 703 | 1,085 | rtx4090* | 4 | 60% |
| 7 | sn56 Gradients | 69.4 | 618 | 5,019 | rtx4090* | 8 | 39% |
| 8 | sn120 Affine | 69.2 | 603 | 603 = | rtx4090* | 65 | 2% |
| 9 | sn67 Harnyx | 68.6 | 8.62 | 1,102 | cpu-small | 107 | 36% |
| 10 | sn107 Minos | 68.5 | 327 | 27,772 | cpu-small | 20 | 80% |
| 11 | sn15 ORO | 66.6 | 8.64 | 20,560 | cpu-small | 51 | 98% |
| 12 | sn111 Claims | 66.1 | 240 | 2,165 | rtx4090* | 5 | 58% |
| 13 | sn4 Targon | 65.4 | 6,499 | 30,740 | rtx4090* | 5 | 70% |
| 14 | sn3 Teutonic | 64 | 4,383 | 4,383 = | rtx4090* | 5 | 20% |
| 15 | sn26 Perturb | 63.3 | 102 | 102 = | rtx3060 | 4 | 91% |
| 16 | sn61 RedTeam | 62.5 | 79.40 | 144 | rtx4090* | 113 | 2% |
| 17 | sn14 Cacheon | 61.1 | 50.80 | 1,779 | rtx4090* | 13 | 24% |
| 18 | sn28 SayGM | 60.9 | 50.49 | 997 | rtx4090* | 72 | 17% |
| 19 | sn62 Ridges | 60 | 37.93 | 2,768 | rtx4090* | 28 | 31% |
| 20 | sn102 ConnitoAI | 59.3 | 1,069 | 1,531 | rtx4090* | 6 | 31% |

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
| wide (<30%) | 21 |
| concentrated (30–60%) | 27 |
| dominated (60–90%) | 21 |
| captured (>90%) | 25 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 96 |
| README keywords (GUESS) | 12 |
| min_compute.yml (curated) | 10 |
| code-submission (validator runs it) | 9 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-10-03T05:11 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Preserve concurrent verifier lease correc |
| 2026-10-03T05:11 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: perf(corpus): verify drand rounds by BLS  |
| 2026-10-03T05:11 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Record verified public full-model update |
| 2026-10-02T23:56 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: Validator v2.0.41: per-event market notic |
| 2026-10-02T23:56 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Reuse exact Arena verifier requests throu |
| 2026-10-02T23:56 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: fix(corpus): bound the audits of one judg |
| 2026-10-02T23:56 | sn117 | RELEASE | sn117 released everycli v0.2.3 |
| 2026-10-02T23:56 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Prepare public dashboard projection for  |
| 2026-10-02T20:11 | sn1 | RELEASE | sn1 released v4.4.12 |
| 2026-10-02T20:11 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: Capture cached input tokens in private ev |
| 2026-10-02T20:11 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Preserve qualification headroom with veri |
| 2026-10-02T20:11 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Archive October 1 optional-signal scores  |
| 2026-10-02T20:11 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: feat(corpus): a GPU process that scores e |
| 2026-10-02T20:11 | sn94 | SCORING_COMMIT | sn94 commit touches scoring: Fix fork sentinel command verification (# |
| 2026-10-02T20:11 | sn104 | SCORING_COMMIT | sn104 commit touches scoring: Merge pull request #15 from taostatus/fe |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

