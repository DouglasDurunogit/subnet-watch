# Subnet watch — dashboard

_snapshot 2026-08-18T23:02:59Z · block 8874785 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 48 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 91 | `miner_burn` < 0.99 |
| Ranked | 91 | passed every gate |
| **Positive margin** | **48** | income beats machine cost |
| New events this window | 5 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 64 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 7 | `███` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 37 | `████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 78.1 | 97.30 | 188 | cpu-small | 10 | 20% |
| 2 | sn67 Harnyx | 71.8 | 19.89 | 424 | cpu-small | 133 | 13% |
| 3 | sn26 Perturb | 70.6 | 38.70 | 71.56 | rtx3060 | 10 | 70% |
| 4 | sn1 Apex | 70.2 | 788 | 1,065 | rtx4090* | 4 | 54% |
| 5 | sn56 Gradients | 69.4 | 614 | 922 | rtx4090* | 5 | 72% |
| 6 | sn91 cascade | 69.1 | 576 | 2,327 | rtx4090* | 5 | 52% |
| 7 | sn41 Almanac | 69.1 | 10.53 | 35.69 | cpu-small | 75 | 67% |
| 8 | sn15 ORO | 68.9 | 12.95 | 15,273 | cpu-small | 67 | 95% |
| 9 | sn62 Ridges | 68.3 | 449 | 2,079 | rtx4090* | 6 | 40% |
| 10 | sn38 ChronoLLM | 67.4 | 142 | 3,004 | cpu-small | 10 | 52% |
| 11 | sn96 Verathos | 66 | 12.46 | 373 | rtx4090 | 89 | 41% |
| 12 | sn107 Minos | 64.1 | 112 | 33,166 | cpu-small | 20 | 90% |
| 13 | sn21 AdTAO | 64.1 | 3.45 | 713 | cpu-small | 16 | 37% |
| 14 | sn85 Vidaio | 63.9 | 120 | 368 | rtx4090* | 13 | 42% |
| 15 | sn28 gm | 62.9 | 90.97 | 1,210 | rtx4090* | 39 | 19% |
| 16 | sn53 engy | 62.8 | 86.25 | 2,038 | rtx4090 | 144 | 11% |
| 17 | sn55 NIOME | 61.3 | 54.34 | 461 | rtx4090* | 11 | 29% |
| 18 | sn81 Reliquary | 61.1 | 51.55 | 158 | rtx4090* | 45 | 37% |
| 19 | sn51 lium.io | 60.8 | 55.01 | 1,052 | rtx4090* | 52 | 81% |
| 20 | sn68 NOVA | 54.9 | 7,618 | 7,618 = | rtx4090* | 1 | 100% |

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
| concentrated (30–60%) | 19 |
| dominated (60–90%) | 16 |
| captured (>90%) | 30 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 101 |
| code-submission (validator runs it) | 10 |
| min_compute.yml (curated) | 10 |
| README keywords (GUESS) | 6 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-08-18T23:03 | sn62 | RELEASE | sn62 released v0.2.9 |
| 2026-08-18T22:37 | sn28 | RELEASE | sn28 released v0.4.6-dev |
| 2026-08-18T22:37 | sn28 | SCORING_COMMIT | sn28 commit touches scoring: Release gm-miner v0.4.6-dev |
| 2026-08-18T22:37 | sn28 | README_TASK_DIFF | sn28 README task/scoring sections changed |
| 2026-08-18T22:37 | sn62 | SCORING_COMMIT | sn62 commit touches scoring: pass pre_screening_policy_version and rem |
| 2026-08-18T21:35 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Verify restored parity database contract |
| 2026-08-18T21:04 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: fix(weights): burn to this validator's ow |
| 2026-08-18T20:36 | sn108 | BURN_DROP | sn108 burn fell 1.000 -> 0.838 - miners can earn again |
| 2026-08-18T20:36 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: feat(scoring): gate Silver coverage on e |
| 2026-08-18T20:36 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Sync Reason v4 (wvk=7) into score, contr |
| 2026-08-18T19:40 | sn75 | SCORING_COMMIT | sn75 commit touches scoring: Merge pull request #51 from thenervelab/f |
| 2026-08-18T19:40 | sn108 | SCORING_COMMIT | sn108 commit touches scoring: docs(validator): clarify CHUTES_API_KEY  |
| 2026-08-18T19:07 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: docs(miner-guide): note that find_product |
| 2026-08-18T19:07 | sn108 | README_TASK_DIFF | sn108 README task/scoring sections changed |
| 2026-08-18T18:13 | sn62 | SCORING_COMMIT | sn62 commit touches scoring: Merge pull request #480 from ridgesai/upd |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

