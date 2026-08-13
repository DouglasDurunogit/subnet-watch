# sn5 - Hone (ε)

snapshot_utc: 2026-08-13T19:46:15Z  |  block: 8837802  |  row_status: ok

## Chain row

- miner_burn: **0.0**
- registration cost: 0.249983951 TAO (50.66174750966 USD), open=True
- tempo: 360.0  |  max_uids: 256  |  active: 254  |  free: 0
- subnet age: 881.4 days  |  registered at block 2491604
- weights_version: 803  |  mechanisms: 1

## Income (miner side)

- **competitive_miner_usd_day: 36.24293569084155** (uid 216) <- the only figure quotable as achievable
- median_miner_usd_day: 34.0315023266546
- top_miner_usd_day: 36.24293569084155 (uid 216, owner=False, validator_permitted=False) <- NOT achievable if owner or permitted

## Incentive structure (display only - never scored)

- earners: 244  |  gini: 0.03964651929988072  |  top1_share: 0.004523360473496174  |  top10_share: 0.044037597558918694
- owner_incentive_share: 0.0 (independent check on miner_burn; disagreement 0.0)

## Repository

- on-chain URL: `https://github.com/manifold-inc/hone`
- resolved URL: `https://github.com/manifold-inc/hone`
- status: **ok** 
- README: 19813 bytes, sha c9674d487ee9e17d
- latest release: (none) 
- last commit: 2026-01-29T17:49:21Z
- scoring-related commit: debug miner changing uid 2025-12-07T21:19:09Z

## Resources

- min_compute.yml present: False  |  unmodified template: False
- required: unknown (~[UNKNOWN] GB VRAM)  |  basis: **no evidence**
- cheapest satisfying machine: rtx4090 at 8.2192 USD/day  <- ASSUMED default box; no hardware evidence was found, so the margin below is indicative only
- net margin: 25.8123 USD/day  |  payback on registration: 1.96 days

## Score

- gate: **OK** 
- score: 28.5 (rank 61), confidence 0.85 - hardware requirement unknown
- components: income 12.99 / freshness 0.0 / resource 11.25 / registration 9.35
- freshness basis: no challenge change on record

## On-chain description

> Hone training

## README excerpt (evidence for the brief)

```markdown
# Hone Subnet — ARC-AGI-2 Benchmarking on Bittensor

A Bittensor subnet where **validators** evaluate **miners** on their ability to solve novel ARC-AGI-2 reasoning problems. Miners don't run solvers directly—they point to a git repository containing their solution, which is executed in a secure GPU sandbox.

---

## Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Quick Start](#quick-start)
- [Validator Setup](#validator-setup)
- [Miner Setup](#miner-setup)
- [Building Your Solver](#building-your-solver)
- [Local Testing with Sandbox Runner](#local-testing-with-sandbox-runner)
- [Configuration Reference](#configuration-reference)
- [Troubleshooting](#troubleshooting)
- [Security Notes](#security-notes)

---

## Overview

### How It Works

1. **Miners** expose an HTTP endpoint (`/info`) that returns a pointer to their solution repository
2. **Validators** fetch miner info, submit jobs to a **Sandbox Runner** (secure GPU execution service)
3. The Sandbox Runner clones the miner's repo, builds a Docker image, runs prep (with internet) and inference (isolated), then calculates metrics
4. Validators aggregate `exact_match_rate` scores and set on-chain weights using exponential distribution

### Scoring Mechanism

- **Metric**: `exact_match_rate` — percentage of ARC problems solved correctly
- **Minimum floor**: 20% accuracy required to qualify
- **Top 5** miners above floor receive rewards
- **Miner rewards**: Rewards distributed via exponential decay (factor 0.8 per rank)
- **No qualifiers**: If no miners meet the floor, 100% is burned

### Key Features

- **Submission caching**: Identical repo+branch+commit combinations use cached scores (no redundant evaluation)
- **Daily limits**: Configurable submissions per miner per day (default: 1)
- **GPU isolation**: Inference runs without network access
- **vLLM support**: Optional LLM sidecar for transformer-based solvers

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              BITTENSOR CHAIN                                │
│                    (miner registration, weights, stake)                     │
└─────────────────────────────────────────────────────────────────────────────┘
                                      │
                 ┌────────────────────┼────────────────────┐
                 │                    │                    │
                 ▼                    ▼                    ▼
          ┌─────────────┐      ┌─────────────┐      ┌─────────────┐
          │  VALIDATOR  │      │  VALIDATOR  │      │  VALIDATOR  │
          │             │      │             │      │             │
          │ • Discover  │      │             │      │             │
          │ • Query     │      │             │      │             │
          │ • Score     │      │             │      │             │
          │ • Set wts   │      │             │      │             │
          └──────┬──────┘      └─────────────┘      └─────────────┘
                 │
        ┌────────┴────────┐
        │                 │
        │ Fetch /info     │ Submit jobs via API
        ▼                 ▼
  ┌───────────┐    ┌─────────────────────────────────────────────────────┐
  │  MINERS   │    │                  SANDBOX RUNNER                      │
  │           │    │                                                      │
  │ ┌───────┐ │    │  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐ │
  │ │ M1    │ │    │  │ H200 #0 │  │ H200 #1 │  │ H200 #2 │  │ H200 #3 │ │
  │ │/info  │ │    │  └─────────┘  └─────────┘  └─────────┘  └─────────┘ │
  │ └───────┘ │    │  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐ │
  │ ┌───────┐ │    │  │ H200 #4 │  │ H200 #5 │  │ H200 #6 │  │ H200 #7 │ │
  │ │ M2    │ │    │  └─────────┘  └─────────┘  └─────────┘  └─────────┘ │
  │ │/info  │ │    │                                                      │
  │ └───────┘ │    │  • Clone repo → Build image → Run prep → Run infer  │
  │ ┌───────┐ │    │  • Calculate exact_match_rate against held-out data │
  │ │ M_N   │ │    └─────────────────────────────────────────────────────┘
  │ │/info  │ │
  │ └───────┘ │
  └───────────┘
```

---

## Quick Start

### Prerequisites

- **Python 3.10+**
- **Docker & Docker Compose**
- **Bittensor CLI** (`btcli`)
- **NVIDIA GPU + drivers** (for sandbox runner / local testing)
- TAO for registration and staking

### Create Wallets

```bash
# create coldkey
btcli wallet new_coldkey --wallet.name default

# create hotkeys
btcli wallet new_hotkey --wallet.name default --wallet.hotkey validator
btcli wallet new_hotkey --wallet.name default --wallet.hotkey miner
```

---

## Validator Setup

### Requirements

- 4+ CPU cores
- 8GB+ RAM
- 20GB disk
- Reliable network connection

### 1. Clone Repository

```bash
git clone https://github.com/manifold-inc/hone.git
cd hone/validator
```

### 2. Configure Environment

Create `validator/.env`:

```ini
# chain
NETUID=5
CHAIN_ENDPOINT=wss://entrypoint-finney.opentensor.ai:443

# wallet
WALLET_NAME=default
WALLET_HOTKEY=validator
WALLET_PATH=/root/.bittensor/wallets

# database
DB_URL=postgresql://postgres:postgres@db:5432/hone
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=hone

# sandbox runner connection
SANDBOX_RUNNER_ENDPOINT=http://your-sandbox-runner:8000
SANDBOX_RUNNER_API_KEY=your_api_key_here
SANDBOX_RUNNER_TIMEOUT_HOURS=3

# scoring parameters
MAX_SUBMISSIONS_PER_DAY=1
MIN_ACCURACY_FLOOR=0.20
TOP_MINERS_COUNT=5
BURN_UID=251
BURN_PERCENTAGE=0.95

# cycle timing
CYCLE_DURATION=30
```

### 3. Register and Stake

```bash
# register validator on subnet
btcli subnet register --netuid 5 --wallet.name default --wallet.hotkey validator

# stake TAO
btcli stake add --wallet.name default --wallet.hotkey validator --amount 100
```

### 4. Start Validator

```bash
cd validator
make up
```

This starts:
- PostgreSQL database
- Adminer (DB UI on port 8080)
- Validator service

### 5. Monitor

```b
```

_(truncated at 6000 of 19813 chars - read the full file at https://github.com/manifold-inc/hone)_
