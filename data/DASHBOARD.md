# Subnet watch — dashboard

_snapshot 2026-08-09T19:10:59Z · block 8808834 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 56 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 89 | `miner_burn` < 0.99 |
| Ranked | 89 | passed every gate |
| **Positive margin** | **56** | income beats machine cost |
| New events this window | 2 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 52 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 5 | `███` |
| 0.4–0.6 | 9 | `█████` |
| 0.6–0.8 | 9 | `█████` |
| 0.8–0.99 | 8 | `████` |
| ≥0.99 dead | 39 | `█████████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn107 Minos | 78.2 | 115 | 34,320 | cpu-small | 20 | 90% |
| 2 | sn76 Phylax | 76.8 | 68.53 | 206 | cpu-small | 10 | 33% |
| 3 | sn60 Bitsec.ai | 74.9 | 1,250 | 1,250 = | cpu-small | 2 | 50% |
| 4 | sn67 Harnyx | 70.8 | 15.19 | 868 | cpu-small | 155 | 22% |
| 5 | sn91 cascade | 70.3 | 800 | 2,739 | rtx4090* | 5 | 48% |
| 6 | sn1 Apex | 70.1 | 760 | 1,567 | rtx4090* | 4 | 49% |
| 7 | sn41 Almanac | 69.5 | 11.72 | 35.02 | cpu-small | 66 | 72% |
| 8 | sn96 Verathos | 68.5 | 23.11 | 216 | rtx4090 | 68 | 42% |
| 9 | sn62 Ridges | 68.3 | 443 | 2,053 | rtx4090* | 7 | 35% |
| 10 | sn26 Perturb | 68.2 | 21.30 | 40.20 | rtx3060 | 11 | 50% |
| 11 | sn100 BASE | 68.1 | 420 | 1,704 | rtx4090* | 5 | 50% |
| 12 | sn15 ORO | 67.7 | 10.12 | 19.34 | cpu-small | 74 | 94% |
| 13 | sn38 ChronoLLM | 65.7 | 219 | 3,683 | rtx4090* | 10 | 52% |
| 14 | sn21 AdTAO | 65.5 | 4.75 | 21.98 | cpu-small | 142 | 45% |
| 15 | sn80 OpenRoboto | 65.4 | 186 | 672 | rtx4090* | 4 | 91% |
| 16 | sn28 gm | 62.9 | 90.17 | 4,158 | rtx4090* | 26 | 42% |
| 17 | sn61 RedTeam | 62.7 | 83.01 | 339 | rtx4090* | 48 | 7% |
| 18 | sn102 ConnitoAI | 59.3 | 1,072 | 1,287 | rtx4090* | 6 | 28% |
| 19 | sn6 Numinous | 59.1 | 29.81 | 342 | cpu-small | 18 | 19% |
| 20 | sn51 lium.io | 58.9 | 33.74 | 2,759 | rtx4090* | 50 | 61% |

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
| concentrated (30–60%) | 21 |
| dominated (60–90%) | 20 |
| captured (>90%) | 23 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 104 |
| code-submission (validator runs it) | 9 |
| min_compute.yml (curated) | 9 |
| README keywords (GUESS) | 5 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-08-09T18:18 | sn90 | RELEASE | sn90 released v1.0.2 — proxy version header + owner miner UID hardcode |
| 2026-08-09T18:18 | sn90 | SCORING_COMMIT | sn90 commit touches scoring: feat(validator): v1.0.2 — proxy version h |
| 2026-08-09T16:15 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Preserve handled scorer transport failure |
| 2026-08-09T13:30 | sn96 | RELEASE | sn96 released v0.1.32 - Miner Hard-Proof Transport |
| 2026-08-09T13:30 | sn96 | SCORING_COMMIT | sn96 commit touches scoring: fix: align miner proxy with hard proof de |
| 2026-08-09T10:49 | sn61 | RELEASE | sn61 released 4.9.3 |
| 2026-08-09T10:49 | sn61 | SCORING_COMMIT | sn61 commit touches scoring: deps: update challenge image version for  |
| 2026-08-09T10:49 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-08-09T10:49 | sn96 | RELEASE | sn96 released v0.1.31 - Validator Auto-Update Drain |
| 2026-08-09T10:49 | sn96 | SCORING_COMMIT | sn96 commit touches scoring: fix: drain validator work before auto-upd |
| 2026-08-09T09:53 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Use fresh identities for scorer retries |
| 2026-08-09T09:02 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Retry transient company homepage verifica |
| 2026-08-09T09:02 | sn96 | RELEASE | sn96 released v0.1.30 - Gleipnir FP8 Runtime Precision |
| 2026-08-09T08:07 | sn2 | BURN_DROP | sn2 burn fell 1.000 -> 0.826 - miners can earn again |
| 2026-08-09T05:16 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: Move inference cost off the validator and |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

