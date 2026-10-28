# sn6 - Numinous (ζ)

snapshot_utc: 2026-10-28T08:21:19Z  |  block: 9381007  |  row_status: ok

## Chain row

- miner_burn: **0.0**
- registration cost: 0.237398782 TAO (60.97112918106 USD), open=True
- tempo: 360.0  |  max_uids: 256  |  active: 45  |  free: 0
- subnet age: 855.7 days  |  registered at block 3219949
- weights_version: 4000  |  mechanisms: 1

## Income (miner side)

- **competitive_miner_usd_day: 175.71133791144365** (uid 120) <- the only figure quotable as achievable
- median_miner_usd_day: 57.96060184757817
- top_miner_usd_day: 175.71133791144365 (uid 120, owner=False, validator_permitted=False) <- NOT achievable if owner or permitted

## Incentive structure (display only - never scored)

- earners: 30  |  gini: 0.4269455594389582  |  top1_share: 0.10553868225454434  |  top10_share: 0.6325910776697546
- owner_incentive_share: 0.0 (independent check on miner_burn; disagreement 0.0)

## Repository

- on-chain URL: `https://github.com/numinouslabs/numinous`
- resolved URL: `https://github.com/numinouslabs/numinous`
- status: **ok** 
- README: 3648 bytes, sha 9502a1ace6b0e8be
- latest release: (none) 
- last commit: 2026-10-22T13:33:46Z
- scoring-related commit: Reference the WorldReasoner paper in the reasoning scoring doc 2026-09-18T10:47:07Z

## Resources

- min_compute.yml present: False  |  unmodified template: False
- required: unknown (~[UNKNOWN] GB VRAM)  |  basis: **no evidence**
- cheapest satisfying machine: rtx4090 at 8.2192 USD/day  <- ASSUMED default box; no hardware evidence was found, so the margin below is indicative only
- net margin: 49.7414 USD/day  |  payback on registration: 1.23 days

## Score

- gate: **OK** 
- score: 60.6 (rank 20), confidence 0.85 - hardware requirement unknown
- components: income 15.51 / freshness 35.0 / resource 11.25 / registration 9.59
- freshness basis: WEIGHTS_VERSION_BUMP 4.7d ago

## On-chain description

> Numinous is a forecasting protocol whose goal is to aggregate agents into superhuman LLM forecasters.

## README excerpt (evidence for the brief)

```markdown
<div align="center">

# **Numinous**



[Discord](https://discord.gg/qKPeYPc3) • [Dashboard](https://app.hex.tech/1644b22a-abe5-4113-9d5f-3ad05e4a8de7/app/Numinous-031erYRYSssIrH3W3KcyHg/latest) • [Website](https://numinouslabs.io/) • [Twitter](https://x.com/numinous_ai) •
[Network](https://taostats.io/subnets/6/chart)
---

</div>

### 👉 New here? Start with the **[Miner Setup Guide](docs/miner-setup.md)**, the entry point to all the documentation.

## Introduction

Numinous (Subnet 6) is a **graph forecasting** subnet. It forecasts how the network of companies and their relationships will change: who will invest in, supply, partner with, acquire or compete with whom.

The Numinous backend builds a **knowledge graph** of companies and their relationships from the news. Every day the subnet asks questions about companies, and miners answer each question with a bundle of statements about relationships that will appear next. A statement is judged correct when the news shows it happened after the question's deadline.

The key principles of the subnet are:

  * **Verifiable:** every forecast is sealed before the deadline, judged against public news, and scored with a fixed formula that any validator can recompute.
  * **Forward-looking:** only new developments count. A statement that repeats what the graph already knew earns nothing.

-----

## 🏗 System Architecture

Every day follows the same cycle: **Questions → Sealed forecasts → Opening → Judging → Scoring → Weight setting.**

### Key Components

  * **The knowledge graph:** companies and their relationships, built from the news by the Numinous backend.
  * **`numi`:** the miners' command line tool to read the open round and the graph, and to seal, sign and send forecasts.
  * **The judge:** checks every statement against the news reported after the deadline.
  * **Validators:** check every forecast against its hash and signature, score every miner, and set weights.

📖 **[Read how the system works](docs/miner-setup.md#system-components)**

-----

## ⚠️ Rules & Scoring

### Rules

1.  **Rounds:** a new round of questions is published every day and accepts forecasts until its deadline.
2.  **One forecast per question:** the first one sent counts. Each of its statements names the company the question asks about.
3.  **Sealed until the deadline:** nobody can read a forecast before the deadline, the backend included.
4.  **New developments only:** a statement comes true through news reported after the deadline, until the round's horizon ends.

### Scoring

Each bundle earns `correct statements / √statements` in **credits**, counting statements judged correct in the last 30 days. A news event pays a miner once: repeats are voided. Validators compute credits daily at 15:00 UTC, and weights **extremise quadratically among the top 25** (98% by credits squared) with **2%** spread by rank over every miner with credits.

⚠️ **[Read the miner guide and rules](docs/miner-setup.md)** • 📊 **[Read the scoring system](docs/scoring-system.md)**


-----

## 🚀 Getting Started

### For Miners

Forecast the knowledge graph and compete for the daily reward pool.

  * [**Miner Setup Guide**](docs/miner-setup.md): **start here.** Installation, wallet registration and the `numi` forecasting loop.
  * [**Scoring System**](docs/scoring-system.md): how you are scored and how weights are set.

### For Validators

Check every forecast, score every miner and set weights. No special hardware needed.

  * [**Validator Setup Guide**](docs/validator-setup.md): requirements and node configuration.

-----

## 📄 License

This repository is licensed under the MIT License.

```
