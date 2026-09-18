# Subnet watch — dashboard

_snapshot 2026-09-18T20:51:04Z · block 9097026 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 49 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 92 | `miner_burn` < 0.99 |
| Ranked | 92 | passed every gate |
| **Positive margin** | **49** | income beats machine cost |
| New events this window | 5 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 61 | `████████████████████████████` |
| 0–0.2 | 9 | `████` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 3 | `█` |
| ≥0.99 dead | 36 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn4 Targon | 77.8 | 7,628 | 21,415 | rtx4090* | 6 | 51% |
| 2 | sn3 Teutonic | 76.2 | 4,755 | 4,755 = | rtx4090* | 5 | 20% |
| 3 | sn91 cascade | 72.7 | 638 | 2,554 | cpu-small | 5 | 52% |
| 4 | sn1 Apex | 70.4 | 835 | 1,012 | rtx4090* | 4 | 54% |
| 5 | sn67 Harnyx | 69.2 | 10.01 | 1,279 | cpu-small | 112 | 41% |
| 6 | sn107 Minos | 68.9 | 348 | 29,238 | cpu-small | 20 | 80% |
| 7 | sn102 ConnitoAI | 68.7 | 505 | 1,422 | rtx4090* | 7 | 29% |
| 8 | sn56 Gradients | 68.4 | 454 | 5,367 | rtx4090* | 9 | 46% |
| 9 | sn15 ORO | 66.9 | 8.43 | 19,773 | cpu-small | 50 | 98% |
| 10 | sn124 Swarm | 66.5 | 272 | 872 | rtx4090* | 25 | 11% |
| 11 | sn38 ChronoLLM | 65.9 | 98.75 | 874 | cpu-small | 10 | 52% |
| 12 | sn62 Ridges | 65.7 | 205 | 1,392 | rtx4090* | 23 | 17% |
| 13 | sn111 Claims | 65.1 | 187 | 2,864 | rtx4090* | 5 | 80% |
| 14 | sn74 Gittensor | 61.7 | 65.98 | 204 | rtx4090* | 10 | 63% |
| 15 | sn81 Reliquary | 60.6 | 44.17 | 111 | rtx4090* | 32 | 64% |
| 16 | sn28 SayGM | 59.9 | 37.36 | 3,345 | rtx4090* | 59 | 22% |
| 17 | sn51 lium.io | 58.6 | 33.08 | 1,681 | rtx4090* | 66 | 82% |
| 18 | sn61 RedTeam | 58.6 | 24.84 | 2,144 | rtx4090* | 122 | 21% |
| 19 | sn80 OpenRoboto | 56.7 | 486 | 1,720 | rtx4090* | 5 | 43% |
| 20 | sn9 iota | 56.3 | 13,612 | 13,612 = | rtx4090* | 2 | 68% |

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
| wide (<30%) | 24 |
| concentrated (30–60%) | 25 |
| dominated (60–90%) | 18 |
| captured (>90%) | 22 |

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
| 2026-09-18T20:51 | sn15 | RELEASE | sn15 released v2.0.26: fix(proxy): fail over user-simulator from Mistr |
| 2026-09-18T20:51 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: validator: strict > infra boundary — 3/10 |
| 2026-09-18T20:51 | sn45 | SCORING_COMMIT | sn45 commit touches scoring: Score pool audits under a second matcher, |
| 2026-09-18T20:51 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Add Sep18 cancelled rerun302 with fresh j |
| 2026-09-18T20:51 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Merge pull request #169 from Umi-BitSign/ |
| 2026-09-18T17:50 | sn12 | RELEASE | sn12 released validator-staging-2026-09-18-35368036673-626-1: fix: evi |
| 2026-09-18T17:50 | sn12 | SCORING_COMMIT | sn12 commit touches scoring: fix: evict old neurons in allowance evict |
| 2026-09-18T17:50 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: validator: hard-fail generated runs at >= |
| 2026-09-18T17:50 | sn25 | RELEASE | sn25 released v2026.9.18-1049469180 |
| 2026-09-18T17:50 | sn28 | RELEASE | sn28 released v0.4.19 |
| 2026-09-18T17:50 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Clarify validator credentials and require |
| 2026-09-18T17:50 | sn74 | RELEASE | sn74 released release-20260918-164355 |
| 2026-09-18T17:50 | sn90 | SCORING_COMMIT | sn90 commit touches scoring: docs: client-facing attestation of infere |
| 2026-09-18T17:50 | sn97 | SCORING_COMMIT | sn97 commit touches scoring: feat: Added scored_output the judge-facin |
| 2026-09-18T17:50 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: docs: document funding-lineage miner sel |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

