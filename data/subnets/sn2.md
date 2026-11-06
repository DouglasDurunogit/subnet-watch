# sn2 - DaniLabs (β)

snapshot_utc: 2026-11-06T20:58:37Z  |  block: 9449585  |  row_status: ok

## Chain row

- miner_burn: **1.0**  <- 100% burn: miners earn NOTHING here
- registration cost: 0.0005 TAO (0.11208 USD), open=True
- tempo: 360.0  |  max_uids: 256  |  active: 6  |  free: 0
- subnet age: 932.7 days  |  registered at block 2734060
- weights_version: 11003  |  mechanisms: 1

## Income (miner side)

- **competitive_miner_usd_day: [UNKNOWN]** (uid [UNKNOWN]) <- the only figure quotable as achievable
- median_miner_usd_day: 2614.028217246391
- top_miner_usd_day: 2614.028217246391 (uid 14, owner=True, validator_permitted=True) <- NOT achievable if owner or permitted

## Incentive structure (display only - never scored)

- earners: 1  |  gini: 0.0  |  top1_share: 1.0  |  top10_share: 1.0
- owner_incentive_share: 1.0 (independent check on miner_burn; disagreement 0.0)

## Repository

- on-chain URL: `https://github.com/DaniLabsAI/subnet`
- resolved URL: `https://github.com/DaniLabsAI/subnet`
- status: **ok** 
- README: 1444 bytes, sha 4ba8968acc9fe237
- latest release: (none) 
- last commit: 2026-11-06T20:42:23Z
- scoring-related commit: Prepare Finney SN2 validator onboarding and cron updates 2026-11-06T20:42:23Z

## Resources

- min_compute.yml present: False  |  unmodified template: False
- required: unknown (~[UNKNOWN] GB VRAM)  |  basis: **no evidence**
- cheapest satisfying machine: rtx4090 at 8.2192 USD/day  <- ASSUMED default box; no hardware evidence was found, so the margin below is indicative only
- net margin: [UNKNOWN] USD/day  |  payback on registration: [UNKNOWN] days

## Score

- gate: **BLOCKED:burn** - miner_burn=1.000 - 100.0% of miner emission is withheld by owner-controlled hotkeys, so miners earn nothing here
- score: [UNKNOWN] (rank -), confidence [UNKNOWN] 
- components: income [UNKNOWN] / freshness [UNKNOWN] / resource [UNKNOWN] / registration [UNKNOWN]
- freshness basis: -

## On-chain description

> Distributed Accelerated Neural intelligence

## README excerpt (evidence for the brief)

```markdown
# DaniLabs SN2 validator

DaniLabs runs distributed AI inference on Bittensor Finney subnet 2. This
repository contains the validator worker, signed-report verifier, miner scoring
code, and isolated burn signer.

**Existing SN2 validators can join the scoring pilot now.** Run the verifier
alongside your current validator and compare results from the same finalized
epoch. The pilot uses a CPU host and public signed reports. It requires no API
account or wallet access.

- [Start the validator scoring pilot](docs/validator-onboarding.md)
- [Signed reports, score calculation, and evidence requirements](docs/validator-reports.md)
- [Cron updates for the managed worker](docs/worker-updates.md)
- [Finney signer custody and activation](docs/production-signer.md)
- [Finalized chain observer](docs/operator-pilot.md) and [localnet testing](docs/localnet-validator.md)

The DaniLabs production signer assigns 100% of its weight to the verified
subnet owner for miner-incentive burn. Scoring runs in shadow mode. Candidate
weights are logged for comparison and are ineligible for miner rewards pending
independent token and correctness verification. A validator’s weight row and
the subnet’s actual burn settlement are checked separately.

For setup and coordination, use [DaniLabs #validators](https://discord.com/channels/1555079929148866610/1564448334322602177).
[Join the DaniLabs Discord](https://discord.gg/df3TYnaX4f) if you need access.

```
