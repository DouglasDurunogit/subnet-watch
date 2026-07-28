# 04_GLOSSARY — the terms this project uses precisely

These five definitions are the ones most likely to be confabulated from general
Bittensor knowledge. Use these, not recollection.

## White box vs black box

**This is the user's own framing, not established Bittensor terminology.** The
ecosystem does not use these words this way (the one adjacent usage in the wild
calls *validators* a "black box", meaning something different — unverifiable
scoring). The analogy comes from adversarial-ML literature and is used here in
this specific sense:

> **WHITE BOX** — you can compute your own score locally, before you submit.
> The scoring function lives in the repo and depends only on the input you were
> given plus the output you produced.
>
> **BLACK BOX** — you cannot. The score depends on something you do not have: a
> future outcome, a hidden ground truth, a private dataset, a closed or hosted
> API, an LLM or human judge, or a comparison against other miners' answers.

**Why it decides whether to enter.** In a white-box subnet you can build a local
scorer, iterate offline, and know your result before spending a submission. In a
black-box subnet every iteration costs a live round and feedback is noisy and
delayed. The same nominal income is worth much less in a black-box subnet.

**GREY** — deterministic, published metric but a hidden target (e.g. the metric
is open, the ground truth is revealed only afterwards). Name which half is
hidden.

**WHITE-with-a-dependency** — open scoring code, but the task or submission path
runs through a closed API. Buildability is white; operational risk is not.
SN26 Perturb is the canonical example: scoring is `verify_and_score` in the repo,
but tasks come from a closed endpoint.

### Decision procedure (do not skip a step)

1. Find the validator's reward path — `reward.py`, `scoring.py`,
   `validator/forward.py`, `verify_and_score`, `neurons/validator.py`.
   **Not found → `BOX TYPE: UNKNOWN (reward path not located)`. Stop. Do not
   infer it from the subnet's marketing description.**
2. Found → list its inputs. All available to the miner at submission time → **WHITE**.
3. Any input is a future value, another miner's submission, a call to a
   non-public host, or an LLM/human judgment → **BLACK**.
4. Open metric, hidden target → **GREY**; name the hidden half.
5. Closed API in the transport but a public metric → **WHITE-with-a-dependency**.

Note: only ~40% of subnet repos have `neurons/validator.py`, and the template's
`reward.py` convention is effectively dead (0 of 40 repos sampled). Half of all
repos have none of the conventional paths, so `UNKNOWN` is a common and correct
answer.

## "New challenge"

A change to **what miners are asked to do, or how they are scored.** Only the
event classes in `ALARMS.md` count. In descending confidence:

| Class | Meaning |
|---|---|
| `NEW_SUBNET` | a netuid that did not exist before |
| `WEIGHTS_VERSION_BUMP` | the owner raised `WeightsVersionKey`; the chain now **rejects** weights from un-upgraded validators — as close to a guaranteed breaking change as exists |
| `MECHANISM_ADDED` | a second distinct incentive mechanism now runs under one netuid |
| `BURN_DROP` | `miner_burn` fell out of ≥0.99 — a subnet that paid miners nothing now pays |
| `RELEASE` | a new entry in the repo's `releases.atom` |
| `SCORING_COMMIT` | a commit whose **message** matches the scoring vocabulary — weaker evidence than a release, since the feed carries no file list |
| `README_TASK_DIFF` | the README's task/scoring sections changed (only those sections are hashed, so badge and typo edits do not trigger it) |
| `REGISTRATION_OPENED` | registration went closed → open |

> **An advancing `last_step` / scoring epoch is NOT a new challenge.** It is a
> routine tempo tick occurring several times an hour on every subnet. It is
> excluded from the detector by design. Never report it as one.

## Burn

Three different things share the word. Keep them apart.

- **`miner_burn`** (chain `MinerBurned`, 0–1) — the fraction of each tempo's
  **miner** emission withheld because it landed on an owner-controlled hotkey,
  then recycled or burned. **This is the burn that matters to you.** 38 of 128
  subnets sit at ≥0.99 today, meaning miners there earn nothing. Gated out.
- **`owner_cut_frac`** (~0.18 everywhere) — the protocol's 18% owner share of
  subnet emission. Normal, not a red flag, identical across subnets.
- **`reg_cost_tao`** (chain `Burn`) — the TAO burned to register one UID.
  This is a **cost to you**, unrelated to the two above. Denominated in TAO, not
  alpha, and it rises with each registration then decays.

## Income chain

```
per-UID alpha/tempo  = metagraph.emission[uid]          (ALPHA, not TAO)
epochs/day           = 86400 / (12 * tempo)             (tempo is NOT always 360 — sn1 is 99)
alpha/day            = alpha/tempo * epochs/day
TAO/day              = alpha/day * subnet price         (spot, from pool reserves)
USD/day              = TAO/day * TAO/USD                (CoinGecko spot)
```

Two traps the pipeline already handles, which you must not undo:

- `metagraph.emission` is a **pre-burn** figure. It includes emission that is
  withheld and destroyed.
- It combines the miner and validator streams. Only the incentive half is what a
  miner competes for.

## Miner vs validator

Do **not** use `validator_permit` as a binary classifier — a UID can legitimately
earn both streams. `incentives[uid] > 0` means it earns as a miner;
`dividends[uid] > 0` means it earns as a validator; `validator_permit` only means
"eligible to have its weights counted".

For income purposes, what matters is the pipeline's `competitive_miner_*`:
the best UID that is neither owner-controlled (by hotkey **or** coldkey, which
catches an owner mining under a fresh hotkey) nor validator-permitted.
