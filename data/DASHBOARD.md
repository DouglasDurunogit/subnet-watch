# Subnet watch — dashboard

_snapshot 2026-09-14T01:20:35Z · block 9062540 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 55 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 90 | `miner_burn` < 0.99 |
| Ranked | 90 | passed every gate |
| **Positive margin** | **55** | income beats machine cost |
| New events this window | 4 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 63 | `████████████████████████████` |
| 0–0.2 | 8 | `████` |
| 0.2–0.4 | 7 | `███` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 7 | `███` |
| 0.8–0.99 | 2 | `█` |
| ≥0.99 dead | 38 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn92 MicroTensor | 80.5 | 179 | 540 | cpu-small | 8 | 30% |
| 2 | sn91 cascade | 71.1 | 1,027 | 2,753 | rtx4090* | 5 | 52% |
| 3 | sn21 AdTAO | 70.9 | 16.56 | 104 | cpu-small | 21 | 34% |
| 4 | sn67 Harnyx | 69.5 | 11.01 | 11.01 = | cpu-small | 219 | 15% |
| 5 | sn107 Minos | 69 | 352 | 29,836 | cpu-small | 20 | 80% |
| 6 | sn96 Verathos | 69 | 26.70 | 231 | rtx4090 | 73 | 30% |
| 7 | sn11 TrajectoryRL | 68.2 | 5,773 | 5,773 = | cpu-small | 1 | 100% |
| 8 | sn80 OpenRoboto | 67.7 | 375 | 1,334 | rtx4090* | 5 | 43% |
| 9 | sn38 ChronoLLM | 66.7 | 121 | 1,653 | cpu-small | 10 | 52% |
| 10 | sn124 Swarm | 66.4 | 261 | 558 | rtx4090* | 25 | 11% |
| 11 | sn61 RedTeam | 64.5 | 147 | 226 | rtx4090* | 82 | 2% |
| 12 | sn111 Claims | 64.4 | 156 | 2,794 | rtx4090* | 5 | 82% |
| 13 | sn3 Teutonic | 63.8 | 4,102 | 4,102 = | rtx4090* | 5 | 20% |
| 14 | sn55 NIOME | 61.9 | 65.30 | 543 | rtx4090* | 11 | 29% |
| 15 | sn62 Ridges | 59.9 | 35.61 | 1,212 | rtx4090* | 17 | 42% |
| 16 | sn81 Reliquary | 59.7 | 33.15 | 223 | rtx4090* | 87 | 6% |
| 17 | sn78 Umi | 59.6 | 32.76 | 32.76 = | rtx4090* | 124 | 1% |
| 18 | sn102 ConnitoAI | 58.5 | 846 | 1,786 | rtx4090* | 5 | 38% |
| 19 | sn51 lium.io | 57.4 | 24.69 | 2,186 | rtx4090* | 64 | 80% |
| 20 | sn28 SayGM | 56.9 | 15.93 | 4,182 | rtx4090* | 40 | 28% |

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
| dominated (60–90%) | 18 |
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
| 2026-09-14T01:21 | sn15 | RELEASE | sn15 released v2.0.12 |
| 2026-09-14T01:21 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: fix: make validator startup logs formatti |
| 2026-09-14T01:21 | sn20 | SCORING_COMMIT | sn20 commit touches scoring: Resolve the validator signing key before  |
| 2026-09-14T01:21 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: fix(weight-only): retain only reward fiel |
| 2026-09-13T23:21 | sn15 | RELEASE | sn15 released v2.0.11: fix: preserve episode inference telemetry witho |
| 2026-09-13T23:21 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Match verified US contact state aliases |
| 2026-09-13T23:21 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Connect independent work signing and auto |
| 2026-09-13T21:25 | sn15 | RELEASE | sn15 released v2.0.10: Capture complete episode resource telemetry (#2 |
| 2026-09-13T21:25 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: Use SDK transient status classification f |
| 2026-09-13T21:25 | sn47 | BURN_DROP | sn47 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-09-13T21:25 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Merge pull request #65 from Umi-BitSign/c |
| 2026-09-13T21:25 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: feat(validator): explain V1 selection ver |
| 2026-09-13T21:25 | sn99 | BURN_DROP | sn99 burn fell 1.000 -> 0.150 - miners can earn again |
| 2026-09-13T19:00 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Bind stage two recovery to tested scorer  |
| 2026-09-13T19:00 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Merge pull request #64 from Umi-BitSign/c |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

