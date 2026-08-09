# Subnet watch — dashboard

_snapshot 2026-08-09T23:42:26Z · block 8810191 · run_status **ok**_

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
| New events this window | 0 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 52 | `████████████████████████████` |
| 0–0.2 | 7 | `████` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 10 | `█████` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 8 | `████` |
| ≥0.99 dead | 39 | `█████████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 78.2 | 115 | 33,090 | cpu-small | 20 | 90% |
| 2 | sn76 Phylax | 76.7 | 67.03 | 202 | cpu-small | 10 | 33% |
| 3 | sn60 Bitsec.ai | 74.8 | 1,199 | 1,199 = | cpu-small | 2 | 50% |
| 4 | sn96 Verathos | 71.2 | 44.86 | 301 | rtx4090 | 35 | 42% |
| 5 | sn67 Harnyx | 70.8 | 14.84 | 849 | cpu-small | 155 | 22% |
| 6 | sn91 cascade | 70.2 | 788 | 2,700 | rtx4090* | 5 | 48% |
| 7 | sn1 Apex | 69.9 | 727 | 1,665 | rtx4090* | 4 | 48% |
| 8 | sn41 Almanac | 69.4 | 11.66 | 34.18 | cpu-small | 65 | 72% |
| 9 | sn15 ORO | 68.3 | 10.27 | 19.62 | cpu-small | 74 | 94% |
| 10 | sn62 Ridges | 68.2 | 433 | 2,010 | rtx4090* | 7 | 35% |
| 11 | sn26 Perturb | 68.2 | 21.09 | 186 | rtx3060 | 11 | 50% |
| 12 | sn100 BASE | 68 | 403 | 1,638 | rtx4090* | 5 | 50% |
| 13 | sn38 ChronoLLM | 65.7 | 216 | 3,629 | rtx4090* | 10 | 52% |
| 14 | sn80 OpenRoboto | 64.9 | 163 | 593 | rtx4090* | 4 | 91% |
| 15 | sn21 AdTAO | 64.9 | 4.61 | 21.41 | cpu-small | 142 | 45% |
| 16 | sn61 RedTeam | 62.6 | 81.05 | 340 | rtx4090* | 47 | 7% |
| 17 | sn28 gm | 61.8 | 66.12 | 3,898 | rtx4090* | 26 | 39% |
| 18 | sn6 Numinous | 59 | 29.13 | 334 | cpu-small | 18 | 19% |
| 19 | sn51 lium.io | 58.9 | 33.72 | 2,716 | rtx4090* | 47 | 60% |
| 20 | sn56 Gradients | 56.6 | 471 | 992 | rtx4090* | 7 | 71% |

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
| concentrated (30–60%) | 23 |
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

