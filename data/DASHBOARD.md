# Subnet watch — dashboard

_snapshot 2026-09-13T18:59:33Z · block 9060638 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 55 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 89 | `miner_burn` < 0.99 |
| Ranked | 90 | passed every gate |
| **Positive margin** | **55** | income beats machine cost |
| New events this window | 3 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 61 | `████████████████████████████` |
| 0–0.2 | 8 | `████` |
| 0.2–0.4 | 7 | `███` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 6 | `███` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 39 | `██████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn92 MicroTensor | 80.6 | 186 | 560 | cpu-small | 8 | 30% |
| 2 | sn21 AdTAO | 72.1 | 22.38 | 106 | cpu-small | 21 | 35% |
| 3 | sn91 cascade | 71.1 | 1,040 | 2,788 | rtx4090* | 5 | 52% |
| 4 | sn67 Harnyx | 69.5 | 11.02 | 1,207 | cpu-small | 111 | 38% |
| 5 | sn107 Minos | 69 | 359 | 30,437 | cpu-small | 20 | 80% |
| 6 | sn96 Verathos | 69 | 26.25 | 227 | rtx4090 | 70 | 31% |
| 7 | sn111 Claims | 68.5 | 485 | 2,148 | rtx4090* | 5 | 60% |
| 8 | sn80 OpenRoboto | 67.8 | 379 | 1,346 | rtx4090* | 5 | 43% |
| 9 | sn38 ChronoLLM | 66.8 | 123 | 1,685 | cpu-small | 10 | 52% |
| 10 | sn124 Swarm | 66.5 | 267 | 866 | rtx4090* | 25 | 11% |
| 11 | sn61 RedTeam | 64.6 | 152 | 235 | rtx4090* | 83 | 2% |
| 12 | sn55 NIOME | 62 | 67.35 | 559 | rtx4090* | 11 | 29% |
| 13 | sn78 Umi | 59.9 | 38.02 | 38.02 = | rtx4090* | 117 | 1% |
| 14 | sn28 SayGM | 59.6 | 34.86 | 4,860 | rtx4090* | 39 | 33% |
| 15 | sn62 Ridges | 59.6 | 32.76 | 109 | rtx4090* | 16 | 52% |
| 16 | sn81 Reliquary | 59.2 | 29.09 | 207 | rtx4090* | 85 | 5% |
| 17 | sn51 lium.io | 58.2 | 29.79 | 2,197 | rtx4090* | 63 | 80% |
| 18 | sn102 ConnitoAI | 57.3 | 591 | 1,238 | rtx4090* | 7 | 26% |
| 19 | sn14 Cacheon | 56.8 | 503 | 1,141 | rtx4090* | 12 | 18% |
| 20 | sn74 Gittensor | 56.7 | 16.01 | 183 | rtx4090 | 11 | 64% |

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
| concentrated (30–60%) | 24 |
| dominated (60–90%) | 15 |
| captured (>90%) | 21 |

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
| 2026-09-13T19:00 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Bind stage two recovery to tested scorer  |
| 2026-09-13T19:00 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Merge pull request #64 from Umi-BitSign/c |
| 2026-09-13T19:00 | sn125 | BURN_DROP | sn125 burn fell 1.000 -> 0.000 - miners can earn again |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

