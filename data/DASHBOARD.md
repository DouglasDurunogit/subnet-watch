# Subnet watch — dashboard

_snapshot 2026-09-09T15:19:48Z · block 9030801 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 59 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 92 | `miner_burn` < 0.99 |
| Ranked | 93 | passed every gate |
| **Positive margin** | **59** | income beats machine cost |
| New events this window | 6 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 62 | `████████████████████████████` |
| 0–0.2 | 8 | `████` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 3 | `█` |
| ≥0.99 dead | 36 | `████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn114 SOMA | 87.2 | 985 | 7,890 | cpu-small | 4 | 80% |
| 2 | sn107 Minos | 83.7 | 425 | 36,014 | cpu-small | 20 | 80% |
| 3 | sn92 MicroTensor | 79.1 | 128 | 386 | cpu-small | 9 | 50% |
| 4 | sn3 Teutonic | 76 | 4,484 | 4,484 = | rtx4090* | 5 | 20% |
| 5 | sn56 Gradients | 72.2 | 1,431 | 5,883 | rtx4090* | 7 | 47% |
| 6 | sn15 ORO | 71.9 | 28.61 | 26,111 | cpu-small | 76 | 92% |
| 7 | sn67 Harnyx | 71.7 | 19.27 | 100 | cpu-small | 125 | 15% |
| 8 | sn102 ConnitoAI | 71 | 998 | 1,669 | rtx4090* | 6 | 28% |
| 9 | sn91 cascade | 70.3 | 822 | 3,313 | rtx4090* | 5 | 52% |
| 10 | sn14 Cacheon | 69.7 | 684 | 1,266 | rtx4090* | 12 | 18% |
| 11 | sn96 Verathos | 69.7 | 31.55 | 185 | rtx4090 | 84 | 30% |
| 12 | sn11 TrajectoryRL | 68.8 | 6,848 | 6,848 = | cpu-small | 1 | 100% |
| 13 | sn62 Ridges | 67.9 | 398 | 1,254 | rtx4090* | 13 | 26% |
| 14 | sn80 OpenRoboto | 67.8 | 382 | 1,358 | rtx4090* | 5 | 43% |
| 15 | sn61 RedTeam | 67.4 | 340 | 574 | rtx4090* | 35 | 6% |
| 16 | sn38 ChronoLLM | 66 | 100 | 1,373 | cpu-small | 10 | 52% |
| 17 | sn111 Claims | 65.2 | 198 | 3,513 | rtx4090* | 5 | 82% |
| 18 | sn121 sundae_bar | 63.1 | 1,261 | 1,261 = | cpu-small | 2 | 60% |
| 19 | sn23 Trishool | 60.7 | 624 | 624 = | cpu-small | 2 | 80% |
| 20 | sn41 Almanac | 60.7 | 42.74 | 93.50 | cpu-small | 85 | 3% |

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
| wide (<30%) | 28 |
| concentrated (30–60%) | 21 |
| dominated (60–90%) | 18 |
| captured (>90%) | 21 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 99 |
| min_compute.yml (curated) | 11 |
| code-submission (validator runs it) | 10 |
| README keywords (GUESS) | 7 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-09-09T15:20 | sn1 | RELEASE | sn1 released v4.4.5 |
| 2026-09-09T15:20 | sn28 | RELEASE | sn28 released v0.4.16-dev |
| 2026-09-09T15:20 | sn28 | SCORING_COMMIT | sn28 commit touches scoring: Anchor deployment staleness to the last s |
| 2026-09-09T15:20 | sn28 | README_TASK_DIFF | sn28 README task/scoring sections changed |
| 2026-09-09T15:20 | sn45 | README_TASK_DIFF | sn45 README task/scoring sections changed |
| 2026-09-09T15:20 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Bind dead preflight verifier removal |
| 2026-09-09T11:41 | sn61 | RELEASE | sn61 released 4.10.3 |
| 2026-09-09T11:41 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: Merge pull request #80 from conjectures-i |
| 2026-09-09T11:41 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Preserve terminal company scores across j |
| 2026-09-09T11:41 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Add legacy validator transition hold |
| 2026-09-09T11:41 | sn89 | SCORING_COMMIT | sn89 commit touches scoring: scoring: points-path earning gate is the  |
| 2026-09-09T11:41 | sn97 | SCORING_COMMIT | sn97 commit touches scoring: fix: show all task results for benchmark  |
| 2026-09-09T11:41 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: docs: clarify Ubuntu validator env setup |
| 2026-09-09T11:41 | sn114 | SCORING_COMMIT | sn114 commit touches scoring: Cap automatic run restarts per miner tas |
| 2026-09-09T06:19 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-2962: delete the dead hashcat scoring |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

