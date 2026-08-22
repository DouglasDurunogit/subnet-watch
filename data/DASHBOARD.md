# Subnet watch — dashboard

_snapshot 2026-08-22T17:02:15Z · block 8901780 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 51 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 89 | `miner_burn` < 0.99 |
| Ranked | 89 | passed every gate |
| **Positive margin** | **51** | income beats machine cost |
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
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 39 | `██████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 77 | 75.30 | 133 | cpu-small | 13 | 20% |
| 2 | sn67 Harnyx | 72.4 | 22.94 | 119 | cpu-small | 151 | 12% |
| 3 | sn62 Ridges | 71.7 | 1,214 | 2,990 | rtx4090* | 6 | 39% |
| 4 | sn56 Gradients | 70 | 731 | 1,076 | rtx4090* | 5 | 73% |
| 5 | sn102 ConnitoAI | 69.8 | 698 | 2,202 | rtx4090* | 7 | 32% |
| 6 | sn91 cascade | 69.7 | 682 | 2,754 | rtx4090* | 5 | 52% |
| 7 | sn15 ORO | 69.7 | 18.33 | 21,885 | cpu-small | 61 | 95% |
| 8 | sn1 Apex | 68.7 | 502 | 1,265 | rtx4090* | 5 | 51% |
| 9 | sn26 Perturb | 67.5 | 17.94 | 257 | rtx3060 | 10 | 70% |
| 10 | sn11 TrajectoryRL | 67.4 | 4,620 | 4,620 = | cpu-small | 1 | 100% |
| 11 | sn96 Verathos | 67.2 | 16.70 | 457 | rtx4090 | 95 | 41% |
| 12 | sn38 ChronoLLM | 66.5 | 115 | 1,567 | cpu-small | 10 | 52% |
| 13 | sn107 Minos | 65.3 | 152 | 44,282 | cpu-small | 20 | 90% |
| 14 | sn85 Vidaio | 64.4 | 137 | 404 | rtx4090* | 13 | 42% |
| 15 | sn108 Prometheon | 63.9 | 119 | 129 | rtx4090* | 8 | 66% |
| 16 | sn81 Reliquary | 63.7 | 113 | 213 | rtx4090* | 39 | 5% |
| 17 | sn51 lium.io | 60.6 | 52.63 | 4,581 | rtx4090* | 53 | 68% |
| 18 | sn60 Bitsec.ai | 59.8 | 481 | 481 = | cpu-small | 3 | 50% |
| 19 | sn28 gm | 59.8 | 36.20 | 1,646 | rtx4090* | 55 | 14% |
| 20 | sn53 engy | 59.6 | 32.46 | 220 | rtx4090 | 144 | 63% |

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
| concentrated (30–60%) | 19 |
| dominated (60–90%) | 19 |
| captured (>90%) | 25 |

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
| 2026-08-22T16:37 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: Build the validator registry from the per |
| 2026-08-22T16:00 | sn81 | SCORING_COMMIT | sn81 commit touches scoring: feat: validator checkpoint intake — stage |
| 2026-08-22T14:35 | sn92 | RELEASE | sn92 released v0.1.14 |
| 2026-08-22T13:41 | sn92 | RELEASE | sn92 released v0.1.13 |
| 2026-08-22T12:57 | sn92 | RELEASE | sn92 released v0.1.11 |
| 2026-08-22T12:57 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: Make the validator guide match the code a |
| 2026-08-22T12:01 | sn92 | RELEASE | sn92 released v0.1.9 |
| 2026-08-22T11:32 | sn92 | RELEASE | sn92 released v0.1.7 |
| 2026-08-22T10:36 | sn44 | SCORING_COMMIT | sn44 commit touches scoring: Merge pull request #54 from score-technol |
| 2026-08-22T10:36 | sn92 | RELEASE | sn92 released v0.1.6 |
| 2026-08-22T09:13 | sn92 | RELEASE | sn92 released v0.1.4 |
| 2026-08-22T08:45 | sn92 | RELEASE | sn92 released v0.1.3 |
| 2026-08-22T08:03 | sn61 | RELEASE | sn61 released 4.9.7 |
| 2026-08-22T08:03 | sn61 | SCORING_COMMIT | sn61 commit touches scoring: deps: update abs_challenge submodule to v |
| 2026-08-22T08:03 | sn92 | RELEASE | sn92 released v0.1.2 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

