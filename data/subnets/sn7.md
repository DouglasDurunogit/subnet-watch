# sn7 - Allways (η)

snapshot_utc: 2026-07-28T11:16:50Z  |  block: 8720095  |  row_status: ok

## Chain row

- miner_burn: **0.41608464252203703**
- registration cost: 0.15 TAO (28.0665 USD), open=True
- tempo: 360.0  |  max_uids: 256  |  active: 28  |  free: 0
- subnet age: 846.2 days  |  registered at block 2627691
- weights_version: 319  |  mechanisms: 1

## Income (miner side)

- **competitive_miner_usd_day: 1184.5535485972725** (uid 73) <- the only figure quotable as achievable
- median_miner_usd_day: 0.21811539457546578
- top_miner_usd_day: 1184.5535485972725 (uid 73, owner=False, validator_permitted=False) <- NOT achievable if owner or permitted

## Incentive structure (display only - never scored)

- earners: 16  |  gini: 0.8837966637160037  |  top1_share: 0.580202069533897  |  top10_share: 0.999893165654284
- owner_incentive_share: 0.4161655627117609 (independent check on miner_burn; disagreement 0.0001)

## Repository

- on-chain URL: `https://github.com/entrius/allways`
- resolved URL: `https://github.com/entrius/allways`
- status: **ok** 
- README: 3103 bytes, sha 0813063647d71f0c
- latest release: release-20260727-232657: Persist the direction pool on every score row (#600) 2026-07-27T22:41:44Z
- last commit: 2026-07-27T22:41:44Z
- scoring-related commit: Persist the direction pool on every score row (#600) 2026-07-27T22:41:44Z

## Resources

- min_compute.yml present: True  |  unmodified template: False
- required: unknown (~[UNKNOWN] GB VRAM)  |  basis: **no evidence**
- cheapest satisfying machine: rtx4090 at 8.2192 USD/day  <- ASSUMED default box; no hardware evidence was found, so the margin below is indicative only
- net margin: -8.0322 USD/day  |  payback on registration: [UNKNOWN] days

## Score

- gate: **OK** 
- score: 9.6 (rank 72), confidence 0.85 - hardware requirement unknown
- components: income 0.0 / freshness 0.0 / resource 11.25 / registration 0.0
- freshness basis: no challenge change on record

## On-chain description

> universal transaction layer

## README excerpt (evidence for the brief)

```markdown
# Allways

**Universal Transaction Layer**

Trustless native transactions across independent assets — Bittensor Subnet 7 (SN7).

[![Twitter](https://img.shields.io/twitter/follow/allways_io?style=social)](https://x.com/allways_io)

## Overview

Allways creates a verification layer above independent systems. Assets move natively. Miners complete transactions, validators independently verify the results, and a smart contract enforces outcomes through collateral and slashing.

Currently live with BTC ↔ TAO. Designed to scale to any verifiable asset.
## Getting Started

### Requirements

- Python 3.10+
- Bittensor wallet
- Docker & Docker Compose

### Installation

### Running with Docker

**Miner:**

```bash
docker compose -f docker-compose.miner.yml up -d
```

**Validator:**

```bash
docker compose -f docker-compose.vali.yml up -d
```

Both require a `.env` file with `PORT` and `WALLET_PATH` configured.

### CLI

```bash
uv sync
# activate the uv virtual environment
source .venv/bin/activate

alw --help
```

## Architecture

- **Miners**: Post exchange rate pairs and collateral, fulfill swap orders
- **Validators**: Monitor swaps, verify on-chain transactions, vote on outcomes
- **Smart Contract**: Manages collateral, swap lifecycle, and validator voting
- **CLI**: User interface for posting pairs, managing collateral, and executing swaps

## Validator Storage Layout

Validator state lives in `~/.allways/validator/state.db` (SQLite, WAL mode).
Tables: `pending_confirms`, `rate_events`, `swap_outcomes`. Collateral /
active / min_collateral state is held in memory and rebuilt from contract
events each startup; only `swap_outcomes` (the all-time credibility ledger)
needs to persist across restarts.

## Miner Environment Variables

- `BTC_MODE`, `BTC_PRIVATE_KEY`, `BTC_RPC_URL`, etc. — see `.env.example`.

## Running a Local Subtensor Lite Node (Validators)

Validators read miner rate commitments every ~3 minutes AND stream contract
events every block via the same connection. Pointing at the public `finney`
entrypoint works but adds latency and RPC pressure — every validator on the
network should run its own lite node for this.

```bash
# Minimal lite-node command (adjust --base-path for storage volume)
subtensor \
  --chain finney \
  --base-path /var/lib/subtensor \
  --rpc-external \
  --ws-external \
  --port 30333 \
  --rpc-port 9933 \
  --ws-port 9944 \
  --pruning 1000
```

Then point the validator at it via `.env`:

```env
SUBTENSOR_NETWORK=ws://127.0.0.1:9944
```

The dev environment in `alw-utils/dev-environment` provisions a local chain
automatically — no manual lite-node step is required there.

## License

MIT License

---

<sub>Allways is permissionless, open-source, beta software. The protocol facilitates trustless peer-to-peer transactions — the creators and contributors do not custody, control, or intermediate any funds. Use at your own risk. This software is provided "as is" without warranty of any kind. Nothing herein constitutes financial advice, and the creators assume no liability for losses arising from use of the protocol.</sub>

```
