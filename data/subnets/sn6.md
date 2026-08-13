# sn6 - Numinous (ζ)

snapshot_utc: 2026-08-13T04:31:55Z  |  block: 8833230  |  row_status: ok

## Chain row

- miner_burn: **0.0**
- registration cost: 0.220649559 TAO (44.015174029319994 USD), open=True
- tempo: 360.0  |  max_uids: 256  |  active: 34  |  free: 0
- subnet age: 779.6 days  |  registered at block 3219949
- weights_version: 2018  |  mechanisms: 1

## Income (miner side)

- **competitive_miner_usd_day: 522.0992233063323** (uid 197) <- the only figure quotable as achievable
- median_miner_usd_day: 15.0256259711816
- top_miner_usd_day: 522.0992233063323 (uid 197, owner=False, validator_permitted=False) <- NOT achievable if owner or permitted

## Incentive structure (display only - never scored)

- earners: 19  |  gini: 0.7038845167125303  |  top1_share: 0.289533925464701  |  top10_share: 0.9731709550407471
- owner_incentive_share: 0.0 (independent check on miner_burn; disagreement 0.0)

## Repository

- on-chain URL: `https://github.com/numinouslabs/numinous`
- resolved URL: `https://github.com/numinouslabs/numinous`
- status: **error** - ConnectionError
- README: 0 bytes, sha (none)
- latest release: (none) 
- last commit: (unknown)
- scoring-related commit: (none) 

## Resources

- min_compute.yml present: False  |  unmodified template: False
- required: unknown (~[UNKNOWN] GB VRAM)  |  basis: **no evidence**
- cheapest satisfying machine: rtx4090 at 8.2192 USD/day  <- ASSUMED default box; no hardware evidence was found, so the margin below is indicative only
- net margin: 2.6235 USD/day  |  payback on registration: 16.78 days

## Score

- gate: **OK** 
- score: 25.0 (rank 64), confidence 0.6 - hardware requirement unknown; no README readable; repo error
- components: income 5.09 / freshness 21.0 / resource 11.25 / registration 4.41
- freshness basis: README_TASK_DIFF 14d ago

## On-chain description

> Numinous is a forecasting protocol whose goal is to aggregate agents into superhuman LLM forecasters.
