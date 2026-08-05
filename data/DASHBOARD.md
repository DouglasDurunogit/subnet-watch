# Subnet watch — dashboard

_snapshot 2026-08-05T12:14:50Z · block 8777955 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 54 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 91 | `miner_burn` < 0.99 |
| Ranked | 91 | passed every gate |
| **Positive margin** | **54** | income beats machine cost |
| New events this window | 8 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 55 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 5 | `███` |
| 0.4–0.6 | 7 | `████` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 10 | `█████` |
| ≥0.99 dead | 37 | `███████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 81 | 201 | 402 | cpu-small | 7 | 25% |
| 2 | sn107 Minos | 77.5 | 97.28 | 28,211 | cpu-small | 20 | 89% |
| 3 | sn60 Bitsec.ai | 76.8 | 2,170 | 2,170 = | cpu-small | 2 | 90% |
| 4 | sn98 NeverPlayAlone | 76 | 1,694 | 1,694 = | cpu-small | 1 | 100% |
| 5 | sn67 Harnyx | 72 | 22.00 | 943 | cpu-small | 155 | 22% |
| 6 | sn91 cascade | 70 | 737 | 2,974 | rtx4090* | 5 | 52% |
| 7 | sn62 Ridges | 69.5 | 637 | 2,618 | rtx4090* | 7 | 35% |
| 8 | sn26 Perturb | 68.9 | 25.44 | 202 | rtx3060 | 11 | 50% |
| 9 | sn41 Almanac | 68.4 | 8.97 | 65.85 | cpu-small | 60 | 78% |
| 10 | sn15 ORO | 67.4 | 8.89 | 10,910 | cpu-small | 72 | 94% |
| 11 | sn74 Gittensor | 66.2 | 244 | 271 | rtx4090* | 9 | 18% |
| 12 | sn124 Swarm | 65.8 | 220 | 633 | rtx4090* | 23 | 10% |
| 13 | sn38 ChronoLLM | 65.5 | 206 | 3,457 | rtx4090* | 10 | 52% |
| 14 | sn21 AdTAO | 65.5 | 4.71 | 21.80 | cpu-small | 142 | 45% |
| 15 | sn80 OpenRoboto | 62.3 | 73.73 | 279 | rtx4090* | 4 | 91% |
| 16 | sn53 engy | 62.2 | 70.91 | 1,564 | rtx4090 | 102 | 11% |
| 17 | sn61 RedTeam | 58.8 | 25.39 | 88.23 | rtx4090* | 90 | 3% |
| 18 | sn101 Tag101 | 57.9 | 0.06 | 0.82 | cpu-small | 235 | 91% |
| 19 | sn102 ConnitoAI | 56.9 | 14.09 | 1,482 | rtx4090* | 9 | 27% |
| 20 | sn51 lium.io | 56.3 | 18.46 | 5,005 | rtx4090* | 46 | 66% |

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
| concentrated (30–60%) | 19 |
| dominated (60–90%) | 22 |
| captured (>90%) | 25 |

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
| 2026-08-05T12:15 | sn12 | RELEASE | sn12 released miner-staging-2026-08-05-31002481795-421-1: fix: replace |
| 2026-08-05T12:15 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: feat(verifiability): W1+W3 — miners can n |
| 2026-08-05T12:15 | sn21 | README_TASK_DIFF | sn21 README task/scoring sections changed |
| 2026-08-05T12:15 | sn61 | RELEASE | sn61 released 4.9.0 |
| 2026-08-05T12:15 | sn61 | SCORING_COMMIT | sn61 commit touches scoring: fix: uncomment validation for miner conta |
| 2026-08-05T12:15 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: Merge pull request #17 from conjectures-i |
| 2026-08-05T12:15 | sn66 | README_TASK_DIFF | sn66 README task/scoring sections changed |
| 2026-08-05T12:15 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-08-05T10:06 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: Make task slug id's permanent |
| 2026-08-05T10:06 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Scope repeated validator weight evidence |
| 2026-08-05T07:16 | sn15 | RELEASE | sn15 released v1.2.5 |
| 2026-08-05T07:16 | sn62 | RELEASE | sn62 released v0.2.5 |
| 2026-08-05T04:24 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: feat(verifiability): daily scoring receip |
| 2026-08-05T04:24 | sn91 | RELEASE | sn91 released worker-v0.5.0 |
| 2026-08-05T00:53 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: Improve silver alignment and scoring |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

