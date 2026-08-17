# Subnet watch — dashboard

_snapshot 2026-08-17T03:09:55Z · block 8861619 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 52 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 89 | `miner_burn` < 0.99 |
| Ranked | 89 | passed every gate |
| **Positive margin** | **52** | income beats machine cost |
| New events this window | 0 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 61 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 7 | `███` |
| 0.6–0.8 | 6 | `███` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 39 | `██████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 77.9 | 106 | 33,199 | cpu-small | 20 | 90% |
| 2 | sn67 Harnyx | 72.1 | 21.45 | 401 | cpu-small | 126 | 11% |
| 3 | sn26 Perturb | 70.8 | 40.68 | 74.62 | rtx3060 | 10 | 70% |
| 4 | sn1 Apex | 70.6 | 890 | 998 | rtx4090* | 4 | 53% |
| 5 | sn76 Phylax | 70.5 | 13.35 | 156 | cpu-small | 10 | 29% |
| 6 | sn96 Verathos | 70 | 33.40 | 373 | rtx4090 | 57 | 41% |
| 7 | sn91 cascade | 69.1 | 570 | 2,307 | rtx4090* | 5 | 51% |
| 8 | sn15 ORO | 68.9 | 12.72 | 21.57 | cpu-small | 67 | 94% |
| 9 | sn85 Vidaio | 68.8 | 522 | 525 | rtx4090* | 10 | 17% |
| 10 | sn56 Gradients | 68.7 | 504 | 963 | rtx4090* | 7 | 68% |
| 11 | sn41 Almanac | 68.7 | 9.77 | 53.61 | cpu-small | 75 | 69% |
| 12 | sn62 Ridges | 68.5 | 472 | 2,187 | rtx4090* | 6 | 40% |
| 13 | sn21 AdTAO | 67.7 | 7.67 | 34.38 | cpu-small | 88 | 45% |
| 14 | sn38 ChronoLLM | 66.1 | 101 | 1,379 | cpu-small | 10 | 52% |
| 15 | sn124 Swarm | 65.9 | 225 | 723 | rtx4090* | 24 | 11% |
| 16 | sn98 NeverPlayAlone | 64.1 | 1,698 | 1,698 = | cpu-small | 1 | 100% |
| 17 | sn55 NIOME | 61.4 | 56.24 | 487 | rtx4090* | 11 | 29% |
| 18 | sn28 gm | 61.2 | 55.38 | 2,192 | rtx4090* | 43 | 24% |
| 19 | sn51 lium.io | 59.3 | 36.84 | 2,577 | rtx4090* | 56 | 77% |
| 20 | sn60 Bitsec.ai | 59.1 | 384 | 384 = | cpu-small | 3 | 50% |

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
| concentrated (30–60%) | 19 |
| dominated (60–90%) | 16 |
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
| 2026-08-17T01:52 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Bound validator worker startup verificati |
| 2026-08-16T17:31 | sn100 | RELEASE | sn100 released v3.3.24 |
| 2026-08-16T17:03 | sn85 | SCORING_COMMIT | sn85 commit touches scoring: retry inviting rejected miner UIDs in com |
| 2026-08-16T16:38 | sn75 | SCORING_COMMIT | sn75 commit touches scoring: Merge pull request #49 from thenervelab/f |
| 2026-08-16T16:00 | sn100 | RELEASE | sn100 released v3.3.23 |
| 2026-08-16T13:40 | sn68 | SCORING_COMMIT | sn68 commit touches scoring: discard individual validator processing f |
| 2026-08-16T12:00 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: Download only the tasks a validator drew |
| 2026-08-16T08:44 | sn100 | RELEASE | sn100 released v3.3.22 |
| 2026-08-16T07:41 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: Match CWEs numerically, draw tasks per va |
| 2026-08-16T06:04 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-08-16T06:04 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Preserve production clocks in parity vali |
| 2026-08-16T04:08 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Regenerate validator protected workflow m |
| 2026-08-16T01:55 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Fix validator RPC boundary fixture |
| 2026-08-16T01:55 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: Implement resilient batch scoring and wi |
| 2026-08-15T23:01 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: Raise tasks per round across all four tra |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

