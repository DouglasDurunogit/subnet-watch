# Subnet watch — dashboard

_snapshot 2026-08-18T15:42:24Z · block 8872582 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 52 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 91 | `miner_burn` < 0.99 |
| Ranked | 91 | passed every gate |
| **Positive margin** | **52** | income beats machine cost |
| New events this window | 8 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 62 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 6 | `███` |
| 0.6–0.8 | 6 | `███` |
| 0.8–0.99 | 8 | `████` |
| ≥0.99 dead | 37 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 78.2 | 98.17 | 190 | cpu-small | 10 | 20% |
| 2 | sn21 AdTAO | 75.7 | 54.07 | 219 | cpu-small | 16 | 43% |
| 3 | sn67 Harnyx | 71.8 | 19.94 | 425 | cpu-small | 130 | 13% |
| 4 | sn26 Perturb | 70.7 | 39.30 | 72.16 | rtx3060 | 10 | 70% |
| 5 | sn1 Apex | 70.4 | 824 | 1,075 | rtx4090* | 4 | 53% |
| 6 | sn56 Gradients | 69.5 | 637 | 932 | rtx4090* | 5 | 72% |
| 7 | sn41 Almanac | 69 | 10.50 | 35.94 | cpu-small | 75 | 67% |
| 8 | sn91 cascade | 68.7 | 502 | 2,031 | rtx4090* | 5 | 51% |
| 9 | sn62 Ridges | 68.4 | 453 | 2,099 | rtx4090* | 6 | 40% |
| 10 | sn38 ChronoLLM | 67.5 | 146 | 3,091 | cpu-small | 10 | 52% |
| 11 | sn11 TrajectoryRL | 67 | 4,096 | 4,096 = | cpu-small | 1 | 100% |
| 12 | sn15 ORO | 67 | 10.31 | 12,378 | cpu-small | 67 | 95% |
| 13 | sn96 Verathos | 66.9 | 15.36 | 415 | rtx4090 | 79 | 41% |
| 14 | sn85 Vidaio | 64.2 | 129 | 1,302 | rtx4090* | 13 | 42% |
| 15 | sn107 Minos | 64 | 115 | 33,321 | cpu-small | 20 | 90% |
| 16 | sn81 Reliquary | 63 | 90.28 | 422 | rtx4090* | 36 | 10% |
| 17 | sn53 engy | 63 | 89.97 | 2,118 | rtx4090 | 144 | 11% |
| 18 | sn55 NIOME | 61.4 | 56.18 | 475 | rtx4090* | 11 | 29% |
| 19 | sn51 lium.io | 59.6 | 39.56 | 930 | rtx4090* | 55 | 82% |
| 20 | sn60 Bitsec.ai | 58.9 | 362 | 362 = | cpu-small | 3 | 50% |

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
| concentrated (30–60%) | 16 |
| dominated (60–90%) | 19 |
| captured (>90%) | 27 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 102 |
| code-submission (validator runs it) | 10 |
| min_compute.yml (curated) | 9 |
| README keywords (GUESS) | 6 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-08-18T15:42 | sn53 | SCORING_COMMIT | sn53 commit touches scoring: miner: tee_miner, a pure gateway leg with |
| 2026-08-18T15:42 | sn108 | SCORING_COMMIT | sn108 commit touches scoring: Burn 60% of miner emission, split the ot |
| 2026-08-18T14:48 | sn1 | RELEASE | sn1 released v4.3.3 |
| 2026-08-18T14:48 | sn23 | SCORING_COMMIT | sn23 commit touches scoring: Merge pull request #47 from TrishoolAI/fe |
| 2026-08-18T14:48 | sn28 | RELEASE | sn28 released v0.4.5 |
| 2026-08-18T14:48 | sn28 | SCORING_COMMIT | sn28 commit touches scoring: Release gm-miner v0.4.5 |
| 2026-08-18T14:48 | sn33 | SCORING_COMMIT | sn33 commit touches scoring: Merge pull request #135 from afterpartyai |
| 2026-08-18T14:48 | sn33 | README_TASK_DIFF | sn33 README task/scoring sections changed |
| 2026-08-18T13:55 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: test: lock v4 canonical reward flow |
| 2026-08-18T13:55 | sn108 | SCORING_COMMIT | sn108 commit touches scoring: Docs: the eligible-miner gate is 50 acti |
| 2026-08-18T13:55 | sn108 | README_TASK_DIFF | sn108 README task/scoring sections changed |
| 2026-08-18T13:05 | sn2 | BURN_DROP | sn2 burn fell 1.000 -> 0.825 - miners can earn again |
| 2026-08-18T12:04 | sn10 | README_TASK_DIFF | sn10 README task/scoring sections changed |
| 2026-08-18T10:55 | sn65 | SCORING_COMMIT | sn65 commit touches scoring: Merge pull request #4 from taofu-labs/doc |
| 2026-08-18T10:55 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

