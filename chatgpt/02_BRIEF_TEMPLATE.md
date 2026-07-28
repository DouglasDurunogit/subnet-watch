# 02_BRIEF_TEMPLATE — the ≤10-paragraph challenge brief

Purpose: after reading one brief the user should know **exactly what to build**
without opening the repo. Load `04_GLOSSARY.md` for the white/black-box
definition before writing one.

Source material, in order: `briefs/sn<NN>.md` (if it exists — quote it),
`data/subnets/sn<NN>.md` (the evidence pack, which embeds a README excerpt), and
only if the user explicitly asks, a `[LIVE-READ]` of the repo itself.

## Evidence tags — exactly three, on every paragraph

| Tag | Means | Limit |
|---|---|---|
| `[VERIFIED: <file> §<anchor>, <date>]` | you read the sentence | — |
| `[INFERRED: <basis>]` | you concluded it from something you read | **max 2 per brief** |
| `[UNKNOWN]` | no evidence | write one sentence naming what is missing; do not pad |

> If a brief needs more than two `[INFERRED]` tags, stop and set the header to
> `CONFIDENCE: OPAQUE — mostly inference; treat as a research to-do, not a build
> spec.` A confident brief built on guesses is worse than an admittedly thin one.

## The ten paragraphs

| ¶ | Name | Must contain |
|---|---|---|
| 1 | **Identity** | netuid, name, symbol, subnet age, snapshot time + block, repo URL **and its HTTP status**, and one sentence stating the challenge. If the repo is dead/placeholder, say so here and mark ¶2–¶7 `[UNKNOWN]`. |
| 2 | **INPUT** | Exactly what the validator hands a miner: payload shape, transport (axon / HTTP pull / API), cadence (per tempo / per block / continuous), and whether every miner gets the same item. |
| 3 | **BOX TYPE** | `WHITE` / `BLACK` / `GREY` / `WHITE-with-a-dependency` / `UNKNOWN`, the one-sentence reason, and the **file path of the reward code** you found — or an explicit statement that you did not find one. |
| 4 | **The box** | What must actually be computed: the algorithmic core, the model or dataset dependency, and the per-round time budget. This is the "what am I building" paragraph. |
| 5 | **OUTPUT** | The exact artifact: format, size, destination, deadline, and the penalty for missing it (zero? skip? decay?). |
| 6 | **SCORING** | How output → score → incentive → emission. Name the metric and thresholds, say whether scoring is absolute or relative to other miners, and give the smoothing window if any. |
| 7 | **RESOURCES** | The requirement **and its basis** (`gpu_class_basis`), then the cheapest satisfying class from `machines.csv` with $/mo, VRAM, vCPU, RAM, bandwidth. If `min_compute_is_template` is True, say so explicitly here. If `machine_assumed` is True, say the margin is indicative. |
| 8 | **ECONOMICS** | `reg_cost_tao` + USD, `miner_burn`, `competitive_miner_usd_day`, `machine_cost_usd_day`, `net_margin_usd_day`, `payback_days` — all cited. **If `miner_burn ≥ 0.99`, this paragraph is one sentence: miners earn nothing here.** |
| 9 | **COMPETITIVE SHAPE** | `earners`, `top1_share`, `top10_share`, `gini`, whether the top miner is owner or validator-permitted, and one sentence naming the shape. Must end with the literal clause **"(display only — not scored)"**. |
| 10 | **VERDICT + UNKNOWNS** | Build / watch / skip, the single first step, and a bullet list of every `[UNKNOWN]` from ¶2–¶7 restated as a question to answer. |

## Worked opening (SN26, the canonical WHITE-with-a-dependency)

> **¶1 Identity.** sn26 "Perturb" (ב), 595 days old, snapshot 2026-07-28T06:35Z
> block 8718690. Repo `https://github.com/0xsigurd/Perturb` — HTTP 200.
> Miners find adversarial perturbations that flip an image classifier away from
> its own clean prediction while staying imperceptible.
> [VERIFIED: pack sn26 §Repository, 2026-07-28]
>
> **¶2 INPUT.** Each round the miner polls `GET /task` on a closed API and
> receives `{task_id, image_url}`, then downloads the clean image. Every miner
> gets the same image that round, on an even-minute boundary.
> [VERIFIED: README §Miner flow, 2026-07-28]
>
> **¶3 BOX TYPE. WHITE-with-a-dependency.** The scoring function
> (`verify_and_score`) is in the repo and depends only on the clean image and
> your submitted PNG, so you can score yourself locally before submitting — but
> the task and submission both route through a closed endpoint you do not
> control. Buildability is white; operational risk is not.
> [VERIFIED: README §Verification, 2026-07-28]

## Regenerating a brief

Rewrite a brief only when that subnet appears in `ALARMS.md` under **NEW SINCE
LAST RUN** with class `RELEASE`, `SCORING_COMMIT`, `README_TASK_DIFF`,
`WEIGHTS_VERSION_BUMP`, or `MECHANISM_ADDED`. When you do, state at the top what
changed and which paragraphs moved, so the user can read the delta instead of
re-reading ten paragraphs.
