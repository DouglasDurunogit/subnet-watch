# sn2 - DaniLabs (β)

snapshot_utc: 2026-11-24T20:44:55Z  |  block: 9579085  |  row_status: ok

## Chain row

- miner_burn: **0.847775052068755**
- registration cost: 0.0005 TAO (0.0897 USD), open=True
- tempo: 360.0  |  max_uids: 256  |  active: 8  |  free: 0
- subnet age: 950.7 days  |  registered at block 2734060
- weights_version: 11003  |  mechanisms: 1

## Income (miner side)

- **competitive_miner_usd_day: 133.48422691884582** (uid 126) <- the only figure quotable as achievable
- median_miner_usd_day: 133.48422691884582
- top_miner_usd_day: 1454.9964055635153 (uid 14, owner=True, validator_permitted=True) <- NOT achievable if owner or permitted

## Incentive structure (display only - never scored)

- earners: 3  |  gini: 0.5155672205860662  |  top1_share: 0.8477866113255916  |  top10_share: 1.0
- owner_incentive_share: 0.8477866113255916 (independent check on miner_burn; disagreement 0.0)

## Repository

- on-chain URL: `https://github.com/DaniLabsAI/subnet`
- resolved URL: `https://github.com/DaniLabsAI/subnet`
- status: **ok** 
- README: 1374 bytes, sha 668296f1d9856c8f
- latest release: (none) 
- last commit: 2026-11-10T21:20:50Z
- scoring-related commit: Merge pull request #1 from mybelovedstar123/test/score-properties 2026-11-10T21:17:39Z

## Resources

- min_compute.yml present: False  |  unmodified template: False
- required: unknown (~[UNKNOWN] GB VRAM)  |  basis: **no evidence**
- cheapest satisfying machine: rtx4090 at 8.2192 USD/day  <- ASSUMED default box; no hardware evidence was found, so the margin below is indicative only
- net margin: 122.3974 USD/day  |  payback on registration: 0.0 days

## Score

- gate: **OK** 
- score: 36.8 (rank 59), confidence 0.6 - hardware requirement unknown; income rests on 2 competitive miners (n<=2: not a distribution)
- components: income 19.02 / freshness 21.0 / resource 11.25 / registration 10.0
- freshness basis: SCORING_COMMIT 14d ago

## On-chain description

> Distributed Accelerated Neural intelligence

## README excerpt (evidence for the brief)

```markdown
# DaniLabs SN2 validator

Validator software for Bittensor Finney subnet 2. The worker verifies signed
performance reports against finalized chain state and scores miners by workload.

## Requirements

Use an Ubuntu 24.04 LTS CPU host (x86-64 or ARM64) with systemd. The recommended
minimum is **4 vCPUs, 8 GB RAM, and 50 GB SSD**. Have `sudo` and `curl` available
and allow outbound HTTPS and WSS connections.

## Install

```sh
curl -fsSLo install-danilabs-validator.sh https://raw.githubusercontent.com/DaniLabsAI/subnet/main/deploy/install-validator.sh && sudo bash install-danilabs-validator.sh
```

Installation starts the worker, verifies a finalized report, and enables
automatic updates. A successful install prints the Git commit and report ID.

## Operate

```sh
sudo systemctl status danilabs-sn2-validator.service danilabs-sn2-update.timer
```

- [Installation, verification, and troubleshooting](docs/validator-onboarding.md)
- [Automatic updates and rollback](docs/worker-updates.md)
- [Report verification and scoring](docs/validator-reports.md)
- [DaniLabs validator documentation](https://danilabs.ai/docs/validators/)

For operator support, share your SN2 UID, Git commit, and report ID in
[DaniLabs #validators](https://discord.com/channels/1555079929148866610/1564448334322602177).
[Join the DaniLabs Discord](https://discord.gg/df3TYnaX4f) for access.

```
