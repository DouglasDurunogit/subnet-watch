# sn9 - iota (ι)

snapshot_utc: 2026-07-28T22:44:06Z  |  block: 8723531  |  row_status: ok

## Chain row

- miner_burn: **0.7960468388628215**
- registration cost: 0.000568856 TAO (0.11051734367999999 USD), open=True
- tempo: 360.0  |  max_uids: 256  |  active: 13  |  free: 0
- subnet age: 1004.7 days  |  registered at block 1489797
- weights_version: 4062  |  mechanisms: 1

## Income (miner side)

- **competitive_miner_usd_day: 2726.874324671995** (uid 21) <- the only figure quotable as achievable
- median_miner_usd_day: 2726.874324671995
- top_miner_usd_day: 15504.695342723555 (uid 209, owner=True, validator_permitted=True) <- NOT achievable if owner or permitted

## Incentive structure (display only - never scored)

- earners: 3  |  gini: 0.48807979694708514  |  top1_share: 0.7960569484076724  |  top10_share: 1.0
- owner_incentive_share: 0.7960569484076724 (independent check on miner_burn; disagreement 0.0)

## Repository

- on-chain URL: `https://github.com/macrocosm-os/iota`
- resolved URL: `https://github.com/macrocosm-os/iota`
- status: **ok** 
- README: 3272 bytes, sha 345999280406c0a7
- latest release: v4.8.3 2026-07-27T14:46:55Z
- last commit: 2026-07-27T14:46:52Z
- scoring-related commit: (none) 

## Resources

- min_compute.yml present: False  |  unmodified template: False
- required: unknown (~[UNKNOWN] GB VRAM)  |  basis: **no evidence**
- cheapest satisfying machine: rtx4090 at 8.2192 USD/day  <- ASSUMED default box; no hardware evidence was found, so the margin below is indicative only
- net margin: 1977.8667 USD/day  |  payback on registration: 0.0 days

## Score

- gate: **OK** 
- score: 30.7 (rank 38), confidence 0.6 - hardware requirement unknown; income rests on 2 competitive miners (n<=2: not a distribution)
- components: income 29.98 / freshness 0.0 / resource 11.25 / registration 10.0
- freshness basis: no challenge change on record

## On-chain description

> The world's first permissionless pipeline parallel training architecture

## README excerpt (evidence for the brief)

```markdown
<div align="center">

# IOTA

</div>

**I**ncentivized **O**rchestrated **T**raining **A**rchitecture (IOTA) is a framework for pretraining large language models across a network of heterogeneous, unreliable, permissionless and token incentivized machines. IOTA employs a data- and pipeline-parallel architecture to accelerate training and reduce hardware requirements for participants.

<div align="center">

<a href="https://iota.macrocosmos.ai">
  <img src="./docs/assets/iota-page.png" alt="iota" width="600"/>
</a>

</div>

## **Overview**

- The orchestrator distributes model layers across heterogeneous miners and streams activations between them.
- All network communication is mediated via the orchestrator, and a shared S3 bucket is used to store activations and layer weights.
- Miners compete to process as many activations as possible in the training stage.
- Miners periodically upload their local weights and merge their activations using a variant of Butterfly All-Reduce.
- Validators spot-check miners to ensure that work was performed as required.

For a more comprehensive overview, please refer to our technical paper [here](https://www.macrocosmos.ai/research/iota_primer.pdf). You can also find the report on [ArXiv](https://arxiv.org/abs/2507.17766)

<div align="center">
    <a href="https://www.macrocosmos.ai/research/iota_primer.pdf">
    <img src="./docs/assets/iota-paper-page.png" alt="iota" width="600"/>
    </a>
</div>

## Current Run Information

- **1.5B parameter** Llama-inspired architecture with uninterrupted residual flow (see paper for details)
- **3 layers**, breaking the model into 3 distinct training sections (1 head, 1 tail, 1 body)

## Future Run Information

1. Scaling the system to 15B, 50B, and 100B models
2. More advanced compression techniques to speed up training

## Comprehensive Dashboard

Visualizing the state of the network, the number of miners, layers, and general metrics is paramount to understanding the training process. We provide a comprehensive dashboard [here](https://iota.macrocosmos.ai/dashboard/mainnet).

<div align="center">
    <a href="https://iota.macrocosmos.ai/dashboard/mainnet">
    <img src="./docs/assets/iota-dashboard.png" alt="iota" width="600"/>
    </a>
</div>

## Installation

1. First install uv (<https://docs.astral.sh/uv/>)
2. Run `bash setup.sh` and choose Miner or Validator
3. Configure your `.env` file

## Additional Miner Documentation

Running the miner is as easy as `bash ./start_miner.sh`. For more information, reference [the official miner docs](https://docs.macrocosmos.ai/subnets/subnet-9-pre-training/subnet-9-iota-mining-setup-guide).

Use PM2 to run the miner in the background: `pm2 start pm2/miner.config.js`

## Additional Validation Documentation

Running the validator `./start_validator.sh`. For more information, reference [the official validator docs](https://docs.macrocosmos.ai/subnets/subnet-9-pre-training/subnet-9-validating)

Use PM2 to run the validator in the background: `pm2 start pm2/validator.config.js`

## Compute Requirements

The runs are currently in bfloat16, resulting in a total footprint of ~2GB for a 1B parameter model. As such, we recommend:

1. Cuda GPU with >= 16GB VRAM (RTX 4090, for example).
2. Ubuntu 22.04 (Jammy)

```
