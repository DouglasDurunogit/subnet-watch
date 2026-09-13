# Subnet watch — dashboard

_snapshot 2026-09-13T12:19:34Z · block 9058642 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 54 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 87 | `miner_burn` < 0.99 |
| Ranked | 88 | passed every gate |
| **Positive margin** | **54** | income beats machine cost |
| New events this window | 8 | see ALARMS.md |

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
| 0.8–0.99 | 2 | `█` |
| ≥0.99 dead | 41 | `███████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn92 MicroTensor | 80.6 | 184 | 554 | cpu-small | 8 | 30% |
| 2 | sn91 cascade | 72.1 | 1,396 | 2,801 | rtx4090* | 5 | 52% |
| 3 | sn21 AdTAO | 71.4 | 18.88 | 104 | cpu-small | 21 | 34% |
| 4 | sn96 Verathos | 71 | 42.37 | 268 | rtx4090 | 52 | 31% |
| 5 | sn67 Harnyx | 69.5 | 10.89 | 1,195 | cpu-small | 111 | 38% |
| 6 | sn107 Minos | 69 | 353 | 29,919 | cpu-small | 20 | 80% |
| 7 | sn14 Cacheon | 68.7 | 497 | 1,127 | rtx4090* | 12 | 18% |
| 8 | sn11 TrajectoryRL | 68.3 | 5,932 | 5,932 = | cpu-small | 1 | 100% |
| 9 | sn80 OpenRoboto | 67.8 | 384 | 1,364 | rtx4090* | 5 | 43% |
| 10 | sn38 ChronoLLM | 66.6 | 118 | 1,617 | cpu-small | 10 | 52% |
| 11 | sn124 Swarm | 66.4 | 261 | 851 | rtx4090* | 25 | 11% |
| 12 | sn111 Claims | 65.9 | 234 | 2,630 | rtx4090* | 5 | 74% |
| 13 | sn61 RedTeam | 64.9 | 162 | 249 | rtx4090* | 69 | 2% |
| 14 | sn28 SayGM | 63.1 | 95.69 | 3,107 | rtx4090* | 40 | 21% |
| 15 | sn55 NIOME | 61.9 | 66.68 | 553 | rtx4090* | 11 | 29% |
| 16 | sn62 Ridges | 59.5 | 32.48 | 108 | rtx4090* | 16 | 52% |
| 17 | sn102 ConnitoAI | 59.2 | 1,023 | 1,281 | rtx4090* | 6 | 26% |
| 18 | sn81 Reliquary | 59.1 | 27.43 | 187 | rtx4090* | 84 | 5% |
| 19 | sn51 lium.io | 58.7 | 33.57 | 2,178 | rtx4090* | 61 | 77% |
| 20 | sn74 Gittensor | 56.9 | 16.64 | 180 | rtx4090 | 11 | 64% |

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
| dominated (60–90%) | 17 |
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
| 2026-09-13T01:22 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: fix(proof): align results_path validatio |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

