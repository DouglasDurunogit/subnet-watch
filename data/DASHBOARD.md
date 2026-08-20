# Subnet watch — dashboard

_snapshot 2026-08-20T07:23:04Z · block 8884485 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 54 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 90 | `miner_burn` < 0.99 |
| Ranked | 90 | passed every gate |
| **Positive margin** | **54** | income beats machine cost |
| New events this window | 1 | see ALARMS.md |

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
| 1 | sn76 Phylax | 76.6 | 67.89 | 120 | cpu-small | 13 | 20% |
| 2 | sn121 sundae_bar | 74.6 | 1,113 | 1,113 = | cpu-small | 2 | 60% |
| 3 | sn23 Trishool | 72 | 521 | 521 = | cpu-small | 2 | 80% |
| 4 | sn67 Harnyx | 71.9 | 20.16 | 358 | cpu-small | 163 | 10% |
| 5 | sn15 ORO | 70.3 | 18.62 | 17,594 | cpu-small | 85 | 92% |
| 6 | sn56 Gradients | 69.6 | 655 | 995 | rtx4090* | 5 | 72% |
| 7 | sn91 cascade | 69.2 | 578 | 2,337 | rtx4090* | 5 | 52% |
| 8 | sn38 ChronoLLM | 67.5 | 149 | 3,166 | cpu-small | 10 | 52% |
| 9 | sn26 Perturb | 67.1 | 16.51 | 239 | rtx3060 | 10 | 70% |
| 10 | sn1 Apex | 66 | 226 | 1,799 | rtx4090* | 4 | 53% |
| 11 | sn96 Verathos | 66 | 12.46 | 296 | rtx4090 | 96 | 40% |
| 12 | sn107 Minos | 64.5 | 123 | 37,041 | cpu-small | 20 | 90% |
| 13 | sn85 Vidaio | 64.1 | 128 | 192 | rtx4090* | 13 | 42% |
| 14 | sn108 Prometheon | 63.8 | 115 | 170 | rtx4090* | 7 | 66% |
| 15 | sn60 Bitsec.ai | 62 | 906 | 906 = | cpu-small | 3 | 50% |
| 16 | sn28 gm | 61.5 | 59.26 | 1,538 | rtx4090* | 48 | 26% |
| 17 | sn81 Reliquary | 61.5 | 58.82 | 201 | rtx4090* | 54 | 5% |
| 18 | sn55 NIOME | 61.5 | 58.73 | 494 | rtx4090* | 11 | 29% |
| 19 | sn51 lium.io | 61.3 | 61.96 | 1,154 | rtx4090* | 49 | 80% |
| 20 | sn53 engy | 59.9 | 35.16 | 235 | rtx4090 | 144 | 63% |

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
| 2026-08-20T07:23 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: fix(scoring): handle missing claim asses |
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

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

