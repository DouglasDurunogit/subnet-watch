# Subnet watch — dashboard

_snapshot 2026-08-06T12:25:09Z · block 8785205 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 55 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 90 | `miner_burn` < 0.99 |
| Ranked | 90 | passed every gate |
| **Positive margin** | **55** | income beats machine cost |
| New events this window | 3 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 56 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 3 | `██` |
| 0.4–0.6 | 9 | `████` |
| 0.6–0.8 | 4 | `██` |
| 0.8–0.99 | 13 | `██████` |
| ≥0.99 dead | 38 | `███████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 77.8 | 88.64 | 445 | cpu-small | 10 | 29% |
| 2 | sn107 Minos | 77.3 | 93.69 | 27,950 | cpu-small | 20 | 90% |
| 3 | sn60 Bitsec.ai | 76.7 | 2,107 | 2,107 = | cpu-small | 2 | 84% |
| 4 | sn98 NeverPlayAlone | 76 | 1,692 | 1,692 = | cpu-small | 1 | 100% |
| 5 | sn67 Harnyx | 72.3 | 22.87 | 1,069 | cpu-small | 126 | 25% |
| 6 | sn114 SOMA | 69.7 | 684 | 1,722 | rtx4090* | 4 | 65% |
| 7 | sn96 Verathos | 69.4 | 28.40 | 303 | rtx4090 | 62 | 45% |
| 8 | sn62 Ridges | 69 | 543 | 1,966 | rtx4090* | 7 | 35% |
| 9 | sn91 cascade | 68.9 | 531 | 1,503 | rtx4090* | 5 | 52% |
| 10 | sn26 Perturb | 68.3 | 21.84 | 901 | rtx3060 | 11 | 51% |
| 11 | sn15 ORO | 67.8 | 9.91 | 10,327 | cpu-small | 81 | 93% |
| 12 | sn41 Almanac | 67.5 | 7.39 | 32.72 | cpu-small | 54 | 82% |
| 13 | sn74 Gittensor | 66 | 228 | 393 | rtx4090* | 9 | 18% |
| 14 | sn21 AdTAO | 66 | 5.20 | 23.74 | cpu-small | 142 | 45% |
| 15 | sn124 Swarm | 65.8 | 217 | 622 | rtx4090* | 23 | 11% |
| 16 | sn61 RedTeam | 62.3 | 74.94 | 172 | rtx4090* | 38 | 5% |
| 17 | sn80 OpenRoboto | 62.1 | 70.41 | 267 | rtx4090* | 4 | 91% |
| 18 | sn101 Tag101 | 60.1 | 0.15 | 0.64 | cpu-small | 244 | 90% |
| 19 | sn28 gm | 59.4 | 32.56 | 3,702 | rtx4090* | 16 | 40% |
| 20 | sn102 ConnitoAI | 57.2 | 15.45 | 1,971 | rtx4090* | 9 | 36% |

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
| wide (<30%) | 24 |
| concentrated (30–60%) | 20 |
| dominated (60–90%) | 19 |
| captured (>90%) | 26 |

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
| 2026-08-06T12:25 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-08-06T12:25 | sn100 | RELEASE | sn100 released v3.3.2 — miner HTML sandboxing + chain endpoint failove |
| 2026-08-06T12:25 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Document the RT-6 incident: sampler + re |
| 2026-08-06T10:19 | sn15 | RELEASE | sn15 released v1.2.6: docs(validator): correct stale weight-salt fallb |
| 2026-08-06T10:19 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: docs(validator): correct stale weight-sal |
| 2026-08-06T10:19 | sn100 | RELEASE | sn100 released v3.3.1 — prod trust-root roll + prism epoch-close emiss |
| 2026-08-06T10:19 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: fix(design): sandbox miner HTML viewer e |
| 2026-08-06T07:28 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Repair Research Lab verifier drift |
| 2026-08-06T07:28 | sn100 | RELEASE | sn100 released v3.3.1 — prod validator trust-root roll |
| 2026-08-06T07:28 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: chore(pins): promote prod validator to v |
| 2026-08-06T07:28 | sn100 | README_TASK_DIFF | sn100 README task/scoring sections changed |
| 2026-08-06T04:41 | sn2 | RELEASE | sn2 released 14.13.1 |
| 2026-08-06T04:41 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: Merge pull request #28 from conjectures-i |
| 2026-08-06T04:41 | sn66 | README_TASK_DIFF | sn66 README task/scoring sections changed |
| 2026-08-06T04:41 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Honor scoring maintenance between rebench |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

