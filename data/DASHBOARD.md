# Subnet watch — dashboard

_snapshot 2026-10-18T14:32:01Z · block 9310942 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 56 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 100 | `miner_burn` < 0.99 |
| Ranked | 100 | passed every gate |
| **Positive margin** | **56** | income beats machine cost |
| New events this window | 1 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 66 | `████████████████████████████` |
| 0–0.2 | 6 | `███` |
| 0.2–0.4 | 6 | `███` |
| 0.4–0.6 | 6 | `███` |
| 0.6–0.8 | 10 | `████` |
| 0.8–0.99 | 6 | `███` |
| ≥0.99 dead | 28 | `████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn41 Almanac | 75.7 | 54.39 | 96.09 | cpu-small | 116 | 7% |
| 2 | sn3 Teutonic | 74.5 | 2,840 | 7,588 | rtx4090* | 5 | 40% |
| 3 | sn91 cascade | 71.2 | 406 | 1,628 | cpu-small | 5 | 52% |
| 4 | sn67 Harnyx | 69.5 | 11.68 | 314 | cpu-small | 124 | 13% |
| 5 | sn53 engy | 69.2 | 591 | 2,457 | rtx4090 | 24 | 16% |
| 6 | sn102 ConnitoAI | 68.4 | 458 | 1,132 | rtx4090* | 7 | 27% |
| 7 | sn1 Apex | 68.3 | 441 | 827 | rtx4090* | 5 | 58% |
| 8 | sn82 Noah | 68.1 | 618 | 618 = | rtx4090* | 64 | 2% |
| 9 | sn58 Attune | 67.8 | 389 | 627 | rtx4090* | 5 | 71% |
| 10 | sn107 Minos | 67.4 | 245 | 20,771 | cpu-small | 20 | 80% |
| 11 | sn15 ORO | 66.6 | 6.57 | 15,781 | cpu-small | 60 | 97% |
| 12 | sn120 Affine | 64.9 | 188 | 361 | rtx4090* | 199 | 1% |
| 13 | sn14 Cacheon | 63.8 | 117 | 2,857 | rtx4090* | 10 | 43% |
| 14 | sn66 conjectures | 63.7 | 111 | 230 | rtx4090* | 4 | 80% |
| 15 | sn97 Ingot | 61.4 | 2,001 | 2,001 = | rtx4090* | 5 | 20% |
| 16 | sn61 RedTeam | 61.4 | 57.39 | 104 | rtx4090* | 123 | 1% |
| 17 | sn55 NIOME | 61.4 | 56.98 | 481 | rtx4090* | 11 | 30% |
| 18 | sn28 SayGM | 60.7 | 49.06 | 2,855 | rtx4090* | 108 | 28% |
| 19 | sn92 REAX | 60.5 | 77.43 | 2,828 | rtx4090 | 243 | 10% |
| 20 | sn81 Reliquary | 58.5 | 22.98 | 106 | rtx4090* | 11 | 90% |

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
| wide (<30%) | 29 |
| concentrated (30–60%) | 20 |
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
| 2026-10-18T14:32 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-10-18T10:56 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: docs: update stale pack digest and runtim |
| 2026-10-18T10:56 | sn55 | BURN_DROP | sn55 burn fell 1.000 -> 0.010 - miners can earn again |
| 2026-10-18T10:56 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: fix(arena): classify unavailable frozen s |
| 2026-10-18T10:56 | sn116 | SCORING_COMMIT | sn116 commit touches scoring: docs: lock bank-version reuse and reward |
| 2026-10-18T05:49 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: fix(validator): send sandbox_metadata whe |
| 2026-10-18T05:49 | sn25 | RELEASE | sn25 released v2026.10.17-1074871400 |
| 2026-10-18T05:49 | sn53 | SCORING_COMMIT | sn53 commit touches scoring: tee_miner: default to half the legs on th |
| 2026-10-18T05:49 | sn55 | SCORING_COMMIT | sn55 commit touches scoring: set weights using valid scores |
| 2026-10-18T05:49 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Prune superseded Deepline score billing h |
| 2026-10-18T05:49 | sn125 | README_TASK_DIFF | sn125 README task/scoring sections changed |
| 2026-10-18T00:59 | sn15 | RELEASE | sn15 released v2.5.6: Bound per-evaluation sandbox disk use |
| 2026-10-18T00:59 | sn15 | SCORING_COMMIT | sn15 commit touches scoring: Bound per-evaluation sandbox disk use |
| 2026-10-17T23:04 | sn51 | RELEASE | sn51 released miner-v1.006 |
| 2026-10-17T23:04 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-4539 - Miner: a portal delete removes |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

