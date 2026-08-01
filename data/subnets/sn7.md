# sn7 - Allways (η)

snapshot_utc: 2026-08-01T09:32:02Z  |  block: 8748352  |  row_status: ok

## Chain row

- miner_burn: **0.9229409645777196**
- registration cost: 0.15 TAO (29.2815 USD), open=True
- tempo: 360.0  |  max_uids: 256  |  active: 15  |  free: 0
- subnet age: 850.1 days  |  registered at block 2627691
- weights_version: 319  |  mechanisms: 1

## Income (miner side)

- **competitive_miner_usd_day: 151.9631877357999** (uid 56) <- the only figure quotable as achievable
- median_miner_usd_day: 151.9631877357999
- top_miner_usd_day: 1865.1261053190176 (uid 53, owner=True, validator_permitted=True) <- NOT achievable if owner or permitted

## Incentive structure (display only - never scored)

- earners: 3  |  gini: 0.6140722994521843  |  top1_share: 0.9229548471762318  |  top10_share: 1.0
- owner_incentive_share: 0.9229548471762319 (independent check on miner_burn; disagreement 0.0)

## Repository

- on-chain URL: `https://github.com/entrius/allways`
- resolved URL: `https://github.com/entrius/allways`
- status: **ok** 
- README: 3314 bytes, sha 9ce1a41a5ac77071
- latest release: release-20260729-181714 2026-07-29T18:16:30Z
- last commit: 2026-07-29T18:16:30Z
- scoring-related commit: Add BURN_RATE with pools scaled to the miner share (#607) 2026-07-29T18:16:30Z

## Resources

- min_compute.yml present: True  |  unmodified template: False
- required: unknown (~[UNKNOWN] GB VRAM)  |  basis: **no evidence**
- cheapest satisfying machine: rtx4090 at 8.2192 USD/day  <- ASSUMED default box; no hardware evidence was found, so the margin below is indicative only
- net margin: 69.628 USD/day  |  payback on registration: 0.42 days

## Score

- gate: **OK** 
- score: 43.8 (rank 27), confidence 0.6 - hardware requirement unknown; income rests on 2 competitive miners (n<=2: not a distribution)
- components: income 16.82 / freshness 35.0 / resource 11.25 / registration 9.86
- freshness basis: RELEASE 2.6d ago

## On-chain description

> universal transaction layer

## README excerpt (evidence for the brief)

```markdown
# Allways

**Universal Transaction Layer**

Native transactions across independent assets — no wrapped tokens, no bridges, no custodian. Bittensor Subnet 7 (SN7).

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

<sub>Allways is permissionless, open-source, beta software. Swaps settle directly between counterparty wallets; the protocol never takes custody of user funds, and the protocol fee is charged against miner collateral rather than any user transfer. Validator operators, including those run by the project, verify swap outcomes but cannot redirect or receive any transferred amount. Use at your own risk. This software is provided "as is" without warranty of any kind. Nothing herein constitutes financial advice, and the creators assume no liability for losses arising from use of the protocol.</sub>

```
