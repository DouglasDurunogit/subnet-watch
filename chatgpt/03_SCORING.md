# 03_SCORING — how the ranking is built

The ranking is computed **deterministically in Python** by the GitHub Action
(`collector/score.py`). You read and explain it; you never re-derive it. A
weighted ranking of 128 rows judged by eye produces a different order every run,
and rank churn that is not a real change destroys the point of a monitor.

## Gates run first

A gated subnet gets **no score** and is listed separately, because a score
implies "you could earn this" and a gated subnet cannot pay.

| Gate | Condition | Count today |
|---|---|---|
| `BLOCKED:burn` | `miner_burn ≥ 0.99` — miners earn nothing | **38 of 128** |
| `BLOCKED:closed` | registration closed; you cannot get a UID | — |
| `BLOCKED:no-machine` | requirement known, no class in `machines.csv` satisfies it | — |
| `BLOCKED:no-data` | `row_status = failed`; values are missing, **not zero** | — |

Negative margin is **not** a gate — those subnets appear under `## BELOW COST` in
`RANKING.md` so the information is never destroyed.

## Weights (sum 100)

| Component | Weight | Why |
|---|---|---|
| Income (net margin) | **40** | the point of the exercise |
| New-challenge freshness | **35** | the user's stated top priority — a fresh challenge is where a newcomer can still win |
| Resource cost / entry | **15** | determines whether entry is possible at all |
| Registration cost | **10** | real but small next to monthly machine cost |
| **Incentive structure** | **0** | **explicit decision: display only** |

### The zero is structural, not a promise

The pipeline **publishes no incentive-structure subscore**. There is nothing to
re-weight. If asked to give it weight, say that it requires editing
`collector/score.py` and re-running the Action — you cannot do it in
conversation, by design.

## Arithmetic

```
income_pts   = 40 * clamp01( log10(1 + max(0, net_margin_usd_day)) / log10(1 + 25000) )
freshness_pts= 35 * decay      decay = 1.00 if a qualifying event ≤ 7d
                                       0.60 if ≤ 30d
                                       0.30 if ≤ 90d
                                       0.00 otherwise
                               a subnet ≤ 30 days old is itself fresh → 1.00
resource_pts = 15 * (1 - tier/4)      tier: cpu=0, 24GB=1, 48GB=2, A100=3, H100/multi=4
reg_pts      = 10 * clamp01(1 - payback_days / 30)
                               payback_days = reg_cost_usd / net_margin_usd_day

score        = round( (income + freshness + resource + reg) * confidence, 1 )
confidence   = 1.00 documented | 0.85 one unknown | 0.60 two or more
```

**Why log on income, and why the ceiling is 25,000.** Competitive margins span
$0.10 to ~$24,000/day. On a linear scale the ranking becomes a pure sort by the
single largest subnet. The ceiling is set from the observed maximum, not a round
guess: at an earlier $500 ceiling the top eight subnets all pinned to full marks
despite spanning $3.2k to $10k/day — a 3× income difference reported as a dead
heat.

## Missing data is never imputed

| Missing | Result |
|---|---|
| `net_margin_usd_day` | `income_pts = 0`, flag `NO-INCOME-DATA`. **Never the median** — unknown income must not outrank measured income. |
| `machine_tier` | half marks (7.5), and confidence pays for it |
| `payback_days` | `reg_pts = 0` |
| no qualifying event | `freshness_pts = 0` — correct: no news is not fresh |

On day one of monitoring almost every subnet has `freshness_pts = 0`, because no
change has been *observed* yet. That is honest, not a bug: the monitor can only
score freshness it has witnessed. The component becomes meaningful as events
accumulate.

## Ties

Broken deterministically, in order: higher `net_margin_usd_day` → lower
`reg_cost_tao` → more `earners` → lower `netuid`. Never random — so any rank
change between runs is a real change, never sort instability.

## Re-ranking on request

`RANKING.md` publishes the four component point values per subnet. The score is
a linear sum, so a re-weight is a **rescale** — no chain data is re-derived.

> Recompute only as `sum(component_pts_i * new_w_i / old_w_i) * confidence` using
> the published points. Show the weight vector. Label it
> **"UNOFFICIAL re-rank (weights: income X, freshness Y, resources Z, reg W) —
> not the pipeline's ranking."** Do not change gates, do not change confidence,
> and do not add a component the pipeline does not publish.
