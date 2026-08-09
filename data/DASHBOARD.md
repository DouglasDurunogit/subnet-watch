# Subnet watch — dashboard

_snapshot 2026-08-09T13:29:54Z · block 8807128 · run_status **ok**_

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
| New events this window | 2 | see ALARMS.md |

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
| 1 | sn107 Minos | 78.4 | 121 | 35,683 | cpu-small | 20 | 90% |
| 2 | sn76 Phylax | 75 | 43.98 | 209 | cpu-small | 10 | 33% |
| 3 | sn67 Harnyx | 70.8 | 15.33 | 875 | cpu-small | 155 | 22% |
| 4 | sn91 cascade | 70.3 | 801 | 2,742 | rtx4090* | 5 | 48% |
| 5 | sn1 Apex | 70.2 | 785 | 1,619 | rtx4090* | 4 | 47% |
| 6 | sn96 Verathos | 69.5 | 29.67 | 206 | rtx4090 | 64 | 44% |
| 7 | sn41 Almanac | 69.5 | 11.97 | 35.43 | cpu-small | 67 | 71% |
| 8 | sn26 Perturb | 68.4 | 22.49 | 43.00 | rtx3060 | 11 | 50% |
| 9 | sn62 Ridges | 68.3 | 449 | 2,080 | rtx4090* | 7 | 35% |
| 10 | sn100 BASE | 68.1 | 414 | 1,680 | rtx4090* | 5 | 50% |
| 11 | sn15 ORO | 67.7 | 9.54 | 19.68 | cpu-small | 72 | 94% |
| 12 | sn11 TrajectoryRL | 67.6 | 4,839 | 4,839 = | cpu-small | 1 | 100% |
| 13 | sn38 ChronoLLM | 65.7 | 218 | 3,656 | rtx4090* | 10 | 52% |
| 14 | sn28 gm | 65.5 | 197 | 4,227 | rtx4090* | 23 | 43% |
| 15 | sn21 AdTAO | 65.5 | 4.83 | 22.28 | cpu-small | 142 | 45% |
| 16 | sn80 OpenRoboto | 65.1 | 172 | 623 | rtx4090* | 4 | 91% |
| 17 | sn61 RedTeam | 63.2 | 97.50 | 275 | rtx4090* | 42 | 6% |
| 18 | sn51 lium.io | 59.6 | 40.74 | 3,068 | rtx4090* | 47 | 65% |
| 19 | sn6 Numinous | 59.1 | 30.10 | 345 | cpu-small | 18 | 19% |
| 20 | sn85 Vidaio | 56.7 | 486 | 551 | rtx4090* | 10 | 16% |

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
| 2026-08-09T13:30 | sn96 | RELEASE | sn96 released v0.1.32 - Miner Hard-Proof Transport |
| 2026-08-09T13:30 | sn96 | SCORING_COMMIT | sn96 commit touches scoring: fix: align miner proxy with hard proof de |
| 2026-08-09T10:49 | sn61 | RELEASE | sn61 released 4.9.3 |
| 2026-08-09T10:49 | sn61 | SCORING_COMMIT | sn61 commit touches scoring: deps: update challenge image version for  |
| 2026-08-09T10:49 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-08-09T10:49 | sn96 | RELEASE | sn96 released v0.1.31 - Validator Auto-Update Drain |
| 2026-08-09T10:49 | sn96 | SCORING_COMMIT | sn96 commit touches scoring: fix: drain validator work before auto-upd |
| 2026-08-09T09:53 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Use fresh identities for scorer retries |
| 2026-08-09T09:02 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Retry transient company homepage verifica |
| 2026-08-09T09:02 | sn96 | RELEASE | sn96 released v0.1.30 - Gleipnir FP8 Runtime Precision |
| 2026-08-09T08:07 | sn2 | BURN_DROP | sn2 burn fell 1.000 -> 0.826 - miners can earn again |
| 2026-08-09T05:16 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: Move inference cost off the validator and |
| 2026-08-09T02:25 | sn6 | BURN_DROP | sn6 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-08-09T02:25 | sn61 | RELEASE | sn61 released 4.9.2 |
| 2026-08-09T02:25 | sn61 | SCORING_COMMIT | sn61 commit touches scoring: refactor: update minimum acceptable score |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

