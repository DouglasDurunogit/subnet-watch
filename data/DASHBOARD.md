# Subnet watch — dashboard

_snapshot 2026-08-18T13:54:58Z · block 8872045 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 53 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 91 | `miner_burn` < 0.99 |
| Ranked | 91 | passed every gate |
| **Positive margin** | **53** | income beats machine cost |
| New events this window | 4 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 63 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 3 | `█` |
| 0.4–0.6 | 6 | `███` |
| 0.6–0.8 | 7 | `███` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 37 | `████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 78.1 | 97.76 | 189 | cpu-small | 10 | 20% |
| 2 | sn67 Harnyx | 71.8 | 19.88 | 424 | cpu-small | 129 | 13% |
| 3 | sn26 Perturb | 70.7 | 39.22 | 72.03 | rtx3060 | 10 | 70% |
| 4 | sn1 Apex | 70.4 | 828 | 1,079 | rtx4090* | 4 | 53% |
| 5 | sn56 Gradients | 69.1 | 562 | 922 | rtx4090* | 6 | 70% |
| 6 | sn41 Almanac | 69.1 | 10.70 | 49.08 | cpu-small | 74 | 67% |
| 7 | sn91 cascade | 68.8 | 519 | 2,100 | rtx4090* | 5 | 51% |
| 8 | sn62 Ridges | 68.3 | 451 | 2,093 | rtx4090* | 6 | 40% |
| 9 | sn15 ORO | 67.7 | 10.10 | 12,147 | cpu-small | 67 | 95% |
| 10 | sn21 AdTAO | 67.7 | 7.75 | 34.70 | cpu-small | 88 | 45% |
| 11 | sn38 ChronoLLM | 67.5 | 147 | 3,110 | cpu-small | 10 | 52% |
| 12 | sn96 Verathos | 67.4 | 17.54 | 385 | rtx4090 | 75 | 40% |
| 13 | sn11 TrajectoryRL | 67 | 4,086 | 4,086 = | cpu-small | 1 | 100% |
| 14 | sn124 Swarm | 66.1 | 241 | 722 | rtx4090* | 24 | 11% |
| 15 | sn85 Vidaio | 64.1 | 125 | 1,310 | rtx4090* | 13 | 42% |
| 16 | sn107 Minos | 64.1 | 112 | 33,302 | cpu-small | 20 | 90% |
| 17 | sn81 Reliquary | 63.2 | 96.35 | 451 | rtx4090* | 36 | 11% |
| 18 | sn55 NIOME | 61.5 | 58.28 | 491 | rtx4090* | 11 | 29% |
| 19 | sn28 gm | 60.5 | 44.22 | 2,547 | rtx4090* | 40 | 26% |
| 20 | sn60 Bitsec.ai | 58.9 | 363 | 363 = | cpu-small | 3 | 50% |

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
| wide (<30%) | 26 |
| concentrated (30–60%) | 18 |
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
| 2026-08-18T13:55 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: test: lock v4 canonical reward flow |
| 2026-08-18T13:55 | sn108 | SCORING_COMMIT | sn108 commit touches scoring: Docs: the eligible-miner gate is 50 acti |
| 2026-08-18T13:55 | sn108 | README_TASK_DIFF | sn108 README task/scoring sections changed |
| 2026-08-18T13:05 | sn2 | BURN_DROP | sn2 burn fell 1.000 -> 0.825 - miners can earn again |
| 2026-08-18T12:04 | sn10 | README_TASK_DIFF | sn10 README task/scoring sections changed |
| 2026-08-18T10:55 | sn65 | SCORING_COMMIT | sn65 commit touches scoring: Merge pull request #4 from taofu-labs/doc |
| 2026-08-18T10:55 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-08-18T09:46 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-08-18T08:51 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-2702: verify GPU persistence mode aft |
| 2026-08-18T07:14 | sn85 | SCORING_COMMIT | sn85 commit touches scoring: debug VBR scoring in compression competit |
| 2026-08-18T07:14 | sn89 | SCORING_COMMIT | sn89 commit touches scoring: hf board: keep a re-rolled miner's retire |
| 2026-08-18T05:02 | sn91 | README_TASK_DIFF | sn91 README task/scoring sections changed |
| 2026-08-18T04:21 | sn91 | RELEASE | sn91 released pre-decay-wsd-contract |
| 2026-08-18T04:21 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: audit fixes + miner CLI: warm-start init  |
| 2026-08-18T02:44 | sn15 | RELEASE | sn15 released v1.2.7 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

