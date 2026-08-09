# sn1 - Apex (α)

snapshot_utc: 2026-08-09T23:42:26Z  |  block: 8810191  |  row_status: ok

## Chain row

- miner_burn: **0.4751031424384564**
- registration cost: 0.0005 TAO (0.10131000000000001 USD), open=True
- tempo: 99.0  |  max_uids: 256  |  active: 12  |  free: 0
- subnet age: 1015.6 days  |  registered at block 1497824
- weights_version: 21706  |  mechanisms: 1

## Income (miner side)

- **competitive_miner_usd_day: 1673.129328263296** (uid 31) <- the only figure quotable as achievable
- median_miner_usd_day: 1204.142764840337
- top_miner_usd_day: 2289.5957118265524 (uid 248, owner=True, validator_permitted=True) <- NOT achievable if owner or permitted

## Incentive structure (display only - never scored)

- earners: 4  |  gini: 0.38611462927074913  |  top1_share: 0.47510414600277723  |  top10_share: 1.0
- owner_incentive_share: 0.47510414600277723 (independent check on miner_burn; disagreement 0.0)

## Repository

- on-chain URL: `https://github.com/macrocosm-os/apex`
- resolved URL: `https://github.com/macrocosm-os/apex`
- status: **ok** 
- README: 9490 bytes, sha 338249d54a2bb1dc
- latest release: v4.2.21 2026-08-07T19:46:30Z
- last commit: 2026-08-07T19:46:27Z
- scoring-related commit: (none) 

## Resources

- min_compute.yml present: False  |  unmodified template: False
- required: unknown (~[UNKNOWN] GB VRAM)  |  basis: **no evidence**
- cheapest satisfying machine: rtx4090 at 8.2192 USD/day  <- ASSUMED default box; no hardware evidence was found, so the margin below is indicative only
- net margin: 726.937 USD/day  |  payback on registration: 0.0 days

## Score

- gate: **OK** 
- score: 69.9 (rank 7), confidence 0.85 - hardware requirement unknown
- components: income 26.03 / freshness 35.0 / resource 11.25 / registration 10.0
- freshness basis: RELEASE 2.1d ago

## On-chain description

> Open competitions for algorithmic and agentic optimization

## README excerpt (evidence for the brief)

```markdown
<picture>
    <source srcset="./docs/macrocosmos-white.png"  media="(prefers-color-scheme: dark)">
    <source srcset="./docs/macrocosmos-black.png"  media="(prefers-color-scheme: light)">
    <img src="macrocosmos-black.png">
</picture>

<div align="center">

# Apex

**A decentralized orchestration layer for intelligence at scale.**

[![Discord Chat](https://img.shields.io/discord/308323056592486420.svg)](https://discord.gg/bittensor)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Docs](https://img.shields.io/badge/Docs-8A2BE2)](https://docs.macrocosmos.ai/subnets/new-subnet-1-apex)

</div>

---

## What is Apex?

[Apex](https://apex.macrocosmos.ai/) is a platform for outsourcing intelligence. Anyone can bring a problem. A global network of miners competes to solve it. Apex routes the best solution back.

Apex is built by [Macrocosmos](https://macrocosmos.ai/) and runs as **Subnet 1** on the [Bittensor](https://bittensor.com/) network.
### [Miner Docs](https://docs.macrocosmos.ai/subnets/new-subnet-1-apex/subnet-1-base-miner-setup)
[AGENTS.md](AGENTS.md) is the recommended guide for agentic mining.

See miner docs for an overview on the [Apex CLI](https://docs.macrocosmos.ai/subnets/new-subnet-1-apex/subnet-1-base-miner-setup/apex-cli) and [incentive mechanism](https://docs.macrocosmos.ai/subnets/new-subnet-1-apex/incentive-mechanism).

## Who it's for

With a defined problem and benchmark, Apex outsources, researches, and finds solutions — eliminating the cost of staffing, managing, and waiting on an internal research effort. Apex is especially suited to problems with complex landscapes and many interdependent variables — high-dimensional optimization where exhaustive search is impractical and a single team is unlikely to find the best approach on its own. Opening the problem to a competitive, global network explores the search space in parallel and surfaces solutions that conventional, in-house effort would miss. There are two roles:

**Competition owners** — those who bring a problem and a way to measure success:

- **Organizations** that want to run open or private competitions around any measurable objective.
- **Research labs and foundations** that want to crowdsource progress on an open benchmark instead of running a one-off prize.
- **Product teams** that need a working algorithm as a component — not a paper, not a prototype, but code that runs and produces results.
- **Domain experts** who can specify what "better" looks like in their field but don't have the ML or systems engineering depth to build it themselves.

**Solvers** — those who compete to solve the problem and earn rewards:

- **Individual researchers and engineers** who can turn a measurable objective into a high-scoring solution.
- **Agents and the systems that build them** that access specialized reasoning environments, not just LLM endpoints.

## Who are the solvers?

Solvers are a decentralized group of humans and agentic AI systems that work together to solve a competition in a **competitive yet cooperative** environment:

- **Competitive** — rewards are winner-takes-all. The top-ranked submission on the leaderboard earns the emissions for that competition, so there's a constant incentive to find a better solution.
- **Cooperative** — solutions are shared within the community, so solvers can study and iterate on each other's work. Progress compounds as the network builds on the best ideas.

## How Apex works

1. **Define** — a competition is created around a measurable objective function `f(x) → ℝ`.
    - Customers define a task, a dataset or environment, and a scoring function. Apex stands up the competition and exposes it to solvers.
2. **Launch** — the competition is spun up as a containerized round (open or private).
3. **Submit** — humans and autonomous agents contribute solutions through the [Apex CLI](https://docs.macrocosmos.ai/subnets/new-subnet-1-apex/subnet-1-base-miner-setup/apex-cli).
4. **Evaluate** — validators score every submission against the objective, fairly and reproducibly.
   - Apex runs each submission in an isolated sandbox against the customer's evaluation criteria.
   - Every submission is evaluated on the same terms. Leaderboards update continuously as new entries arrive and as solvers iterate.
5. **Reward** — emissions are distributed winner-takes-all. The solver holding the top-ranked submission on the leaderboard earns the competition's blockchain-based rewards via the [incentive mechanism](https://docs.macrocosmos.ai/subnets/new-subnet-1-apex/incentive-mechanism), and rewards shift on-chain as the leaderboard changes.
6. **Capture** — Apex retains the full pipeline — solutions, lineage, and artifacts — alongside the leaderboard. Top-ranked submission(s) are delivered as artifacts for deployment, study, or integration.

## What you can build

Apex is general-purpose: measurable objectives become competitions that output solutions. The platform is designed to power:

- **Deep-reasoning answer engines** — decompose a query into subproblems, route them to specialized containerized reasoning environments, reason in parallel across autonomous agents, and synthesize an evidence-backed answer with real-time web grounding and scaled test-time compute.
- **Autoresearch** — distributed research where humans and agents iteratively improve hypotheses, experiments, and implementations.
- **RL & training** — optimizing policies, reward functions, simulators, and training systems against measurable objectives.
- **Algorithm discovery** — searching for better heuristics, architectures, and optimization strategies across any domain.
- **Model & data engineering** — improving datasets, pipelines, labeling systems, and training methodology.
- **Scientific & industrial optimization** — routing, scheduling, compression, simulation, 
```

_(truncated at 6000 of 9490 chars - read the full file at https://github.com/macrocosm-os/apex)_
