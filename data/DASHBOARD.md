# Subnet watch — dashboard

_snapshot 2026-09-14T06:41:32Z · block 9064140 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 50 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 90 | `miner_burn` < 0.99 |
| Ranked | 90 | passed every gate |
| **Positive margin** | **50** | income beats machine cost |
| New events this window | 7 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 63 | `████████████████████████████` |
| 0–0.2 | 9 | `████` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 2 | `█` |
| 0.6–0.8 | 7 | `███` |
| 0.8–0.99 | 3 | `█` |
| ≥0.99 dead | 38 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn92 MicroTensor | 80.5 | 182 | 548 | cpu-small | 8 | 30% |
| 2 | sn91 cascade | 71.2 | 1,050 | 2,815 | rtx4090* | 5 | 52% |
| 3 | sn67 Harnyx | 69.5 | 11.11 | 11.11 = | cpu-small | 223 | 14% |
| 4 | sn107 Minos | 69 | 352 | 29,864 | cpu-small | 20 | 80% |
| 5 | sn96 Verathos | 68.9 | 25.82 | 238 | rtx4090 | 78 | 30% |
| 6 | sn80 OpenRoboto | 67.8 | 386 | 1,372 | rtx4090* | 5 | 43% |
| 7 | sn38 ChronoLLM | 66.8 | 124 | 1,689 | cpu-small | 10 | 52% |
| 8 | sn124 Swarm | 66.4 | 263 | 852 | rtx4090* | 25 | 11% |
| 9 | sn61 RedTeam | 64.6 | 153 | 237 | rtx4090* | 81 | 2% |
| 10 | sn111 Claims | 64.5 | 160 | 2,860 | rtx4090* | 5 | 82% |
| 11 | sn3 Teutonic | 63.9 | 4,161 | 4,161 = | rtx4090* | 5 | 20% |
| 12 | sn55 NIOME | 62 | 67.45 | 559 | rtx4090* | 11 | 29% |
| 13 | sn62 Ridges | 60.6 | 44.69 | 1,169 | rtx4090* | 18 | 35% |
| 14 | sn81 Reliquary | 60.5 | 42.55 | 204 | rtx4090* | 86 | 5% |
| 15 | sn102 ConnitoAI | 59.2 | 1,029 | 1,444 | rtx4090* | 6 | 29% |
| 16 | sn78 Umi | 59.1 | 28.57 | 28.57 = | rtx4090* | 142 | 1% |
| 17 | sn74 Gittensor | 58.5 | 26.09 | 176 | rtx4090 | 11 | 64% |
| 18 | sn21 AdTAO | 58.5 | 10.29 | 16.89 | cpu-small | 21 | 34% |
| 19 | sn51 lium.io | 58.1 | 28.74 | 2,185 | rtx4090* | 63 | 77% |
| 20 | sn14 Cacheon | 56.7 | 493 | 1,118 | rtx4090* | 12 | 18% |

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
| concentrated (30–60%) | 20 |
| dominated (60–90%) | 20 |
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
| 2026-09-14T06:42 | sn15 | RELEASE | sn15 released v2.0.14: feat: capture per-episode wall time (#304) |
| 2026-09-14T06:42 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: fix: reject any generated evaluation infr |
| 2026-09-14T06:42 | sn25 | RELEASE | sn25 released v2026.9.13-1045655440 |
| 2026-09-14T06:42 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Retain native provider billing receipts a |
| 2026-09-14T06:42 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: docs: use private holdout for automatic c |
| 2026-09-14T06:42 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: Warn miners about Transformers runtime di |
| 2026-09-14T06:42 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: feat(funding): miner-chosen submission la |
| 2026-09-14T01:21 | sn15 | RELEASE | sn15 released v2.0.12 |
| 2026-09-14T01:21 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: fix: make validator startup logs formatti |
| 2026-09-14T01:21 | sn20 | SCORING_COMMIT | sn20 commit touches scoring: Resolve the validator signing key before  |
| 2026-09-14T01:21 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: fix(weight-only): retain only reward fiel |
| 2026-09-13T23:21 | sn15 | RELEASE | sn15 released v2.0.11: fix: preserve episode inference telemetry witho |
| 2026-09-13T23:21 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Match verified US contact state aliases |
| 2026-09-13T23:21 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Connect independent work signing and auto |
| 2026-09-13T21:25 | sn15 | RELEASE | sn15 released v2.0.10: Capture complete episode resource telemetry (#2 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

