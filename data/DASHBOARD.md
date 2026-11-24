# Subnet watch — dashboard

_snapshot 2026-11-24T20:44:55Z · block 9579085 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 49 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 104 | `miner_burn` < 0.99 |
| Ranked | 104 | passed every gate |
| **Positive margin** | **49** | income beats machine cost |
| New events this window | 13 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 72 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 6 | `██` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 9 | `████` |
| ≥0.99 dead | 24 | `█████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn42 CADmind | 81.2 | 213 | 213 = | cpu-small | 5 | 20% |
| 2 | sn3 Teutonic | 72.9 | 1,771 | 3,550 | rtx4090* | 4 | 40% |
| 3 | sn124 Swarm | 66.3 | 252 | 1,059 | rtx4090* | 10 | 27% |
| 4 | sn67 Harnyx | 64.7 | 2.33 | 244 | cpu-small | 119 | 19% |
| 5 | sn66 conjectures | 64.3 | 133 | 758 | rtx4090* | 3 | 80% |
| 6 | sn120 Affine | 63 | 3,175 | 3,175 = | rtx4090* | 6 | 17% |
| 7 | sn53 engy | 62.3 | 73.12 | 787 | rtx4090 | 20 | 61% |
| 8 | sn111 Claims | 59.8 | 35.71 | 146 | rtx4090* | 4 | 88% |
| 9 | sn62 Ridges | 59.8 | 34.89 | 366 | rtx4090* | 47 | 10% |
| 10 | sn127 Zils | 59 | 26.66 | 63.56 | rtx4090 | 5 | 88% |
| 11 | sn56 Gradients | 58.6 | 164 | 3,075 | a100-80 | 7 | 43% |
| 12 | sn25 UR | 58.1 | 20.10 | 20.10 = | rtx4090* | 10 | 45% |
| 13 | sn61 RedTeam | 57.8 | 20.90 | 39.73 | rtx4090* | 98 | 2% |
| 14 | sn58 Attune | 57.6 | 52.41 | 1,495 | rtx4090* | 57 | 30% |
| 15 | sn4 Targon | 56.8 | 7,160 | 18,010 | rtx4090* | 3 | 67% |
| 16 | sn102 ConnitoAI | 56.7 | 488 | 499 | rtx4090* | 4 | 25% |
| 17 | sn28 SayGM | 55.8 | 12.71 | 2,077 | rtx4090* | 108 | 23% |
| 18 | sn116 Carbon | 55.2 | 8,479 | 8,479 = | rtx4090* | 1 | 100% |
| 19 | sn46 Instant | 54.8 | 108 | 139 | cpu-small | 11 | 21% |
| 20 | sn38 ChronoLLM | 54.4 | 104 | 265 | cpu-small | 6 | 53% |

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
| concentrated (30–60%) | 19 |
| dominated (60–90%) | 26 |
| captured (>90%) | 29 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 97 |
| README keywords (GUESS) | 13 |
| min_compute.yml (curated) | 10 |
| code-submission (validator runs it) | 8 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-11-24T20:45 | sn12 | RELEASE | sn12 released validator-staging-2026-11-24-45412581463-636-1: feat: ad |
| 2026-11-24T20:45 | sn39 | SCORING_COMMIT | sn39 commit touches scoring: Merge pull request #34 from kokoahdotcom/ |
| 2026-11-24T20:45 | sn42 | SCORING_COMMIT | sn42 commit touches scoring: miner prompt: a community model comes fro |
| 2026-11-24T20:45 | sn50 | RELEASE | sn50 released 1.16.0 |
| 2026-11-24T20:45 | sn50 | SCORING_COMMIT | sn50 commit touches scoring: Add a synth-miner Claude Code skill and a |
| 2026-11-24T20:45 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-7069 - Validator: log VerifyX per-tes |
| 2026-11-24T20:45 | sn61 | SCORING_COMMIT | sn61 commit touches scoring: docs: update Bot Virus challenge document |
| 2026-11-24T20:45 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Verify retired champion weights before co |
| 2026-11-24T20:45 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: feat(miner): lane-b test previews with th |
| 2026-11-24T20:45 | sn92 | RELEASE | sn92 released v1.2.0-rc11.post8.19 |
| 2026-11-24T20:45 | sn99 | SCORING_COMMIT | sn99 commit touches scoring: Evaluation-host transfers resume a cut fi |
| 2026-11-24T20:45 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: King hand-over: the previous king's mine |
| 2026-11-24T20:45 | sn117 | RELEASE | sn117 released everycli v1.3.2 |
| 2026-11-24T10:13 | sn2 | BURN_DROP | sn2 burn fell 1.000 -> 0.881 - miners can earn again |
| 2026-11-24T10:13 | sn39 | README_TASK_DIFF | sn39 README task/scoring sections changed |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

