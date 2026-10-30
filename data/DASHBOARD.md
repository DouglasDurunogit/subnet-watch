# Subnet watch — dashboard

_snapshot 2026-10-30T09:54:41Z · block 9395874 · run_status **ok**_

> Numbers here are quotable. Income is always `competitive_miner_usd_day` —
> the best miner that is neither the owner nor validator-permitted.

## The one number

# 60 of 128

subnets are worth looking at: not 100% burned, registration open, and the
competitive miner out-earns the cheapest machine that meets the requirement.

| | count | meaning |
|---|---:|---|
| Total subnets | 128 | everything on chain |
| Pays miners at all | 99 | `miner_burn` < 0.99 |
| Ranked | 99 | passed every gate |
| **Positive margin** | **60** | income beats machine cost |
| New events this window | 6 | see ALARMS.md |

![viability funnel](charts/funnel.svg)

## Where miner emission goes

The distribution is bimodal — subnets either burn nothing or burn everything.
There is very little middle ground, which is why burn is a gate and not a score.

| miner_burn | subnets | |
|---|---:|---|
| 0 (none) | 68 | `████████████████████████████` |
| 0–0.2 | 7 | `███` |
| 0.2–0.4 | 5 | `██` |
| 0.4–0.6 | 6 | `██` |
| 0.6–0.8 | 9 | `████` |
| 0.8–0.99 | 4 | `██` |
| ≥0.99 dead | 29 | `████████████` |

![burn distribution](charts/burn.svg)

## Top 20

| # | subnet | score | net $/day (median) | ceiling $/day | machine | earners | top-1 share |
|---:|---|---:|---:|---:|---|---:|---:|
| 1 | sn120 Affine | 75.3 | 3,563 | 3,563 = | rtx4090* | 8 | 12% |
| 2 | sn3 Teutonic | 73.2 | 1,927 | 1,927 = | rtx4090* | 7 | 25% |
| 3 | sn97 Ingot | 72.7 | 1,658 | 1,658 = | rtx4090* | 5 | 20% |
| 4 | sn103 Terza Inference | 69.5 | 645 | 1,700 | rtx4090* | 5 | 40% |
| 5 | sn56 Gradients | 69.4 | 618 | 5,084 | rtx4090* | 6 | 51% |
| 6 | sn60 Bitsec.ai | 69.3 | 233 | 233 = | cpu-small | 3 | 50% |
| 7 | sn91 cascade | 68.8 | 524 | 1,412 | rtx4090* | 5 | 52% |
| 8 | sn46 Instant | 68.1 | 162 | 185 | cpu-small | 8 | 41% |
| 9 | sn53 engy | 67.9 | 397 | 2,144 | rtx4090 | 29 | 26% |
| 10 | sn1 Apex | 67.5 | 347 | 774 | rtx4090* | 5 | 62% |
| 11 | sn67 Harnyx | 67.4 | 6.74 | 356 | cpu-small | 125 | 18% |
| 12 | sn15 ORO | 66.8 | 7.12 | 12,438 | cpu-small | 68 | 96% |
| 13 | sn107 Minos | 65.7 | 166 | 14,117 | cpu-small | 20 | 80% |
| 14 | sn125 Refinery | 64.6 | 149 | 804 | rtx4090* | 4 | 50% |
| 15 | sn121 sundae_bar | 62.1 | 940 | 940 = | cpu-small | 2 | 60% |
| 16 | sn62 Ridges | 62.1 | 69.86 | 691 | rtx4090* | 44 | 15% |
| 17 | sn124 Swarm | 61.6 | 69.12 | 214 | rtx4090* | 11 | 85% |
| 18 | sn66 conjectures | 58.7 | 24.60 | 156 | rtx4090* | 7 | 80% |
| 19 | sn4 Targon | 58.4 | 11,531 | 25,422 | rtx4090* | 4 | 64% |
| 20 | sn28 SayGM | 57.9 | 22.68 | 921 | rtx4090* | 155 | 26% |

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
| concentrated (30–60%) | 24 |
| dominated (60–90%) | 25 |
| captured (>90%) | 23 |

## Hardware evidence quality

Most subnets do not state a requirement anywhere machine-readable, so their
margin assumes a default box. Treat those as indicative.

| basis | subnets |
|---|---:|
| no evidence | 100 |
| README keywords (GUESS) | 10 |
| min_compute.yml (curated) | 9 |
| code-submission (validator runs it) | 8 |
| README stated VRAM (explicit) | 1 |

## Recent changes (last 7 days)

| when | subnet | class | what |
|---|---|---|---|
| 2026-10-30T09:55 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Expose validator preparation stages throu |
| 2026-10-30T09:55 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-5327 - [P1] Validator: a killed fille |
| 2026-10-30T09:55 | sn62 | RELEASE | sn62 released v0.3.15 |
| 2026-10-30T09:55 | sn66 | RELEASE | sn66 released deployed/dev: Merge pull request #174 from conjectures-i |
| 2026-10-30T09:55 | sn67 | SCORING_COMMIT | sn67 commit touches scoring: chore(validator): bump repo-owned validat |
| 2026-10-30T09:55 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Verify accepted Greenhouse API judgments  |
| 2026-10-30T03:00 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Merge leadertop/head-summary-upload: the  |
| 2026-10-30T03:00 | sn71 | SCORING_COMMIT | sn71 commit touches scoring: Ignore validator runtime state at checkou |
| 2026-10-30T03:00 | sn89 | SCORING_COMMIT | sn89 commit touches scoring: Agent competition scoreboard builder |
| 2026-10-30T03:00 | sn124 | SCORING_COMMIT | sn124 commit touches scoring: Merge pull request #239 from swarm-subne |
| 2026-10-29T23:29 | sn1 | RELEASE | sn1 released v4.5.4 |
| 2026-10-29T23:29 | sn25 | SCORING_COMMIT | sn25 commit touches scoring: Merge leadertop/head-summary-spec: valida |
| 2026-10-29T23:29 | sn51 | SCORING_COMMIT | sn51 commit touches scoring: DAH-5177 connector lead lock TTL 15 s ->  |
| 2026-10-29T23:29 | sn62 | SCORING_COMMIT | sn62 commit touches scoring: Merge pull request #528 from ridgesai/fea |
| 2026-10-29T23:29 | sn94 | SCORING_COMMIT | sn94 commit touches scoring: Validate claims-room upload paths and req |

---

_Regenerated every sweep. Charts are SVG and follow the same numbers._

