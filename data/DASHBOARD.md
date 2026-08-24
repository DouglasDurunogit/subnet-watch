# Subnet watch — dashboard

_snapshot 2026-08-24T11:39:23Z · block 8914566 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 51 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 88 | `miner_burn` < 0.99 |
| Ranked | 88 | passed every gate |
| **Positive margin** | **51** | income beats machine cost |
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
| 0.6–0.8 | 7 | `███` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 40 | `███████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 77.2 | 79.15 | 88.60 | cpu-small | 13 | 20% |
| 2 | sn3 Teutonic | 75.6 | 3,921 | 3,921 = | rtx4090* | 5 | 20% |
| 3 | sn62 Ridges | 72.4 | 1,520 | 3,107 | rtx4090* | 6 | 39% |
| 4 | sn23 Trishool | 72.4 | 588 | 588 = | cpu-small | 2 | 80% |
| 5 | sn102 ConnitoAI | 71.5 | 1,167 | 2,340 | rtx4090* | 6 | 33% |
| 6 | sn67 Harnyx | 71.5 | 19.10 | 164 | cpu-small | 174 | 5% |
| 7 | sn15 ORO | 71.4 | 26.39 | 25,385 | cpu-small | 80 | 93% |
| 8 | sn91 cascade | 69.9 | 715 | 2,886 | rtx4090* | 5 | 52% |
| 9 | sn1 Apex | 68.7 | 505 | 1,342 | rtx4090* | 5 | 52% |
| 10 | sn26 Perturb | 68.2 | 21.59 | 410 | rtx3060 | 10 | 70% |
| 11 | sn96 Verathos | 67.9 | 19.95 | 186 | rtx4090 | 95 | 40% |
| 12 | sn124 Swarm | 66.9 | 306 | 2,657 | rtx4090* | 21 | 30% |
| 13 | sn38 ChronoLLM | 66.6 | 120 | 1,633 | cpu-small | 10 | 52% |
| 14 | sn107 Minos | 65.3 | 151 | 43,785 | cpu-small | 20 | 90% |
| 15 | sn98 NeverPlayAlone | 64.7 | 2,025 | 2,025 = | cpu-small | 1 | 100% |
| 16 | sn85 Vidaio | 64.4 | 139 | 433 | rtx4090* | 13 | 42% |
| 17 | sn60 Bitsec.ai | 64.2 | 1,761 | 1,761 = | cpu-small | 2 | 50% |
| 18 | sn108 Prometheon | 63.7 | 114 | 126 | rtx4090* | 9 | 66% |
| 19 | sn81 Reliquary | 63.7 | 111 | 411 | rtx4090* | 38 | 9% |
| 20 | sn51 lium.io | 61.5 | 67.83 | 2,254 | rtx4090* | 50 | 72% |

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
| 2026-08-24T01:55 | sn53 | SCORING_COMMIT | sn53 commit touches scoring: tee_miner: report live KV-cache pressure  |
| 2026-08-23T23:01 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: test: verify pinned model runtime in CI |
| 2026-08-23T19:44 | sn102 | RELEASE | sn102 released v0.5.1 — release the finished round on swap |
| 2026-08-23T19:44 | sn102 | SCORING_COMMIT | sn102 commit touches scoring: 🩹 fix(validator): release the finished r |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

