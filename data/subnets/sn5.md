# sn5 - Hone (ε)

snapshot_utc: 2026-11-27T18:20:43Z  |  block: 9599964  |  row_status: ok

## Chain row

- miner_burn: **0.0**
- registration cost: 0.413523544 TAO (76.42742140208 USD), open=True
- tempo: 360.0  |  max_uids: 256  |  active: 253  |  free: 0
- subnet age: 987.3 days  |  registered at block 2491604
- weights_version: 803  |  mechanisms: 1

## Income (miner side)

- **competitive_miner_usd_day: 46.82270896234585** (uid 132) <- the only figure quotable as achievable
- median_miner_usd_day: 25.408058488095996
- top_miner_usd_day: 46.82270896234585 (uid 132, owner=False, validator_permitted=False) <- NOT achievable if owner or permitted

## Incentive structure (display only - never scored)

- earners: 242  |  gini: 0.19787949238595348  |  top1_share: 0.007169171035937572  |  top10_share: 0.06978095048839023
- owner_incentive_share: 0.0 (independent check on miner_burn; disagreement 0.0)

## Repository

- on-chain URL: `https://github.com/hone-subnet-org/hone-subnet`
- resolved URL: `https://github.com/hone-subnet-org/hone-subnet`
- status: **error** - HTTP 504
- README: 0 bytes, sha (none)
- latest release: (none) 
- last commit: (unknown)
- scoring-related commit: (none) 

## Resources

- min_compute.yml present: False  |  unmodified template: False
- required: unknown (~[UNKNOWN] GB VRAM)  |  basis: **no evidence**
- cheapest satisfying machine: rtx4090 at 8.2192 USD/day  <- ASSUMED default box; no hardware evidence was found, so the margin below is indicative only
- net margin: 17.1889 USD/day  |  payback on registration: 4.45 days

## Score

- gate: **OK** 
- score: 31.3 (rank 37), confidence 0.6 - hardware requirement unknown; no README readable; repo error
- components: income 11.46 / freshness 21.0 / resource 11.25 / registration 8.52
- freshness basis: SCORING_COMMIT 14d ago

## On-chain description

> Hone (SN5) is an RLVR subnet: reinforcement learning from verifiable rewards. Miners are paid to solve real software-engineering tasks- repository patches submitted as git diffs and terminal tasks submitted as scripts with full trajectories. Validators lease tasks from a problem server and grade eve
