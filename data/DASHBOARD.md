# Subnet watch — dashboard

_snapshot 2026-09-09T06:19:26Z · block 9028103 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 60 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 91 | `miner_burn` < 0.99 |
| Ranked | 92 | passed every gate |
| **Positive margin** | **60** | income beats machine cost |
| New events this window | 6 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 60 | `████████████████████████████` |
| 0–0.2 | 9 | `████` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 10 | `█████` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 37 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn114 SOMA | 87.1 | 961 | 7,698 | cpu-small | 4 | 80% |
| 2 | sn107 Minos | 83.7 | 419 | 35,540 | cpu-small | 20 | 80% |
| 3 | sn92 MicroTensor | 79.2 | 129 | 389 | cpu-small | 9 | 50% |
| 4 | sn3 Teutonic | 76.1 | 4,529 | 4,529 = | rtx4090* | 5 | 20% |
| 5 | sn67 Harnyx | 71.7 | 19.36 | 549 | cpu-small | 119 | 15% |
| 6 | sn15 ORO | 70.6 | 23.60 | 50.23 | cpu-small | 77 | 92% |
| 7 | sn91 cascade | 70.2 | 793 | 3,199 | rtx4090* | 5 | 52% |
| 8 | sn96 Verathos | 70.1 | 34.47 | 534 | rtx4090 | 84 | 30% |
| 9 | sn14 Cacheon | 69.7 | 680 | 1,259 | rtx4090* | 12 | 18% |
| 10 | sn11 TrajectoryRL | 68.7 | 6,686 | 6,686 = | cpu-small | 1 | 100% |
| 11 | sn62 Ridges | 68 | 409 | 1,252 | rtx4090* | 13 | 26% |
| 12 | sn80 OpenRoboto | 67.5 | 354 | 1,260 | rtx4090* | 5 | 43% |
| 13 | sn56 Gradients | 67.4 | 339 | 5,912 | rtx4090* | 9 | 47% |
| 14 | sn111 Claims | 65.9 | 234 | 2,107 | rtx4090* | 5 | 48% |
| 15 | sn38 ChronoLLM | 65.9 | 98.20 | 1,343 | cpu-small | 10 | 52% |
| 16 | sn121 sundae_bar | 63.2 | 1,327 | 1,327 = | cpu-small | 2 | 60% |
| 17 | sn65 True Performance | 62.5 | 88.85 | 186 | rtx4090* | 6 | 75% |
| 18 | sn41 Almanac | 60.7 | 42.01 | 92.40 | cpu-small | 86 | 3% |
| 19 | sn28 SayGM | 59.6 | 34.60 | 1,183 | rtx4090* | 62 | 55% |
| 20 | sn102 ConnitoAI | 59.1 | 29.50 | 1,568 | rtx4090* | 8 | 28% |

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
| concentrated (30–60%) | 21 |
| dominated (60–90%) | 19 |
| captured (>90%) | 20 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 99 |
| min_compute.yml (curated) | 11 |
| code-submission (validator runs it) | 10 |
| README keywords (GUESS) | 7 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-09-09T06:19 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-2962: delete the dead hashcat scoring |
| 2026-09-09T06:19 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-09-09T06:19 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Stop Arena scoring after exhausted judge  |
| 2026-09-09T06:19 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: feat(proof): name the topic_id / custom_ |
| 2026-09-09T06:19 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: fix(validator): normalize provider routi |
| 2026-09-09T06:19 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: AGENTS.md: first wvk-13 verdicts verifie |
| 2026-09-09T01:13 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: build: refresh protected scoring source m |
| 2026-09-09T01:13 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: fix(validator): enable rigor validation  |
| 2026-09-08T22:52 | sn15 | RELEASE | sn15 released v1.2.13: compose: forward SUBTENSOR_CHAIN_ENDPOINT to th |
| 2026-09-08T22:52 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: compose: forward SUBTENSOR_CHAIN_ENDPOINT |
| 2026-09-08T22:52 | sn25 | RELEASE | sn25 released v2026.9.8-1040985530 |
| 2026-09-08T22:52 | sn28 | RELEASE | sn28 released v0.4.15 |
| 2026-09-08T22:52 | sn28 | SCORING_COMMIT | sn28 commit touches scoring: fix(miner): render node secret last and p |
| 2026-09-08T22:52 | sn28 | README_TASK_DIFF | sn28 README task/scoring sections changed |
| 2026-09-08T22:52 | sn78 | WEIGHTS_VERSION_BUMP | sn78 weights_version 0 -> 1 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

