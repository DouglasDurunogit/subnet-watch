# Subnet watch — dashboard

_snapshot 2026-11-14T08:54:42Z · block 9503561 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 63 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 100 | `miner_burn` < 0.99 |
| Ranked | 100 | passed every gate |
| **Positive margin** | **63** | income beats machine cost |
| New events this window | 4 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 66 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 2 | `█` |
| 0.6–0.8 | 14 | `██████` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 28 | `████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn42 CADmind | 82.1 | 267 | 267 = | cpu-small | 5 | 20% |
| 2 | sn3 Teutonic | 73.9 | 2,394 | 2,394 = | rtx4090* | 4 | 40% |
| 3 | sn97 Ingot | 72 | 1,334 | 1,334 = | rtx4090* | 5 | 20% |
| 4 | sn34 Yugos | 69.9 | 723 | 6,208 | rtx4090* | 3 | 85% |
| 5 | sn58 Attune | 69 | 551 | 887 | rtx4090* | 5 | 70% |
| 6 | sn41 Almanac | 68.7 | 9.71 | 131 | cpu-small | 154 | 2% |
| 7 | sn67 Harnyx | 68.2 | 7.41 | 127 | cpu-small | 134 | 8% |
| 8 | sn56 Gradients | 68 | 411 | 1,063 | rtx4090* | 6 | 50% |
| 9 | sn15 ORO | 66.2 | 6.41 | 10,145 | cpu-small | 70 | 95% |
| 10 | sn124 Swarm | 65.5 | 204 | 853 | rtx4090* | 10 | 31% |
| 11 | sn53 engy | 65 | 167 | 6,664 | rtx4090 | 23 | 40% |
| 12 | sn38 ChronoLLM | 63.4 | 51.14 | 352 | cpu-small | 9 | 52% |
| 13 | sn120 Affine | 62.1 | 2,502 | 2,502 = | rtx4090* | 10 | 10% |
| 14 | sn121 sundae_bar | 61.5 | 800 | 800 = | cpu-small | 2 | 60% |
| 15 | sn60 Bitsec.ai | 60.7 | 620 | 620 = | cpu-small | 3 | 50% |
| 16 | sn111 Claims | 60.6 | 44.39 | 176 | rtx4090* | 4 | 88% |
| 17 | sn62 Ridges | 59.9 | 35.98 | 658 | rtx4090* | 44 | 15% |
| 18 | sn4 Targon | 58.2 | 11,029 | 20,854 | rtx4090* | 5 | 60% |
| 19 | sn102 ConnitoAI | 57.6 | 636 | 636 | rtx4090* | 4 | 25% |
| 20 | sn5 Hone | 57.3 | 20.56 | 45.12 | rtx4090* | 243 | 1% |

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
| concentrated (30–60%) | 17 |
| dominated (60–90%) | 32 |
| captured (>90%) | 24 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 98 |
| README keywords (GUESS) | 11 |
| min_compute.yml (curated) | 10 |
| code-submission (validator runs it) | 8 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-11-14T08:55 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Merge release/validator-1114-idle-fleet:  |
| 2026-11-14T08:55 | sn94 | SCORING_COMMIT | sn94 commit touches scoring: Admit miner hotels on a declared capacity |
| 2026-11-14T08:55 | sn108 | BURN_DROP | sn108 burn fell 1.000 -> 0.800 - miners can earn again |
| 2026-11-14T08:55 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Re-class: replace the miner-facing marke |
| 2026-11-14T01:52 | sn5 | SCORING_COMMIT | sn5 commit touches scoring: Lengthen the new-miner ramp to 30 observat |
| 2026-11-14T01:52 | sn8 | SCORING_COMMIT | sn8 commit touches scoring: Put new regular miners on the static drawd |
| 2026-11-14T01:52 | sn42 | RELEASE | sn42 released v0.6.11 |
| 2026-11-14T01:52 | sn42 | README_TASK_DIFF | sn42 README task/scoring sections changed |
| 2026-11-14T01:52 | sn66 | RELEASE | sn66 released v2026.11.13.2 |
| 2026-11-14T01:52 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Expect mandatory reward history reader in |
| 2026-11-14T01:52 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Test: the in-range case rows add no scor |
| 2026-11-13T21:41 | sn25 | RELEASE | sn25 released v2026.11.13-1097983310 |
| 2026-11-13T21:41 | sn45 | SCORING_COMMIT | sn45 commit touches scoring: AlphaRidge 4.1.2: re-verify reads a repub |
| 2026-11-13T21:41 | sn66 | RELEASE | sn66 released v2026.11.13 |
| 2026-11-13T21:41 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Preserve verified research pairs when jud |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

