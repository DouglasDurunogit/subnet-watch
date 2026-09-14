# Subnet watch — dashboard

_snapshot 2026-09-14T13:23:21Z · block 9066146 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 57 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 91 | `miner_burn` < 0.99 |
| Ranked | 92 | passed every gate |
| **Positive margin** | **57** | income beats machine cost |
| New events this window | 17 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 62 | `████████████████████████████` |
| 0–0.2 | 10 | `█████` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 6 | `███` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 37 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn114 SOMA | 87.3 | 997 | 7,980 | cpu-small | 3 | 80% |
| 2 | sn92 MicroTensor | 80.6 | 184 | 555 | cpu-small | 8 | 30% |
| 3 | sn91 cascade | 74.3 | 1,040 | 2,775 | cpu-small | 5 | 52% |
| 4 | sn67 Harnyx | 69.4 | 10.96 | 10.96 = | cpu-small | 221 | 15% |
| 5 | sn96 Verathos | 69.3 | 28.51 | 220 | rtx4090 | 79 | 30% |
| 6 | sn107 Minos | 68.9 | 350 | 29,681 | cpu-small | 20 | 80% |
| 7 | sn11 TrajectoryRL | 68.2 | 5,770 | 5,770 = | cpu-small | 1 | 100% |
| 8 | sn80 OpenRoboto | 67.6 | 366 | 1,303 | rtx4090* | 5 | 43% |
| 9 | sn38 ChronoLLM | 66.8 | 123 | 1,680 | cpu-small | 10 | 52% |
| 10 | sn124 Swarm | 66.4 | 266 | 864 | rtx4090* | 25 | 11% |
| 11 | sn61 RedTeam | 64.7 | 156 | 241 | rtx4090* | 81 | 2% |
| 12 | sn111 Claims | 64.5 | 161 | 2,878 | rtx4090* | 5 | 82% |
| 13 | sn3 Teutonic | 63.9 | 4,144 | 4,144 = | rtx4090* | 5 | 20% |
| 14 | sn28 SayGM | 63.4 | 105 | 2,812 | rtx4090* | 41 | 18% |
| 15 | sn55 NIOME | 61.9 | 65.03 | 541 | rtx4090* | 11 | 29% |
| 16 | sn69 Herald | 61.1 | 1,818 | 1,818 = | rtx4090* | 3 | 33% |
| 17 | sn81 Reliquary | 60.8 | 46.77 | 214 | rtx4090* | 81 | 5% |
| 18 | sn23 Trishool | 60.3 | 553 | 553 = | cpu-small | 2 | 80% |
| 19 | sn62 Ridges | 60.2 | 38.88 | 1,150 | rtx4090* | 18 | 35% |
| 20 | sn21 AdTAO | 58.5 | 10.37 | 17.02 | cpu-small | 21 | 34% |

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
| wide (<30%) | 27 |
| concentrated (30–60%) | 22 |
| dominated (60–90%) | 17 |
| captured (>90%) | 22 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 95 |
| README keywords (GUESS) | 11 |
| min_compute.yml (curated) | 11 |
| code-submission (validator runs it) | 10 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-09-14T13:23 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: chore(validator): bump oro-env-runtime 0. |
| 2026-09-14T13:23 | sn25 | RELEASE | sn25 released v2026.9.14-1045806490 |
| 2026-09-14T13:23 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Validate capture ownership against growin |
| 2026-09-14T13:23 | sn28 | SCORING_COMMIT | sn28 commit touches scoring: refactor(near): fold the path check into  |
| 2026-09-14T13:23 | sn38 | SCORING_COMMIT | sn38 commit touches scoring: Update validator image to the latest vers |
| 2026-09-14T13:23 | sn40 | README_TASK_DIFF | sn40 README task/scoring sections changed |
| 2026-09-14T13:23 | sn51 | RELEASE | sn51 released executor-v1.128 |
| 2026-09-14T13:23 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-3247 - [P1] lium_protocol: the valida |
| 2026-09-14T13:23 | sn66 | README_TASK_DIFF | sn66 README task/scoring sections changed |
| 2026-09-14T13:23 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-09-14T13:23 | sn67 | README_TASK_DIFF | sn67 README task/scoring sections changed |
| 2026-09-14T13:23 | sn69 | BURN_DROP | sn69 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-09-14T13:23 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Prioritize pending evaluator evidence ove |
| 2026-09-14T13:23 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: Merge pull request #278 from TensorLink-A |
| 2026-09-14T13:23 | sn91 | README_TASK_DIFF | sn91 README task/scoring sections changed |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

