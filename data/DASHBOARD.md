# Subnet watch — dashboard

_snapshot 2026-08-24T14:27:26Z · block 8915406 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 50 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 89 | `miner_burn` < 0.99 |
| Ranked | 89 | passed every gate |
| **Positive margin** | **50** | income beats machine cost |
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
| 0.4–0.6 | 4 | `██` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 39 | `██████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 78.9 | 121 | 181 | cpu-small | 13 | 21% |
| 2 | sn3 Teutonic | 75.7 | 3,997 | 3,997 = | rtx4090* | 5 | 20% |
| 3 | sn102 ConnitoAI | 72.6 | 1,607 | 2,001 | rtx4090* | 5 | 28% |
| 4 | sn62 Ridges | 72.4 | 1,523 | 3,113 | rtx4090* | 6 | 39% |
| 5 | sn23 Trishool | 72.4 | 583 | 583 = | cpu-small | 2 | 80% |
| 6 | sn15 ORO | 71.6 | 27.56 | 26,223 | cpu-small | 81 | 93% |
| 7 | sn67 Harnyx | 71.6 | 19.17 | 165 | cpu-small | 178 | 4% |
| 8 | sn91 cascade | 69 | 545 | 1,468 | rtx4090* | 5 | 52% |
| 9 | sn1 Apex | 68.7 | 500 | 1,330 | rtx4090* | 5 | 53% |
| 10 | sn26 Perturb | 68.2 | 21.68 | 411 | rtx3060 | 10 | 70% |
| 11 | sn96 Verathos | 68 | 20.70 | 187 | rtx4090 | 93 | 40% |
| 12 | sn124 Swarm | 66.9 | 299 | 2,603 | rtx4090* | 21 | 30% |
| 13 | sn38 ChronoLLM | 66.7 | 120 | 1,634 | cpu-small | 10 | 52% |
| 14 | sn107 Minos | 65.3 | 154 | 43,702 | cpu-small | 20 | 90% |
| 15 | sn98 NeverPlayAlone | 64.7 | 2,046 | 2,046 = | cpu-small | 1 | 100% |
| 16 | sn85 Vidaio | 64.7 | 152 | 433 | rtx4090* | 13 | 42% |
| 17 | sn60 Bitsec.ai | 64.2 | 1,744 | 1,744 = | cpu-small | 2 | 50% |
| 18 | sn81 Reliquary | 64 | 124 | 395 | rtx4090* | 35 | 9% |
| 19 | sn108 Prometheon | 63.7 | 114 | 126 | rtx4090* | 9 | 66% |
| 20 | sn51 lium.io | 62 | 77.51 | 2,321 | rtx4090* | 50 | 73% |

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
| concentrated (30–60%) | 18 |
| dominated (60–90%) | 21 |
| captured (>90%) | 24 |

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
| 2026-08-24T14:27 | sn11 | RELEASE | sn11 released v0.6.33 |
| 2026-08-24T13:30 | sn3 | SCORING_COMMIT | sn3 commit touches scoring: Enforce miner upload size limit |
| 2026-08-24T13:30 | sn89 | SCORING_COMMIT | sn89 commit touches scoring: HF scoreboard: pick the tick dir by newes |
| 2026-08-24T12:16 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-08-24T11:01 | sn3 | SCORING_COMMIT | sn3 commit touches scoring: Update evaluation dataset size to 2000 for |
| 2026-08-24T11:01 | sn53 | SCORING_COMMIT | sn53 commit touches scoring: tee_miner: log the WebSocket close code,  |
| 2026-08-24T11:01 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: fix(miner): accept monitoring task metada |
| 2026-08-24T09:13 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: docs(quickstart): troubleshooting row for |
| 2026-08-24T09:13 | sn53 | SCORING_COMMIT | sn53 commit touches scoring: Merge pull request #43 from hanlinai/fix/ |
| 2026-08-24T09:13 | sn65 | SCORING_COMMIT | sn65 commit touches scoring: update leader default url to mainnet vali |
| 2026-08-24T07:17 | sn97 | SCORING_COMMIT | sn97 commit touches scoring: feat: weighted score breakdown on eval de |
| 2026-08-24T06:03 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-08-24T04:14 | sn25 | RELEASE | sn25 released v2026.8.23-1027441210 |
| 2026-08-24T04:14 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-2742: stop transient checks from clea |
| 2026-08-24T03:13 | sn53 | SCORING_COMMIT | sn53 commit touches scoring: tee_miner: withdraw on a health stall tha |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

