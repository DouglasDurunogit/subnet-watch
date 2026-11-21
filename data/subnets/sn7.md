# sn7 - Allways (η)

snapshot_utc: 2026-11-21T00:54:23Z  |  block: 9551553  |  row_status: ok

## Chain row

- miner_burn: **0.0**
- registration cost: 0.15 TAO (27.0945 USD), open=True
- tempo: 360.0  |  max_uids: 256  |  active: 13  |  free: 0
- subnet age: 961.6 days  |  registered at block 2627691
- weights_version: 319  |  mechanisms: 1

## Income (miner side)

- **competitive_miner_usd_day: [UNKNOWN]** (uid [UNKNOWN]) <- the only figure quotable as achievable
- median_miner_usd_day: 1186.5629558845098
- top_miner_usd_day: 1186.5629558845098 (uid 78, owner=False, validator_permitted=True) <- NOT achievable if owner or permitted

## Incentive structure (display only - never scored)

- earners: 1  |  gini: 0.0  |  top1_share: 1.0  |  top10_share: 1.0
- owner_incentive_share: 0.0 (independent check on miner_burn; disagreement 0.0)

## Repository

- on-chain URL: `https://github.com/entrius/allways`
- resolved URL: `https://github.com/entrius/allways`
- status: **ok** 
- README: 3427 bytes, sha d73b7f4f20c2f067
- latest release: release-20261117-160316 2026-11-17T16:01:21Z
- last commit: 2026-11-17T16:01:21Z
- scoring-related commit: Drop VALIDATOR_MODE: the validator always sets weights unless told no… 2026-11-17T16:01:21Z

## Resources

- min_compute.yml present: False  |  unmodified template: False
- required: unknown (~[UNKNOWN] GB VRAM)  |  basis: **no evidence**
- cheapest satisfying machine: rtx4090 at 8.2192 USD/day  <- ASSUMED default box; no hardware evidence was found, so the margin below is indicative only
- net margin: [UNKNOWN] USD/day  |  payback on registration: [UNKNOWN] days

## Score

- gate: **OK** 
- score: 39.3 (rank 56), confidence 0.85 - hardware requirement unknown
- components: income 0.0 / freshness 35.0 / resource 11.25 / registration 0.0
- freshness basis: RELEASE 3.3d ago

## On-chain description

> universal transaction layer

## README excerpt (evidence for the brief)

```markdown
# Allways

Bittensor Subnet 7 (SN7).

**Links:** [Website](https://all-ways.io) · [Docs](https://docs.all-ways.io)

## What this repository is now

This repository holds the SN7 validator and nothing else. Every epoch the validator puts 100% of its
weight on one pinned UID, the Allways treasury miner. It does no scoring, serves no axon, and talks to
no chain other than Bittensor.

The previous code (cross-chain swap miner and validator, the `alw` CLI, the smart contracts) is
preserved on the [`allways-old`](https://github.com/entrius/allways/tree/allways-old) branch.

## How the target is chosen

`allways/constants.py` pins the target:

| Constant          | Meaning                                                                     |
| ----------------- | --------------------------------------------------------------------------- |
| `NETUID_FINNEY`   | The subnet the treasury constants are pinned for (7)                        |
| `TREASURY_UID`    | The UID that receives the full weight (78). `None` burns everything instead |
| `TREASURY_HOTKEY` | The hotkey expected at that UID. A guard, not a lookup                      |

On every pass the validator syncs the metagraph and sets weights `[1.0]` on:

- `TREASURY_UID`, when the netuid is 7 and the UID is set, in range, and held by `TREASURY_HOTKEY`
- otherwise the UID where the subnet owner hotkey is registered, read from the chain on each pass.
  Weight placed there is burned. A `TREASURY FALLBACK` warning says why (another netuid, unset, out
  of range, or hotkey mismatch)
- nothing at all, with a `NO WEIGHTS SET` error, if the treasury cannot be used and the subnet owner
  hotkey is not registered on the subnet. There is no hard-coded fallback UID

The hotkey check stops emissions going to a stranger if the UID slot is ever recycled.

Weights are set once the validator's last update is more than `--neuron.epoch_length` blocks old
(default 150), and never more often than the subnet's `weights_rate_limit`. Commit-reveal is handled
by the Bittensor SDK. A validator without a validator permit logs an error and submits nothing. Any
chain error drops the connection and reconnects on the next pass.

## Running a validator

Requirements: a hotkey registered on SN7 with a validator permit. No GPU, and no open ports.

### Docker (recommended)

```bash
cp .env.example .env          # set WALLET_NAME, HOTKEY_NAME, WALLET_PATH
docker compose -f docker-compose.vali.yml up -d
docker logs -f aw-vali
```

The compose file runs `entrius/allways:latest` with watchtower, so the validator updates itself when
a new image is published. An `.env` and compose file from the previous validator keep working:
variables and flags that no longer apply are ignored.

### From source

```bash
uv sync
uv run python neurons/validator.py --netuid 7 --subtensor.network finney \
  --wallet.name <coldkey> --wallet.hotkey <hotkey> --logging.info
```

### Check without submitting

```bash
uv run python neurons/validator.py --netuid 7 --subtensor.network finney --dry-run
```

`--dry-run` needs no wallet. It logs the weights that would be set and exits (exit code 1 if there
is no safe target). `--neuron.disable_set_weights` runs the normal loop but only logs.

## Development

```bash
uv sync
uv run ruff check . && uv run ruff format --check .
uv run pytest tests/ -q
```

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT, see [LICENSE](LICENSE).

```
