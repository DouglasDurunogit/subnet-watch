# Subnet watch — dashboard

_snapshot 2026-09-27T05:12:04Z · block 9156948 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 57 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 96 | `miner_burn` < 0.99 |
| Ranked | 96 | passed every gate |
| **Positive margin** | **57** | income beats machine cost |
| New events this window | 4 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 64 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 7 | `███` |
| 0.4–0.6 | 2 | `█` |
| 0.6–0.8 | 10 | `████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 32 | `██████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn91 cascade | 72.6 | 616 | 2,466 | cpu-small | 5 | 52% |
| 2 | sn1 Apex | 71.3 | 1,091 | 1,201 | rtx4090* | 4 | 54% |
| 3 | sn56 Gradients | 71.2 | 1,052 | 5,984 | rtx4090* | 8 | 40% |
| 4 | sn38 ChronoLLM | 70.5 | 349 | 3,070 | cpu-small | 10 | 52% |
| 5 | sn67 Harnyx | 70.1 | 12.72 | 1,289 | cpu-small | 103 | 36% |
| 6 | sn102 ConnitoAI | 69.9 | 723 | 1,623 | rtx4090* | 7 | 27% |
| 7 | sn107 Minos | 69.3 | 389 | 30,922 | cpu-small | 20 | 79% |
| 8 | sn15 ORO | 69.3 | 14.16 | 21,996 | cpu-small | 73 | 95% |
| 9 | sn96 Verathos | 68.6 | 24.65 | 271 | rtx4090 | 77 | 30% |
| 10 | sn4 Targon | 68.5 | 16,420 | 29,703 | rtx4090* | 5 | 58% |
| 11 | sn124 Swarm | 67.2 | 331 | 995 | rtx4090* | 25 | 11% |
| 12 | sn111 Claims | 67.1 | 332 | 2,966 | rtx4090* | 5 | 70% |
| 13 | sn3 Teutonic | 64.9 | 5,631 | 5,631 = | rtx4090* | 5 | 20% |
| 14 | sn14 Cacheon | 64.4 | 141 | 2,517 | rtx4090* | 14 | 30% |
| 15 | sn62 Ridges | 64 | 124 | 1,312 | rtx4090* | 25 | 14% |
| 16 | sn28 SayGM | 63.4 | 105 | 1,132 | rtx4090* | 62 | 20% |
| 17 | sn23 Trishool | 62.3 | 990 | 990 = | cpu-small | 2 | 80% |
| 18 | sn100 Cortex | 60.2 | 38.56 | 260 | rtx4090* | 19 | 70% |
| 19 | sn51 lium.io | 58.3 | 33.03 | 2,477 | rtx4090* | 65 | 79% |
| 20 | sn80 OpenRoboto | 58 | 714 | 2,313 | rtx4090* | 5 | 43% |

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
| concentrated (30–60%) | 21 |
| dominated (60–90%) | 21 |
| captured (>90%) | 25 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 97 |
| README keywords (GUESS) | 11 |
| min_compute.yml (curated) | 10 |
| code-submission (validator runs it) | 9 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-09-27T05:12 | sn25 | RELEASE | sn25 released v2026.9.26-1056759680 |
| 2026-09-27T05:12 | sn34 | SCORING_COMMIT | sn34 commit touches scoring: Merge pull request #464 from BitMind-AI/d |
| 2026-09-27T05:12 | sn34 | README_TASK_DIFF | sn34 README task/scoring sections changed |
| 2026-09-27T05:12 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Preserve fresh investigation budget when  |
| 2026-09-26T23:56 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Bind verified homepage navigation source |
| 2026-09-26T21:37 | sn15 | RELEASE | sn15 released v2.0.32: fix(validator): save downloaded agent source as |
| 2026-09-26T21:37 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: fix(validator): save downloaded agent sou |
| 2026-09-26T21:37 | sn25 | RELEASE | sn25 released v2026.9.26-1056505490 |
| 2026-09-26T21:37 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Reuse verified investigator source for at |
| 2026-09-26T18:34 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Bind protected manifest to evidence quali |
| 2026-09-26T18:34 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: Merge pull request #281 from reliquadotai |
| 2026-09-26T15:04 | sn7 | RELEASE | sn7 released release-20260926-135859 |
| 2026-09-26T15:04 | sn7 | SCORING_COMMIT | sn7 commit touches scoring: Hide alpha price flags from alw miner quot |
| 2026-09-26T15:04 | sn14 | SCORING_COMMIT | sn14 commit touches scoring: Show potential winners and link scoring b |
| 2026-09-26T15:04 | sn22 | SCORING_COMMIT | sn22 commit touches scoring: feat: burn all emission and stop querying |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

