# sn2 - DaniLabs (β)

snapshot_utc: 2026-10-29T19:16:38Z  |  block: 9391484  |  row_status: ok

## Chain row

- miner_burn: **1.0**  <- 100% burn: miners earn NOTHING here
- registration cost: 0.000645766 TAO (0.16264262476 USD), open=True
- tempo: 360.0  |  max_uids: 256  |  active: 6  |  free: 0
- subnet age: 924.6 days  |  registered at block 2734060
- weights_version: 11003  |  mechanisms: 1

## Income (miner side)

- **competitive_miner_usd_day: [UNKNOWN]** (uid [UNKNOWN]) <- the only figure quotable as achievable
- median_miner_usd_day: 2603.5628956947976
- top_miner_usd_day: 2603.5628956947976 (uid 14, owner=True, validator_permitted=True) <- NOT achievable if owner or permitted

## Incentive structure (display only - never scored)

- earners: 1  |  gini: 0.0  |  top1_share: 1.0  |  top10_share: 1.0
- owner_incentive_share: 1.0 (independent check on miner_burn; disagreement 0.0)

## Repository

- on-chain URL: `https://github.com/DaniLabsAI/subnet`
- resolved URL: `https://github.com/DaniLabsAI/subnet`
- status: **ok** 
- README: 2796 bytes, sha dd981426f3c98a20
- latest release: (none) 
- last commit: 2026-10-27T07:35:19Z
- scoring-related commit: Gate unverified miner scores and refresh narrow validator dependencies 2026-10-27T07:31:43Z

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

Validators fetch signed aggregate reports over HTTPS, verify registered miner
identities against finalized chain state, and calculate candidate weights.
The current policy weights TPS at 50%, TTFT at 35%, completion reliability at
10%, and gateway-to-miner RTT at 5%. Reports exclude customer prompts and
responses. See [report setup and scoring](docs/validator-reports.md).

Performance reports are not execution proofs. Gateway timing is observed by the
gateway, while token usage is still miner-reported. Candidate scores remain
explicitly ineligible for miner rewards pending independent token and correctness
verification. Current live signing remains constrained to **100% burn**.

## Current status

The validator includes a finalized-chain observer and a **100% burn mode**.
It runs an isolated signer, a PM2 worker, and a staged worker
updater with health checks and rollback. It targets the subnet owner's registered
UID and verifies the resulting weight row and miner-burn settlement separately.

The signer supports encrypted hotkey custody, an explicit operator policy, and
optional automatic recovery through OCI Secret Management.
The production validator runs on Finney with 100% miner-incentive burn. Miner
scores and candidate weights are logged without changing the burn signer.
Changes are tested on localnet before deployment.

See the [observer guide](docs/operator-pilot.md) for chain monitoring and the
[localnet guide](docs/localnet-validator.md) for burn testing, PM2 controls and
updates. The [signer guide](docs/production-signer.md) covers key custody and
production activation requirements.

```
