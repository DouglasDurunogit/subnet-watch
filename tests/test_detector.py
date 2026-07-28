"""Regression tests for the parts that fail silently.

Each test here corresponds to a bug that was actually hit during the build, or
to a failure mode that would degrade the monitor without raising anything:

  * epoch ticks reported as new challenges  -> ~3000 alarms/day, user stops reading
  * first population of a field read as a change -> 131 false alarms, measured
  * seeded baseline events counted as fresh -> every subnet scores 35/35 freshness
  * template min_compute.yml quoted as a requirement -> fabricated hardware specs
  * missing data imputed -> unknown income outranks measured income

Run:  python -m pytest tests/ -q
"""

from __future__ import annotations

import os
import sys
from datetime import datetime, timedelta, timezone

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from collector import events, margin, score  # noqa: E402


def base(**kw):
    row = {
        "netuid": 26, "name": "Perturb", "block": 100,
        "miner_burn": 0.5, "weights_version": 100, "mechanism_count": 1,
        "registration_allowed": "True", "latest_release": "v1.0.0",
        "latest_release_utc": "2026-07-01T00:00:00Z",
        "scoring_commit_utc": "2026-07-01T00:00:00Z", "scoring_commit_title": "fix scoring",
        "readme_task_sections": "abc123", "row_status": "ok",
    }
    row.update(kw)
    return row


# --- the noise the whole detector exists to suppress -------------------------

def test_epoch_tick_is_not_a_new_challenge():
    """last_step advances several times an hour on EVERY subnet. If it produced
    an event the feed would be pure noise and the top requirement would fail."""
    prev = base(last_step=1000)
    cur = base(last_step=1360)
    assert events.detect(prev, cur) == []


def test_block_and_price_movement_produce_no_events():
    prev = base(block=100, price_tao=0.005)
    cur = base(block=7300, price_tao=0.009)
    assert events.detect(prev, cur) == []


def test_first_population_of_a_field_is_not_a_change():
    """Measured bug: enabling GitHub probing after a chain-only run fired 131
    false events, because empty -> value looked like a change. Also protects
    against a transient 404 that empties a field and then refills it."""
    prev = base(latest_release="", scoring_commit_utc="", readme_task_sections="")
    cur = base(latest_release="v2.0.0", scoring_commit_utc="2026-07-27T00:00:00Z",
               readme_task_sections="def456")
    assert events.detect(prev, cur) == []


# --- the signals that must fire ---------------------------------------------

def test_weights_version_bump_fires_p0():
    evs = events.detect(base(weights_version=100), base(weights_version=101))
    assert len(evs) == 1
    assert evs[0]["class"] == "WEIGHTS_VERSION_BUMP"
    assert evs[0]["severity"] == "P0"


def test_weights_version_decrease_does_not_fire():
    assert events.detect(base(weights_version=101), base(weights_version=100)) == []


def test_burn_drop_fires_only_when_crossing_out_of_dead():
    """The user's 'unseen subnet' trigger: a subnet that paid miners nothing
    starts paying. Ordinary burn wobble below the threshold is not an event."""
    evs = events.detect(base(miner_burn=1.0), base(miner_burn=0.4))
    assert [e["class"] for e in evs] == ["BURN_DROP"]

    assert events.detect(base(miner_burn=0.8), base(miner_burn=0.4)) == []   # both alive
    assert events.detect(base(miner_burn=0.4), base(miner_burn=1.0)) == []   # went dead


def test_release_and_mechanism_and_readme_fire():
    assert [e["class"] for e in events.detect(base(), base(latest_release="v2.0.0"))] == ["RELEASE"]
    assert [e["class"] for e in events.detect(base(), base(mechanism_count=2))] == ["MECHANISM_ADDED"]
    assert [e["class"] for e in events.detect(base(), base(readme_task_sections="zzz"))] == ["README_TASK_DIFF"]


def test_new_subnet_when_no_previous_row():
    evs = events.detect(None, base(netuid=131))
    assert [e["class"] for e in evs] == ["NEW_SUBNET"]


def test_event_ids_are_stable_across_runs():
    """Dedup depends entirely on the id being a pure function of the change."""
    a = events.detect(base(weights_version=100), base(weights_version=101))[0]
    b = events.detect(base(weights_version=100), base(weights_version=101))[0]
    assert a["event_id"] == b["event_id"] == "sn26:weights_version_bump:101"


# --- windowing / dedup without memory ----------------------------------------

def _log(first_seen, **kw):
    rec = {"event_id": "sn1:release:v1", "netuid": 1, "class": "RELEASE",
           "severity": "P1", "one_line": "x", "first_seen_utc": first_seen,
           "resolved_utc": "", "seeded": False}
    rec.update(kw)
    return {rec["event_id"]: rec}


def test_event_is_new_for_exactly_one_window_then_still_open():
    now = datetime(2026, 7, 27, 12, 0, tzinfo=timezone.utc)
    recent = events.iso(now - timedelta(minutes=10))
    old = events.iso(now - timedelta(hours=5))

    w = events.window(_log(recent), interval_minutes=60, overlap_minutes=15, now=now)
    assert len(w["new"]) == 1 and len(w["still_open"]) == 0

    w = events.window(_log(old), interval_minutes=60, overlap_minutes=15, now=now)
    assert len(w["new"]) == 0 and len(w["still_open"]) == 1


def test_seeded_events_never_appear_in_any_window():
    """The baseline run records one NEW_SUBNET per subnet. Alarming those would
    be 128 false P0s on day one."""
    now = datetime(2026, 7, 27, 12, 0, tzinfo=timezone.utc)
    log = _log(events.iso(now - timedelta(minutes=5)), seeded=True)
    w = events.window(log, interval_minutes=60, overlap_minutes=15, now=now)
    assert w["new"] == [] and w["still_open"] == []


def test_missed_run_delays_but_never_loses_an_event():
    """If a run is skipped, the event ages past NEW but must still be listed."""
    now = datetime(2026, 7, 27, 12, 0, tzinfo=timezone.utc)
    w = events.window(_log(events.iso(now - timedelta(hours=30))),
                      interval_minutes=60, overlap_minutes=15, now=now)
    assert len(w["still_open"]) == 1


# --- hardware evidence quality ------------------------------------------------

TEMPLATE_YML = """version: '1.0' # update this version key as needed, ideally should match your release version
compute_spec:
  miner:
    gpu:
      min_vram: 24
"""


def test_template_min_compute_is_not_evidence():
    """~19 of 34 repos carrying min_compute.yml never edited it. Quoting the
    template's own numbers as a subnet's requirement is fabrication."""
    got = margin.infer_requirement({
        "min_compute_present": True, "min_compute_is_template": True,
        "min_compute_text": TEMPLATE_YML, "readme_text": "",
    })
    assert got["required_vram_gb"] is None
    assert got["gpu_class_basis"] == margin.BASIS_NONE


def test_edited_min_compute_is_evidence():
    got = margin.infer_requirement({
        "min_compute_present": True, "min_compute_is_template": False,
        "min_compute_text": "gpu:\n  min_vram: 80\n", "readme_text": "",
    })
    assert got["required_vram_gb"] == 80
    assert got["gpu_class_basis"] == margin.BASIS_MIN_COMPUTE


def test_stated_vram_beats_a_model_name_keyword():
    """Real bug, caught in review: sn26's README states '8+ GB VRAM' but the word
    'EfficientNetV2-L' matched a 24 GB keyword hint, so the pipeline priced an
    RTX 4090 and understated the margin. A number the author wrote must always
    beat one inferred from a model name they happened to mention."""
    # Verbatim shape of sn26's README, including the two traps it exposed:
    # "16 GB RAM" is system memory and must NOT be read as VRAM, and the "+" in
    # "8+ GB VRAM" must not prevent a match.
    got = margin.infer_requirement({
        "min_compute_present": False, "min_compute_is_template": False,
        "readme_text": ("Attacks EfficientNetV2-L. Minimum: 4 vCPU, 16 GB RAM, 50 GB SSD. "
                        "Recommended: 8 vCPU, 32 GB RAM, an NVIDIA GPU with 8+ GB VRAM."),
    })
    assert got["required_vram_gb"] == 8, "system RAM or the '+' broke VRAM parsing"
    assert got["gpu_class_basis"] == margin.BASIS_README_STATED


def test_system_ram_is_never_mistaken_for_vram():
    got = margin.infer_requirement({
        "min_compute_present": False, "min_compute_is_template": False,
        "readme_text": "Requires 64 GB RAM and 1 TB of disk. No GPU needed.",
    })
    assert got["gpu_class_basis"] != margin.BASIS_README_STATED


def test_reversed_vram_phrasing_is_caught():
    got = margin.infer_requirement({
        "min_compute_present": False, "min_compute_is_template": False,
        "readme_text": "Hardware: VRAM 48 GB, CPU 16 cores.",
    })
    assert got["required_vram_gb"] == 48


def test_stated_vram_takes_the_minimum_of_several():
    """READMEs say 'minimum X, recommended Y'. The entry requirement decides
    whether you can play at all, so the minimum is the one that matters."""
    got = margin.infer_requirement({
        "min_compute_present": False, "min_compute_is_template": False,
        "readme_text": "Recommended 24 GB VRAM. Minimum 8 GB VRAM.",
    })
    assert got["required_vram_gb"] == 8


def test_readme_inference_is_labelled_a_guess():
    got = margin.infer_requirement({
        "min_compute_present": False, "min_compute_is_template": False,
        "readme_text": "Miners must run Llama-3-70B locally.",
    })
    assert got["gpu_class_basis"].endswith("(GUESS)")


# --- gates and scoring --------------------------------------------------------

def test_dead_burn_is_gated_out_of_the_ranking():
    st, reason = score.gate(base(miner_burn=0.995, row_status="ok"))
    assert st == "BLOCKED:burn" and "earn nothing" in reason


def test_failed_row_is_gated_so_zeros_are_never_read_as_data():
    st, reason = score.gate(base(row_status="failed"))
    assert st == "BLOCKED:no-data" and "not zero" in reason


def test_closed_registration_is_gated():
    assert score.gate(base(registration_allowed="False"))[0] == "BLOCKED:closed"


def test_missing_income_scores_zero_and_is_never_imputed():
    """Unknown income must never outrank measured income."""
    r = base(net_margin_usd_day=None, machine_tier=1, payback_days=1)
    out = score.score_row(r, {}, now=datetime.now(timezone.utc))
    assert out["income_pts"] == 0.0
    assert r.get("income_flag") == "NO-INCOME-DATA" or out.get("income_flag") == "NO-INCOME-DATA"


def test_incentive_structure_never_produces_a_subscore():
    """Weight zero is enforced structurally: there is no component to re-weight,
    so it cannot be eroded in conversation without editing score.py."""
    out = score.score_row(base(net_margin_usd_day=10, machine_tier=1, payback_days=1,
                               gini=0.99, top1_share=0.99), {},
                          now=datetime.now(timezone.utc))
    assert not any("gini" in k or "structure" in k or "top1" in k for k in out)
    assert "incentive" not in score.WEIGHTS


def test_ranking_ties_break_deterministically():
    rows = [
        {"netuid": 50, "score": 10.0, "net_margin_usd_day": 5.0, "reg_cost_tao": 1.0, "earners": 10},
        {"netuid": 10, "score": 10.0, "net_margin_usd_day": 5.0, "reg_cost_tao": 1.0, "earners": 10},
        {"netuid": 30, "score": 10.0, "net_margin_usd_day": 9.0, "reg_cost_tao": 1.0, "earners": 10},
    ]
    order = [r["netuid"] for r in score.rank(list(rows))]
    assert order == [30, 10, 50]
    assert [r["netuid"] for r in score.rank(list(reversed(rows)))] == order


def test_disk_size_after_the_word_vram_is_not_read_as_vram():
    """sn26 again: '...NVIDIA GPU with 8+ GB VRAM, 100+ GB SSD'. A permissive
    separator let the reversed pattern reach past the comma and claim a 100 GB
    VRAM requirement."""
    got = margin.infer_requirement({
        "min_compute_present": False, "min_compute_is_template": False,
        "readme_text": "Recommended: 8 vCPU, 32 GB RAM, NVIDIA GPU with 8+ GB VRAM, 100+ GB SSD",
    })
    assert got["required_vram_gb"] == 8


SN53_README = """# engy
engy serves frontier open models on consumer GPUs, with cryptographic
verification that the model you pay for is the model that ran.

## Miner
Serve frontier open models. Each response carries an activation fingerprint.

## Validator
The light validator syncs the master-signed epoch result from the provider API
and submits that weight vector on chain. CPU-only; no GPU, no database.
"""


def test_validator_section_does_not_set_the_miner_requirement():
    """The bug the user caught. sn53's README says miners serve models on
    consumer GPUs; thirty lines later the VALIDATOR runbook says 'CPU-only; no
    GPU'. A whole-document scan priced a $30/month CPU box against $2,767/day of
    income and ranked the subnet 8th on a margin that does not exist."""
    got = margin.infer_requirement({
        "min_compute_present": False, "min_compute_is_template": False,
        "readme_text": SN53_README,
    })
    assert got["gpu_class_required"] != "cpu-only", "validator hardware leaked into the miner requirement"


def test_miner_scope_drops_validator_sections():
    scope = margin._miner_scope(SN53_README)
    assert "activation fingerprint" in scope
    assert "no GPU, no database" not in scope


def test_contradictory_hardware_evidence_yields_unknown():
    """'CPU-only' beside a GPU signal is a contradiction, not a cheaper answer.
    Resolving toward CPU is the expensive direction to be wrong in."""
    got = margin.infer_requirement({
        "min_compute_present": False, "min_compute_is_template": False,
        "readme_text": "Runs Llama-3-70B. Also supports a cpu-only mode.",
    })
    assert got["required_vram_gb"] is None
    assert got["gpu_class_basis"] == margin.BASIS_NONE


def test_genuine_cpu_only_readme_still_classifies_as_cpu():
    got = margin.infer_requirement({
        "min_compute_present": False, "min_compute_is_template": False,
        "readme_text": "A scraping subnet. Miners need no GPU required at all.",
    })
    assert got["required_vram_gb"] == 0


SN106_README = """# nodexo
bash scripts/setup_miner.sh      # GPU host
bash scripts/setup_validator.sh  # CPU-only validator host

| Role | Minimum |
|---|---|
| Miner | Ubuntu GPU host, supported NVIDIA GPU, working `nvidia-smi`, 16 GB RAM |
"""


def test_cpu_phrase_loses_to_a_bare_gpu_requirement():
    """sn106 slipped past the first fix: 'CPU-only validator host' sat in a setup
    snippet with no heading to drop, and no SIZING keyword opposed it, so the CPU
    phrase won unopposed even though the miner row demands nvidia-smi."""
    got = margin.infer_requirement({
        "min_compute_present": False, "min_compute_is_template": False,
        "readme_text": SN106_README,
    })
    assert got["gpu_class_required"] != "cpu-only"


def test_no_gpu_required_is_not_read_as_a_gpu_signal():
    """The contradiction tokens must not appear inside a negation, or every
    genuinely CPU-only subnet would be forced to UNKNOWN."""
    assert not margin._GPU_PRESENT.search("Miners need no GPU required at all.")


def test_thin_competitive_sample_costs_confidence():
    """Scoring the median instead of the ceiling fixes winner-take-all bias, but
    where a single competitive miner exists the two are the same number by
    definition. n=1 must not be presented as a supported estimate."""
    thin = score.score_row(
        base(net_margin_usd_day=5000, machine_tier=1, payback_days=1,
             competitive_earners=1, readme_sha="abc", repo_status="ok",
             gpu_class_basis="min_compute.yml (curated)"),
        {}, now=datetime.now(timezone.utc))
    thick = score.score_row(
        base(net_margin_usd_day=5000, machine_tier=1, payback_days=1,
             competitive_earners=40, readme_sha="abc", repo_status="ok",
             gpu_class_basis="min_compute.yml (curated)"),
        {}, now=datetime.now(timezone.utc))
    assert thin["confidence"] < thick["confidence"]
    assert "not a distribution" in thin["confidence_reason"]
    assert thin["score"] < thick["score"]


ORO_README = """## For Miners
Miners submit Python agents that define an `agent_main()` function. Inside the
sandbox, your agent can search 2.5M real products.

## How It Works
Validators run each agent in an isolated Docker sandbox against the benchmark.
"""


def test_code_submission_subnet_is_not_charged_for_a_served_gpu():
    """sn15 ORO: miners submit Python agents, the VALIDATOR executes them in a
    sandbox. There is no persistent miner process, so pricing a rented RTX 4090
    against its income is the wrong cost model entirely."""
    got = margin.infer_requirement({
        "min_compute_present": False, "min_compute_is_template": False,
        "readme_text": ORO_README,
    })
    assert got["required_vram_gb"] == 0
    assert got["gpu_class_basis"] == margin.BASIS_SUBMISSION


def test_submission_plus_training_still_needs_hardware():
    """Submitting a MODEL you had to train yourself is a large GPU bill, even
    though the validator does the serving."""
    got = margin.infer_requirement({
        "min_compute_present": False, "min_compute_is_template": False,
        "readme_text": ORO_README + "\nMiners train a 70B model before submitting.",
    })
    assert got["gpu_class_basis"] != margin.BASIS_SUBMISSION


def test_submit_alone_does_not_trigger_the_submission_rung():
    """'Miners submit responses' is near-universal phrasing; both halves of the
    pattern are required."""
    got = margin.infer_requirement({
        "min_compute_present": False, "min_compute_is_template": False,
        "readme_text": "Miners submit responses to each query within 12 seconds.",
    })
    assert got["gpu_class_basis"] != margin.BASIS_SUBMISSION


def test_missing_chain_value_never_fires_an_event():
    """The false-alarm bug: a transient query_map failure returned {}, every
    subnet fell back to the MechanismCount default of 1, and the next successful
    sweep read 2 - firing MECHANISM_ADDED for all six multi-mechanism subnets in
    the same second. chain._query_map now returns None on failure so the column
    is MISSING, and a missing value on either side must fire nothing."""
    for field in ("mechanism_count", "weights_version", "miner_burn"):
        assert events.detect(base(**{field: ""}), base()) == [], f"{field}: missing -> value fired"
        assert events.detect(base(), base(**{field: ""})) == [], f"{field}: value -> missing fired"


def test_burn_drop_needs_both_sides_present():
    """The same bug in its worst form: MinerBurned's default is 0.0, so one
    failed query would make every dead subnet look alive and fire a P0 per
    subnet."""
    assert events.detect(base(miner_burn=""), base(miner_burn=0.4)) == []
    assert events.detect(base(miner_burn=1.0), base(miner_burn="")) == []


def test_median_can_never_exceed_the_ceiling():
    """An invariant, not a preference: both come from the same set of competitive
    miners, so median <= max always. The user questioned the table when rounding
    made 6301.11 and 6301 look like a ceiling below its own median; if this ever
    fails for real, the two figures are being computed from different sets."""
    import csv, os
    snap = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                        "data", "SNAPSHOT.csv")
    if not os.path.exists(snap):
        return
    bad = []
    for r in csv.DictReader(open(snap, encoding="utf-8")):
        try:
            m, c = float(r["net_margin_usd_day"]), float(r["net_margin_top_usd_day"])
        except (ValueError, KeyError):
            continue
        if m > c + 1e-6:
            bad.append((r["netuid"], m, c))
    assert not bad, f"median above ceiling on {bad}"
