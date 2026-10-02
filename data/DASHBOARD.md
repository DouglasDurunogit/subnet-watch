# Subnet watch — dashboard

_snapshot 2026-10-02T23:55:48Z · block 9198566 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 61 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 97 | `miner_burn` < 0.99 |
| Ranked | 97 | passed every gate |
| **Positive margin** | **61** | income beats machine cost |
| New events this window | 5 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 64 | `████████████████████████████` |
| 0–0.2 | 8 | `████` |
| 0.2–0.4 | 8 | `████` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 7 | `███` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 31 | `██████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn41 Almanac | 74.7 | 42.51 | 125 | cpu-small | 121 | 2% |
| 2 | sn23 Trishool | 74 | 943 | 943 = | cpu-small | 2 | 79% |
| 3 | sn91 cascade | 72.7 | 636 | 2,545 | cpu-small | 5 | 52% |
| 4 | sn53 engy | 71.9 | 1,321 | 3,624 | rtx4090 | 14 | 22% |
| 5 | sn1 Apex | 70 | 731 | 1,115 | rtx4090* | 4 | 59% |
| 6 | sn46 Instant | 69.7 | 262 | 319 | cpu-small | 7 | 48% |
| 7 | sn56 Gradients | 69.4 | 623 | 5,055 | rtx4090* | 8 | 39% |
| 8 | sn120 Affine | 69.2 | 608 | 608 = | rtx4090* | 65 | 2% |
| 9 | sn67 Harnyx | 68.7 | 8.86 | 1,078 | cpu-small | 120 | 35% |
| 10 | sn107 Minos | 68.6 | 329 | 27,901 | cpu-small | 20 | 80% |
| 11 | sn111 Claims | 66.8 | 293 | 2,624 | rtx4090* | 5 | 70% |
| 12 | sn4 Targon | 65.4 | 6,548 | 30,972 | rtx4090* | 5 | 70% |
| 13 | sn3 Teutonic | 64 | 4,392 | 4,392 = | rtx4090* | 5 | 20% |
| 14 | sn61 RedTeam | 62.4 | 79.16 | 143 | rtx4090* | 113 | 2% |
| 15 | sn14 Cacheon | 61.7 | 61.67 | 1,935 | rtx4090* | 13 | 26% |
| 16 | sn62 Ridges | 60.7 | 46.14 | 2,788 | rtx4090* | 28 | 31% |
| 17 | sn5 Hone | 59.1 | 36.92 | 39.09 | rtx4090* | 243 | 0% |
| 18 | sn80 OpenRoboto | 58.7 | 894 | 3,342 | rtx4090* | 8 | 33% |
| 19 | sn28 SayGM | 58.5 | 25.44 | 2,299 | rtx4090* | 70 | 35% |
| 20 | sn38 ChronoLLM | 58.3 | 322 | 4,374 | cpu-small | 10 | 52% |

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
| concentrated (30–60%) | 26 |
| dominated (60–90%) | 24 |
| captured (>90%) | 23 |

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
| 2026-10-02T20:11 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Project the separated math pilot and pub |
| 2026-10-02T15:44 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Record scoped native miner monitor and ba |
| 2026-10-02T15:44 | sn51 | RELEASE | sn51 released validator-v2026.10.02.2 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

