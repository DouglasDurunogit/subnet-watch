# Subnet watch — dashboard

_snapshot 2026-08-20T09:47:00Z · block 8885205 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 54 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 92 | `miner_burn` < 0.99 |
| Ranked | 92 | passed every gate |
| **Positive margin** | **54** | income beats machine cost |
| New events this window | 9 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 60 | `████████████████████████████` |
| 0–0.2 | 4 | `██` |
| 0.2–0.4 | 7 | `███` |
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 8 | `████` |
| ≥0.99 dead | 36 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 76.7 | 69.26 | 123 | cpu-small | 13 | 20% |
| 2 | sn23 Trishool | 72.1 | 532 | 532 = | cpu-small | 2 | 80% |
| 3 | sn67 Harnyx | 71.9 | 20.62 | 365 | cpu-small | 166 | 10% |
| 4 | sn15 ORO | 70.3 | 18.79 | 18,406 | cpu-small | 80 | 92% |
| 5 | sn56 Gradients | 69.7 | 668 | 1,015 | rtx4090* | 5 | 72% |
| 6 | sn91 cascade | 69.3 | 597 | 2,412 | rtx4090* | 5 | 52% |
| 7 | sn38 ChronoLLM | 67.6 | 152 | 3,222 | cpu-small | 10 | 52% |
| 8 | sn26 Perturb | 67.2 | 16.86 | 244 | rtx3060 | 10 | 70% |
| 9 | sn1 Apex | 66.1 | 233 | 1,810 | rtx4090* | 4 | 53% |
| 10 | sn96 Verathos | 65.7 | 11.64 | 288 | rtx4090 | 96 | 40% |
| 11 | sn107 Minos | 64.5 | 128 | 37,894 | cpu-small | 20 | 90% |
| 12 | sn85 Vidaio | 64.4 | 139 | 218 | rtx4090* | 13 | 42% |
| 13 | sn108 Prometheon | 64.1 | 127 | 187 | rtx4090* | 7 | 66% |
| 14 | sn60 Bitsec.ai | 62.1 | 939 | 939 = | cpu-small | 3 | 50% |
| 15 | sn51 lium.io | 61.6 | 68.52 | 1,276 | rtx4090* | 47 | 80% |
| 16 | sn55 NIOME | 61.6 | 60.09 | 504 | rtx4090* | 11 | 29% |
| 17 | sn28 gm | 61.5 | 59.85 | 1,556 | rtx4090* | 49 | 32% |
| 18 | sn81 Reliquary | 61.2 | 53.22 | 204 | rtx4090* | 54 | 5% |
| 19 | sn53 engy | 59.8 | 35.05 | 234 | rtx4090 | 144 | 63% |
| 20 | sn102 ConnitoAI | 57.5 | 614 | 1,798 | rtx4090* | 7 | 30% |

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
| wide (<30%) | 23 |
| concentrated (30–60%) | 21 |
| dominated (60–90%) | 19 |
| captured (>90%) | 27 |

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
| 2026-08-20T09:47 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-08-20T09:47 | sn67 | README_TASK_DIFF | sn67 README task/scoring sections changed |
| 2026-08-20T09:47 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: Take telemetry from miners and serve it b |
| 2026-08-20T09:47 | sn100 | RELEASE | sn100 released v3.3.26: fix(validator): persist last sealed bundle acr |
| 2026-08-20T09:47 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: Merge pull request #183 from BaseIntelli |
| 2026-08-20T08:54 | sn7 | BURN_DROP | sn7 burn fell 0.992 -> 0.978 - miners can earn again |
| 2026-08-20T08:54 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Keep validator CID diagnostics off JSON s |
| 2026-08-20T08:54 | sn75 | SCORING_COMMIT | sn75 commit touches scoring: Merge pull request #53 from thenervelab/f |
| 2026-08-20T08:54 | sn113 | BURN_DROP | sn113 burn fell 1.000 -> 0.990 - miners can earn again |
| 2026-08-20T08:05 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-2715: withhold the unrented incentive |
| 2026-08-20T07:23 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: fix(scoring): handle missing claim asses |
| 2026-08-20T05:42 | sn80 | BURN_DROP | sn80 burn fell 1.000 -> 0.908 - miners can earn again |
| 2026-08-20T05:42 | sn92 | README_TASK_DIFF | sn92 README task/scoring sections changed |
| 2026-08-20T04:49 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Preserve restart timing across miner boot |
| 2026-08-20T03:58 | sn21 | RELEASE | sn21 released SN21 rich training data v2 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

