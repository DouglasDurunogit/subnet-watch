# sn8 - Vanta (θ)

snapshot_utc: 2026-08-20T17:40:42Z  |  block: 8887572  |  row_status: ok

## Chain row

- miner_burn: **0.0**
- registration cost: 0.0005 TAO (0.106745 USD), open=True
- tempo: 360.0  |  max_uids: 256  |  active: 75  |  free: 0
- subnet age: 1029.2 days  |  registered at block 1477264
- weights_version: 199  |  mechanisms: 1

## Income (miner side)

- **competitive_miner_usd_day: 2935.791477865656** (uid 210) <- the only figure quotable as achievable
- median_miner_usd_day: 0.2706297453784713
- top_miner_usd_day: 11500.140400112758 (uid 117, owner=False, validator_permitted=True) <- NOT achievable if owner or permitted

## Incentive structure (display only - never scored)

- earners: 61  |  gini: 0.9516539834989526  |  top1_share: 0.6486643260570905  |  top10_share: 0.9988246069302396
- owner_incentive_share: 0.0 (independent check on miner_burn; disagreement 0.0)

## Repository

- on-chain URL: `https://github.com/taoshidev/vanta-network`
- resolved URL: `https://github.com/taoshidev/vanta-network`
- status: **ok** 
- README: 9328 bytes, sha 4358d75b67d7eabc
- latest release: (none) 
- last commit: 2026-08-19T17:56:33Z
- scoring-related commit: create subaccount elimination cache on entity miner (#861) 2026-07-30T22:26:28Z

## Resources

- min_compute.yml present: False  |  unmodified template: False
- required: unknown (~[UNKNOWN] GB VRAM)  |  basis: **no evidence**
- cheapest satisfying machine: rtx4090 at 8.2192 USD/day  <- ASSUMED default box; no hardware evidence was found, so the margin below is indicative only
- net margin: -7.9485 USD/day  |  payback on registration: [UNKNOWN] days

## Score

- gate: **OK** 
- score: 27.4 (rank 70), confidence 0.85 - hardware requirement unknown
- components: income 0.0 / freshness 21.0 / resource 11.25 / registration 0.0
- freshness basis: SCORING_COMMIT 21d ago

## On-chain description

> The first decentralized & trustless liquidity and execution engine for prop firms and traders

## README excerpt (evidence for the brief)

```markdown
> Proprietary Trading Network is now Vanta Network!

<p align="center">
  <a href="https://www.vantanetwork.io">
    <img width="385" alt="Vanta Network logo" src="https://www.taoshi.io/white-black.png">
  </a>
</p>

<div align='center'>

[![Discord Chat](https://img.shields.io/discord/1163496128499683389.svg)](https://discord.gg/vantatrading)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

</div>

<p align="center">
  <a href="https://www.vantanetwork.io">Vanta Network</a>
  ·
  <a href="https://www.vantatrading.io">Vanta Trading</a>
  ·
  <a href="#get-started">Installation</a>
  ·  
  <a href="https://www.vantanetwork.io/dashboard">Dashboard</a>
  ·
  <a href="https://x.com/VantaNetworkSN8">Twitter</a>
    ·
  <a href="https://www.bittensor.com">Bittensor</a>
</p>

---

<details>
  <summary>Table of contents</summary>
  <ol>
    <li><a href="#vanta-network">Vanta Network</a></li>
    <li><a href="#features">Features</a></li>
    <li><a href="#how-does-it-work">How does it work?</a></li>
    <li>
      <a href="#get-started">Get Started</a>
    </li>
    <li><a href="#building-a-strategy">Building a Strategy</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>

  </ol>
</details>

---

<details id='bittensor'>
  <summary>What is Bittensor?</summary>

Bittensor is a mining network, similar to Bitcoin, that includes built-in incentives designed to encourage computers to provide access to machine learning models in an efficient and censorship-resistant manner. Bittensor is comprised of Subnets, Miners, and Validators.

> Explain Like I'm Five

Bittensor is an API that connects machine learning models and incentivizes correctness through the power of the blockchain.

### Subnets

Subnets are decentralized networks of machines that collaborate to train and serve machine learning models.

### Miners

Miners run machine learning models. They send signals to the Validators.

### Validators

Validators recieve trade signals from Miners. Validators ensure trades are valid, store them, and track portfolio returns. 

</details>

<br />
<br />

# Vanta Network

This repository contains the code for the Vanta Network developed by Taoshi.

Vanta receives signals from quant and deep learning machine learning trading systems to deliver the world's
most complete trading signals across a variety of asset classes.

# Features

🛠️&nbsp;Open Source Strategy Building Techniques (In Our Taoshi Community)<br>
🫰&nbsp;Signals From a <a href="https://github.com/taoshidev/vanta-network/blob/main/vali_objects/trade_pair.py#L46"> Variety of Asset Classes</a> - Forex, Crypto, Equities, and Commodities<br>
📈&nbsp;<a href="https://tokenomics.taoshi.io">Millions of $ Funding</a> to Top Traders<br>
💪&nbsp;Innovative Trader Performance Metrics that Identify the Best Traders<br>
🔎&nbsp;<a href="https://www.vantanetwork.io/dashboard">Trading + Metrics Visualization Dashboard</a><br>
🔎&nbsp;Maximum <a href="https://www.vantanetwork.io/transparency">Transparency</a> for all updates

## How does it work?

Vanta is the most challenging & competitive network in the world. Our miners need to provide futures based signals (long/short)
that are highly efficient and effective across various markets to compete (forex, crypto, equities, commodities). The top miners are
those that provide the most returns, while never exceeding certain drawdown limits.

### Rules

1. Miners can submit LONG, SHORT, or FLAT signal for Forex, Crypto, Equities, or Commodities trade pairs into the network during market hours. <a href="https://github.com/taoshidev/vanta-network/blob/main/vali_objects/trade_pair.py#L125">Currently supported trade pairs</a>
2. Miners are eliminated if they are detected as plagiarising other miners, if they exceed a 5% intraday drawdown from the day's opening equity, an 8% end-of-day drawdown from their highest-ever end-of-day equity (high-water mark), or if they go 60 days without submitting a single order (more info in the "Eliminations" section).
3. There is a fee for leaving positions open "carry fee". The fee is equal to 10.95%/3% per year for a 1x leverage position (crypto/forex respectively); equities instead pay a 3%/yr stock-borrow fee (short) or 6.6%/yr margin interest on the borrowed amount (long); commodities currently carry no fee for standard positions <a href="https://docs.taoshi.io/tips/p4/">More info</a>
4. There is a spread (transaction) fee applied to crypto, equities, commodities, and indices orders, calculated as a percentage of order value - 0.05% for crypto and equities, 0.045% for commodities and indices (forex has no spread fee). This simulates a transaction cost that a normal exchange would add.
5. There is a slippage assessed per order. The slippage cost is is greater for orders with higher leverages, and in assets with lower liquidity.
6. Miners are rewarded using a debt-based scoring system that tracks their emissions, performance, and penalties. Weights are set based on the previous week's performance (PnL scaled by penalties), with payout periods starting and ending at midnight UTC on Sunday <a href="https://github.com/taoshidev/vanta-network/blob/main/docs/miner.md">More info</a>

With this system only the world's best traders & deep learning / quant based trading systems can compete.


# Eliminations

In the Vanta Network, eliminations occur for miners that commit plagiarism, breach drawdown limits, fail to exit probation in time, or are inactive.


### Plagiarism Eliminations

Miners who repeatedly copy another miner's trades will be eliminated. Our system analyzes the uniqueness of each submitted order. If an order is found to be a copy (plagiarized), it triggers the miner's elimination.

### Max Drawdown Elimination

Miners who exceed a 5% intraday drawdown (measured from the day's opening equity) or an 8% end-of-day drawdown (measured from their highest-ever end-of-day equity) wil
```

_(truncated at 6000 of 9328 chars - read the full file at https://github.com/taoshidev/vanta-network)_
