# Subnet watch — dashboard

_snapshot 2026-08-20T15:04:16Z · block 8886790 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 55 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 92 | `miner_burn` < 0.99 |
| Ranked | 92 | passed every gate |
| **Positive margin** | **55** | income beats machine cost |
| New events this window | 3 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 61 | `████████████████████████████` |
| 0–0.2 | 4 | `██` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 9 | `████` |
| ≥0.99 dead | 36 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 76.7 | 69.20 | 123 | cpu-small | 13 | 20% |
| 2 | sn67 Harnyx | 72 | 21.21 | 282 | cpu-small | 174 | 8% |
| 3 | sn23 Trishool | 71.9 | 512 | 512 = | cpu-small | 2 | 80% |
| 4 | sn15 ORO | 69.9 | 18.55 | 18,150 | cpu-small | 82 | 92% |
| 5 | sn56 Gradients | 69.6 | 665 | 1,013 | rtx4090* | 5 | 72% |
| 6 | sn1 Apex | 69.5 | 642 | 1,422 | rtx4090* | 4 | 52% |
| 7 | sn91 cascade | 69.2 | 592 | 2,393 | rtx4090* | 5 | 52% |
| 8 | sn38 ChronoLLM | 67.6 | 153 | 3,246 | cpu-small | 10 | 52% |
| 9 | sn26 Perturb | 67.2 | 16.85 | 244 | rtx3060 | 10 | 70% |
| 10 | sn96 Verathos | 66.1 | 13.02 | 366 | rtx4090 | 96 | 41% |
| 11 | sn107 Minos | 64.7 | 129 | 38,281 | cpu-small | 20 | 90% |
| 12 | sn85 Vidaio | 64.5 | 142 | 403 | rtx4090* | 13 | 42% |
| 13 | sn108 Prometheon | 63.8 | 117 | 173 | rtx4090* | 7 | 66% |
| 14 | sn28 gm | 63.5 | 108 | 1,360 | rtx4090* | 49 | 12% |
| 15 | sn60 Bitsec.ai | 62.1 | 953 | 953 = | cpu-small | 3 | 50% |
| 16 | sn81 Reliquary | 61.7 | 61.77 | 227 | rtx4090* | 53 | 6% |
| 17 | sn55 NIOME | 61.6 | 59.90 | 500 | rtx4090* | 11 | 29% |
| 18 | sn51 lium.io | 61.5 | 66.05 | 1,163 | rtx4090* | 45 | 82% |
| 19 | sn53 engy | 59.9 | 35.25 | 235 | rtx4090 | 144 | 63% |
| 20 | sn41 Almanac | 55.3 | 11.38 | 24.17 | cpu-small | 76 | 72% |

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
| concentrated (30–60%) | 20 |
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
| 2026-08-20T14:10 | sn10 | SCORING_COMMIT | sn10 commit touches scoring: feat(api): public read API for rounds, le |
| 2026-08-20T14:10 | sn28 | RELEASE | sn28 released v0.4.9 |
| 2026-08-20T14:10 | sn89 | SCORING_COMMIT | sn89 commit touches scoring: README: a validator needs NO market-data  |
| 2026-08-20T13:27 | sn66 | RELEASE | sn66 released Payment and IAM update |
| 2026-08-20T12:15 | sn28 | RELEASE | sn28 released v0.4.9-dev |
| 2026-08-20T11:38 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: docs: point miners at rich training v2 an |
| 2026-08-20T11:38 | sn89 | SCORING_COMMIT | sn89 commit touches scoring: build_hf_scoreboard: HF status speaks the |
| 2026-08-20T10:57 | sn89 | SCORING_COMMIT | sn89 commit touches scoring: scripts/import_checkpoint.py: seed a vali |
| 2026-08-20T10:16 | sn44 | SCORING_COMMIT | sn44 commit touches scoring: update min challenge private |
| 2026-08-20T10:16 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: Add the miner axon and document telemetry |
| 2026-08-20T09:47 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-08-20T09:47 | sn67 | README_TASK_DIFF | sn67 README task/scoring sections changed |
| 2026-08-20T09:47 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: Take telemetry from miners and serve it b |
| 2026-08-20T09:47 | sn100 | RELEASE | sn100 released v3.3.26: fix(validator): persist last sealed bundle acr |
| 2026-08-20T09:47 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: Merge pull request #183 from BaseIntelli |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

