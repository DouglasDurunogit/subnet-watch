# Subnet watch — dashboard

_snapshot 2026-09-19T01:24:58Z · block 9098383 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 52 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 93 | `miner_burn` < 0.99 |
| Ranked | 93 | passed every gate |
| **Positive margin** | **52** | income beats machine cost |
| New events this window | 4 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 61 | `████████████████████████████` |
| 0–0.2 | 8 | `████` |
| 0.2–0.4 | 7 | `███` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 35 | `████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn4 Targon | 77.8 | 7,639 | 21,447 | rtx4090* | 6 | 52% |
| 2 | sn3 Teutonic | 76.3 | 4,831 | 4,831 = | rtx4090* | 5 | 20% |
| 3 | sn91 cascade | 71.7 | 479 | 1,279 | cpu-small | 5 | 52% |
| 4 | sn102 ConnitoAI | 70.8 | 947 | 1,370 | rtx4090* | 6 | 30% |
| 5 | sn1 Apex | 70.3 | 810 | 1,024 | rtx4090* | 4 | 55% |
| 6 | sn67 Harnyx | 69.2 | 9.99 | 1,278 | cpu-small | 112 | 41% |
| 7 | sn107 Minos | 68.7 | 331 | 28,793 | cpu-small | 20 | 81% |
| 8 | sn56 Gradients | 68.4 | 454 | 5,369 | rtx4090* | 9 | 46% |
| 9 | sn124 Swarm | 66.6 | 275 | 882 | rtx4090* | 25 | 11% |
| 10 | sn15 ORO | 66.1 | 6.56 | 19,944 | cpu-small | 34 | 99% |
| 11 | sn38 ChronoLLM | 65.9 | 97.71 | 865 | cpu-small | 10 | 52% |
| 12 | sn62 Ridges | 65.7 | 204 | 1,382 | rtx4090* | 23 | 17% |
| 13 | sn111 Claims | 64.6 | 162 | 2,903 | rtx4090* | 5 | 82% |
| 14 | sn74 Gittensor | 61.8 | 67.56 | 191 | rtx4090* | 11 | 61% |
| 15 | sn23 Trishool | 61.1 | 693 | 693 = | cpu-small | 2 | 80% |
| 16 | sn28 SayGM | 60.9 | 50.44 | 1,948 | rtx4090* | 61 | 20% |
| 17 | sn81 Reliquary | 60.5 | 42.80 | 108 | rtx4090* | 30 | 66% |
| 18 | sn51 lium.io | 60 | 45.93 | 1,697 | rtx4090* | 62 | 83% |
| 19 | sn61 RedTeam | 58.6 | 24.51 | 2,122 | rtx4090* | 122 | 21% |
| 20 | sn80 OpenRoboto | 56.3 | 427 | 1,516 | rtx4090* | 5 | 43% |

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
| dominated (60–90%) | 19 |
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
| 2026-09-18T17:50 | sn12 | RELEASE | sn12 released validator-staging-2026-09-18-35368036673-626-1: fix: evi |
| 2026-09-18T17:50 | sn12 | SCORING_COMMIT | sn12 commit touches scoring: fix: evict old neurons in allowance evict |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

