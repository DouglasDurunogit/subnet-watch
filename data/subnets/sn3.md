# sn3 - Teutonic (γ)

snapshot_utc: 2026-10-09T06:48:15Z  |  block: 9243824  |  row_status: ok

## Chain row

- miner_burn: **0.0**
- registration cost: 0.999999999 TAO (276.03999972396 USD), open=True
- tempo: 360.0  |  max_uids: 256  |  active: 16  |  free: 0
- subnet age: 705.3 days  |  registered at block 4165565
- weights_version: 2000  |  mechanisms: 1

## Income (miner side)

- **competitive_miner_usd_day: 6274.191548275041** (uid 182) <- the only figure quotable as achievable
- median_miner_usd_day: 4182.581608936556
- top_miner_usd_day: 6274.191548275041 (uid 182, owner=False, validator_permitted=False) <- NOT achievable if owner or permitted

## Incentive structure (display only - never scored)

- earners: 5  |  gini: 0.1399987792223647  |  top1_share: 0.3000061038881768  |  top10_share: 1.0
- owner_incentive_share: 0.0 (independent check on miner_burn; disagreement 0.0)

## Repository

- on-chain URL: `https://github.com/unarbos/teutonic`
- resolved URL: `https://github.com/unarbos/teutonic`
- status: **ok** 
- README: 5093 bytes, sha fbca33fd060cacc2
- latest release: (none) 
- last commit: 2026-10-08T10:48:25Z
- scoring-related commit: Add competition dataset panel and update evaluation history layout 2026-10-08T10:48:25Z

## Resources

- min_compute.yml present: False  |  unmodified template: False
- required: unknown (~[UNKNOWN] GB VRAM)  |  basis: **no evidence**
- cheapest satisfying machine: rtx4090 at 8.2192 USD/day  <- ASSUMED default box; no hardware evidence was found, so the margin below is indicative only
- net margin: 3128.8766 USD/day  |  payback on registration: 0.09 days

## Score

- gate: **OK** 
- score: 74.8 (rank 2), confidence 0.85 - hardware requirement unknown
- components: income 31.79 / freshness 35.0 / resource 11.25 / registration 9.97
- freshness basis: SCORING_COMMIT 0.7d ago

## On-chain description

> Coordinated Learning

## README excerpt (evidence for the brief)

```markdown
# [Teutonic](https://teutonic.ai/)

[Teutonic](https://teutonic.ai/) is a king-of-the-hill pretraining system for Bittensor subnet 3.

Miners submit immutable model checkpoints. The validator verifies each
submission and sends the challenger and current king to a remote GPU evaluator
for paired cross-entropy scoring. A successful challenger becomes the new king,
and the validator updates subnet weights and publishes the resulting state.

## Miner CLI

Each hotkey can submit one model. Teutonic requires an Ed25519 hotkey because
the validator encrypts its temporary upload credentials to that hotkey.

### Install

Use Python 3.11 or newer. `btcli` must also be available on `PATH` if the
hotkey still needs to be registered on the subnet.

```bash
git clone https://github.com/unarbos/teutonic.git
cd teutonic

python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e '.[miner]'
```

Set the wallet and target subnet values used in the examples:

```bash
WALLET_PATH="$HOME/.bittensor/wallets"
WALLET_NAME=your-coldkey-wallet
HOTKEY_NAME=your-hotkey
NETWORK=finney
NETUID=3
```

Create a new Ed25519 hotkey if needed:

```bash
btcli wallet new-hotkey \
  --wallet-name "$WALLET_NAME" \
  --hotkey "$HOTKEY_NAME" \
  --wallet-path "$WALLET_PATH" \
  --crypto-type ed25519
```

Save the common wallet location:

```bash
teutonic-miner configure --wallet-path "$WALLET_PATH"
```

### Register and activate the mailbox

This command validates the Ed25519 hotkey, registers it on the subnet if
necessary, waits for its finalized UID, and commits its signed mailbox
activation. Subnet registration can spend TAO.

```bash
teutonic-miner register \
  --wallet-name "$WALLET_NAME" \
  --hotkey-name "$HOTKEY_NAME" \
  --network "$NETWORK" \
  --netuid "$NETUID"
```

Add `--check-only` to fail instead of paying for a missing subnet registration.
The active chain generation is read automatically from `chain.toml`.

Registration creates local state under
`.teutonic-miner/<hotkey-address>/registration.json` and selects the hotkey as
active. Inspect the saved state with:

```bash
teutonic-miner list
teutonic-miner status --hotkey "$HOTKEY_NAME"
```

### Retrieve upload authorization

Poll the public mailbox and decrypt the temporary, prefix-scoped R2
credentials:

```bash
teutonic-miner auth --hotkey "$HOTKEY_NAME"
```

The public mailbox URL is built in. The encrypted result is written locally as
`upload-auth.json` with mode `0600`. Never share or commit this file.

Credentials last seven days. While the registration remains eligible, the
controller renews them one day before expiry and replaces already-expired
credentials after an outage. The same hotkey and upload prefix are retained;
the expired secret and session token cannot be reused.

The current CLI discovers and decrypts the latest generation automatically.
`auth` refreshes the local file, and `upload` and `submit` retrieve current
credentials before uploading. Update older CLI installations to use automatic
discovery; `auth --generation N` remains available to select an explicit generation.
Renewal never restores upload access after a finalized ready submission,
deregistration, or upload quota revocation.

### Upload and submit a model

The model directory must contain a complete checkpoint. It must not contain
symlinks or a file named `manifest.json`; the CLI creates and signs that
manifest itself.

```bash
MODEL_DIR=/absolute/path/to/model
MODEL_NAME=your-model-name

teutonic-miner upload \
  --hotkey "$HOTKEY_NAME" \
  --name "$MODEL_NAME" \
  "$MODEL_DIR"
```

After the upload finishes, commit the model as ready:

```bash
teutonic-miner ready --hotkey "$HOTKEY_NAME"
```

`ready` is the irreversible submission point. Once it finalizes, that
hotkey's one submission is consumed, its R2 upload authority is revoked, the
public mailbox credential is removed, and validator processing continues
asynchronously. If evaluation rejects the checkpoint because it has reached
the allowed evaluation reuse limit, the access controller automatically
deletes that checkpoint's private R2 prefix.

For an already saved hotkey, the complete check, registration validation,
authorization, upload, and ready flow can be run as one command:

```bash
teutonic-miner submit \
  --hotkey "$HOTKEY_NAME" \
  --name "$MODEL_NAME" \
  "$MODEL_DIR"
```

### Multiple hotkeys

List saved hotkeys and select the default used when `--hotkey` is omitted:

```bash
teutonic-miner list
teutonic-miner use your-other-hotkey
teutonic-miner status
```

## Competitions

Miners can select `main`, `math`, `code`, or `text` with
`teutonic-miner ready --competition math` (also supported by `submit`). Omission
selects MAIN. One ready submission per hotkey is shared across all competitions.
Specialists use 30,000 planned samples with a 70/15/15 category-group mix;
early stopping remains enabled. PostgreSQL controls active manifests and thresholds.
See [deployment and configuration](DEPLOY.md#main-math-code-and-text-competitions)
for manifest publication, `scripts/configure_evaluation.py`, and gradual rewards.

```
