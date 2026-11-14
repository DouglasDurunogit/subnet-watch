# sn5 - Hone (ε)

snapshot_utc: 2026-11-14T08:54:42Z  |  block: 9503561  |  row_status: ok

## Chain row

- miner_burn: **0.0**
- registration cost: 0.297207197 TAO (61.59321950628 USD), open=True
- tempo: 360.0  |  max_uids: 256  |  active: 254  |  free: 0
- subnet age: 973.9 days  |  registered at block 2491604
- weights_version: 803  |  mechanisms: 1

## Income (miner side)

- **competitive_miner_usd_day: 53.34144822232756** (uid 60) <- the only figure quotable as achievable
- median_miner_usd_day: 28.783822167080395
- top_miner_usd_day: 53.34144822232756 (uid 60, owner=False, validator_permitted=False) <- NOT achievable if owner or permitted

## Incentive structure (display only - never scored)

- earners: 243  |  gini: 0.19803694217895074  |  top1_share: 0.007157307503678274  |  top10_share: 0.0695806768023541
- owner_incentive_share: 0.0 (independent check on miner_burn; disagreement 0.0)

## Repository

- on-chain URL: `https://github.com/hone-subnet-org/hone-subnet`
- resolved URL: `https://github.com/hone-subnet-org/hone-subnet`
- status: **ok** 
- README: 5705 bytes, sha 0671b9a26a219d80
- latest release: (none) 
- last commit: 2026-11-14T00:46:59Z
- scoring-related commit: Lengthen the new-miner ramp to 30 observations 2026-11-14T00:45:57Z

## Resources

- min_compute.yml present: False  |  unmodified template: False
- required: unknown (~[UNKNOWN] GB VRAM)  |  basis: **no evidence**
- cheapest satisfying machine: rtx4090 at 8.2192 USD/day  <- ASSUMED default box; no hardware evidence was found, so the margin below is indicative only
- net margin: 20.5646 USD/day  |  payback on registration: 3.0 days

## Score

- gate: **OK** 
- score: 57.3 (rank 20), confidence 0.85 - hardware requirement unknown
- components: income 12.13 / freshness 35.0 / resource 11.25 / registration 9.0
- freshness basis: SCORING_COMMIT 0.3d ago

## On-chain description

> Hone (SN5) is an RLVR subnet: reinforcement learning from verifiable rewards. Miners are paid to solve real software-engineering tasks- repository patches submitted as git diffs and terminal tasks submitted as scripts with full trajectories. Validators lease tasks from a problem server and grade eve

## README excerpt (evidence for the brief)

```markdown
# RLVR subnet

This repository contains the public validator for Bittensor Finney NETUID 5.
Validators lease V3 repository or terminal tasks, send the server-assigned task
to miners, commit the signed responses, retrieve the verifier, grade each miner
in an isolated Docker workspace, and submit locally calculated weights.

## Run a validator

Requirements:

- Linux with Python 3.10–3.12
- Docker with the daemon running
- an ordinary user in the `docker` group to run everything as: the validator
  refuses to run as root, since it runs miner code in containers
- at least 25 GB free on the filesystem holding `data/`: grading refuses to
  start a round with less than about 20 GB free, since each of the two
  concurrent gradings may use a 10 GB workspace
- at least 12 GB of RAM: each concurrent grading may use 4 GB, plus the
  validator itself and Docker
- a registered validator hotkey on Finney NETUID 5
- a system clock synchronized with NTP
- a direct route to miners and the problem server: the validator's HTTP
  client ignores `HTTP_PROXY`, `HTTPS_PROXY` and `ALL_PROXY`. It sends a TCP
  keepalive probe every minute while a miner works, to help keep slow
  answers from being dropped by idle-connection timeouts on the path

From the repository root:

```bash
./setup_validator.sh --wallet-name YOUR_WALLET --wallet-hotkey YOUR_HOTKEY
./start_validator.sh
```

Setup creates `.venv` and a four-line `.env`, installs dependencies, pulls and
checks the release-pinned V3 sandbox image, and verifies the problem service
and local clock. If wallet arguments are omitted, set `WALLET_NAME` and
`WALLET_HOTKEY` in `.env`. Nothing else is required; `.env.example` lists the
optional settings.

Dispatch, grading, scoring, cadence, resource limits, sandbox image, and owner
burn are fixed in release policy. Operators do not configure them in `.env`.
The owner burn share is 0%. The one sizing choice is how many miners are graded
at the same time, `VALIDATOR_GRADING_CONCURRENCY`. Unset, the validator sizes it
from the host at startup: one per two CPUs, one per 4 GB of RAM after 4 GB for
the system, one per 10 GB of free disk after 2 GB, at most 16, and prints the
result. Each concurrent grading may use a full sandbox memory limit and a copy
of the task workspace on disk, so set it higher only on a machine with the
memory and disk to match. Byte-identical submissions in a round are graded
once, so the number of distinct answers, not the number of miners, sets the
grading time.

The validator stores its scoring window in `data/validator_scores.json`.
Preserve that file across restarts.

Scoring is pooled across validators. After each round the validator posts
its signed verdicts to the problem server's ledger and reads the other
validators' signed rounds back. A round counts when its signature verifies
and the signing validator is validating and holds at least 0.75% of stake;
every admitted round counts equally, and one validator contributes at most
50 rounds per miner inside a four-day window. A miner's score is the
plain mean of this validator's own observations and the admitted ones, so a
validator that cannot reach the ledger scores exactly as before. The pool is
kept in `data/ledger_pool.json` and is rebuilt from the server if lost.
A round counts once: a round already held, or one numbered far below the
newest held from its validator, is refused however it is dated.
Rounds waiting for the server, and the validator's round counter, live in
`data/feedback-outbox/`: keep that directory with the data directory. A
round the server has not taken by the end of its grading window is dropped,
and if the counter is lost the server refuses rounds until the numbering
passes what it already holds.

## Protocol

```text
problem server -> workspace and public task -> validator -> selected miners
problem server <- exact signed responses ---- validator <- artifact references
problem server -> verifier after commit ----- validator
                                              |
                                              v
                                   isolated per-miner grading
                                              |
                                              v
                                     local scores and weights
```

Miners return either a Git unified diff or a Bash script plus a canonical
trajectory. The verifier is unavailable until the response set is durably
committed. Candidate code cannot access verifier files, expected outputs, other
miners' workspaces, the network, or the trusted result record. Infrastructure
or protocol failures abandon the round without changing miner scores.

The complete V3 contract is documented in [`docs/V3_TASKS.md`](docs/V3_TASKS.md).
Miners can grade a patch or a script against a real retired task with `scripts/try_task.py`; see [`docs/DEMO_MINER.md`](docs/DEMO_MINER.md).

## Demo miner

The included demo miner is a protocol reference backed by Amazon Bedrock Chat
Completions. It requires its own Bedrock API key; validators do not need one.
See [`docs/DEMO_MINER.md`](docs/DEMO_MINER.md).

## Development

```bash
. .venv/bin/activate
pip install -e '.[chain,dev]'
pytest -q
```

V3 sandbox throughput can be measured with
[`scripts/benchmark_v3_supervisor.py`](scripts/benchmark_v3_supervisor.py).
Problem construction and private task provenance are not part of this
repository.

## Repository contents

- `rlvr/v3/`: V3 wire models, artifact handling, grading, and orchestration.
- `rlvr/neurons/`: validator lifecycle, signed miner transport, and demo miner.
- `rlvr/scoring/`: local score history and weight calculation.
- `docker/polyglot-sandbox/`: reproducible V3 grading image.

```
