# Subnet watch — dashboard

_snapshot 2026-08-10T03:01:07Z · block 8811184 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 59 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 90 | `miner_burn` < 0.99 |
| Ranked | 90 | passed every gate |
| **Positive margin** | **59** | income beats machine cost |
| New events this window | 3 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 53 | `████████████████████████████` |
| 0–0.2 | 8 | `████` |
| 0.2–0.4 | 3 | `██` |
| 0.4–0.6 | 9 | `█████` |
| 0.6–0.8 | 10 | `█████` |
| 0.8–0.99 | 7 | `████` |
| ≥0.99 dead | 38 | `████████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 78.2 | 116 | 33,003 | cpu-small | 20 | 90% |
| 2 | sn76 Phylax | 76.7 | 67.28 | 203 | cpu-small | 10 | 33% |
| 3 | sn98 NeverPlayAlone | 76.1 | 1,780 | 1,780 = | cpu-small | 1 | 100% |
| 4 | sn60 Bitsec.ai | 74.9 | 1,223 | 1,223 = | cpu-small | 2 | 50% |
| 5 | sn67 Harnyx | 71.2 | 17.59 | 764 | cpu-small | 121 | 20% |
| 6 | sn91 cascade | 70.2 | 786 | 2,693 | rtx4090* | 5 | 48% |
| 7 | sn96 Verathos | 70.2 | 35.01 | 265 | rtx4090 | 48 | 42% |
| 8 | sn1 Apex | 69.9 | 719 | 1,650 | rtx4090* | 4 | 49% |
| 9 | sn41 Almanac | 69.2 | 11.08 | 34.35 | cpu-small | 69 | 70% |
| 10 | sn15 ORO | 68.3 | 10.26 | 19.79 | cpu-small | 75 | 94% |
| 11 | sn62 Ridges | 68.2 | 432 | 2,005 | rtx4090* | 7 | 35% |
| 12 | sn26 Perturb | 68.2 | 21.24 | 39.52 | rtx3060 | 11 | 50% |
| 13 | sn100 BASE | 67.1 | 309 | 839 | rtx4090* | 5 | 50% |
| 14 | sn28 gm | 65.8 | 213 | 4,376 | rtx4090* | 24 | 43% |
| 15 | sn38 ChronoLLM | 65.7 | 218 | 3,657 | rtx4090* | 10 | 52% |
| 16 | sn21 AdTAO | 65.4 | 4.66 | 21.59 | cpu-small | 142 | 45% |
| 17 | sn80 OpenRoboto | 64.9 | 163 | 591 | rtx4090* | 4 | 91% |
| 18 | sn61 RedTeam | 62.7 | 83.93 | 351 | rtx4090* | 47 | 7% |
| 19 | sn51 lium.io | 58.9 | 33.81 | 3,224 | rtx4090* | 50 | 56% |
| 20 | sn6 Numinous | 58 | 22.97 | 451 | cpu-small | 18 | 26% |

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
| wide (<30%) | 22 |
| concentrated (30–60%) | 25 |
| dominated (60–90%) | 18 |
| captured (>90%) | 24 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 104 |
| code-submission (validator runs it) | 9 |
| min_compute.yml (curated) | 9 |
| README keywords (GUESS) | 5 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-08-10T03:01 | sn58 | BURN_DROP | sn58 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-08-10T03:01 | sn89 | SCORING_COMMIT | sn89 commit touches scoring: Retire MINER_EMISSION_CAP, and make it re |
| 2026-08-10T03:01 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: Tell a validator when no directive exists |
| 2026-08-09T22:14 | sn89 | SCORING_COMMIT | sn89 commit touches scoring: Referrer: score recruiters across every c |
| 2026-08-09T20:49 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Close and verify dev snapshot request set |
| 2026-08-09T19:56 | sn126 | SCORING_COMMIT | sn126 commit touches scoring: Document miner training benchmark |
| 2026-08-09T19:56 | sn126 | README_TASK_DIFF | sn126 README task/scoring sections changed |
| 2026-08-09T18:18 | sn90 | RELEASE | sn90 released v1.0.2 — proxy version header + owner miner UID hardcode |
| 2026-08-09T18:18 | sn90 | SCORING_COMMIT | sn90 commit touches scoring: feat(validator): v1.0.2 — proxy version h |
| 2026-08-09T16:15 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Preserve handled scorer transport failure |
| 2026-08-09T13:30 | sn96 | RELEASE | sn96 released v0.1.32 - Miner Hard-Proof Transport |
| 2026-08-09T13:30 | sn96 | SCORING_COMMIT | sn96 commit touches scoring: fix: align miner proxy with hard proof de |
| 2026-08-09T10:49 | sn61 | RELEASE | sn61 released 4.9.3 |
| 2026-08-09T10:49 | sn61 | SCORING_COMMIT | sn61 commit touches scoring: deps: update challenge image version for  |
| 2026-08-09T10:49 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

