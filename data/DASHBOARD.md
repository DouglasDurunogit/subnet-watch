# Subnet watch — dashboard

_snapshot 2026-09-17T00:47:29Z · block 9083886 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 0 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 93 | `miner_burn` < 0.99 |
| Ranked | 93 | passed every gate |
| **Positive margin** | **0** | income beats machine cost |
| New events this window | 3 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 64 | `████████████████████████████` |
| 0–0.2 | 9 | `████` |
| 0.2–0.4 | 7 | `███` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 5 | `██` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 35 | `███████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn11 TrajectoryRL | 50 | n/a | n/a | cpu-small | 1 | 100% |
| 2 | sn67 Harnyx | 50 | n/a | n/a | cpu-small | 117 | 33% |
| 3 | sn92 MicroTensor | 50 | n/a | n/a | cpu-small | 8 | 43% |
| 4 | sn21 AdTAO | 50 | n/a | n/a | cpu-small | 20 | 40% |
| 5 | sn114 SOMA | 50 | n/a | n/a | cpu-small | 40 | 80% |
| 6 | sn91 cascade | 42.5 | n/a | n/a | cpu-small | 5 | 52% |
| 7 | sn38 ChronoLLM | 42.5 | n/a | n/a | cpu-small | 10 | 52% |
| 8 | sn53 engy | 39.3 | n/a | n/a | rtx4090 | 67 | 44% |
| 9 | sn81 Reliquary | 39.3 | n/a | n/a | rtx4090* | 45 | 36% |
| 10 | sn63 Enigma | 39.3 | n/a | n/a | rtx4090* | 12 | 100% |
| 11 | sn1 Apex | 39.3 | n/a | n/a | rtx4090* | 3 | 51% |
| 12 | sn9 iota | 39.3 | n/a | n/a | rtx4090* | 3 | 68% |
| 13 | sn66 conjectures | 39.3 | n/a | n/a | rtx4090* | 1 | 100% |
| 14 | sn76 Ormas | 39.3 | n/a | n/a | rtx4090* | 1 | n/a |
| 15 | sn62 Ridges | 39.3 | n/a | n/a | rtx4090* | 19 | 26% |
| 16 | sn55 NIOME | 39.3 | n/a | n/a | rtx4090* | 11 | 29% |
| 17 | sn45 AlphaRidge.ai | 39.3 | n/a | n/a | rtx4090* | 239 | 54% |
| 18 | sn44 Score | 39.3 | n/a | n/a | rtx4090* | 1 | 100% |
| 19 | sn102 ConnitoAI | 39.3 | n/a | n/a | rtx4090* | 4 | 25% |
| 20 | sn28 SayGM | 39.3 | n/a | n/a | rtx4090* | 47 | 20% |

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
| concentrated (30–60%) | 24 |
| dominated (60–90%) | 17 |
| captured (>90%) | 23 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 96 |
| min_compute.yml (curated) | 11 |
| code-submission (validator runs it) | 10 |
| README keywords (GUESS) | 10 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-09-17T00:48 | sn40 | SCORING_COMMIT | sn40 commit touches scoring: Docs: round-7 rules, miner CLI flow, audi |
| 2026-09-17T00:48 | sn40 | README_TASK_DIFF | sn40 README task/scoring sections changed |
| 2026-09-17T00:48 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Merge pull request #135 from Umi-BitSign/ |
| 2026-09-16T22:24 | sn28 | RELEASE | sn28 released v0.4.18 |
| 2026-09-16T22:24 | sn28 | README_TASK_DIFF | sn28 README task/scoring sections changed |
| 2026-09-16T22:24 | sn45 | SCORING_COMMIT | sn45 commit touches scoring: Allow a per-model scale on audit scores |
| 2026-09-16T22:24 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: release: pin fresh validator installs to  |
| 2026-09-16T22:24 | sn102 | RELEASE | sn102 released v0.6.1 |
| 2026-09-16T22:24 | sn102 | SCORING_COMMIT | sn102 commit touches scoring: Merge pull request #274 from Connito-AI/ |
| 2026-09-16T19:46 | sn34 | SCORING_COMMIT | sn34 commit touches scoring: Exclude no_answer rows before the reward- |
| 2026-09-16T19:46 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Fix Sep16 benchmark bank verification |
| 2026-09-16T19:46 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: fix: keep valid bridge miners eligible du |
| 2026-09-16T19:46 | sn92 | RELEASE | sn92 released v0.4.6 |
| 2026-09-16T19:46 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: mt-4g: 3 GiB disk ceiling, matching the a |
| 2026-09-16T16:47 | sn9 | RELEASE | sn9 released v4.13.0 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

