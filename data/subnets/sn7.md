# sn7 - Allways (η)

snapshot_utc: 2026-09-04T23:01:35Z  |  block: 8997169  |  row_status: ok

## Chain row

- miner_burn: **0.05229283822700381**
- registration cost: 0.15 TAO (33.372 USD), open=True
- tempo: 360.0  |  max_uids: 256  |  active: 15  |  free: 0
- subnet age: 884.6 days  |  registered at block 2627691
- weights_version: 319  |  mechanisms: 1

## Income (miner side)

- **competitive_miner_usd_day: 1079.601782820201** (uid 45) <- the only figure quotable as achievable
- median_miner_usd_day: 879.9174154267514
- top_miner_usd_day: 1079.601782820201 (uid 45, owner=False, validator_permitted=False) <- NOT achievable if owner or permitted

## Incentive structure (display only - never scored)

- earners: 3  |  gini: 0.3132318084251433  |  top1_share: 0.5221411786248359  |  top10_share: 1.0
- owner_incentive_share: 0.05229346598712119 (independent check on miner_burn; disagreement 0.0)

## Repository

- on-chain URL: `https://github.com/entrius/allways`
- resolved URL: `https://github.com/entrius/allways`
- status: **ok** 
- README: 10900 bytes, sha dfc91260798a797c
- latest release: release-20260904-214340: Bump version to 3.3.2 (#722) 2026-09-04T21:43:18Z
- last commit: 2026-09-04T21:43:18Z
- scoring-related commit: CLI: --send verifies source-address control BEFORE the bid (#716) 2026-09-02T22:52:26Z

## Resources

- min_compute.yml present: True  |  unmodified template: False
- required: unknown (~[UNKNOWN] GB VRAM)  |  basis: **no evidence**
- cheapest satisfying machine: rtx4090 at 8.2192 USD/day  <- ASSUMED default box; no hardware evidence was found, so the margin below is indicative only
- net margin: 1071.3826 USD/day  |  payback on registration: 0.03 days

## Score

- gate: **OK** 
- score: 50.3 (rank 31), confidence 0.6 - hardware requirement unknown; income rests on 1 competitive miner (n<=2: not a distribution)
- components: income 27.56 / freshness 35.0 / resource 11.25 / registration 9.99
- freshness basis: RELEASE 0.0d ago

## On-chain description

> universal transaction layer

## README excerpt (evidence for the brief)

```markdown
# Allways

**Settlement layer for agents and applications**

Native cross-chain transactions for programs that hold one asset and need to pay in another — no wrapped tokens, no bridges, no custodian. Bittensor Subnet 7 (SN7).

[![Twitter](https://img.shields.io/twitter/follow/allways_io?style=social)](https://x.com/allways_io)

## Overview

Allways is a settlement layer built to be driven by software. An agent or application that holds SOL, TAO, BTC, or any supported asset submits a single swap and receives the destination asset natively in its own wallet — no account, no custodian, no bridge in the path. Allways creates a verification layer above independent systems: miners complete transactions, validators independently verify both legs on-chain, and a smart contract enforces outcomes through collateral and slashing.

Currently live with SOL and TAO as hubs, each paired against BTC, ETH, USDC-on-Arbitrum, HYPE, BNB, AVAX, USDC-on-Base, USDC-on-Ethereum, CRO, ASTER, UNI, QNT, POL, USDC-on-Polygon, PAXG, and USDC-on-Solana — plus SOL ↔ TAO itself (hub-and-spoke: every pair has a SOL or TAO leg). Designed to scale to any verifiable asset.

## For agents

Allways is designed to be operated by software, not clicked through by people. Every step of a swap — quote discovery, reservation, deposit, and settlement — is a CLI command (`alw swap now`) or a public API call (`api.all-ways.io`) with structured output, so an autonomous agent can clear a payment in another native asset as a single tool call, with no human in the loop, no exchange account, and no custodian holding its keys. This is how the network is used in practice: agents operated by the team and by users originate swaps today, and the miner and validator neurons in this repo are themselves unattended programs that quote, fulfill, and verify around the clock.

**Why agents need a settlement layer.** An agent's wallet is a single-chain identity, but the things it pays for are not. An LLM agent earning TAO may need to buy inference from a provider that bills in USDC; a trading agent holding SOL may need to settle an obligation in BTC; a multi-agent pipeline may split revenue across operators who each want a different native asset. Bridges and centralized exchanges break the autonomy model — they require accounts, KYC, custody, and a human to unblock them. Allways lets the agent stay self-custodial: it sends the source asset from its own wallet and receives the destination asset in its own wallet, and the protocol verifies the outcome on-chain.

**Swap lifecycle as tool calls.**

- **Discover**: `GET` live quotes per pair from the API and select a rate, liquidity, and miner.
- **Reserve**: lock that miner's quote and collateral for the swap window.
- **Deposit**: send the source asset natively from the agent's wallet; validators attest the deposit on-chain.
- **Settle**: the miner delivers the destination asset to the agent's wallet; validators verify the delivery or slash the miner's collateral to reimburse the agent.

Each call returns machine-readable state (swap id, reservation window, deadlines, attestation status), so an agent can plan, retry, and reason over the full lifecycle without parsing prose.

**Use cases in production and in reach.**

- **Agent-to-agent payments**: an orchestrator pays sub-agents or tool providers in whatever asset they accept, funded from a single treasury.
- **Inference and compute procurement**: convert earned TAO or SOL into the stablecoin or native token a GPU or model provider bills in.
- **Treasury automation**: an agent rebalances a multi-chain treasury on a schedule or on a signal, without moving funds through a custodian.
- **Autonomous market-making**: the reference miner is itself an agent — it posts quotes, manages collateral, and fulfills swaps programmatically; operators extend it with their own pricing and risk logic.
- **Bittensor-native economics**: agents earning alpha or TAO on other subnets settle into the asset they actually spend, with SOL and TAO as hubs.

See the Swap guide at [docs.all-ways.io](https://docs.all-ways.io/) for the full lifecycle and API reference.

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
so activ
```

_(truncated at 6000 of 10900 chars - read the full file at https://github.com/entrius/allways)_
