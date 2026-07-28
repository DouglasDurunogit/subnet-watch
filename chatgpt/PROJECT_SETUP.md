# Setting up the ChatGPT Project

GitHub's scheduler drops most scheduled runs under load (measured: a hourly cron
fired twice in five hours). The workflow therefore attempts every 20 min and the
staleness alarm is 180 min, so STALE FEED means a real outage, not a skipped slot.

Everything below assumes the repo `DouglasDurunogit/subnet-watch` is **public** and
the Action is committing to `data/`. The URLs below are already filled in; if the
repo ever moves, `01_SOURCES.md` is the only file that needs editing.

---

## Step 1 — Attach five files to the Project

Upload to the Project's file area:

```
00_INSTRUCTIONS.md   02_BRIEF_TEMPLATE.md   04_GLOSSARY.md
01_SOURCES.md        03_SCORING.md
```

Do **not** attach anything from `data/`. Those change hourly; attached copies go
stale and would silently contradict the live repo. Policy is attached, data is
fetched.

---

## Step 2 — Paste this into the Project *instructions box*

Not a file — the actual "Instructions" field. Attached files are retrieved by
semantic search and **can be missed**; the instructions box is always in context.
This is the safety net that survives a failed retrieval.

```
You are a read-only reporter for a Bittensor subnet watch. Five rules override
everything else:

1. Fetch 01_SOURCES.md first. Every URL you visit must appear literally in it.
   If a URL is not in that file, you do not have it - do not construct one.
2. State no number without a citation of the form
   [snap:<netuid>.<column> @<UTC> b<block>]. No citation = do not state it.
3. You never fetch chain data, prices, or subnet lists yourself. The only
   numbers that exist are the ones in the repo snapshot. taomarketcap serves
   placeholder ZEROS that look like data; taostats and tao.app need paid keys;
   the chain is POST-only and unreachable from browsing.
4. If MANIFEST.json generated_utc is more than 180 minutes old, your first line
   is "STALE FEED" and you may NOT say "no new challenges" - say "no changes
   are known since <timestamp>".
5. Quote competitive_miner_usd_day as achievable income, never
   top_miner_usd_day (owner/validator-captured on most subnets).

Follow 00_INSTRUCTIONS.md. If it and this box disagree, this box wins.
```

---

## Step 3 — Create the WATCH task (hourly)

⚠️ **ChatGPT Tasks run plain-text prompts and may not see Project files**, so
this prompt is deliberately self-contained: it carries its own URLs and its own
rule kernel. Do not shorten it to "run the subnet watch".

```
Run the Bittensor subnet watch.

1. Fetch https://raw.githubusercontent.com/DouglasDurunogit/subnet-watch/main/data/MANIFEST.json
   If generated_utc is more than 180 minutes old, reply exactly:
     "STALE FEED - last sweep <generated_utc> (<N>h <M>m ago). Pipeline may be
      down. No changes are known since then."
   and STOP. Do not say "no new challenges" - a dead pipeline is not quiet.

2. Fetch https://raw.githubusercontent.com/DouglasDurunogit/subnet-watch/main/data/ALARMS.md

3. Report ONLY rows under "## NEW SINCE LAST RUN".
   Never promote anything from "## STILL OPEN" into the headline - those were
   already reported in an earlier window.

4. If NEW is empty and the feed is fresh, reply in the QUIET format (4 lines):
     QUIET - <utc>, block <n>, sweep <m> min old.
     New challenges: 0.  Still open: <k> (<netuid+class, up to 3>).
     Gates: <burn-blocked>/128 burn-blocked, <closed> closed.
     Top of ranking unchanged: #1 sn<N> <name> <score>, #2 ...
   Do not elaborate, do not re-rank, do not fetch anything else.

5. If NEW is non-empty, for each event give: class, netuid, name, first_seen,
   the one_line, and its detail. For NEW_SUBNET / RELEASE /
   WEIGHTS_VERSION_BUMP / MECHANISM_ADDED also fetch
   https://raw.githubusercontent.com/DouglasDurunogit/subnet-watch/main/data/subnets/sn<NN>.md
   and add three lines: INPUT / BOX TYPE / cheapest machine + net margin.
   Cap at 5 alarms; list any remainder by netuid only.

Rules: every number needs a citation [snap:<netuid>.<column> @<utc> b<block>].
Quote competitive_miner_usd_day as achievable income, never top_miner_usd_day.
If miner_burn >= 0.99 say miners earn nothing there regardless of other columns.
Never fetch taostats, taomarketcap, or any subnet list - they are stale, paywalled,
or serve placeholder zeros.
```

**Why the quiet format is four lines.** If a quiet day is not scannable in two
seconds you will stop reading it, and the alarms lose their meaning.

---

## Step 4 — Create the DIGEST task (daily, 08:00)

```
Run the daily Bittensor subnet digest.

Fetch, in order:
  https://raw.githubusercontent.com/DouglasDurunogit/subnet-watch/main/data/MANIFEST.json
  https://raw.githubusercontent.com/DouglasDurunogit/subnet-watch/main/data/ALARMS.md
  https://raw.githubusercontent.com/DouglasDurunogit/subnet-watch/main/data/RANKING.md
Apply the staleness gate first (>180 min = STALE FEED; >24 h = refuse rankings).

Produce:
(a) 24h event roll-up by class, counts only;
(b) top 10 of the ranking: score, net margin/day, cheapest feasible machine,
    confidence + its reason;
(c) movers: any subnet whose rank moved >= 5 places, and which component moved;
(d) gate roll-up: how many burn-blocked / closed / no-machine / no-data;
(e) one line naming the highest-scoring subnet with no brief yet.

Do not write briefs. Do not re-rank. Cite every number.
```

---

## Step 5 — The acceptance test (do this once, before trusting it)

**Deliberately break the feed and confirm the Task says `STALE FEED`, not
`QUIET`.** Disable the workflow in the Actions tab, wait 180 minutes, and run the
WATCH task manually.

This is the only failure in the whole system that can mislead you indefinitely: a
dead cron produces a confident all-clear forever, and it looks exactly like
success. If this drill fails, nothing else in the system is trustworthy.

---

## Asking things directly

The Project is also a query surface. Useful shapes:

- *"brief 26"* → the ≤10-paragraph challenge brief
- *"what changed on sn9 this week"* → reads `EVENTS.jsonl`
- *"top 10 for a 24 GB box"* → re-ranks from published component points, labelled UNOFFICIAL
- *"which subnets came back to life"* → `BURN_DROP` events
- *"why is sn46 ranked so low"* → gate reason + component breakdown

## Known limits — state these to yourself before acting on output

- **Latency is Task cadence.** ChatGPT Tasks cap at hourly and are best-effort,
  so worst-case notice of a new challenge is ~1 h plus sweep time, not instant.
- **Tasks are stateless.** Dedup is handled by the Action's window
  (`first_seen_utc` + interval + 15 min overlap), not by ChatGPT remembering.
  A missed run makes an event *late*, never *lost*.
- **`SCORING_COMMIT` matches commit messages, not file diffs.** The atom feed
  carries no file list. It is a weaker signal than `RELEASE` and is labelled so.
- **Hardware is mostly unknown.** 98 of 128 subnets have no usable requirement
  evidence, so their margin assumes a 24 GB box (`machine_assumed=True`).
