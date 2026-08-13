# sn2 - DSperse (β)

snapshot_utc: 2026-08-13T04:31:55Z  |  block: 8833230  |  row_status: ok

## Chain row

- miner_burn: **0.8262028191238642**
- registration cost: 0.0005 TAO (0.09974 USD), open=True
- tempo: 360.0  |  max_uids: 256  |  active: 26  |  free: 0
- subnet age: 847.1 days  |  registered at block 2734060
- weights_version: 11003  |  mechanisms: 1

## Income (miner side)

- **competitive_miner_usd_day: 106.07243891122084** (uid 145) <- the only figure quotable as achievable
- median_miner_usd_day: 0.8403626322191793
- top_miner_usd_day: 2022.285987622554 (uid 14, owner=True, validator_permitted=True) <- NOT achievable if owner or permitted

## Incentive structure (display only - never scored)

- earners: 16  |  gini: 0.8715844232148582  |  top1_share: 0.8263006089093046  |  top10_share: 0.9997558258427823
- owner_incentive_share: 0.8263006089093045 (independent check on miner_burn; disagreement 0.0001)

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
- net margin: -7.3975 USD/day  |  payback on registration: [UNKNOWN] days

## Score

- gate: **OK** 
- score: 27.8 (rank 55), confidence 0.6 - hardware requirement unknown; no README readable; repo error
- components: income 0.0 / freshness 35.0 / resource 11.25 / registration 0.0
- freshness basis: RELEASE 2.3d ago

## On-chain description

> Verifiable and distributed inference on Bittensor
