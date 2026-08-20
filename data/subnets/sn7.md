# sn7 - Allways (η)

snapshot_utc: 2026-08-20T19:54:55Z  |  block: 8888243  |  row_status: ok

## Chain row

- miner_burn: **0.9542602456640452**
- registration cost: 0.15 TAO (31.464 USD), open=True
- tempo: 360.0  |  max_uids: 256  |  active: 14  |  free: 0
- subnet age: 869.5 days  |  registered at block 2627691
- weights_version: 319  |  mechanisms: 1

## Income (miner side)

- **competitive_miner_usd_day: 91.35874369972461** (uid 56) <- the only figure quotable as achievable
- median_miner_usd_day: 91.35874369972461
- top_miner_usd_day: 1934.0899643702364 (uid 53, owner=True, validator_permitted=True) <- NOT achievable if owner or permitted

## Incentive structure (display only - never scored)

- earners: 3  |  gini: 0.6357412437309897  |  top1_share: 0.9542680135502182  |  top10_share: 1.0
- owner_incentive_share: 0.9542680135502183 (independent check on miner_burn; disagreement 0.0)

## Repository

- on-chain URL: `https://github.com/entrius/allways`
- resolved URL: `https://github.com/entrius/allways`
- status: **ok** 
- README: 10642 bytes, sha 3459a8729098b6cc
- latest release: release-20260819-235753: Activate: quorum short-circuit + 30s default dendrite timeout (#697) 2026-08-19T23:57:15Z
- last commit: 2026-08-19T23:57:15Z
- scoring-related commit: (none) 

## Resources

- min_compute.yml present: True  |  unmodified template: False
- required: unknown (~[UNKNOWN] GB VRAM)  |  basis: **no evidence**
- cheapest satisfying machine: rtx4090 at 8.2192 USD/day  <- ASSUMED default box; no hardware evidence was found, so the margin below is indicative only
- net margin: 83.1396 USD/day  |  payback on registration: 0.38 days

## Score

- gate: **OK** 
- score: 44.2 (rank 42), confidence 0.6 - hardware requirement unknown; income rests on 1 competitive miner (n<=2: not a distribution)
- components: income 17.51 / freshness 35.0 / resource 11.25 / registration 9.87
- freshness basis: RELEASE 0.8d ago

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

Currently live with SOL ↔ BTC, SOL ↔ TAO, SOL ↔ ETH, SOL ↔ USDC-on-Arbitrum, SOL ↔ HYPE, SOL ↔ BNB, SOL ↔ AVAX, SOL ↔ USDC-on-Base, SOL ↔ USDC-on-Ethereum, and SOL ↔ CRO (hub-and-spoke: every pair has a SOL leg). Designed to scale to any verifiable asset.
Currently live with SOL ↔ BTC, SOL ↔ TAO, SOL ↔ ETH, SOL ↔ USDC-on-Arbitrum, SOL ↔ HYPE, SOL ↔ BNB, SOL ↔ AVAX, SOL ↔ USDC-on-Base, SOL ↔ USDC-on-Ethereum, and SOL ↔ ASTER (hub-and-spoke: every pair has a SOL leg). Designed to scale to any verifiable asset.
Currently live with SOL ↔ BTC, SOL ↔ TAO, SOL ↔ ETH, SOL ↔ USDC-on-Arbitrum, SOL ↔ HYPE, SOL ↔ BNB, SOL ↔ AVAX, SOL ↔ USDC-on-Base, SOL ↔ USDC-on-Ethereum, and SOL ↔ UNI (hub-and-spoke: every pair has a SOL leg). Designed to scale to any verifiable asset.
Currently live with SOL and TAO as hubs, each paired against BTC, ETH, USDC-on-Arbitrum, HYPE, BNB, AVAX, USDC-on-Base, USDC-on-Ethereum, and QNT — plus SOL ↔ TAO itself (hub-and-spoke: every pair has a SOL or TAO leg). Designed to scale to any verifiable asset.
Currently live with SOL ↔ BTC, SOL ↔ TAO, SOL ↔ ETH, SOL ↔ USDC-on-Arbitrum, SOL ↔ HYPE, SOL ↔ BNB, SOL ↔ AVAX, SOL ↔ USDC-on-Base, SOL ↔ USDC-on-Ethereum, and SOL ↔ POL (hub-and-spoke: every pair has a SOL leg). Designed to scale to any verifiable asset.
Currently live with SOL ↔ BTC, SOL ↔ TAO, SOL ↔ ETH, SOL ↔ USDC-on-Arbitrum, SOL ↔ HYPE, SOL ↔ BNB, SOL ↔ AVAX, SOL ↔ USDC-on-Base, SOL ↔ USDC-on-Ethereum, SOL ↔ POL, and SOL ↔ USDC-on-Polygon (hub-and-spoke: every pair has a SOL leg). Designed to scale to any verifiable asset.
Currently live with SOL ↔ BTC, SOL ↔ TAO, SOL ↔ ETH, SOL ↔ USDC-on-Arbitrum, SOL ↔ HYPE, SOL ↔ BNB, SOL ↔ AVAX, SOL ↔ USDC-on-Base, SOL ↔ USDC-on-Ethereum, and SOL ↔ PAXG (hub-and-spoke: every pair has a SOL or TAO leg). Designed to scale to any verifiable asset.

## Miner Risk Disclaimer

The miner in this repository is **reference software**. Review the code thoroughly and build it out with your own safety and optimization measures before running it. Running the base miner, or anything you build on top of it, is at your own risk.

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

## Miner Onboarding

Bond, then activate, then quote — in that order, for either backing. A quote is a promise that
one specific bond answers for, so `set_quote` refuses a purse you are not already serving
(`MinerNotActive`). Quoting before activation is rejected, not queued.

**SOL-backed** (collateral held on Solana):

```bash
alw collateral deposit <SOL>                   # fund the local purse (bind-hotkey needs it — see below)
alw miner bind-hotkey                          # bind your hotkey to your Solana pubkey (once)
alw miner activate                             # validators vote you active
alw miner post sol <addr> btc <addr> <rate>    # quote
```

**TAO-backed** (bond held in the Bittensor vault). Same order; the bond lives on another chain,
so activation waits on validators mirroring it to Solana rather than on a local read:

```bash
alw collateral deposit 0.1                     # one-time identity deposit — see the note below
alw miner bind-hotkey                          # the vault keys bonds by hotkey, joined via this binding
alw vault post-collateral <TAO>                # bond into the vault (signed by the hotkey)
alw vault lock                                 # enter service — only a LOCKED bond is attested
                                               # wait a minute: validators mirror the bond to Solana
alw miner activate --backing tao               # validators vote that purse active
alw miner post sol <addr> tao <addr> <rate> --backing tao
```

Purses activate one at a time, so `alw miner activate` lights one. It infers the backing when only
one purse is funded and not yet serving — which is every step of the order above — and asks for
`--backing` only when both are candidates at once. Activation is refused, not queued, while the
bond has yet to be mirrored: retry rather than wait on the request.

`alw miner status` shows the required bond and whether each purse is serving yet.

**A TAO-only miner still posts a small SOL deposit — once.** `bind-hotkey` requires a live local
collateral stake (`min_collateral`, currently 0.1 SOL) — which is why the deposit comes first in both
recipes above — because binding a hotkey is what claims that identity on Solana and the deposit is the
anti-squat cost of the claim. Since the vault keys bonds by
hotkey and validators join them to your Solana pubkey through that binding, a TAO-backed miner needs
the binding to set rates or be credited for its swaps — so it needs the deposit too. That is the whole
of it: the SOL purse never has to be activated, it posts no quotes, a
```

_(truncated at 6000 of 10642 chars - read the full file at https://github.com/entrius/allways)_
