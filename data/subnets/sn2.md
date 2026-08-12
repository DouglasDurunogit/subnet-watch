# sn2 - DSperse (β)

snapshot_utc: 2026-08-12T16:39:35Z  |  block: 8829669  |  row_status: ok

## Chain row

- miner_burn: **0.8261781032197177**
- registration cost: 0.0005 TAO (0.09988 USD), open=True
- tempo: 360.0  |  max_uids: 256  |  active: 24  |  free: 0
- subnet age: 846.6 days  |  registered at block 2734060
- weights_version: 11003  |  mechanisms: 1

## Income (miner side)

- **competitive_miner_usd_day: 94.2671734747442** (uid 145) <- the only figure quotable as achievable
- median_miner_usd_day: 39.80586013128363
- top_miner_usd_day: 2029.3867091224947 (uid 14, owner=True, validator_permitted=True) <- NOT achievable if owner or permitted

## Incentive structure (display only - never scored)

- earners: 14  |  gini: 0.8318908383766155  |  top1_share: 0.8262574777194482  |  top10_share: 0.9957117568062508
- owner_incentive_share: 0.8262574777194481 (independent check on miner_burn; disagreement 0.0001)

## Repository

- on-chain URL: `https://github.com/inference-labs-inc/subnet-2`
- resolved URL: `https://github.com/inference-labs-inc/subnet-2`
- status: **error** - ConnectionError
- README: 0 bytes, sha (none)
- latest release: (none) 
- last commit: (unknown)
- scoring-related commit: (none) 

## Resources

- min_compute.yml present: False  |  unmodified template: False
- required: unknown (~[UNKNOWN] GB VRAM)  |  basis: **no evidence**
- cheapest satisfying machine: rtx4090 at 8.2192 USD/day  <- ASSUMED default box; no hardware evidence was found, so the margin below is indicative only
- net margin: 30.912 USD/day  |  payback on registration: 0.0 days

## Score

- gate: **OK** 
- score: 42.0 (rank 20), confidence 0.6 - hardware requirement unknown; no README readable; repo error
- components: income 13.68 / freshness 35.0 / resource 11.25 / registration 10.0
- freshness basis: RELEASE 1.8d ago

## On-chain description

> Verifiable and distributed inference on Bittensor
