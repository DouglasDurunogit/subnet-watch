# Subnet watch — dashboard

_snapshot 2026-09-19T06:16:11Z · block 9099823 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 54 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 92 | `miner_burn` < 0.99 |
| Ranked | 92 | passed every gate |
| **Positive margin** | **54** | income beats machine cost |
| New events this window | 2 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 60 | `████████████████████████████` |
| 0–0.2 | 10 | `█████` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 36 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn11 TrajectoryRL | 80.4 | 6,301 | 6,301 = | cpu-small | 1 | 100% |
| 2 | sn4 Targon | 77.9 | 7,732 | 21,707 | rtx4090* | 6 | 52% |
| 3 | sn3 Teutonic | 76.3 | 4,888 | 4,888 = | rtx4090* | 5 | 20% |
| 4 | sn91 cascade | 71.8 | 485 | 1,296 | cpu-small | 5 | 52% |
| 5 | sn102 ConnitoAI | 71.1 | 1,038 | 1,347 | rtx4090* | 5 | 29% |
| 6 | sn1 Apex | 70.2 | 796 | 1,016 | rtx4090* | 4 | 56% |
| 7 | sn67 Harnyx | 69.5 | 11.01 | 1,022 | cpu-small | 116 | 32% |
| 8 | sn107 Minos | 68.7 | 337 | 28,520 | cpu-small | 20 | 80% |
| 9 | sn56 Gradients | 68.4 | 460 | 5,432 | rtx4090* | 9 | 46% |
| 10 | sn111 Claims | 66.5 | 276 | 2,479 | rtx4090* | 5 | 70% |
| 11 | sn124 Swarm | 66.5 | 274 | 880 | rtx4090* | 25 | 11% |
| 12 | sn38 ChronoLLM | 66 | 99.89 | 884 | cpu-small | 10 | 52% |
| 13 | sn62 Ridges | 65.7 | 206 | 1,397 | rtx4090* | 23 | 17% |
| 14 | sn15 ORO | 61.9 | 3.73 | 20,492 | cpu-small | 21 | 100% |
| 15 | sn74 Gittensor | 61.8 | 67.05 | 187 | rtx4090* | 11 | 61% |
| 16 | sn28 SayGM | 61.5 | 60.04 | 1,285 | rtx4090* | 66 | 13% |
| 17 | sn23 Trishool | 61 | 690 | 690 = | cpu-small | 2 | 80% |
| 18 | sn81 Reliquary | 60.4 | 41.79 | 117 | rtx4090* | 27 | 69% |
| 19 | sn61 RedTeam | 58.6 | 24.82 | 2,132 | rtx4090* | 122 | 21% |
| 20 | sn51 lium.io | 57.3 | 24.67 | 1,618 | rtx4090* | 64 | 83% |

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
| concentrated (30–60%) | 25 |
| dominated (60–90%) | 18 |
| captured (>90%) | 22 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 97 |
| min_compute.yml (curated) | 11 |
| code-submission (validator runs it) | 10 |
| README keywords (GUESS) | 9 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-09-19T06:16 | sn15 | RELEASE | sn15 released v2.0.27 |
| 2026-09-19T06:16 | sn25 | RELEASE | sn25 released v2026.9.18-1049819730 |
| 2026-09-19T01:25 | sn61 | RELEASE | sn61 released 4.10.6 |
| 2026-09-19T01:25 | sn61 | SCORING_COMMIT | sn61 commit touches scoring: deps: update ada_detection challenge imag |
| 2026-09-19T01:25 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Keep baseline source update independent o |
| 2026-09-19T01:25 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: feat(bounty): python subnet with product |
| 2026-09-18T23:15 | sn10 | BURN_DROP | sn10 burn fell 1.000 -> 0.814 - miners can earn again |
| 2026-09-18T23:15 | sn25 | RELEASE | sn25 released v2026.9.18-1049702080 |
| 2026-09-18T23:15 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Refresh protected verifier integrity mani |
| 2026-09-18T23:15 | sn71 | README_TASK_DIFF | sn71 README task/scoring sections changed |
| 2026-09-18T20:51 | sn15 | RELEASE | sn15 released v2.0.26: fix(proxy): fail over user-simulator from Mistr |
| 2026-09-18T20:51 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: validator: strict > infra boundary — 3/10 |
| 2026-09-18T20:51 | sn45 | SCORING_COMMIT | sn45 commit touches scoring: Score pool audits under a second matcher, |
| 2026-09-18T20:51 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Add Sep18 cancelled rerun302 with fresh j |
| 2026-09-18T20:51 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Merge pull request #169 from Umi-BitSign/ |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

