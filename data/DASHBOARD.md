# Subnet watch — dashboard

_snapshot 2026-08-24T12:15:59Z · block 8914749 · run_status **ok**_

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
| New events this window | 4 | see ALARMS.md |

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
| 1 | sn76 Phylax | 77.4 | 82.35 | 175 | cpu-small | 13 | 23% |
| 2 | sn3 Teutonic | 75.6 | 3,906 | 3,906 = | rtx4090* | 5 | 20% |
| 3 | sn62 Ridges | 72.4 | 1,514 | 3,095 | rtx4090* | 6 | 39% |
| 4 | sn23 Trishool | 72.4 | 585 | 585 = | cpu-small | 2 | 80% |
| 5 | sn102 ConnitoAI | 72.3 | 1,476 | 1,900 | rtx4090* | 6 | 27% |
| 6 | sn15 ORO | 71.6 | 26.48 | 25,469 | cpu-small | 80 | 93% |
| 7 | sn67 Harnyx | 71.6 | 19.01 | 164 | cpu-small | 175 | 4% |
| 8 | sn91 cascade | 69.9 | 712 | 2,874 | rtx4090* | 5 | 52% |
| 9 | sn1 Apex | 68.7 | 501 | 1,333 | rtx4090* | 5 | 52% |
| 10 | sn26 Perturb | 68.2 | 21.50 | 408 | rtx3060 | 10 | 70% |
| 11 | sn96 Verathos | 67.6 | 18.87 | 183 | rtx4090 | 93 | 40% |
| 12 | sn124 Swarm | 66.9 | 304 | 2,643 | rtx4090* | 21 | 30% |
| 13 | sn38 ChronoLLM | 66.6 | 119 | 1,621 | cpu-small | 10 | 52% |
| 14 | sn107 Minos | 65.2 | 148 | 43,384 | cpu-small | 20 | 90% |
| 15 | sn98 NeverPlayAlone | 64.7 | 2,025 | 2,025 = | cpu-small | 1 | 100% |
| 16 | sn85 Vidaio | 64.6 | 147 | 431 | rtx4090* | 13 | 42% |
| 17 | sn60 Bitsec.ai | 64.2 | 1,741 | 1,741 = | cpu-small | 2 | 50% |
| 18 | sn81 Reliquary | 63.8 | 114 | 375 | rtx4090* | 38 | 8% |
| 19 | sn108 Prometheon | 63.7 | 115 | 127 | rtx4090* | 9 | 66% |
| 20 | sn51 lium.io | 62.1 | 79.96 | 2,334 | rtx4090* | 50 | 72% |

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
| dominated (60–90%) | 19 |
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
| 2026-08-24T01:55 | sn53 | SCORING_COMMIT | sn53 commit touches scoring: tee_miner: report live KV-cache pressure  |
| 2026-08-23T23:01 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: test: verify pinned model runtime in CI |
| 2026-08-23T19:44 | sn102 | RELEASE | sn102 released v0.5.1 — release the finished round on swap |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

