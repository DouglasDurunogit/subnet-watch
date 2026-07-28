# Subnet watch — dashboard

_snapshot 2026-07-28T21:37:21Z · block 8723197 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 52 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 92 | `miner_burn` < 0.99 |
| Ranked | 92 | passed every gate |
| **Positive margin** | **52** | income beats machine cost |
| New events this window | 3 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 58 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 7 | `███` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 36 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 76.2 | 1,805 | 1,805 = | cpu-small | 1 | 100% |
| 2 | sn98 NeverPlayAlone | 76.1 | 1,764 | 1,764 = | cpu-small | 1 | 100% |
| 3 | sn67 Harnyx | 68.8 | 8.62 | 897 | cpu-small | 60 | 19% |
| 4 | sn85 Vidaio | 68 | 413 | 714 | rtx4090* | 10 | 23% |
| 5 | sn15 ORO | 67.6 | 9.24 | 18.29 | cpu-small | 83 | 93% |
| 6 | sn124 Swarm | 67.4 | 346 | 703 | rtx4090* | 16 | 13% |
| 7 | sn28 gm | 61 | 51.92 | 1,587 | rtx4090* | 9 | 66% |
| 8 | sn102 ConnitoAI | 55.4 | 8.67 | 1,277 | rtx4090* | 9 | 33% |
| 9 | sn71 Leadpoet | 53.6 | 4.58 | 310 | rtx4090* | 47 | 31% |
| 10 | sn23 Trishool | 52.2 | 971 | 971 = | cpu-small | 3 | 33% |
| 11 | sn120 Affine | 47.6 | 6,535 | 6,535 = | rtx4090* | 5 | 20% |
| 12 | sn4 Targon | 47.3 | 6,123 | 10,113 | rtx4090* | 8 | 32% |
| 13 | sn60 Bitsec.ai | 44.4 | 976 | 976 = | cpu-small | 2 | 51% |
| 14 | sn107 Minos | 42.7 | 103 | 27,161 | cpu-small | 20 | 89% |
| 15 | sn1 Apex | 41.6 | 1,110 | 1,983 | rtx4090* | 5 | 41% |
| 16 | sn77 Liquidity | 39.3 | 551 | 707 | rtx4090* | 11 | 19% |
| 17 | sn74 Gittensor | 39.3 | -2.21 | 268 | rtx4090* | 55 | 29% |
| 18 | sn103 Djinn | 39.3 | -7.31 | -7.24 | rtx4090* | 250 | 79% |
| 19 | sn56 Gradients | 39.3 | -7.33 | 703 | rtx4090* | 22 | 70% |
| 20 | sn89 InfiniteQuant | 39.3 | -8.15 | 152 | rtx4090* | 34 | 44% |

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
| dominated (60–90%) | 15 |
| captured (>90%) | 27 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 107 |
| min_compute.yml (curated) | 9 |
| code-submission (validator runs it) | 8 |
| README keywords (GUESS) | 3 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-07-28T21:37 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: feat(agent-challenge): NO_PHALA host pip |
| 2026-07-28T21:37 | sn103 | RELEASE | sn103 released v2004: validator: default settle gate budget to 1024 |
| 2026-07-28T21:37 | sn103 | SCORING_COMMIT | sn103 commit touches scoring: validator: default settle gate budget to |
| 2026-07-28T20:08 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: feat(validator): warn on startup when hos |
| 2026-07-28T20:08 | sn62 | BURN_DROP | sn62 burn fell 1.000 -> 0.038 - miners can earn again |
| 2026-07-28T20:08 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: Let the sandboxed agent write its workspa |
| 2026-07-28T18:40 | sn69 | SCORING_COMMIT | sn69 commit touches scoring: Add miner/validator operator guides + val |
| 2026-07-28T18:40 | sn76 | BURN_DROP | sn76 burn fell 1.000 -> 0.000 - miners can earn again |
| 2026-07-28T18:40 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: Stop counting unrunnable tasks as wrong a |
| 2026-07-28T18:40 | sn98 | SCORING_COMMIT | sn98 commit touches scoring: feat: auto-prune old validator round work |
| 2026-07-28T16:58 | sn55 | BURN_DROP | sn55 burn fell 1.000 -> 0.020 - miners can earn again |
| 2026-07-28T16:58 | sn74 | RELEASE | sn74 released release-20260728-153232: chore(weights): zero metagraphe |
| 2026-07-28T16:58 | sn76 | SCORING_COMMIT | sn76 commit touches scoring: Pay the reserved share in full from the f |
| 2026-07-28T16:58 | sn102 | RELEASE | sn102 released v0.3.2 |
| 2026-07-28T16:58 | sn102 | SCORING_COMMIT | sn102 commit touches scoring: 📊 telemetry: per-round baseline loss (va |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

