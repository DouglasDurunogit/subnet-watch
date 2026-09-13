# Subnet watch — dashboard

_snapshot 2026-09-13T16:32:38Z · block 9059904 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 55 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 88 | `miner_burn` < 0.99 |
| Ranked | 89 | passed every gate |
| **Positive margin** | **55** | income beats machine cost |
| New events this window | 1 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 60 | `████████████████████████████` |
| 0–0.2 | 8 | `████` |
| 0.2–0.4 | 7 | `███` |
| 0.4–0.6 | 2 | `█` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 3 | `█` |
| ≥0.99 dead | 40 | `███████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn92 MicroTensor | 80.6 | 186 | 559 | cpu-small | 8 | 30% |
| 2 | sn91 cascade | 72.1 | 1,393 | 2,794 | rtx4090* | 5 | 52% |
| 3 | sn21 AdTAO | 71.4 | 18.70 | 103 | cpu-small | 21 | 34% |
| 4 | sn67 Harnyx | 69.5 | 10.89 | 1,195 | cpu-small | 111 | 38% |
| 5 | sn107 Minos | 68.9 | 351 | 29,790 | cpu-small | 20 | 80% |
| 6 | sn14 Cacheon | 68.7 | 498 | 1,128 | rtx4090* | 12 | 18% |
| 7 | sn111 Claims | 68.4 | 484 | 2,144 | rtx4090* | 5 | 60% |
| 8 | sn96 Verathos | 68.4 | 22.50 | 247 | rtx4090 | 74 | 31% |
| 9 | sn11 TrajectoryRL | 68.3 | 5,901 | 5,901 = | cpu-small | 1 | 100% |
| 10 | sn38 ChronoLLM | 68 | 173 | 3,669 | cpu-small | 10 | 52% |
| 11 | sn80 OpenRoboto | 67.8 | 379 | 1,347 | rtx4090* | 5 | 43% |
| 12 | sn124 Swarm | 66.4 | 263 | 854 | rtx4090* | 25 | 11% |
| 13 | sn61 RedTeam | 64.7 | 153 | 247 | rtx4090* | 83 | 2% |
| 14 | sn28 SayGM | 62.3 | 76.46 | 3,736 | rtx4090* | 42 | 25% |
| 15 | sn55 NIOME | 62 | 66.96 | 556 | rtx4090* | 11 | 29% |
| 16 | sn78 Umi | 60.3 | 43.31 | 43.31 = | rtx4090* | 110 | 2% |
| 17 | sn62 Ridges | 59.6 | 32.26 | 108 | rtx4090* | 16 | 52% |
| 18 | sn81 Reliquary | 58.4 | 22.42 | 195 | rtx4090* | 85 | 5% |
| 19 | sn51 lium.io | 58.2 | 30.05 | 2,164 | rtx4090* | 61 | 79% |
| 20 | sn102 ConnitoAI | 57.4 | 598 | 1,181 | rtx4090* | 7 | 25% |

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
| concentrated (30–60%) | 22 |
| dominated (60–90%) | 16 |
| captured (>90%) | 20 |

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
| 2026-09-13T16:33 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Merge pull request #61 from Umi-BitSign/c |
| 2026-09-13T12:20 | sn15 | RELEASE | sn15 released v2.0.9 |
| 2026-09-13T12:20 | sn61 | RELEASE | sn61 released 4.10.5 |
| 2026-09-13T12:20 | sn61 | SCORING_COMMIT | sn61 commit touches scoring: deps: update ada_detection challenge imag |
| 2026-09-13T12:20 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Bind recovered Arena future stages to the |
| 2026-09-13T12:20 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Accept the verified stopped successor dur |
| 2026-09-13T12:20 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: fix: bound validator startup memory (#255 |
| 2026-09-13T12:20 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: pool: publish packs mv_channels iff effec |
| 2026-09-13T12:20 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: docs(proof): keep miner tbench rebake pi |
| 2026-09-13T06:30 | sn15 | RELEASE | sn15 released v2.0.8 |
| 2026-09-13T06:30 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: chore(validator): pin oro-env-runtime 0.2 |
| 2026-09-13T06:30 | sn53 | SCORING_COMMIT | sn53 commit touches scoring: Merge pull request #45 from hanlinai/fix/ |
| 2026-09-13T06:30 | sn71 | README_TASK_DIFF | sn71 README task/scoring sections changed |
| 2026-09-13T06:30 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Record finalized funding-cap rollout on b |
| 2026-09-13T01:22 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: provision: pin the Lium pull by digest an |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

