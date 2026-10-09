# Subnet watch — dashboard

_snapshot 2026-10-09T00:41:47Z · block 9241992 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 53 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 102 | `miner_burn` < 0.99 |
| Ranked | 102 | passed every gate |
| **Positive margin** | **53** | income beats machine cost |
| New events this window | 8 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 69 | `████████████████████████████` |
| 0–0.2 | 6 | `██` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 6 | `██` |
| 0.6–0.8 | 7 | `███` |
| 0.8–0.99 | 10 | `████` |
| ≥0.99 dead | 26 | `███████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn3 Teutonic | 74.7 | 3,063 | 6,135 | rtx4090* | 5 | 30% |
| 2 | sn41 Almanac | 73.8 | 33.99 | 112 | cpu-small | 137 | 2% |
| 3 | sn91 cascade | 72 | 519 | 2,080 | cpu-small | 5 | 52% |
| 4 | sn80 OpenRoboto | 69.1 | 562 | 2,945 | rtx4090* | 7 | 35% |
| 5 | sn1 Apex | 68.7 | 501 | 1,017 | rtx4090* | 4 | 70% |
| 6 | sn38 ChronoLLM | 68.7 | 209 | 953 | cpu-small | 9 | 52% |
| 7 | sn67 Harnyx | 68.5 | 7.94 | 961 | cpu-small | 138 | 35% |
| 8 | sn15 ORO | 67.5 | 7.89 | 18,258 | cpu-small | 59 | 97% |
| 9 | sn4 Targon | 66.7 | 9,717 | 28,650 | rtx4090* | 5 | 70% |
| 10 | sn26 Perturb | 66.3 | 244 | 408 | rtx3060 | 4 | 60% |
| 11 | sn62 Ridges | 63.5 | 105 | 1,287 | rtx4090* | 34 | 17% |
| 12 | sn120 Affine | 62.9 | 136 | 374 | rtx4090* | 245 | 1% |
| 13 | sn65 True Performance | 62.3 | 77.71 | 164 | rtx4090* | 6 | 75% |
| 14 | sn61 RedTeam | 62.2 | 76.38 | 102 | rtx4090* | 126 | 1% |
| 15 | sn53 engy | 60 | 1,292 | 4,273 | rtx4090 | 18 | 17% |
| 16 | sn23 Trishool | 59.3 | 416 | 416 = | cpu-small | 3 | 80% |
| 17 | sn28 SayGM | 59.2 | 31.22 | 2,363 | rtx4090* | 72 | 30% |
| 18 | sn74 Gittensor | 57.9 | 22.44 | 145 | rtx4090* | 21 | 50% |
| 19 | sn111 Claims | 57.8 | 19.58 | 235 | rtx4090* | 6 | 90% |
| 20 | sn5 Hone | 57.7 | 33.47 | 36.10 | rtx4090* | 243 | 0% |

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
| concentrated (30–60%) | 23 |
| dominated (60–90%) | 28 |
| captured (>90%) | 25 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 96 |
| README keywords (GUESS) | 12 |
| min_compute.yml (curated) | 10 |
| code-submission (validator runs it) | 9 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-10-09T00:42 | sn25 | RELEASE | sn25 released v2026.10.8-1066946420 |
| 2026-10-09T00:42 | sn37 | BURN_DROP | sn37 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-10-09T00:42 | sn62 | RELEASE | sn62 released v0.3.10 |
| 2026-10-09T00:42 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge pull request #295 from leadpoet/fix |
| 2026-10-09T00:42 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Select policy-budget miner release and re |
| 2026-10-09T00:42 | sn116 | RELEASE | sn116 released worker-images-v3 |
| 2026-10-09T00:42 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Merge pull request #846 from carbonphysi |
| 2026-10-09T00:42 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Confirm fresh public epoch and authentic |
| 2026-10-08T20:40 | sn25 | RELEASE | sn25 released v2026.10.8-1066912010 |
| 2026-10-08T20:40 | sn41 | SCORING_COMMIT | sn41 commit touches scoring: Merge pull request #55 from corvxai/forec |
| 2026-10-08T20:40 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-3769 - Validator: dropped SSH transpo |
| 2026-10-08T20:40 | sn58 | SCORING_COMMIT | sn58 commit touches scoring: fix(miner): `attune miner status` checks  |
| 2026-10-08T20:40 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Allow bounded score batch RPC reads to fi |
| 2026-10-08T20:40 | sn90 | SCORING_COMMIT | sn90 commit touches scoring: docs(nemotron-omni): 256k context verifie |
| 2026-10-08T20:40 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Record the owner's canary answers 2-4 in |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

