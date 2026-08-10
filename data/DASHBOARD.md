# Subnet watch — dashboard

_snapshot 2026-08-10T06:19:58Z · block 8812178 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 57 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 89 | `miner_burn` < 0.99 |
| Ranked | 89 | passed every gate |
| **Positive margin** | **57** | income beats machine cost |
| New events this window | 2 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 53 | `████████████████████████████` |
| 0–0.2 | 7 | `████` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 9 | `█████` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 8 | `████` |
| ≥0.99 dead | 39 | `█████████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 78 | 111 | 32,212 | cpu-small | 20 | 90% |
| 2 | sn76 Phylax | 76.7 | 67.23 | 203 | cpu-small | 10 | 33% |
| 3 | sn98 NeverPlayAlone | 76.1 | 1,778 | 1,778 = | cpu-small | 1 | 100% |
| 4 | sn60 Bitsec.ai | 74.9 | 1,225 | 1,225 = | cpu-small | 2 | 50% |
| 5 | sn96 Verathos | 72.9 | 68.58 | 312 | rtx4090 | 30 | 42% |
| 6 | sn67 Harnyx | 71.2 | 17.30 | 752 | cpu-small | 129 | 19% |
| 7 | sn91 cascade | 70.3 | 809 | 2,772 | rtx4090* | 5 | 50% |
| 8 | sn1 Apex | 69.8 | 708 | 1,625 | rtx4090* | 4 | 50% |
| 9 | sn41 Almanac | 69.3 | 11.18 | 34.26 | cpu-small | 69 | 70% |
| 10 | sn26 Perturb | 68.3 | 21.69 | 40.16 | rtx3060 | 11 | 50% |
| 11 | sn62 Ridges | 68.2 | 428 | 1,984 | rtx4090* | 7 | 35% |
| 12 | sn38 ChronoLLM | 65.7 | 216 | 3,632 | rtx4090* | 10 | 52% |
| 13 | sn15 ORO | 65.7 | 7.14 | 17.78 | cpu-small | 72 | 95% |
| 14 | sn21 AdTAO | 65.4 | 4.67 | 21.63 | cpu-small | 142 | 45% |
| 15 | sn80 OpenRoboto | 64.9 | 162 | 589 | rtx4090* | 4 | 91% |
| 16 | sn28 gm | 64.1 | 127 | 4,380 | rtx4090* | 26 | 43% |
| 17 | sn100 BASE | 63.2 | 97.94 | 841 | rtx4090* | 8 | 51% |
| 18 | sn61 RedTeam | 62.7 | 84.50 | 353 | rtx4090* | 45 | 8% |
| 19 | sn102 ConnitoAI | 59.9 | 1,265 | 1,265 = | rtx4090* | 4 | 25% |
| 20 | sn51 lium.io | 58.6 | 31.42 | 3,304 | rtx4090* | 50 | 52% |

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
| wide (<30%) | 23 |
| concentrated (30–60%) | 24 |
| dominated (60–90%) | 18 |
| captured (>90%) | 23 |

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
| 2026-08-10T06:20 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: miner: `cascade duel` — full settled-roun |
| 2026-08-10T06:20 | sn96 | RELEASE | sn96 released v0.1.33 - Maximum-Concurrency Proof Serving |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

