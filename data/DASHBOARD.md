# Subnet watch — dashboard

_snapshot 2026-08-17T23:02:33Z · block 8867582 · run_status **ok**_

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
| New events this window | 3 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 62 | `████████████████████████████` |
| 0–0.2 | 3 | `█` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 6 | `███` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 37 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 78.3 | 101 | 196 | cpu-small | 10 | 20% |
| 2 | sn121 sundae_bar | 74.3 | 1,042 | 1,042 = | cpu-small | 2 | 61% |
| 3 | sn67 Harnyx | 71.9 | 19.89 | 373 | cpu-small | 129 | 11% |
| 4 | sn26 Perturb | 71.2 | 44.94 | 342 | rtx3060 | 10 | 70% |
| 5 | sn1 Apex | 69.8 | 688 | 1,141 | rtx4090* | 4 | 54% |
| 6 | sn96 Verathos | 69.1 | 26.58 | 564 | rtx4090 | 53 | 42% |
| 7 | sn91 cascade | 68.8 | 516 | 2,089 | rtx4090* | 5 | 51% |
| 8 | sn41 Almanac | 68.7 | 9.69 | 53.38 | cpu-small | 75 | 69% |
| 9 | sn62 Ridges | 68.4 | 462 | 2,142 | rtx4090* | 6 | 40% |
| 10 | sn21 AdTAO | 67.8 | 7.95 | 35.52 | cpu-small | 88 | 45% |
| 11 | sn15 ORO | 67.4 | 10.76 | 20.90 | cpu-small | 66 | 94% |
| 12 | sn56 Gradients | 67.3 | 330 | 951 | rtx4090* | 9 | 68% |
| 13 | sn38 ChronoLLM | 66.2 | 104 | 1,419 | cpu-small | 10 | 52% |
| 14 | sn124 Swarm | 65.8 | 223 | 491 | rtx4090* | 24 | 11% |
| 15 | sn85 Vidaio | 64.2 | 131 | 1,314 | rtx4090* | 13 | 42% |
| 16 | sn107 Minos | 64.2 | 115 | 34,133 | cpu-small | 20 | 90% |
| 17 | sn55 NIOME | 61.6 | 59.86 | 502 | rtx4090* | 11 | 29% |
| 18 | sn60 Bitsec.ai | 59 | 372 | 372 = | cpu-small | 3 | 50% |
| 19 | sn28 gm | 59 | 28.77 | 2,079 | rtx4090* | 41 | 35% |
| 20 | sn74 Gittensor | 58.1 | 22.66 | 203 | rtx4090* | 14 | 63% |

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
| concentrated (30–60%) | 21 |
| dominated (60–90%) | 20 |
| captured (>90%) | 26 |

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
| 2026-08-17T23:02 | sn14 | RELEASE | sn14 released v2-finite-debt-preextraction: Pre-extraction snapshot of |
| 2026-08-17T22:36 | sn54 | SCORING_COMMIT | sn54 commit touches scoring: updating miner info |
| 2026-08-17T22:36 | sn62 | RELEASE | sn62 released v0.2.8 |
| 2026-08-17T21:09 | sn21 | RELEASE | sn21 released SN21 training bundle — 10,791 records, refreshed 2026-08 |
| 2026-08-17T19:36 | sn51 | RELEASE | sn51 released executor-v1.121 |
| 2026-08-17T19:36 | sn65 | SCORING_COMMIT | sn65 commit touches scoring: Merge pull request #3 from taofu-labs/val |
| 2026-08-17T18:54 | sn21 | RELEASE | sn21 released SN21 training bundle (1977 records, refreshed 2026-08-17 |
| 2026-08-17T17:55 | sn123 | README_TASK_DIFF | sn123 README task/scoring sections changed |
| 2026-08-17T16:41 | sn10 | SCORING_COMMIT | sn10 commit touches scoring: feat: better miner commit patch logs (#83 |
| 2026-08-17T15:52 | sn121 | BURN_DROP | sn121 burn fell 1.000 -> 0.620 - miners can earn again |
| 2026-08-17T13:03 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: feat: add adaptive miner selection and r |
| 2026-08-17T13:03 | sn114 | SCORING_COMMIT | sn114 commit touches scoring: hotfix(scoring): exclude comp 112 stage  |
| 2026-08-17T11:12 | sn85 | SCORING_COMMIT | sn85 commit touches scoring: treat miner sandbox raised error as miner |
| 2026-08-17T10:46 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-08-17T10:46 | sn85 | SCORING_COMMIT | sn85 commit touches scoring: ensure comp scoring worker can access Mod |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

