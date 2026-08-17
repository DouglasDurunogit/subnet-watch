# sn1 - Apex (α)

snapshot_utc: 2026-08-17T15:48:40Z  |  block: 8865413  |  row_status: ok

## Chain row

- miner_burn: **0.51947824168019**
- registration cost: 0.0005 TAO (0.098595 USD), open=True
- tempo: 99.0  |  max_uids: 256  |  active: 11  |  free: 0
- subnet age: 1023.3 days  |  registered at block 1497824
- weights_version: 21706  |  mechanisms: 1

## Income (miner side)

- **competitive_miner_usd_day: 1982.6651205339394** (uid 38) <- the only figure quotable as achievable
- median_miner_usd_day: 1982.6651205339394
- top_miner_usd_day: 2375.012363246215 (uid 248, owner=True, validator_permitted=True) <- NOT achievable if owner or permitted

## Incentive structure (display only - never scored)

- earners: 3  |  gini: 0.31509343750317886  |  top1_share: 0.5194860683004242  |  top10_share: 1.0
- owner_incentive_share: 0.5194860683004242 (independent check on miner_burn; disagreement 0.0)

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
- net margin: 1090.1996 USD/day  |  payback on registration: 0.0 days

## Score

- gate: **OK** 
- score: 50.3 (rank 21), confidence 0.6 - hardware requirement unknown; no README readable; income rests on 2 competitive miners (n<=2: not a distribution)
- components: income 27.63 / freshness 35.0 / resource 11.25 / registration 10.0
- freshness basis: RELEASE 4.1d ago

## On-chain description

> Open competitions for algorithmic and agentic optimization
