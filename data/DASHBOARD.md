# Subnet watch — dashboard

_snapshot 2026-08-18T22:36:50Z · block 8874654 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 49 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 92 | `miner_burn` < 0.99 |
| Ranked | 92 | passed every gate |
| **Positive margin** | **49** | income beats machine cost |
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
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 36 | `████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 78.1 | 97.66 | 189 | cpu-small | 10 | 20% |
| 2 | sn67 Harnyx | 71.9 | 19.97 | 426 | cpu-small | 131 | 13% |
| 3 | sn26 Perturb | 70.6 | 38.85 | 71.84 | rtx3060 | 10 | 70% |
| 4 | sn1 Apex | 70.2 | 793 | 1,072 | rtx4090* | 4 | 54% |
| 5 | sn56 Gradients | 69.4 | 618 | 925 | rtx4090* | 5 | 72% |
| 6 | sn91 cascade | 69.2 | 578 | 2,335 | rtx4090* | 5 | 52% |
| 7 | sn41 Almanac | 69.1 | 10.58 | 35.83 | cpu-small | 75 | 67% |
| 8 | sn15 ORO | 69 | 13.24 | 15,596 | cpu-small | 67 | 95% |
| 9 | sn62 Ridges | 68.3 | 450 | 2,087 | rtx4090* | 6 | 40% |
| 10 | sn38 ChronoLLM | 67.4 | 142 | 3,015 | cpu-small | 10 | 52% |
| 11 | sn96 Verathos | 66 | 12.39 | 374 | rtx4090 | 89 | 41% |
| 12 | sn107 Minos | 64.1 | 111 | 33,237 | cpu-small | 20 | 90% |
| 13 | sn21 AdTAO | 64.1 | 3.47 | 715 | cpu-small | 16 | 37% |
| 14 | sn85 Vidaio | 63.9 | 121 | 369 | rtx4090* | 13 | 42% |
| 15 | sn28 gm | 62.9 | 91.23 | 1,213 | rtx4090* | 39 | 19% |
| 16 | sn53 engy | 62.8 | 86.68 | 2,047 | rtx4090 | 144 | 11% |
| 17 | sn55 NIOME | 61.2 | 53.32 | 465 | rtx4090* | 11 | 30% |
| 18 | sn51 lium.io | 60.6 | 51.05 | 858 | rtx4090* | 54 | 82% |
| 19 | sn81 Reliquary | 59.5 | 31.46 | 171 | rtx4090* | 41 | 52% |
| 20 | sn68 NOVA | 54.9 | 7,668 | 7,668 = | rtx4090* | 1 | 100% |

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
| concentrated (30–60%) | 18 |
| dominated (60–90%) | 18 |
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
| 2026-08-18T17:39 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: validator: daily-stream API path crashed  |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

