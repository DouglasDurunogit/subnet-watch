# Subnet watch — dashboard

_snapshot 2026-10-08T20:40:05Z · block 9240787 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 55 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 101 | `miner_burn` < 0.99 |
| Ranked | 101 | passed every gate |
| **Positive margin** | **55** | income beats machine cost |
| New events this window | 8 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 68 | `████████████████████████████` |
| 0–0.2 | 6 | `██` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 8 | `███` |
| 0.8–0.99 | 9 | `████` |
| ≥0.99 dead | 27 | `███████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn3 Teutonic | 74.7 | 3,055 | 6,119 | rtx4090* | 5 | 30% |
| 2 | sn41 Almanac | 73.1 | 29.11 | 111 | cpu-small | 135 | 2% |
| 3 | sn91 cascade | 72 | 523 | 2,095 | cpu-small | 5 | 52% |
| 4 | sn80 OpenRoboto | 69.2 | 582 | 3,047 | rtx4090* | 7 | 35% |
| 5 | sn1 Apex | 68.7 | 509 | 1,034 | rtx4090* | 4 | 69% |
| 6 | sn38 ChronoLLM | 68.6 | 205 | 933 | cpu-small | 9 | 52% |
| 7 | sn67 Harnyx | 68.5 | 7.92 | 960 | cpu-small | 136 | 35% |
| 8 | sn15 ORO | 67.3 | 7.85 | 18,174 | cpu-small | 59 | 97% |
| 9 | sn4 Targon | 66.7 | 9,697 | 28,592 | rtx4090* | 5 | 70% |
| 10 | sn26 Perturb | 66.3 | 244 | 407 | rtx3060 | 4 | 60% |
| 11 | sn62 Ridges | 63.5 | 106 | 1,305 | rtx4090* | 34 | 17% |
| 12 | sn120 Affine | 62.4 | 139 | 353 | rtx4090* | 245 | 1% |
| 13 | sn65 True Performance | 62.3 | 77.80 | 164 | rtx4090* | 6 | 75% |
| 14 | sn61 RedTeam | 62.1 | 73.27 | 98.37 | rtx4090* | 128 | 1% |
| 15 | sn53 engy | 60 | 1,302 | 4,304 | rtx4090 | 18 | 17% |
| 16 | sn23 Trishool | 59.3 | 416 | 416 = | cpu-small | 3 | 80% |
| 17 | sn111 Claims | 57.8 | 19.54 | 234 | rtx4090* | 6 | 90% |
| 18 | sn5 Hone | 57.7 | 33.38 | 35.85 | rtx4090* | 244 | 0% |
| 19 | sn107 Minos | 57.5 | 284 | 24,049 | cpu-small | 20 | 80% |
| 20 | sn74 Gittensor | 57.4 | 19.88 | 143 | rtx4090* | 21 | 51% |

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
| wide (<30%) | 22 |
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
| 2026-10-08T20:40 | sn25 | RELEASE | sn25 released v2026.10.8-1066912010 |
| 2026-10-08T20:40 | sn41 | SCORING_COMMIT | sn41 commit touches scoring: Merge pull request #55 from corvxai/forec |
| 2026-10-08T20:40 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-3769 - Validator: dropped SSH transpo |
| 2026-10-08T20:40 | sn58 | SCORING_COMMIT | sn58 commit touches scoring: fix(miner): `attune miner status` checks  |
| 2026-10-08T20:40 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Allow bounded score batch RPC reads to fi |
| 2026-10-08T20:40 | sn90 | SCORING_COMMIT | sn90 commit touches scoring: docs(nemotron-omni): 256k context verifie |
| 2026-10-08T20:40 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: Record the owner's canary answers 2-4 in |
| 2026-10-08T20:40 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: Verify longer harness cannot reuse short |
| 2026-10-08T14:58 | sn3 | SCORING_COMMIT | sn3 commit touches scoring: Add competition dataset panel and update e |
| 2026-10-08T14:58 | sn15 | RELEASE | sn15 released v2.4.0: Prepare runtime 3.5 validator and practice deliv |
| 2026-10-08T14:58 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: Prepare runtime 3.5 validator and practic |
| 2026-10-08T14:58 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: fix(scoring): copy groups agree on one ea |
| 2026-10-08T14:58 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-4001 - validator: shadow never delays |
| 2026-10-08T14:58 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Merge PR #276: verify judging through the |
| 2026-10-08T14:58 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: docs(corpus): the open route and the agen |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

