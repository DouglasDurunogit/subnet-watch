# Subnet watch — dashboard

_snapshot 2026-08-22T12:00:41Z · block 8900272 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 51 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 90 | `miner_burn` < 0.99 |
| Ranked | 90 | passed every gate |
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
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 38 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 77.2 | 78.94 | 133 | cpu-small | 13 | 20% |
| 2 | sn67 Harnyx | 72.3 | 22.79 | 444 | cpu-small | 141 | 12% |
| 3 | sn23 Trishool | 72.2 | 562 | 562 = | cpu-small | 2 | 80% |
| 4 | sn102 ConnitoAI | 71.9 | 1,314 | 2,490 | rtx4090* | 6 | 36% |
| 5 | sn62 Ridges | 71.6 | 1,206 | 2,968 | rtx4090* | 6 | 39% |
| 6 | sn56 Gradients | 70 | 730 | 1,067 | rtx4090* | 5 | 73% |
| 7 | sn91 cascade | 69.8 | 706 | 2,849 | rtx4090* | 5 | 52% |
| 8 | sn15 ORO | 69.3 | 17.95 | 21,458 | cpu-small | 61 | 95% |
| 9 | sn1 Apex | 68.5 | 479 | 1,127 | rtx4090* | 5 | 55% |
| 10 | sn11 TrajectoryRL | 67.4 | 4,579 | 4,579 = | cpu-small | 1 | 100% |
| 11 | sn26 Perturb | 67.4 | 17.80 | 255 | rtx3060 | 10 | 70% |
| 12 | sn96 Verathos | 67 | 16.21 | 414 | rtx4090 | 95 | 41% |
| 13 | sn38 ChronoLLM | 66.5 | 113 | 1,543 | cpu-small | 10 | 52% |
| 14 | sn107 Minos | 65.5 | 158 | 43,596 | cpu-small | 20 | 90% |
| 15 | sn85 Vidaio | 64.2 | 131 | 404 | rtx4090* | 13 | 42% |
| 16 | sn108 Prometheon | 63.8 | 119 | 128 | rtx4090* | 8 | 66% |
| 17 | sn81 Reliquary | 63.6 | 108 | 234 | rtx4090* | 42 | 6% |
| 18 | sn51 lium.io | 62 | 75.68 | 5,347 | rtx4090* | 50 | 65% |
| 19 | sn53 engy | 59.8 | 34.15 | 229 | rtx4090 | 144 | 63% |
| 20 | sn60 Bitsec.ai | 59.7 | 460 | 460 = | cpu-small | 3 | 50% |

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
| concentrated (30–60%) | 18 |
| dominated (60–90%) | 20 |
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
| 2026-08-22T12:01 | sn92 | RELEASE | sn92 released v0.1.9 |
| 2026-08-22T11:32 | sn92 | RELEASE | sn92 released v0.1.7 |
| 2026-08-22T10:36 | sn44 | SCORING_COMMIT | sn44 commit touches scoring: Merge pull request #54 from score-technol |
| 2026-08-22T10:36 | sn92 | RELEASE | sn92 released v0.1.6 |
| 2026-08-22T09:13 | sn92 | RELEASE | sn92 released v0.1.4 |
| 2026-08-22T08:45 | sn92 | RELEASE | sn92 released v0.1.3 |
| 2026-08-22T08:03 | sn61 | RELEASE | sn61 released 4.9.7 |
| 2026-08-22T08:03 | sn61 | SCORING_COMMIT | sn61 commit touches scoring: deps: update abs_challenge submodule to v |
| 2026-08-22T08:03 | sn92 | RELEASE | sn92 released v0.1.2 |
| 2026-08-22T05:38 | sn25 | RELEASE | sn25 released v2026.8.21-1025763520 |
| 2026-08-22T05:38 | sn92 | RELEASE | sn92 released v0.1.1 |
| 2026-08-22T05:38 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: Package the version validators actually r |
| 2026-08-22T04:17 | sn53 | RELEASE | sn53 released v0.4.5: Merge pull request #42 from hanlinai/release/0.4 |
| 2026-08-22T04:17 | sn100 | RELEASE | sn100 released v3.3.29 |
| 2026-08-22T02:43 | sn53 | SCORING_COMMIT | sn53 commit touches scoring: fix(validator): reuse one chain connectio |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

