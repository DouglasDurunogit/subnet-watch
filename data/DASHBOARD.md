# Subnet watch — dashboard

_snapshot 2026-09-10T15:12:51Z · block 9037953 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 57 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 91 | `miner_burn` < 0.99 |
| Ranked | 91 | passed every gate |
| **Positive margin** | **57** | income beats machine cost |
| New events this window | 6 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 61 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 8 | `████` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 37 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn114 SOMA | 84.2 | 456 | 7,318 | cpu-small | 6 | 80% |
| 2 | sn107 Minos | 83.4 | 391 | 32,693 | cpu-small | 20 | 80% |
| 3 | sn92 MicroTensor | 78.2 | 102 | 227 | cpu-small | 9 | 50% |
| 4 | sn3 Teutonic | 75.8 | 4,191 | 4,191 = | rtx4090* | 5 | 20% |
| 5 | sn15 ORO | 70.8 | 20.59 | 21,205 | cpu-small | 80 | 92% |
| 6 | sn67 Harnyx | 70.5 | 14.41 | 690 | cpu-small | 150 | 21% |
| 7 | sn91 cascade | 70.2 | 788 | 3,178 | rtx4090* | 5 | 52% |
| 8 | sn102 ConnitoAI | 69.5 | 634 | 1,386 | rtx4090* | 7 | 26% |
| 9 | sn14 Cacheon | 69.5 | 633 | 1,173 | rtx4090* | 12 | 18% |
| 10 | sn96 Verathos | 69.3 | 28.33 | 247 | rtx4090 | 82 | 30% |
| 11 | sn11 TrajectoryRL | 68.5 | 6,352 | 6,352 = | cpu-small | 1 | 100% |
| 12 | sn56 Gradients | 68.2 | 429 | 5,568 | rtx4090* | 9 | 48% |
| 13 | sn80 OpenRoboto | 67.4 | 343 | 1,219 | rtx4090* | 5 | 43% |
| 14 | sn38 ChronoLLM | 67.4 | 144 | 3,063 | cpu-small | 10 | 52% |
| 15 | sn61 RedTeam | 67 | 302 | 476 | rtx4090* | 39 | 5% |
| 16 | sn124 Swarm | 66.6 | 278 | 865 | rtx4090* | 25 | 11% |
| 17 | sn21 AdTAO | 66.6 | 6.32 | 116 | cpu-small | 16 | 45% |
| 18 | sn111 Claims | 65.9 | 239 | 3,293 | rtx4090* | 5 | 78% |
| 19 | sn121 sundae_bar | 62.8 | 1,171 | 1,171 = | cpu-small | 2 | 60% |
| 20 | sn28 SayGM | 61.9 | 68.21 | 4,260 | rtx4090* | 43 | 28% |

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
| wide (<30%) | 27 |
| concentrated (30–60%) | 20 |
| dominated (60–90%) | 20 |
| captured (>90%) | 20 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 97 |
| min_compute.yml (curated) | 11 |
| code-submission (validator runs it) | 10 |
| README keywords (GUESS) | 9 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-09-10T15:13 | sn9 | RELEASE | sn9 released v4.12.16 |
| 2026-09-10T15:13 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-2748, hide a node the validator canno |
| 2026-09-10T15:13 | sn63 | SCORING_COMMIT | sn63 commit touches scoring: Fix issue with migrated validator db |
| 2026-09-10T15:13 | sn66 | README_TASK_DIFF | sn66 README task/scoring sections changed |
| 2026-09-10T15:13 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: Document V6 miner submission allowance |
| 2026-09-10T15:13 | sn108 | SCORING_COMMIT | sn108 commit touches scoring: feat(evaluation): optionally discard a c |
| 2026-09-10T11:39 | sn15 | RELEASE | sn15 released v2.0.0 |
| 2026-09-10T11:39 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: Verify scope-bound environment deliveries |
| 2026-09-10T11:39 | sn25 | RELEASE | sn25 released v2026.9.10-1042298530 |
| 2026-09-10T11:39 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: crv4: accept reviewed runtime 455 validat |
| 2026-09-10T11:39 | sn51 | RELEASE | sn51 released executor-v1.125 |
| 2026-09-10T11:39 | sn62 | RELEASE | sn62 released v0.3.3 |
| 2026-09-10T11:39 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-09-10T11:39 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: docs: state midnight continuous evaluatio |
| 2026-09-10T11:39 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: docs: concise miner quickstart for funded |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

