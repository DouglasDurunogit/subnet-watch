# sn3 - Teutonic (γ)

snapshot_utc: 2026-08-22T19:11:11Z  |  block: 8902425  |  row_status: ok

## Chain row

- miner_burn: **0.0**
- registration cost: 0.0005 TAO (0.11239 USD), open=True
- tempo: 360.0  |  max_uids: 256  |  active: 8  |  free: 0
- subnet age: 657.9 days  |  registered at block 4165565
- weights_version: 2000  |  mechanisms: 1

## Income (miner side)

- **competitive_miner_usd_day: 3647.0408926640825** (uid 110) <- the only figure quotable as achievable
- median_miner_usd_day: 3647.0408926640825
- top_miner_usd_day: 3647.0408926640825 (uid 110, owner=False, validator_permitted=False) <- NOT achievable if owner or permitted

## Incentive structure (display only - never scored)

- earners: 5  |  gini: 0.0  |  top1_share: 0.2  |  top10_share: 1.0
- owner_incentive_share: 0.0 (independent check on miner_burn; disagreement 0.0)

## Repository

- on-chain URL: `https://github.com/unarbos/teutonic`
- resolved URL: `https://github.com/unarbos/teutonic`
- status: **ok** 
- README: 441 bytes, sha d7d29fdb32fafaa4
- latest release: (none) 
- last commit: 2026-08-13T14:45:04Z
- scoring-related commit: Adjust default evaluation parameters 2026-08-13T14:45:04Z

## Resources

- min_compute.yml present: False  |  unmodified template: False
- required: unknown (~[UNKNOWN] GB VRAM)  |  basis: **no evidence**
- cheapest satisfying machine: rtx4090 at 8.2192 USD/day  <- ASSUMED default box; no hardware evidence was found, so the margin below is indicative only
- net margin: 3638.8217 USD/day  |  payback on registration: 0.0 days

## Score

- gate: **OK** 
- score: 45.6 (rank 37), confidence 0.85 - hardware requirement unknown
- components: income 32.39 / freshness 0.0 / resource 11.25 / registration 10.0
- freshness basis: no challenge change on record

## On-chain description

> Coordinated Learning

## README excerpt (evidence for the brief)

```markdown
# [Teutonic](https://teutonic.ai/)

[Teutonic](https://teutonic.ai/) is a king-of-the-hill pretraining system for Bittensor subnet 3.

Miners submit immutable model checkpoints. The validator verifies each
submission and sends the challenger and current king to a remote GPU evaluator
for paired cross-entropy scoring. A successful challenger becomes the new king,
and the validator updates subnet weights and publishes the resulting state.

```
