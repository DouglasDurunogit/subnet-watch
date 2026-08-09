# Subnet watch — dashboard

_snapshot 2026-08-09T22:14:14Z · block 8809750 · run_status **ok**_

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
| New events this window | 1 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 52 | `████████████████████████████` |
| 0–0.2 | 8 | `████` |
| 0.2–0.4 | 3 | `██` |
| 0.4–0.6 | 10 | `█████` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 8 | `████` |
| ≥0.99 dead | 39 | `█████████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 78.2 | 116 | 33,531 | cpu-small | 20 | 89% |
| 2 | sn76 Phylax | 76.7 | 68.21 | 206 | cpu-small | 10 | 33% |
| 3 | sn60 Bitsec.ai | 74.8 | 1,201 | 1,201 = | cpu-small | 2 | 50% |
| 4 | sn67 Harnyx | 70.8 | 15.11 | 864 | cpu-small | 155 | 22% |
| 5 | sn91 cascade | 70.2 | 798 | 2,732 | rtx4090* | 5 | 48% |
| 6 | sn1 Apex | 70 | 746 | 1,700 | rtx4090* | 4 | 47% |
| 7 | sn96 Verathos | 69.9 | 32.63 | 273 | rtx4090 | 51 | 42% |
| 8 | sn41 Almanac | 69.5 | 11.86 | 34.74 | cpu-small | 65 | 72% |
| 9 | sn62 Ridges | 68.3 | 440 | 2,042 | rtx4090* | 7 | 35% |
| 10 | sn26 Perturb | 68.3 | 21.71 | 191 | rtx3060 | 11 | 50% |
| 11 | sn15 ORO | 68.1 | 10.41 | 19.88 | cpu-small | 74 | 94% |
| 12 | sn100 BASE | 68 | 410 | 1,666 | rtx4090* | 5 | 50% |
| 13 | sn38 ChronoLLM | 65.7 | 220 | 3,686 | rtx4090* | 10 | 52% |
| 14 | sn21 AdTAO | 65.4 | 4.71 | 21.79 | cpu-small | 142 | 45% |
| 15 | sn80 OpenRoboto | 65.3 | 182 | 656 | rtx4090* | 4 | 91% |
| 16 | sn28 gm | 65.2 | 176 | 4,555 | rtx4090* | 25 | 45% |
| 17 | sn61 RedTeam | 62.6 | 80.49 | 338 | rtx4090* | 47 | 7% |
| 18 | sn6 Numinous | 59.1 | 29.65 | 340 | cpu-small | 18 | 19% |
| 19 | sn51 lium.io | 59 | 35.10 | 2,658 | rtx4090* | 47 | 60% |
| 20 | sn56 Gradients | 56.6 | 479 | 1,009 | rtx4090* | 7 | 71% |

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
| 2026-08-09T10:49 | sn96 | RELEASE | sn96 released v0.1.31 - Validator Auto-Update Drain |
| 2026-08-09T10:49 | sn96 | SCORING_COMMIT | sn96 commit touches scoring: fix: drain validator work before auto-upd |
| 2026-08-09T09:53 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Use fresh identities for scorer retries |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

