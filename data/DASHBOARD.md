# Subnet watch — dashboard

_snapshot 2026-09-21T22:50:33Z · block 9119048 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 56 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 96 | `miner_burn` < 0.99 |
| Ranked | 96 | passed every gate |
| **Positive margin** | **56** | income beats machine cost |
| New events this window | 4 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 63 | `████████████████████████████` |
| 0–0.2 | 12 | `█████` |
| 0.2–0.4 | 3 | `█` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 32 | `██████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn4 Targon | 78.5 | 9,230 | 25,916 | rtx4090* | 6 | 53% |
| 2 | sn3 Teutonic | 76.8 | 5,674 | 5,674 = | rtx4090* | 5 | 20% |
| 3 | sn91 cascade | 73 | 698 | 2,797 | cpu-small | 5 | 52% |
| 4 | sn102 ConnitoAI | 70.8 | 927 | 1,367 | rtx4090* | 6 | 28% |
| 5 | sn107 Minos | 69.3 | 384 | 32,011 | cpu-small | 20 | 80% |
| 6 | sn67 Harnyx | 69 | 9.53 | 1,291 | cpu-small | 142 | 36% |
| 7 | sn15 ORO | 68 | 9.98 | 19.92 | cpu-small | 55 | 97% |
| 8 | sn124 Swarm | 67.1 | 326 | 1,039 | rtx4090* | 25 | 11% |
| 9 | sn38 ChronoLLM | 66.9 | 129 | 1,143 | cpu-small | 10 | 52% |
| 10 | sn111 Claims | 66.8 | 296 | 3,064 | rtx4090* | 5 | 73% |
| 11 | sn14 Cacheon | 65.9 | 221 | 2,285 | rtx4090* | 16 | 28% |
| 12 | sn28 SayGM | 62.7 | 86.71 | 1,467 | rtx4090* | 66 | 13% |
| 13 | sn62 Ridges | 62.6 | 79.92 | 2,859 | rtx4090* | 19 | 30% |
| 14 | sn23 Trishool | 61.4 | 768 | 768 = | cpu-small | 2 | 80% |
| 15 | sn74 Gittensor | 61 | 53.15 | 306 | rtx4090* | 14 | 62% |
| 16 | sn61 RedTeam | 59.2 | 28.66 | 909 | rtx4090* | 125 | 9% |
| 17 | sn81 Reliquary | 59.1 | 27.57 | 95.78 | rtx4090* | 24 | 85% |
| 18 | sn51 lium.io | 57.6 | 28.40 | 2,012 | rtx4090* | 68 | 82% |
| 19 | sn80 OpenRoboto | 57.5 | 625 | 2,209 | rtx4090* | 5 | 43% |
| 20 | sn9 iota | 56.2 | 12,870 | 12,870 = | rtx4090* | 3 | 56% |

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
| wide (<30%) | 25 |
| concentrated (30–60%) | 26 |
| dominated (60–90%) | 19 |
| captured (>90%) | 23 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 98 |
| README keywords (GUESS) | 10 |
| min_compute.yml (curated) | 10 |
| code-submission (validator runs it) | 9 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-09-21T22:51 | sn62 | RELEASE | sn62 released v0.3.6 |
| 2026-09-21T22:51 | sn66 | README_TASK_DIFF | sn66 README task/scoring sections changed |
| 2026-09-21T22:51 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: fix(validator): make gateway authoritati |
| 2026-09-21T22:51 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: coverage: unverified / errored_only cell |
| 2026-09-21T19:40 | sn10 | BURN_DROP | sn10 burn fell 1.000 -> 0.810 - miners can earn again |
| 2026-09-21T19:40 | sn10 | SCORING_COMMIT | sn10 commit touches scoring: fix(bench): validate both baselines befor |
| 2026-09-21T19:40 | sn14 | SCORING_COMMIT | sn14 commit touches scoring: Merge pull request #120 from latent-to/re |
| 2026-09-21T19:40 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: fix(validator): fail fast on invalid pref |
| 2026-09-21T19:40 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: verify: the grouping recheck narrows to t |
| 2026-09-21T19:40 | sn26 | SCORING_COMMIT | sn26 commit touches scoring: feat: report model evaluations in the tra |
| 2026-09-21T19:40 | sn26 | README_TASK_DIFF | sn26 README task/scoring sections changed |
| 2026-09-21T19:40 | sn28 | RELEASE | sn28 released v0.4.20 |
| 2026-09-21T19:40 | sn28 | SCORING_COMMIT | sn28 commit touches scoring: chore(release): promote gm-miner 0.4.20 |
| 2026-09-21T19:40 | sn33 | SCORING_COMMIT | sn33 commit touches scoring: Merge pull request #137 from afterpartyai |
| 2026-09-21T19:40 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: docs: use validators consistently in setu |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

