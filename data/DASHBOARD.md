# Subnet watch — dashboard

_snapshot 2026-08-20T17:00:45Z · block 8887372 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 56 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 91 | `miner_burn` < 0.99 |
| Ranked | 91 | passed every gate |
| **Positive margin** | **56** | income beats machine cost |
| New events this window | 6 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 61 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 4 | `██` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 8 | `████` |
| ≥0.99 dead | 37 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 76.8 | 70.43 | 125 | cpu-small | 13 | 20% |
| 2 | sn67 Harnyx | 72.1 | 21.40 | 285 | cpu-small | 178 | 8% |
| 3 | sn23 Trishool | 72 | 520 | 520 = | cpu-small | 2 | 80% |
| 4 | sn15 ORO | 69.9 | 18.80 | 18,377 | cpu-small | 82 | 92% |
| 5 | sn56 Gradients | 69.7 | 675 | 1,030 | rtx4090* | 5 | 72% |
| 6 | sn1 Apex | 69.5 | 646 | 1,432 | rtx4090* | 4 | 53% |
| 7 | sn91 cascade | 69.3 | 601 | 2,430 | rtx4090* | 5 | 52% |
| 8 | sn38 ChronoLLM | 67.7 | 156 | 3,302 | cpu-small | 10 | 52% |
| 9 | sn26 Perturb | 67.3 | 17.15 | 247 | rtx3060 | 10 | 70% |
| 10 | sn96 Verathos | 66.8 | 15.11 | 367 | rtx4090 | 95 | 41% |
| 11 | sn85 Vidaio | 64.6 | 145 | 417 | rtx4090* | 13 | 42% |
| 12 | sn107 Minos | 64.6 | 127 | 38,830 | cpu-small | 20 | 90% |
| 13 | sn108 Prometheon | 63.8 | 118 | 173 | rtx4090* | 7 | 66% |
| 14 | sn28 gm | 63 | 91.70 | 1,512 | rtx4090* | 49 | 13% |
| 15 | sn60 Bitsec.ai | 62.2 | 967 | 967 = | cpu-small | 3 | 50% |
| 16 | sn81 Reliquary | 61.9 | 64.67 | 211 | rtx4090* | 52 | 5% |
| 17 | sn55 NIOME | 61.6 | 60.57 | 508 | rtx4090* | 11 | 29% |
| 18 | sn51 lium.io | 61.2 | 62.10 | 1,199 | rtx4090* | 45 | 82% |
| 19 | sn102 ConnitoAI | 60.5 | 1,496 | 1,497 | rtx4090* | 4 | 25% |
| 20 | sn53 engy | 59.9 | 35.85 | 239 | rtx4090 | 144 | 63% |

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
| dominated (60–90%) | 18 |
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
| 2026-08-20T17:01 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Bind local readiness verifier environment |
| 2026-08-20T16:17 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: docs: rich-era corrections in scoring arc |
| 2026-08-20T15:47 | sn10 | SCORING_COMMIT | sn10 commit touches scoring: fix(worker): pass leaders.last_score to r |
| 2026-08-20T15:47 | sn53 | SCORING_COMMIT | sn53 commit touches scoring: tee_miner: lift the 1 MiB websocket frame |
| 2026-08-20T15:47 | sn100 | RELEASE | sn100 released v3.3.27 |
| 2026-08-20T15:47 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: fix(design-challenge): drop crate_name s |
| 2026-08-20T14:10 | sn10 | SCORING_COMMIT | sn10 commit touches scoring: feat(api): public read API for rounds, le |
| 2026-08-20T14:10 | sn28 | RELEASE | sn28 released v0.4.9 |
| 2026-08-20T14:10 | sn89 | SCORING_COMMIT | sn89 commit touches scoring: README: a validator needs NO market-data  |
| 2026-08-20T13:27 | sn66 | RELEASE | sn66 released Payment and IAM update |
| 2026-08-20T12:15 | sn28 | RELEASE | sn28 released v0.4.9-dev |
| 2026-08-20T11:38 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: docs: point miners at rich training v2 an |
| 2026-08-20T11:38 | sn89 | SCORING_COMMIT | sn89 commit touches scoring: build_hf_scoreboard: HF status speaks the |
| 2026-08-20T10:57 | sn89 | SCORING_COMMIT | sn89 commit touches scoring: scripts/import_checkpoint.py: seed a vali |
| 2026-08-20T10:16 | sn44 | SCORING_COMMIT | sn44 commit touches scoring: update min challenge private |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

