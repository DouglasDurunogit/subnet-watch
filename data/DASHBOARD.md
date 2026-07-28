# Subnet watch — dashboard

_snapshot 2026-07-28T20:08:11Z · block 8722752 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 53 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 93 | `miner_burn` < 0.99 |
| Ranked | 93 | passed every gate |
| **Positive margin** | **53** | income beats machine cost |
| New events this window | 3 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 57 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 7 | `███` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 9 | `████` |
| ≥0.99 dead | 35 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 76.2 | 1,832 | 1,832 = | cpu-small | 1 | 100% |
| 2 | sn67 Harnyx | 68.9 | 8.71 | 906 | cpu-small | 60 | 19% |
| 3 | sn98 NeverPlayAlone | 68.7 | 194 | 194 = | cpu-small | 2 | 89% |
| 4 | sn85 Vidaio | 67.8 | 389 | 676 | rtx4090* | 10 | 21% |
| 5 | sn102 ConnitoAI | 67.7 | 370 | 1,263 | rtx4090* | 7 | 33% |
| 6 | sn15 ORO | 67.6 | 9.13 | 18.23 | cpu-small | 82 | 93% |
| 7 | sn124 Swarm | 67.4 | 347 | 706 | rtx4090* | 16 | 13% |
| 8 | sn28 gm | 64.1 | 128 | 1,863 | rtx4090* | 8 | 64% |
| 9 | sn23 Trishool | 52.2 | 976 | 976 = | cpu-small | 3 | 33% |
| 10 | sn71 Leadpoet | 51.6 | 2.07 | 312 | rtx4090* | 50 | 30% |
| 11 | sn120 Affine | 47.5 | 6,486 | 6,486 = | rtx4090* | 5 | 20% |
| 12 | sn4 Targon | 47.4 | 6,164 | 10,182 | rtx4090* | 8 | 32% |
| 13 | sn60 Bitsec.ai | 43.9 | 851 | 851 = | cpu-small | 2 | 59% |
| 14 | sn107 Minos | 42.3 | 93.05 | 28,205 | cpu-small | 20 | 90% |
| 15 | sn1 Apex | 41.7 | 1,125 | 2,009 | rtx4090* | 5 | 42% |
| 16 | sn74 Gittensor | 39.3 | -1.97 | 282 | rtx4090* | 55 | 26% |
| 17 | sn103 Djinn | 39.3 | -7.32 | -7.21 | rtx4090* | 250 | 79% |
| 18 | sn56 Gradients | 39.3 | -7.33 | 705 | rtx4090* | 22 | 70% |
| 19 | sn89 InfiniteQuant | 39.3 | -8.15 | 152 | rtx4090* | 34 | 43% |
| 20 | sn64 Chutes | 37.6 | 2,230 | 11,044 | a100-80 | 17 | 23% |

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
| dominated (60–90%) | 16 |
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
| 2026-07-28T16:58 | sn124 | SCORING_COMMIT | sn124 commit touches scoring: Start evaluation at the full worker widt |
| 2026-07-28T15:04 | sn28 | RELEASE | sn28 released v0.3.12 |
| 2026-07-28T15:04 | sn56 | SCORING_COMMIT | sn56 commit touches scoring: feat(validator): auto-balance emission sp |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

