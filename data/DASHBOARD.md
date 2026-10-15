# Subnet watch — dashboard

_snapshot 2026-10-15T05:51:14Z · block 9286738 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 56 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 101 | `miner_burn` < 0.99 |
| Ranked | 101 | passed every gate |
| **Positive margin** | **56** | income beats machine cost |
| New events this window | 8 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 67 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 11 | `█████` |
| 0.8–0.99 | 9 | `████` |
| ≥0.99 dead | 27 | `███████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 81.7 | 264 | 22,444 | cpu-small | 20 | 80% |
| 2 | sn41 Almanac | 70.8 | 16.63 | 132 | cpu-small | 117 | 3% |
| 3 | sn101 Tag101 | 69.9 | 12.12 | 13.07 | cpu-small | 242 | 1% |
| 4 | sn53 engy | 69.3 | 595 | 2,479 | rtx4090 | 24 | 16% |
| 5 | sn91 cascade | 69.2 | 228 | 914 | cpu-small | 5 | 52% |
| 6 | sn96 Verathos | 68.5 | 23.21 | 175 | rtx4090 | 61 | 40% |
| 7 | sn58 Attune | 68.2 | 440 | 709 | rtx4090* | 5 | 71% |
| 8 | sn14 Cacheon | 67.8 | 384 | 639 | rtx4090* | 5 | 77% |
| 9 | sn67 Harnyx | 67.8 | 6.91 | 913 | cpu-small | 119 | 37% |
| 10 | sn79 MVTRX | 66.9 | 6.76 | 33.05 | cpu-small | 247 | 1% |
| 11 | sn4 Targon | 66.6 | 9,239 | 27,243 | rtx4090* | 5 | 70% |
| 12 | sn15 ORO | 66.5 | 6.94 | 15,529 | cpu-small | 58 | 97% |
| 13 | sn7 Allways | 65.5 | 197 | 356 | rtx4090* | 8 | 21% |
| 14 | sn28 SayGM | 64 | 125 | 1,570 | rtx4090* | 66 | 29% |
| 15 | sn62 Ridges | 63.8 | 116 | 1,173 | rtx4090* | 37 | 17% |
| 16 | sn66 conjectures | 63.5 | 107 | 223 | rtx4090* | 4 | 81% |
| 17 | sn120 Affine | 62 | 76.96 | 549 | rtx4090* | 270 | 2% |
| 18 | sn61 RedTeam | 61.5 | 62.47 | 82.06 | rtx4090* | 126 | 1% |
| 19 | sn111 Claims | 59.4 | 31.27 | 2,816 | rtx4090* | 6 | 90% |
| 20 | sn81 Reliquary | 59 | 27.21 | 47.01 | rtx4090* | 7 | 95% |

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
| concentrated (30–60%) | 21 |
| dominated (60–90%) | 30 |
| captured (>90%) | 23 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 95 |
| README keywords (GUESS) | 13 |
| min_compute.yml (curated) | 10 |
| code-submission (validator runs it) | 9 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-10-15T05:51 | sn15 | RELEASE | sn15 released v2.5.2 |
| 2026-10-15T05:51 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: Treat a miner's OpenRouter credit 402 as  |
| 2026-10-15T05:51 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Update the SN25 timeline with the validat |
| 2026-10-15T05:51 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-4071 - [P1] validator: SCORING_EXCLUD |
| 2026-10-15T05:51 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-10-15T05:51 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Merge pull request #266 from Umi-BitSign/ |
| 2026-10-15T05:51 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Merge pull request #1371 from carbonphys |
| 2026-10-15T05:51 | sn118 | BURN_DROP | sn118 burn fell 1.000 -> 0.700 - miners can earn again |
| 2026-10-15T00:57 | sn8 | SCORING_COMMIT | sn8 commit touches scoring: Sync price updates and challenge loop (#95 |
| 2026-10-15T00:57 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Select the startup verified tests and pin |
| 2026-10-14T22:42 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: perf(scoring): read receipts through a sm |
| 2026-10-14T22:42 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: State that any v2 request checkpoint writ |
| 2026-10-14T22:42 | sn28 | RELEASE | sn28 released v0.5.0 |
| 2026-10-14T22:42 | sn28 | SCORING_COMMIT | sn28 commit touches scoring: chore(release): promote gm-miner 0.5.0 (# |
| 2026-10-14T22:42 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Keep stopped reward reconciliation alive  |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

