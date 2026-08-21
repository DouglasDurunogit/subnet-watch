# Subnet watch — dashboard

_snapshot 2026-08-21T08:05:08Z · block 8891895 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 56 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 92 | `miner_burn` < 0.99 |
| Ranked | 92 | passed every gate |
| **Positive margin** | **56** | income beats machine cost |
| New events this window | 2 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 61 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 7 | `███` |
| 0.8–0.99 | 9 | `████` |
| ≥0.99 dead | 36 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 77.2 | 78.97 | 133 | cpu-small | 13 | 20% |
| 2 | sn23 Trishool | 72.3 | 568 | 568 = | cpu-small | 2 | 80% |
| 3 | sn67 Harnyx | 71.6 | 19.57 | 913 | cpu-small | 146 | 23% |
| 4 | sn62 Ridges | 71 | 993 | 2,027 | rtx4090* | 5 | 36% |
| 5 | sn15 ORO | 70.6 | 20.58 | 20,485 | cpu-small | 76 | 93% |
| 6 | sn1 Apex | 70.1 | 763 | 1,222 | rtx4090* | 4 | 52% |
| 7 | sn56 Gradients | 69.9 | 709 | 1,087 | rtx4090* | 5 | 72% |
| 8 | sn91 cascade | 69.5 | 635 | 2,564 | rtx4090* | 5 | 52% |
| 9 | sn96 Verathos | 67.9 | 19.84 | 314 | rtx4090 | 91 | 40% |
| 10 | sn38 ChronoLLM | 67.8 | 160 | 3,384 | cpu-small | 10 | 52% |
| 11 | sn26 Perturb | 67.5 | 18.24 | 261 | rtx3060 | 10 | 70% |
| 12 | sn107 Minos | 65.2 | 146 | 42,148 | cpu-small | 20 | 90% |
| 13 | sn85 Vidaio | 65.1 | 172 | 1,519 | rtx4090* | 13 | 42% |
| 14 | sn98 NeverPlayAlone | 64.5 | 1,914 | 1,914 = | cpu-small | 1 | 100% |
| 15 | sn81 Reliquary | 62 | 68.24 | 192 | rtx4090* | 53 | 4% |
| 16 | sn55 NIOME | 62 | 67.32 | 560 | rtx4090* | 11 | 29% |
| 17 | sn51 lium.io | 61.8 | 72.10 | 1,305 | rtx4090* | 45 | 83% |
| 18 | sn60 Bitsec.ai | 61.5 | 796 | 1,115 | cpu-small | 3 | 50% |
| 19 | sn108 Prometheon | 61.4 | 57.22 | 396 | rtx4090* | 8 | 66% |
| 20 | sn28 gm | 60.2 | 41.08 | 1,669 | rtx4090* | 53 | 14% |

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
| concentrated (30–60%) | 18 |
| dominated (60–90%) | 20 |
| captured (>90%) | 26 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 101 |
| code-submission (validator runs it) | 10 |
| min_compute.yml (curated) | 10 |
| README keywords (GUESS) | 6 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-08-21T07:23 | sn100 | RELEASE | sn100 released v3.3.28 |
| 2026-08-21T07:23 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: feat(prism): miner Verda BYOK alongside  |
| 2026-08-21T05:46 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-08-21T05:04 | sn53 | SCORING_COMMIT | sn53 commit touches scoring: tee_miner: absorb the reference miner's n |
| 2026-08-21T01:54 | sn34 | RELEASE | sn34 released Release 4.9.8 |
| 2026-08-20T23:08 | sn34 | SCORING_COMMIT | sn34 commit touches scoring: fix: restore validator config parsing (#4 |
| 2026-08-20T23:08 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: Merge pull request #203 from TensorLink-A |
| 2026-08-20T22:40 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: Drop the task generator in favour of uplo |
| 2026-08-20T21:53 | sn34 | SCORING_COMMIT | sn34 commit touches scoring: tune: double generator challenge frequenc |
| 2026-08-20T21:13 | sn13 | RELEASE | sn13 released Release v1.18.71 |
| 2026-08-20T21:13 | sn13 | SCORING_COMMIT | sn13 commit touches scoring: fix(s3): stop charging miners for passing |
| 2026-08-20T21:13 | sn25 | RELEASE | sn25 released v2026.8.20-1024590520 |
| 2026-08-20T21:13 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Fix miner Windows arm64 cross-build |
| 2026-08-20T20:41 | sn25 | RELEASE | sn25 released v2026.8.20-1024555910 |
| 2026-08-20T19:55 | sn18 | RELEASE | sn18 released Release 2.1.2 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

