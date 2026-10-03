# Subnet watch — dashboard

_snapshot 2026-10-03T10:31:18Z · block 9201743 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 59 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 97 | `miner_burn` < 0.99 |
| Ranked | 97 | passed every gate |
| **Positive margin** | **59** | income beats machine cost |
| New events this window | 5 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 66 | `████████████████████████████` |
| 0–0.2 | 8 | `███` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 8 | `███` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 31 | `█████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn41 Almanac | 74.8 | 43.43 | 125 | cpu-small | 124 | 2% |
| 2 | sn23 Trishool | 73.9 | 909 | 909 = | cpu-small | 2 | 80% |
| 3 | sn91 cascade | 72.8 | 661 | 2,648 | cpu-small | 5 | 52% |
| 4 | sn53 engy | 71.9 | 1,304 | 3,580 | rtx4090 | 14 | 22% |
| 5 | sn26 Perturb | 71 | 43.68 | 112 | rtx3060 | 4 | 90% |
| 6 | sn46 Instant | 70.4 | 325 | 348 | cpu-small | 6 | 50% |
| 7 | sn111 Claims | 70 | 737 | 1,339 | rtx4090* | 5 | 36% |
| 8 | sn1 Apex | 69.7 | 679 | 1,061 | rtx4090* | 4 | 61% |
| 9 | sn56 Gradients | 69.4 | 620 | 5,031 | rtx4090* | 8 | 39% |
| 10 | sn107 Minos | 68.6 | 328 | 27,823 | cpu-small | 20 | 80% |
| 11 | sn67 Harnyx | 68.6 | 8.54 | 1,099 | cpu-small | 114 | 36% |
| 12 | sn15 ORO | 66.2 | 8.56 | 20,385 | cpu-small | 51 | 98% |
| 13 | sn4 Targon | 65.4 | 6,514 | 30,811 | rtx4090* | 5 | 70% |
| 14 | sn61 RedTeam | 62.5 | 79.25 | 143 | rtx4090* | 113 | 2% |
| 15 | sn28 SayGM | 61.5 | 60.91 | 813 | rtx4090* | 73 | 18% |
| 16 | sn14 Cacheon | 61 | 50.29 | 1,763 | rtx4090* | 13 | 23% |
| 17 | sn62 Ridges | 60 | 38.07 | 2,776 | rtx4090* | 28 | 31% |
| 18 | sn5 Hone | 59 | 37.50 | 40.00 | rtx4090* | 241 | 0% |
| 19 | sn102 ConnitoAI | 58.8 | 910 | 1,522 | rtx4090* | 6 | 31% |
| 20 | sn80 OpenRoboto | 58.8 | 905 | 3,380 | rtx4090* | 8 | 33% |

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
| wide (<30%) | 20 |
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
| 2026-10-03T10:31 | sn15 | RELEASE | sn15 released Validator v2.1.0: runtime contract on claim and delivery |
| 2026-10-03T10:31 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: Validator v2.1.0: runtime contract on cla |
| 2026-10-03T10:31 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Verify HTTP retry controls and preserve q |
| 2026-10-03T10:31 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: fix: prefer verified exact homepage brand |
| 2026-10-03T10:31 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Document verified successor, external mi |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

