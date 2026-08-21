# Subnet watch — dashboard

_snapshot 2026-08-21T05:46:04Z · block 8891199 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 53 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 91 | `miner_burn` < 0.99 |
| Ranked | 91 | passed every gate |
| **Positive margin** | **53** | income beats machine cost |
| New events this window | 2 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 61 | `████████████████████████████` |
| 0–0.2 | 5 | `██` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 5 | `██` |
| 0.6–0.8 | 8 | `████` |
| 0.8–0.99 | 7 | `███` |
| ≥0.99 dead | 37 | `█████████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn76 Phylax | 77.1 | 76.88 | 129 | cpu-small | 13 | 20% |
| 2 | sn23 Trishool | 72.2 | 551 | 551 = | cpu-small | 2 | 80% |
| 3 | sn67 Harnyx | 70.8 | 15.77 | 890 | cpu-small | 142 | 23% |
| 4 | sn15 ORO | 69.9 | 19.21 | 19,809 | cpu-small | 77 | 93% |
| 5 | sn56 Gradients | 69.8 | 691 | 1,059 | rtx4090* | 5 | 72% |
| 6 | sn91 cascade | 69.4 | 618 | 2,496 | rtx4090* | 5 | 52% |
| 7 | sn1 Apex | 68.3 | 441 | 1,230 | rtx4090* | 5 | 53% |
| 8 | sn38 ChronoLLM | 67.7 | 156 | 3,302 | cpu-small | 10 | 52% |
| 9 | sn96 Verathos | 67.6 | 18.39 | 322 | rtx4090 | 92 | 40% |
| 10 | sn26 Perturb | 67.4 | 17.68 | 254 | rtx3060 | 10 | 70% |
| 11 | sn107 Minos | 65.3 | 149 | 42,157 | cpu-small | 20 | 90% |
| 12 | sn85 Vidaio | 64.9 | 163 | 1,475 | rtx4090* | 13 | 42% |
| 13 | sn108 Prometheon | 64 | 125 | 184 | rtx4090* | 7 | 66% |
| 14 | sn55 NIOME | 61.9 | 65.15 | 545 | rtx4090* | 11 | 29% |
| 15 | sn51 lium.io | 61.7 | 69.56 | 1,293 | rtx4090* | 44 | 83% |
| 16 | sn60 Bitsec.ai | 61.4 | 776 | 1,086 | cpu-small | 3 | 50% |
| 17 | sn81 Reliquary | 61 | 50.36 | 197 | rtx4090* | 53 | 5% |
| 18 | sn28 gm | 60.1 | 39.77 | 1,799 | rtx4090* | 53 | 16% |
| 19 | sn53 engy | 60.1 | 37.86 | 250 | rtx4090 | 144 | 63% |
| 20 | sn102 ConnitoAI | 57.6 | 633 | 1,546 | rtx4090* | 7 | 26% |

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
| concentrated (30–60%) | 19 |
| dominated (60–90%) | 19 |
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
| 2026-08-21T05:46 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-08-21T05:04 | sn53 | SCORING_COMMIT | sn53 commit touches scoring: tee_miner: absorb the reference miner's n |
| 2026-08-21T01:54 | sn34 | RELEASE | sn34 released Release 4.9.8 |
| 2026-08-20T23:08 | sn34 | SCORING_COMMIT | sn34 commit touches scoring: fix: restore validator config parsing (#4 |
| 2026-08-20T23:08 | sn91 | SCORING_COMMIT | sn91 commit touches scoring: Merge pull request #203 from TensorLink-A |
| 2026-08-20T22:40 | sn92 | SCORING_COMMIT | sn92 commit touches scoring: Drop the task generator in favour of uplo |
| 2026-08-20T21:53 | sn34 | SCORING_COMMIT | sn34 commit touches scoring: tune: double generator challenge frequenc |
| 2026-08-20T21:13 | sn13 | RELEASE | sn13 released Release v1.18.71 |
| 2026-08-20T21:13 | sn13 | SCORING_COMMIT | sn13 commit touches scoring: fix(s3): stop charging miners for passing |
| 2026-08-20T21:13 | sn25 | RELEASE | sn25 released v2026.8.20-1024590520 |
| 2026-08-20T21:13 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Fix miner Windows arm64 cross-build |
| 2026-08-20T20:41 | sn25 | RELEASE | sn25 released v2026.8.20-1024555910 |
| 2026-08-20T19:55 | sn18 | RELEASE | sn18 released Release 2.1.2 |
| 2026-08-20T18:15 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Repair release verifier test isolation |
| 2026-08-20T18:15 | sn89 | SCORING_COMMIT | sn89 commit touches scoring: HF: apply owner-hosted miner integrity ve |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

