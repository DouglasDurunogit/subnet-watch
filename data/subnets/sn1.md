# sn1 - Apex (α)

snapshot_utc: 2026-08-17T15:08:11Z  |  block: 8865211  |  row_status: ok

## Chain row

- miner_burn: **0.5181415139231831**
- registration cost: 0.000511673 TAO (0.10046699355000001 USD), open=True
- tempo: 99.0  |  max_uids: 256  |  active: 11  |  free: 0
- subnet age: 1023.2 days  |  registered at block 1497824
- weights_version: 21706  |  mechanisms: 1

## Income (miner side)

- **competitive_miner_usd_day: 1977.3477719917166** (uid 38) <- the only figure quotable as achievable
- median_miner_usd_day: 1977.3477719917166
- top_miner_usd_day: 2355.971119890197 (uid 248, owner=True, validator_permitted=True) <- NOT achievable if owner or permitted

## Incentive structure (display only - never scored)

- earners: 3  |  gini: 0.31410667236345513  |  top1_share: 0.5181432538834804  |  top10_share: 1.0
- owner_incentive_share: 0.5181432538834804 (independent check on miner_burn; disagreement 0.0)

## Repository

- on-chain URL: `https://github.com/macrocosm-os/apex`
- resolved URL: `https://github.com/macrocosm-os/apex`
- status: **ok** 
- README: 0 bytes, sha (none)
- latest release: v4.3.1 2026-08-13T13:58:06Z
- last commit: 2026-08-13T13:58:02Z
- scoring-related commit: (none) 

## Resources

- min_compute.yml present: False  |  unmodified template: False
- required: unknown (~[UNKNOWN] GB VRAM)  |  basis: **no evidence**
- cheapest satisfying machine: rtx4090 at 8.2192 USD/day  <- ASSUMED default box; no hardware evidence was found, so the margin below is indicative only
- net margin: 1087.2699 USD/day  |  payback on registration: 0.0 days

## Score

- gate: **OK** 
- score: 50.3 (rank 27), confidence 0.6 - hardware requirement unknown; no README readable; income rests on 2 competitive miners (n<=2: not a distribution)
- components: income 27.62 / freshness 35.0 / resource 11.25 / registration 10.0
- freshness basis: RELEASE 4.0d ago

## On-chain description

> Open competitions for algorithmic and agentic optimization
