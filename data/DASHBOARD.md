# Subnet watch — dashboard

_snapshot 2026-08-20T05:41:58Z · block 8883980 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 55 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 90 | `miner_burn` < 0.99 |
| Ranked | 90 | passed every gate |
| **Positive margin** | **55** | income beats machine cost |
| New events this window | 3 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 60 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 38 | `██████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 76.7 | 67.95 | 120 | cpu-small | 13 | 20% |
| 2 | sn121 sundae_bar | 74.6 | 1,115 | 1,115 = | cpu-small | 2 | 60% |
| 3 | sn67 Harnyx | 72.4 | 22.92 | 307 | cpu-small | 147 | 9% |
| 4 | sn23 Trishool | 72 | 522 | 522 = | cpu-small | 2 | 80% |
| 5 | sn15 ORO | 70.2 | 18.59 | 17,566 | cpu-small | 85 | 92% |
| 6 | sn56 Gradients | 69.6 | 656 | 996 | rtx4090* | 5 | 72% |
| 7 | sn91 cascade | 69.1 | 574 | 2,320 | rtx4090* | 5 | 52% |
| 8 | sn38 ChronoLLM | 67.5 | 148 | 3,144 | cpu-small | 10 | 52% |
| 9 | sn26 Perturb | 67.1 | 16.23 | 235 | rtx3060 | 10 | 70% |
| 10 | sn96 Verathos | 65.8 | 11.93 | 294 | rtx4090 | 95 | 40% |
| 11 | sn85 Vidaio | 64.1 | 128 | 192 | rtx4090* | 13 | 42% |
| 12 | sn107 Minos | 64 | 111 | 37,178 | cpu-small | 19 | 91% |
| 13 | sn108 Prometheon | 63.7 | 113 | 166 | rtx4090* | 7 | 66% |
| 14 | sn60 Bitsec.ai | 62 | 909 | 909 = | cpu-small | 3 | 50% |
| 15 | sn51 lium.io | 61.7 | 70.53 | 1,128 | rtx4090* | 47 | 81% |
| 16 | sn55 NIOME | 61.6 | 59.26 | 495 | rtx4090* | 11 | 29% |
| 17 | sn81 Reliquary | 61.3 | 54.88 | 223 | rtx4090* | 55 | 6% |
| 18 | sn102 ConnitoAI | 60 | 1,316 | 1,568 | rtx4090* | 6 | 27% |
| 19 | sn53 engy | 59.8 | 34.60 | 232 | rtx4090 | 144 | 63% |
| 20 | sn21 AdTAO | 58.6 | 1.40 | 382 | cpu-small | 16 | 37% |

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
| dominated (60–90%) | 20 |
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
| 2026-08-20T05:42 | sn80 | BURN_DROP | sn80 burn fell 1.000 -> 0.908 - miners can earn again |
| 2026-08-20T05:42 | sn92 | README_TASK_DIFF | sn92 README task/scoring sections changed |
| 2026-08-20T04:49 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Preserve restart timing across miner boot |
| 2026-08-20T03:58 | sn21 | RELEASE | sn21 released SN21 rich training data v2 |
| 2026-08-20T03:58 | sn23 | SCORING_COMMIT | sn23 commit touches scoring: Merge pull request #48 from TrishoolAI/fe |
| 2026-08-20T03:58 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: Merge pull request #166 from BaseIntelli |
| 2026-08-20T03:07 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: test: rehearse miner maintenance first ro |
| 2026-08-20T03:07 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: Show miners the cutoff and what their com |
| 2026-08-20T01:53 | sn26 | SCORING_COMMIT | sn26 commit touches scoring: Merge pull request #51 from 0xsigurd/feat |
| 2026-08-20T01:53 | sn26 | README_TASK_DIFF | sn26 README task/scoring sections changed |
| 2026-08-20T01:53 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Preserve verifier literals in restart boo |
| 2026-08-20T01:53 | sn108 | SCORING_COMMIT | sn108 commit touches scoring: fix(cli): model verify printed fields th |
| 2026-08-20T00:02 | sn7 | RELEASE | sn7 released release-20260819-235753: Activate: quorum short-circuit + |
| 2026-08-19T21:50 | sn7 | RELEASE | sn7 released release-20260819-213008: Record the finney TAO bond vault |
| 2026-08-19T21:50 | sn7 | SCORING_COMMIT | sn7 commit touches scoring: Trim pre-window crown tails before the sco |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

