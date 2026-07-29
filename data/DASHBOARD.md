# Subnet watch — dashboard

_snapshot 2026-07-29T12:28:21Z · block 8727644 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 52 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 93 | `miner_burn` < 0.99 |
| Ranked | 93 | passed every gate |
| **Positive margin** | **52** | income beats machine cost |
| New events this window | 2 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 60 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 7 | `███` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 35 | `████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 81 | 203 | 340 | cpu-small | 4 | 60% |
| 2 | sn56 Gradients | 69.2 | 576 | 1,419 | rtx4090* | 6 | 62% |
| 3 | sn15 ORO | 68.6 | 11.24 | 11,548 | cpu-small | 76 | 93% |
| 4 | sn67 Harnyx | 68.5 | 8.57 | 1,000 | cpu-small | 112 | 21% |
| 5 | sn124 Swarm | 67.4 | 345 | 701 | rtx4090* | 16 | 13% |
| 6 | sn101 Tag101 | 65.1 | 3.33 | 63.08 | cpu-small | 243 | 2% |
| 7 | sn85 Vidaio | 64.5 | 142 | 534 | rtx4090* | 10 | 17% |
| 8 | sn53 engy | 63 | 91.63 | 2,207 | rtx4090 | 34 | 13% |
| 9 | sn71 Leadpoet | 61.9 | 65.14 | 267 | rtx4090* | 6 | 71% |
| 10 | sn61 RedTeam | 58.4 | 22.70 | 153 | rtx4090* | 82 | 5% |
| 11 | sn28 gm | 57.2 | 16.85 | 2,321 | rtx4090* | 9 | 55% |
| 12 | sn102 ConnitoAI | 55.2 | 8.10 | 1,023 | rtx4090* | 9 | 27% |
| 13 | sn51 lium.io | 54.4 | 12.67 | 3,082 | rtx4090* | 37 | 67% |
| 14 | sn7 Allways | 51.8 | 2,027 | 2,027 = | rtx4090* | 1 | 100% |
| 15 | sn23 Trishool | 50.1 | 581 | 581 = | cpu-small | 5 | 20% |
| 16 | sn98 NeverPlayAlone | 50 | n/a | n/a | cpu-small | 1 | 100% |
| 17 | sn120 Affine | 47.6 | 6,582 | 6,582 = | rtx4090* | 5 | 20% |
| 18 | sn4 Targon | 47.4 | 6,159 | 10,173 | rtx4090* | 8 | 31% |
| 19 | sn60 Bitsec.ai | 44.4 | 992 | 992 = | cpu-small | 2 | 51% |
| 20 | sn107 Minos | 43.4 | 119 | 35,430 | cpu-small | 20 | 90% |

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
| captured (>90%) | 25 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 106 |
| min_compute.yml (curated) | 9 |
| code-submission (validator runs it) | 8 |
| README keywords (GUESS) | 4 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-07-29T12:28 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Cap champion lifetime rewards |
| 2026-07-29T12:28 | sn93 | SCORING_COMMIT | sn93 commit touches scoring: feat: Double product placement reward pay |
| 2026-07-29T10:20 | sn8 | SCORING_COMMIT | sn8 commit touches scoring: Full miner payouts (#862) |
| 2026-07-29T10:20 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-2520, review fixes: guard the scoring |
| 2026-07-29T10:20 | sn53 | SCORING_COMMIT | sn53 commit touches scoring: Merge pull request #29 from hanlinai/docs |
| 2026-07-29T10:20 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: fix(proxy+agent-challenge): unblock mine |
| 2026-07-29T07:34 | sn7 | BURN_DROP | sn7 burn fell 1.000 -> 0.317 - miners can earn again |
| 2026-07-29T07:34 | sn61 | RELEASE | sn61 released 4.8.1 |
| 2026-07-29T07:34 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Preserve live validator runtime during re |
| 2026-07-29T07:34 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: fix(agent-challenge): copy golden digest |
| 2026-07-29T04:44 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: Create a writable state directory in the  |
| 2026-07-29T04:44 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: fix(master): allowlist public FE agent-c |
| 2026-07-29T04:44 | sn101 | SCORING_COMMIT | sn101 commit touches scoring: Penalize incomplete tag submissions in m |
| 2026-07-29T01:13 | sn7 | RELEASE | sn7 released release-20260728-234943 |
| 2026-07-29T01:13 | sn7 | SCORING_COMMIT | sn7 commit touches scoring: Verify TAO transfers by settlement rather  |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

