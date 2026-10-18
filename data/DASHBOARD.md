# Subnet watch — dashboard

_snapshot 2026-10-18T00:58:36Z · block 9306875 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 54 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 99 | `miner_burn` < 0.99 |
| Ranked | 99 | passed every gate |
| **Positive margin** | **54** | income beats machine cost |
| New events this window | 2 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 67 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 6 | `███` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 29 | `████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn41 Almanac | 76.1 | 60.48 | 101 | cpu-small | 120 | 6% |
| 2 | sn53 engy | 69.3 | 602 | 2,502 | rtx4090 | 24 | 16% |
| 3 | sn91 cascade | 68.9 | 208 | 835 | cpu-small | 5 | 52% |
| 4 | sn1 Apex | 68.6 | 489 | 920 | rtx4090* | 5 | 55% |
| 5 | sn82 Noah | 68.1 | 640 | 640 = | rtx4090* | 64 | 2% |
| 6 | sn67 Harnyx | 68.1 | 7.37 | 153 | cpu-small | 191 | 6% |
| 7 | sn58 Attune | 67.8 | 393 | 634 | rtx4090* | 5 | 71% |
| 8 | sn15 ORO | 67.7 | 8.22 | 16.39 | cpu-small | 65 | 97% |
| 9 | sn107 Minos | 67.5 | 254 | 21,551 | cpu-small | 20 | 80% |
| 10 | sn14 Cacheon | 65.1 | 171 | 602 | rtx4090* | 9 | 52% |
| 11 | sn66 conjectures | 63.8 | 116 | 240 | rtx4090* | 4 | 80% |
| 12 | sn120 Affine | 63.7 | 127 | 557 | rtx4090* | 196 | 2% |
| 13 | sn97 Ingot | 61.6 | 2,080 | 2,080 = | rtx4090* | 5 | 20% |
| 14 | sn28 SayGM | 61.4 | 58.42 | 2,909 | rtx4090* | 95 | 31% |
| 15 | sn61 RedTeam | 61.1 | 52.20 | 94.96 | rtx4090* | 135 | 1% |
| 16 | sn92 REAX | 61 | 92.20 | 3,397 | rtx4090 | 229 | 11% |
| 17 | sn80 OpenRoboto | 58.2 | 758 | 3,272 | rtx4090* | 10 | 35% |
| 18 | sn4 Targon | 57.9 | 9,870 | 29,102 | rtx4090* | 5 | 70% |
| 19 | sn23 Trishool | 57.5 | 242 | 242 = | cpu-small | 4 | 80% |
| 20 | sn102 ConnitoAI | 57.3 | 16.50 | 1,536 | rtx4090* | 8 | 35% |

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
| concentrated (30–60%) | 22 |
| dominated (60–90%) | 26 |
| captured (>90%) | 24 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 95 |
| README keywords (GUESS) | 13 |
| min_compute.yml (curated) | 10 |
| code-submission (validator runs it) | 9 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-10-18T00:59 | sn15 | RELEASE | sn15 released v2.5.6: Bound per-evaluation sandbox disk use |
| 2026-10-18T00:59 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: Bound per-evaluation sandbox disk use |
| 2026-10-17T23:04 | sn51 | RELEASE | sn51 released miner-v1.006 |
| 2026-10-17T23:04 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-4539 - Miner: a portal delete removes |
| 2026-10-17T23:04 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Recover historical reward coverage gaps f |
| 2026-10-17T20:51 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: Merge pull request #373 from TensorLink-A |
| 2026-10-17T18:25 | sn41 | SCORING_COMMIT | sn41 commit touches scoring: Merge pull request #59 from corvxai/vali_ |
| 2026-10-17T18:25 | sn78 | SCORING_COMMIT | sn78 commit touches scoring: Backport current reward coverage capture  |
| 2026-10-17T15:58 | sn7 | RELEASE | sn7 released release-20261017-152034: Bound event ingest per pass and  |
| 2026-10-17T15:58 | sn28 | RELEASE | sn28 released v0.5.2 |
| 2026-10-17T15:58 | sn28 | SCORING_COMMIT | sn28 commit touches scoring: chore(release): promote gm-miner 0.5.2 (# |
| 2026-10-17T15:58 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-4601 - [P0] Validator: fail a node wh |
| 2026-10-17T15:58 | sn92 | RELEASE | sn92 released v1.2.0-rc8 |
| 2026-10-17T12:28 | sn21 | SCORING_COMMIT | sn21 commit touches scoring: feat(scoring): absence charges stop once  |
| 2026-10-17T12:28 | sn25 | RELEASE | sn25 released v2026.10.17-1074370910 |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

