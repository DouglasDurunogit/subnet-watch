# sn7 - Allways (η)

snapshot_utc: 2026-08-26T10:48:37Z  |  block: 8928712  |  row_status: ok

## Chain row

- miner_burn: **0.9995738533325493**  <- 100% burn: miners earn NOTHING here
- registration cost: 0.15 TAO (35.364 USD), open=True
- tempo: 360.0  |  max_uids: 256  |  active: 13  |  free: 0
- subnet age: 875.1 days  |  registered at block 2627691
- weights_version: 319  |  mechanisms: 1

## Income (miner side)

- **competitive_miner_usd_day: [UNKNOWN]** (uid [UNKNOWN]) <- the only figure quotable as achievable
- median_miner_usd_day: 1121.3600191113517
- top_miner_usd_day: 2241.7960378407333 (uid 53, owner=True, validator_permitted=True) <- NOT achievable if owner or permitted

## Incentive structure (display only - never scored)

- earners: 2  |  gini: 0.49958800012207405  |  top1_share: 0.9995880001220739  |  top10_share: 1.0
- owner_incentive_share: 0.999588000122074 (independent check on miner_burn; disagreement 0.0)

## Repository

- on-chain URL: `https://github.com/entrius/allways`
- resolved URL: `https://github.com/entrius/allways`
- status: **ok** 
- README: 9134 bytes, sha 7579607a23dc6d8d
- latest release: release-20260824-151246: Bump allways to 3.3.0 (#705) 2026-08-24T14:36:35Z
- last commit: 2026-08-24T14:36:35Z
- scoring-related commit: fix(validator): non-earner trace reads live quotes, not dead last_kno… 2026-08-22T21:11:25Z

## Resources

- min_compute.yml present: True  |  unmodified template: False
- required: unknown (~[UNKNOWN] GB VRAM)  |  basis: **no evidence**
- cheapest satisfying machine: rtx4090 at 8.2192 USD/day  <- ASSUMED default box; no hardware evidence was found, so the margin below is indicative only
- net margin: [UNKNOWN] USD/day  |  payback on registration: [UNKNOWN] days

## Score

- gate: **BLOCKED:burn** - miner_burn=1.000 - 100.0% of miner emission is withheld by owner-controlled hotkeys, so miners earn nothing here
- score: [UNKNOWN] (rank -), confidence [UNKNOWN] 
- components: income [UNKNOWN] / freshness [UNKNOWN] / resource [UNKNOWN] / registration [UNKNOWN]
- freshness basis: -

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

Currently live with SOL and TAO as hubs, each paired against BTC, ETH, USDC-on-Arbitrum, HYPE, BNB, AVAX, USDC-on-Base, USDC-on-Ethereum, CRO, ASTER, UNI, QNT, POL, USDC-on-Polygon, PAXG, and USDC-on-Solana — plus SOL ↔ TAO itself (hub-and-spoke: every pair has a SOL or TAO leg). Designed to scale to any verifiable asset.

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
of it: the SOL purse never has to be activated, it posts no quotes, and it backs nothing. Withdraw it
by deactivating and waiting out the cooldown, the same as any SOL collateral.

**What a TAO-backed quote guarantees.** If the miner fails to deliver, the user is reimbursed in
TAO from the miner's bond, shortly after the timeout. That differs from a SOL-backed quote in
timing only: a SOL refund is instant because the collateral sits beside the swap, while the TAO
reimbursement waits for validators to carry the timeout verdict to the vault and reach quorum
there. Either way the user is made whole out of the bond that backed the quote.

**Leaving.** A locked bond is not withdrawable on demand. Deactivate the purse
(`alw miner deactivate --backing tao`), let in-flight swaps and their timeout windows drain, and
validators unlock the bond once nothing is owed on it — then `alw vault withdraw` succeeds.

## Validator Storage Layout

Validator state lives in `~/.allways/validator/state.db` (SQLite, WAL mode).
Tables: `pending_confirms`, `rate_events`, `swap_outcomes`. Collateral /
active / min_collateral state is held in memory and rebuilt from contract
events each startup; only `swap_outcomes` (the all-time credibility ledger)
needs to persist across restarts.

## Miner Environment Variables

- `BTC_PRIVATE_KEY`, `ETH_PRIVATE_KEY`, `ARB_PRIVATE_KEY`, `HYPE_PRIVATE_KEY`, `BNB_PRIVATE_KEY`, `AVAX_PRIVATE_KEY`, `BASE_PRIVATE_KEY`, `CRO_PRIVATE_KEY`, `{ETH,ARB,HYPE,BNB,AVAX,BASE,CRO}_RPC_URLS`, etc. — keyed by network, so assets sharing one share its config (ET
```

_(truncated at 6000 of 9134 chars - read the full file at https://github.com/entrius/allways)_
