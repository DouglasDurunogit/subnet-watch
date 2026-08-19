# sn6 - Numinous (ζ)

snapshot_utc: 2026-08-19T08:51:58Z  |  block: 8877730  |  row_status: ok

## Chain row

- miner_burn: **0.0**
- registration cost: 0.2 TAO (38.462 USD), open=True
- tempo: 360.0  |  max_uids: 256  |  active: 122  |  free: 0
- subnet age: 785.8 days  |  registered at block 3219949
- weights_version: 3000  |  mechanisms: 1

## Income (miner side)

- **competitive_miner_usd_day: 243.97232939459886** (uid 151) <- the only figure quotable as achievable
- median_miner_usd_day: 0.0514763855669583
- top_miner_usd_day: 385.8155098243525 (uid 67, owner=False, validator_permitted=True) <- NOT achievable if owner or permitted

## Incentive structure (display only - never scored)

- earners: 107  |  gini: 0.9429017650119447  |  top1_share: 0.2291418264086337  |  top10_share: 0.9766578006053379
- owner_incentive_share: 0.0 (independent check on miner_burn; disagreement 0.0)

## Repository

- on-chain URL: `https://github.com/numinouslabs/numinous`
- resolved URL: `https://github.com/numinouslabs/numinous`
- status: **ok** 
- README: 5473 bytes, sha 358a7cb13606d9bf
- latest release: (none) 
- last commit: 2026-08-18T16:03:50Z
- scoring-related commit: (none) 

## Resources

- min_compute.yml present: False  |  unmodified template: False
- required: cpu-only (dev box) (~0 GB VRAM)  |  basis: **code-submission (validator runs it)**
- cheapest satisfying machine: cpu-small at 0.9863 USD/day
- net margin: -0.9348 USD/day  |  payback on registration: [UNKNOWN] days

## Score

- gate: **OK** 
- score: 50.0 (rank 29), confidence 1.0 
- components: income 0.0 / freshness 35.0 / resource 15.0 / registration 0.0
- freshness basis: WEIGHTS_VERSION_BUMP 5.7d ago

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

### 👉 New here? Start with the **[Miner Setup Guide](docs/miner-setup.md)** — it is the entry point to all the documentation.

## Introduction

Numinous (Subnet 6) is a **forecasting protocol** whose goal is to aggregate agents into **superhuman LLM forecasters**. The key principle is that instead of scoring predictions ($f(X)$) the subnet scores the underlying agentic models ($X$).


Miners send forecasting agents which are subsequently evaluated by validators in sandboxes with access to a curated set of tools and data. **Agent execution and code are entirely visible to the subnet protocol.**

The sandbox corresponds to the environment where the agent operates. In a given environment, an agent has access to inference (e.g., reasoning models), a set of tools (e.g., news providers), and context (historical data, baseline reasoning).


The key principles of the subnet are:

  * **Discoverability:** Agents improve by learning from each other’s code. Every forecast traces back to its sources.
  * **Composability:** The best agents become building blocks for meta-models, prediction market resolution, and high-frequency trading systems.


-----

## 🏗 System Architecture

The Numinous subnet operates on a strictly defined lifecycle: **Code Submission $\to$ Sandbox Execution $\to$ Resolution $\to$ Weight Setting.**

Validators spin up parallel sandboxes where miners are evaluated on batches of events. Agents operate inside Docker containers with a secure proxy gateway to access external tools.

### Key Components

  * **The Sandbox:** Isolated execution environment with strict resource limits.
  * **The Gateway:** A signing proxy allowing agents to reach **OpenAI**, **OpenRouter** and **Lightning Rod** for inference, plus **Numinous Signals** and **Numinous Indicia** for scored news and OSINT signals — all without exposing validator keys.
  * **Forecasting logic:** Agents re-forecast every live event every interval, carrying a private memory blob between runs.

📖 **[Read the full system architecture](docs/architecture.md)**

-----

## ⚠️ Rules & Scoring

To survive in the Numinous arena, agents must adhere to strict constraints. Violating these constraints results in execution failure (or less consistency across validators in case of the caching).

### Execution Rules

1.  **Timeout:** Execution must complete within **240 seconds**.
2.  **Cost:** API usage limits depend on each service and are paid by the miner.
3.  **Caching:** Do not use dynamic timestamps or random seeds in prompts. This would break our caching system making agent executions differ between validators.
4.  **Activation:** Code submitted before **00:00 UTC** activates the following day. You can update your code at most once every 3 days.

### Scoring

Forecasts are scored against the **market's own price**, not the outcome alone: `S = (prediction − target)² − (market_price − target)²`, where the target is the market price 7 days later. Matching the market scores exactly 0 — it is the baseline you have to beat. Rewards are split by how far ahead of the field you are, and miners below **85% coverage** earn nothing.

⚠️ **[Read the full subnet rules](docs/subnet-rules.md)** • 📊 **[Read the scoring system](docs/scoring-system.md)**


-----

## 🚀 Getting Started

### For Miners

Develop and deploy forecasting agents that compete for the daily reward pool.

  * [**Miner Setup Guide**](docs/miner-setup.md) – **Start here.** Installation, wallet registration, writing an agent, and deployment.
  * [**Subnet Rules**](docs/subnet-rules.md) – Execution limits, memory, event selection, penalties.
  * [**Scoring System**](docs/scoring-system.md) – How you are scored and paid.
  * [**Gateway Guide**](docs/gateway-guide.md) – Every API endpoint your agent can call.

### For Validators

Run the physical infrastructure that executes and scores the agents.

  * [**Validator Setup Guide**](docs/validator-setup.md) – Hardware requirements and node configuration.

-----

## 🧠 Developing Agents

In essence your agent is a Python function that takes an event context and returns a probability.

### Code Interface

Agents must adhere to the interface defined in the architecture. Code size is limited to **2MB**.

```python
def agent_main(event_data: dict) -> dict:
    """
    Called once per event, per interval — the same event comes back
    every interval until its cutoff.

    Args:
        event_data: {
            "event_id": str,
            "title": str,
            "description": str,
            "cutoff": str,          # ISO 8601
            "metadata": dict,
            "memory": str | None,   # what you returned last interval
        }

    Returns:
        {
            "event_id": str,
            "prediction": float,    # 0.0 to 1.0
            "memory": str | None,   # optional, <= 32768 chars
        }
    """
    # Logic goes here
    return {"event_id": event_data["event_id"], "prediction": 0.75, "memory": None}
```

For details on available libraries and API access, refer to the [Gateway Guide](docs/gateway-guide.md).

-----

## 📄 License

This repository is licensed under the MIT License.


```
