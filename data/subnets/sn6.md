# sn6 - Numinous (ζ)

snapshot_utc: 2026-11-28T17:49:50Z  |  block: 9607010  |  row_status: ok

## Chain row

- miner_burn: **0.0**
- registration cost: 0.2 TAO (36.128 USD), open=True
- tempo: 360.0  |  max_uids: 256  |  active: 186  |  free: 0
- subnet age: 887.1 days  |  registered at block 3219949
- weights_version: 4000  |  mechanisms: 1

## Income (miner side)

- **competitive_miner_usd_day: 34.96018189422316** (uid 49) <- the only figure quotable as achievable
- median_miner_usd_day: 0.031186602938646883
- top_miner_usd_day: 118.08807202718644 (uid 237, owner=False, validator_permitted=True) <- NOT achievable if owner or permitted

## Incentive structure (display only - never scored)

- earners: 173  |  gini: 0.8942504340007513  |  top1_share: 0.11571548628619452  |  top10_share: 0.6218351287340514
- owner_incentive_share: 0.0 (independent check on miner_burn; disagreement 0.0)

## Repository

- on-chain URL: `https://github.com/numinouslabs/numinous`
- resolved URL: `https://github.com/numinouslabs/numinous`
- status: **ok** 
- README: 4156 bytes, sha 3992d3e5b591a253
- latest release: (none) 
- last commit: 2026-11-26T18:58:59Z
- scoring-related commit: Reference the WorldReasoner paper in the reasoning scoring doc 2026-09-18T10:47:07Z

## Resources

- min_compute.yml present: False  |  unmodified template: False
- required: unknown (~[UNKNOWN] GB VRAM)  |  basis: **no evidence**
- cheapest satisfying machine: rtx4090 at 8.2192 USD/day  <- ASSUMED default box; no hardware evidence was found, so the margin below is indicative only
- net margin: -8.188 USD/day  |  payback on registration: [UNKNOWN] days

## Score

- gate: **OK** 
- score: 39.3 (rank 51), confidence 0.85 - hardware requirement unknown
- components: income 0.0 / freshness 35.0 / resource 11.25 / registration 0.0
- freshness basis: README_TASK_DIFF 1.7d ago

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

Numinous (Subnet 6) is a **graph forecasting** subnet. It forecasts how a network of entities and their relationships will change: who will invest in, supply, partner with, acquire, attack or negotiate with whom, and when.

The Numinous backend builds a **knowledge graph** of entities and their relationships from the news. Every day the subnet asks questions about entities in the graph, and miners answer each question with a bundle of statements about relationships that will appear next, each with the chance it first appears on each of the next 30 days. A statement is judged correct when the news shows it happened after the question's deadline.

The key principles of the subnet are:

  * **Verifiable:** every forecast is sealed before the deadline, judged against public news, and scored with a fixed formula that any validator can recompute.
  * **Forward-looking:** only new developments count. A statement that repeats what the graph already knew earns nothing.

-----

## 🏗 System Architecture

Every day follows the same cycle: **Questions → Sealed forecasts → Opening → Judging → Scoring → Weight setting.**

### Key Components

  * **The knowledge graph:** entities and their relationships, built from the news by the Numinous backend.
  * **`numi`:** the miners' command line tool to read the open round and the graph, and to seal, sign and send forecasts.
  * **The judge:** checks every statement against the news reported after the deadline.
  * **Validators:** check every forecast against its hash and signature, score every miner, and set weights.

📖 **[Read how the system works](docs/miner-setup.md#system-components)**

-----

## ⚠️ Rules & Scoring

### Rules

1.  **Rounds:** a new round of questions is published every day and accepts forecasts until its deadline.
2.  **One forecast per question:** the last one sent before the deadline counts. Each of its statements names the subject the question asks about, and says when it expects the development: a chance for each of the next 30 days, and for "not within 30 days".
3.  **Sealed until the deadline:** nobody can read a forecast before the deadline, the backend included.
4.  **New developments only:** a statement comes true through news reported after the deadline, until the horizon ends 30 days later.

### Scoring

Every statement is scored against the **house's** own forecast of the same statement: a miner earns points for calling whether and when it appears better than the house, and loses points for doing worse. A statement that does not appear can lose points but never earn them, and a news event that several miners are paid for is shared among them. Each bundle earns `points / √statements` in **credits**. A news event pays a miner once: repeats are voided. Validators compute credits daily at 15:00 UTC, and weights **extremise quadratically among the top 25** (98% by credits squared) with **2%** spread by rank over every miner with credits.

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
