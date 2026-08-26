# Subnet watch — dashboard

_snapshot 2026-08-26T11:39:58Z · block 8928969 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 54 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 89 | `miner_burn` < 0.99 |
| Ranked | 89 | passed every gate |
| **Positive margin** | **54** | income beats machine cost |
| New events this window | 3 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 61 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 6 | `███` |
| 0.6–0.8 | 7 | `███` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 39 | `██████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 80.1 | 164 | 369 | cpu-small | 13 | 20% |
| 2 | sn60 Bitsec.ai | 76.3 | 1,847 | 1,847 = | cpu-small | 2 | 50% |
| 3 | sn3 Teutonic | 75.6 | 3,899 | 3,899 = | rtx4090* | 5 | 20% |
| 4 | sn23 Trishool | 72.1 | 542 | 542 = | cpu-small | 2 | 80% |
| 5 | sn15 ORO | 71 | 22.73 | 43.00 | cpu-small | 95 | 92% |
| 6 | sn67 Harnyx | 70.5 | 14.44 | 256 | cpu-small | 137 | 7% |
| 7 | sn38 ChronoLLM | 70.3 | 323 | 817 | cpu-small | 6 | 53% |
| 8 | sn56 Gradients | 69.6 | 655 | 1,080 | rtx4090* | 6 | 73% |
| 9 | sn91 cascade | 68.9 | 538 | 1,449 | rtx4090* | 5 | 52% |
| 10 | sn1 Apex | 68.7 | 500 | 1,206 | rtx4090* | 5 | 54% |
| 11 | sn26 Perturb | 68.1 | 21.22 | 403 | rtx3060 | 10 | 70% |
| 12 | sn124 Swarm | 66.7 | 289 | 867 | rtx4090* | 25 | 10% |
| 13 | sn21 AdTAO | 66.5 | 6.42 | 1,185 | cpu-small | 16 | 45% |
| 14 | sn61 RedTeam | 65.1 | 173 | 259 | rtx4090* | 30 | 5% |
| 15 | sn107 Minos | 65.1 | 143 | 41,386 | cpu-small | 20 | 90% |
| 16 | sn81 Reliquary | 63.3 | 101 | 298 | rtx4090* | 38 | 7% |
| 17 | sn121 sundae_bar | 63 | 1,241 | 1,241 = | cpu-small | 2 | 60% |
| 18 | sn108 Prometheon | 62.6 | 80.67 | 207 | rtx4090* | 9 | 29% |
| 19 | sn28 gm | 61.9 | 67.48 | 1,689 | rtx4090* | 71 | 14% |
| 20 | sn51 lium.io | 59.6 | 41.65 | 2,396 | rtx4090* | 55 | 75% |

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
| dominated (60–90%) | 15 |
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
| 2026-08-26T11:40 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-2467, mixed scoring for partially ren |
| 2026-08-26T10:49 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: feat(rewards): publish the allocation aud |
| 2026-08-26T10:49 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: feat(batch): reuse canonical miner artif |
| 2026-08-26T09:54 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: fix(selection): retain serving miners an |
| 2026-08-26T09:54 | sn112 | SCORING_COMMIT | sn112 commit touches scoring: feat(scoring): give the JS sandbox the A |
| 2026-08-26T08:58 | sn25 | RELEASE | sn25 released v2026.8.26-1029312040 |
| 2026-08-26T08:58 | sn44 | SCORING_COMMIT | sn44 commit touches scoring: Merge pull request #55 from score-technol |
| 2026-08-26T08:58 | sn61 | RELEASE | sn61 released 4.10.0 |
| 2026-08-26T08:58 | sn61 | SCORING_COMMIT | sn61 commit touches scoring: deps: update bot virus challenge image ve |
| 2026-08-26T08:58 | sn112 | SCORING_COMMIT | sn112 commit touches scoring: fix(964): optimizeYield can be scored —  |
| 2026-08-26T07:56 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: fix(validation): make claim assessments  |
| 2026-08-26T05:48 | sn82 | SCORING_COMMIT | sn82 commit touches scoring: fix: score title fights by complete topic |
| 2026-08-26T04:09 | sn25 | RELEASE | sn25 released v2026.8.25-1029146630 |
| 2026-08-26T01:55 | sn25 | RELEASE | sn25 released v2026.8.25-1029027010 |
| 2026-08-26T01:55 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: fix(validator): close submission ingress  |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

