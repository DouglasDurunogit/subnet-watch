# Subnet watch — dashboard

_snapshot 2026-09-09T11:40:47Z · block 9029710 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 59 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 92 | `miner_burn` < 0.99 |
| Ranked | 93 | passed every gate |
| **Positive margin** | **59** | income beats machine cost |
| New events this window | 8 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 60 | `████████████████████████████` |
| 0–0.2 | 9 | `████` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 3 | `█` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 5 | `██` |
| ≥0.99 dead | 36 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn114 SOMA | 87.2 | 981 | 7,853 | cpu-small | 4 | 80% |
| 2 | sn107 Minos | 83.9 | 450 | 36,482 | cpu-small | 20 | 79% |
| 3 | sn92 MicroTensor | 79.3 | 134 | 404 | cpu-small | 9 | 50% |
| 4 | sn3 Teutonic | 76.2 | 4,640 | 4,640 = | rtx4090* | 5 | 20% |
| 5 | sn67 Harnyx | 71.8 | 19.78 | 560 | cpu-small | 125 | 15% |
| 6 | sn15 ORO | 71.7 | 30.28 | 27,576 | cpu-small | 76 | 92% |
| 7 | sn91 cascade | 70.4 | 826 | 3,328 | rtx4090* | 5 | 52% |
| 8 | sn96 Verathos | 70.1 | 34.78 | 184 | rtx4090 | 83 | 30% |
| 9 | sn14 Cacheon | 69.8 | 699 | 1,294 | rtx4090* | 12 | 18% |
| 10 | sn62 Ridges | 68.1 | 423 | 1,292 | rtx4090* | 13 | 26% |
| 11 | sn56 Gradients | 67.9 | 390 | 6,048 | rtx4090* | 8 | 47% |
| 12 | sn80 OpenRoboto | 67.8 | 381 | 1,354 | rtx4090* | 5 | 43% |
| 13 | sn61 RedTeam | 67.3 | 331 | 574 | rtx4090* | 37 | 5% |
| 14 | sn38 ChronoLLM | 66.1 | 104 | 1,416 | cpu-small | 10 | 52% |
| 15 | sn111 Claims | 65.9 | 234 | 3,616 | rtx4090* | 5 | 80% |
| 16 | sn121 sundae_bar | 63.2 | 1,316 | 1,316 = | cpu-small | 2 | 60% |
| 17 | sn28 SayGM | 60.9 | 52.54 | 4,004 | rtx4090* | 47 | 35% |
| 18 | sn41 Almanac | 60.8 | 43.31 | 95.29 | cpu-small | 86 | 3% |
| 19 | sn23 Trishool | 60.7 | 627 | 627 = | cpu-small | 2 | 80% |
| 20 | sn102 ConnitoAI | 58.6 | 25.42 | 1,966 | rtx4090* | 8 | 33% |

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
| concentrated (30–60%) | 21 |
| dominated (60–90%) | 20 |
| captured (>90%) | 21 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 99 |
| min_compute.yml (curated) | 11 |
| code-submission (validator runs it) | 10 |
| README keywords (GUESS) | 7 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-09-09T11:41 | sn61 | RELEASE | sn61 released 4.10.3 |
| 2026-09-09T11:41 | sn66 | SCORING_COMMIT | sn66 commit touches scoring: Merge pull request #80 from conjectures-i |
| 2026-09-09T11:41 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Preserve terminal company scores across j |
| 2026-09-09T11:41 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Add legacy validator transition hold |
| 2026-09-09T11:41 | sn89 | SCORING_COMMIT | sn89 commit touches scoring: scoring: points-path earning gate is the  |
| 2026-09-09T11:41 | sn97 | SCORING_COMMIT | sn97 commit touches scoring: fix: show all task results for benchmark  |
| 2026-09-09T11:41 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: docs: clarify Ubuntu validator env setup |
| 2026-09-09T11:41 | sn114 | SCORING_COMMIT | sn114 commit touches scoring: Cap automatic run restarts per miner tas |
| 2026-09-09T06:19 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-2962: delete the dead hashcat scoring |
| 2026-09-09T06:19 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-09-09T06:19 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Stop Arena scoring after exhausted judge  |
| 2026-09-09T06:19 | sn100 | SCORING_COMMIT | sn100 commit touches scoring: feat(proof): name the topic_id / custom_ |
| 2026-09-09T06:19 | sn111 | SCORING_COMMIT | sn111 commit touches scoring: fix(validator): normalize provider routi |
| 2026-09-09T06:19 | sn120 | SCORING_COMMIT | sn120 commit touches scoring: AGENTS.md: first wvk-13 verdicts verifie |
| 2026-09-09T01:13 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: build: refresh protected scoring source m |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

