# Subnet watch — dashboard

_snapshot 2026-08-22T08:44:36Z · block 8899292 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 52 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 90 | `miner_burn` < 0.99 |
| Ranked | 90 | passed every gate |
| **Positive margin** | **52** | income beats machine cost |
| New events this window | 4 | see ALARMS.md |

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
| 1 | sn76 Phylax | 77.3 | 79.98 | 134 | cpu-small | 13 | 20% |
| 2 | sn102 ConnitoAI | 72.8 | 1,703 | 1,705 | rtx4090* | 4 | 25% |
| 3 | sn23 Trishool | 72.3 | 569 | 569 = | cpu-small | 2 | 80% |
| 4 | sn67 Harnyx | 72.2 | 23.15 | 451 | cpu-small | 139 | 12% |
| 5 | sn56 Gradients | 70 | 750 | 1,084 | rtx4090* | 5 | 73% |
| 6 | sn91 cascade | 69.9 | 722 | 2,912 | rtx4090* | 5 | 52% |
| 7 | sn15 ORO | 69.6 | 17.68 | 22,006 | cpu-small | 59 | 95% |
| 8 | sn1 Apex | 68.6 | 492 | 1,160 | rtx4090* | 5 | 54% |
| 9 | sn26 Perturb | 67.5 | 18.12 | 259 | rtx3060 | 10 | 70% |
| 10 | sn96 Verathos | 66.7 | 14.88 | 453 | rtx4090 | 97 | 40% |
| 11 | sn38 ChronoLLM | 66.6 | 117 | 1,597 | cpu-small | 10 | 52% |
| 12 | sn107 Minos | 65.7 | 162 | 44,510 | cpu-small | 20 | 90% |
| 13 | sn85 Vidaio | 64.2 | 131 | 410 | rtx4090* | 13 | 42% |
| 14 | sn81 Reliquary | 63.3 | 98.84 | 222 | rtx4090* | 42 | 5% |
| 15 | sn108 Prometheon | 61.4 | 57.24 | 396 | rtx4090* | 8 | 66% |
| 16 | sn53 engy | 59.8 | 35.02 | 234 | rtx4090 | 144 | 63% |
| 17 | sn60 Bitsec.ai | 59.7 | 462 | 462 = | cpu-small | 3 | 50% |
| 18 | sn51 lium.io | 59.3 | 38.53 | 5,264 | rtx4090* | 53 | 67% |
| 19 | sn28 gm | 59.3 | 31.50 | 1,412 | rtx4090* | 55 | 20% |
| 20 | sn61 RedTeam | 58.1 | 20.33 | 279 | rtx4090* | 84 | 6% |

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
| concentrated (30–60%) | 17 |
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
| 2026-08-22T02:43 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: Sort the constants import in the validato |
| 2026-08-22T01:47 | sn25 | RELEASE | sn25 released v2026.8.21-1025613560 |
| 2026-08-22T00:02 | sn97 | SCORING_COMMIT | sn97 commit touches scoring: feat: weighted reference-anchored scoring |
| 2026-08-21T23:35 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: chore: remove dead BackendClient top-mine |
| 2026-08-21T22:02 | sn90 | RELEASE | sn90 released v1.1.5 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

