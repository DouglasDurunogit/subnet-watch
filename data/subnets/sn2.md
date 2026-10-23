# sn2 - DaniLabs (β)

snapshot_utc: 2026-10-23T00:12:08Z  |  block: 9342561  |  row_status: ok

## Chain row

- miner_burn: **1.0**  <- 100% burn: miners earn NOTHING here
- registration cost: 0.0005 TAO (0.12847999999999998 USD), open=True
- tempo: 360.0  |  max_uids: 256  |  active: 5  |  free: 0
- subnet age: 917.8 days  |  registered at block 2734060
- weights_version: 11003  |  mechanisms: 1

## Income (miner side)

- **competitive_miner_usd_day: [UNKNOWN]** (uid [UNKNOWN]) <- the only figure quotable as achievable
- median_miner_usd_day: 2698.268329693228
- top_miner_usd_day: 2698.268329693228 (uid 14, owner=True, validator_permitted=True) <- NOT achievable if owner or permitted

## Incentive structure (display only - never scored)

- earners: 1  |  gini: 0.0  |  top1_share: 1.0  |  top10_share: 1.0
- owner_incentive_share: 1.0 (independent check on miner_burn; disagreement 0.0)

## Repository

- on-chain URL: `https://github.com/DaniLabsAI/subnet`
- resolved URL: `https://github.com/DaniLabsAI/subnet`
- status: **ok** 
- README: 2054 bytes, sha 555163fcd4a58ced
- latest release: (none) 
- last commit: 2026-10-22T01:50:24Z
- scoring-related commit: Add finalized-chain observer for validator pilot 2026-10-22T01:50:24Z

## Resources

- min_compute.yml present: False  |  unmodified template: False
- required: unknown (~[UNKNOWN] GB VRAM)  |  basis: **no evidence**
- cheapest satisfying machine: rtx4090 at 8.2192 USD/day  <- ASSUMED default box; no hardware evidence was found, so the margin below is indicative only
- net margin: [UNKNOWN] USD/day  |  payback on registration: [UNKNOWN] days

## Score

- gate: **BLOCKED:burn** - miner_burn=1.000 - 100.0% of miner emission is withheld by owner-controlled hotkeys, so miners earn nothing here
- score: [UNKNOWN] (rank -), confidence [UNKNOWN] 
- components: income [UNKNOWN] / freshness [UNKNOWN] / resource [UNKNOWN] / registration [UNKNOWN]
- freshness basis: -

## On-chain description

> Distributed Accelerated Neural intelligence

## README excerpt (evidence for the brief)

```markdown
# DaniLabs Subnet

DaniLabs is a Bittensor subnet for distributed AI inference. This repository is
home to its validator software: the code that evaluates miner performance,
calculates scores, and submits weights to Bittensor.

The validator's role is to determine how miners are rewarded for the inference
work they contribute. This repo is intended for validator operators and
contributors developing the subnet's evaluation and incentive rules.

## Validator responsibilities

The validator is being developed to:

- Track subnet state and associate registered miners with their on-chain
  identities.
- Check the source, format, and freshness of performance reports, rejecting
  invalid or duplicate submissions.
- Evaluate inference performance using latency, token throughput, completed
  requests, and availability.
- Calculate miner scores using consistent, documented evaluation rules.
- Convert eligible miner scores into weights and submit them to Bittensor.

## Scoring

The goal is to reward useful, fast, reliable inference. Scoring needs to account
for both performance and successful completion, so generation speed alone does
not determine a miner's score.

The scoring formula, eligibility requirements, and measurement definitions are
still being developed. They will be documented and tested here before live
weight submission is enabled. Validator reports should contain operational
measurements, without customer prompts or generated responses.

## Current status

The first executable pilot is a **read-only chain observer**. It checks finalized
registered subnet identities, validator state and burn evidence. It does not open wallets,
submit weights, maintain the existing burn process, or calculate trusted miner
scores. Authenticated evaluation and live weight submission are still pending.

The CLI provides `status`, `watch` and a `shadow` command that explicitly reports
scoring as pending. See the [operator guide](docs/operator-pilot.md) for setup,
host sizing, configuration pins and the boundaries of burn verification.

```
