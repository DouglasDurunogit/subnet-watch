# sn4 - Targon (δ)

snapshot_utc: 2026-11-27T18:20:43Z  |  block: 9599964  |  row_status: ok

## Chain row

- miner_burn: **1.025339588522911e-05**
- registration cost: 0.0005 TAO (0.09240999999999999 USD), open=True
- tempo: 360.0  |  max_uids: 256  |  active: 16  |  free: 0
- subnet age: 1137.3 days  |  registered at block 1411451
- weights_version: 70001  |  mechanisms: 1

## Income (miner side)

- **competitive_miner_usd_day: 18572.032404045218** (uid 156) <- the only figure quotable as achievable
- median_miner_usd_day: 7388.247388944355
- top_miner_usd_day: 18572.032404045218 (uid 156, owner=False, validator_permitted=False) <- NOT achievable if owner or permitted

## Incentive structure (display only - never scored)

- earners: 3  |  gini: 0.40767247035844556  |  top1_share: 0.6720736117681169  |  top10_share: 1.0
- owner_incentive_share: 0.0 (independent check on miner_burn; disagreement 0.0)

## Repository

- on-chain URL: `https://github.com/manifold-inc/targon`
- resolved URL: `https://github.com/manifold-inc/targon`
- status: **error** - HTTP 504
- README: 0 bytes, sha (none)
- latest release: (none) 
- last commit: (unknown)
- scoring-related commit: (none) 

## Resources

- min_compute.yml present: False  |  unmodified template: False
- required: unknown (~[UNKNOWN] GB VRAM)  |  basis: **no evidence**
- cheapest satisfying machine: rtx4090 at 8.2192 USD/day  <- ASSUMED default box; no hardware evidence was found, so the margin below is indicative only
- net margin: 12971.9207 USD/day  |  payback on registration: 0.0 days

## Score

- gate: **OK** 
- score: 41.5 (rank 21), confidence 0.6 - hardware requirement unknown; no README readable; repo error; income rests on 2 competitive miners (n<=2: not a distribution)
- components: income 37.41 / freshness 10.5 / resource 11.25 / registration 10.0
- freshness basis: RELEASE 71d ago

## On-chain description

> Incentivized Compute Marketplace powered by the Targon Virtual Machine (TVM).
