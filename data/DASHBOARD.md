# Subnet watch — dashboard

_snapshot 2026-08-09T20:48:53Z · block 8809323 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 56 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 89 | `miner_burn` < 0.99 |
| Ranked | 89 | passed every gate |
| **Positive margin** | **56** | income beats machine cost |
| New events this window | 3 | see ALARMS.md |

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
| 1 | sn107 Minos | 78.1 | 113 | 33,490 | cpu-small | 20 | 90% |
| 2 | sn76 Phylax | 76.7 | 68.16 | 205 | cpu-small | 10 | 33% |
| 3 | sn60 Bitsec.ai | 74.8 | 1,195 | 1,195 = | cpu-small | 2 | 50% |
| 4 | sn67 Harnyx | 70.8 | 15.10 | 863 | cpu-small | 155 | 22% |
| 5 | sn91 cascade | 70.2 | 796 | 2,727 | rtx4090* | 5 | 48% |
| 6 | sn1 Apex | 70 | 750 | 1,546 | rtx4090* | 4 | 50% |
| 7 | sn96 Verathos | 69.5 | 29.12 | 194 | rtx4090 | 62 | 42% |
| 8 | sn41 Almanac | 69.5 | 11.83 | 34.73 | cpu-small | 65 | 72% |
| 9 | sn62 Ridges | 68.3 | 440 | 2,042 | rtx4090* | 7 | 35% |
| 10 | sn26 Perturb | 68.2 | 21.18 | 41.35 | rtx3060 | 11 | 50% |
| 11 | sn15 ORO | 68.2 | 10.31 | 19.69 | cpu-small | 74 | 94% |
| 12 | sn100 BASE | 68 | 410 | 1,665 | rtx4090* | 5 | 50% |
| 13 | sn38 ChronoLLM | 65.7 | 219 | 3,680 | rtx4090* | 10 | 52% |
| 14 | sn28 gm | 65.7 | 209 | 4,179 | rtx4090* | 24 | 43% |
| 15 | sn21 AdTAO | 65.4 | 4.70 | 21.77 | cpu-small | 142 | 45% |
| 16 | sn80 OpenRoboto | 65.2 | 178 | 642 | rtx4090* | 4 | 91% |
| 17 | sn61 RedTeam | 62.6 | 81.49 | 342 | rtx4090* | 47 | 7% |
| 18 | sn51 lium.io | 59.3 | 37.91 | 3,108 | rtx4090* | 50 | 60% |
| 19 | sn6 Numinous | 59.1 | 29.65 | 340 | cpu-small | 18 | 19% |
| 20 | sn102 ConnitoAI | 58.9 | 927 | 1,440 | rtx4090* | 6 | 31% |

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
| 2026-08-09T09:02 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Retry transient company homepage verifica |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

