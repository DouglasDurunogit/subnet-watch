"""gh.py — GitHub side: repo URL hygiene, atom feeds, README, min_compute.

Everything here uses unauthenticated endpoints that were measured to work:
  * raw.githubusercontent.com/<o>/<r>/<branch>/<file>   full content
  * github.com/<o>/<r>/releases.atom                    10 entries
  * github.com/<o>/<r>/commits/<branch>.atom            20 entries
Atom feeds carry no x-ratelimit headers and survived a 30-request burst, so 128
repos/hour needs no token. The REST API is deliberately NOT used: unauthenticated
it allows only 60 requests/hour, which cannot cover even one pass.

Three hazards this module exists to absorb, all observed in live on-chain data:

  * PLACEHOLDER URLS. The chain contains literal template values
    (github.com/username/repo), org URLs with no repo path, and
    github.com/deprecated/deprecated. These are not repositories. Following one
    and briefing whatever it returns is worse than reporting nothing.
  * SILENT REDIRECTS. github.com/opentensor/* now 301s to RaoFoundation/*, and
    several subnets renamed their repos. A fetcher that does not follow
    redirects gets a 0-byte body that reads as "no activity"; one that follows
    silently attributes data to the wrong canonical name. We follow, and record
    BOTH urls so identity can be marked UNCONFIRMED downstream.
  * TEMPLATE min_compute.yml. Present in only ~31 of 100 repos and ~23 of those
    are unmodified copies carrying the template's own comment. Quoting those
    numbers as a subnet's requirement is fabrication with a citation attached.
"""

from __future__ import annotations

import hashlib
import re
from typing import Any, Dict, List, Optional
from xml.etree import ElementTree

import requests

UA = {"User-Agent": "subnet-watch/1.0 (+https://github.com/)"}
TIMEOUT = (5, 15)  # (connect, read) — a scalar timeout applies per phase and a
                   # stalled read can hang far longer than intended.

# Repo paths whose presence in a commit means the scoring rules may have moved.
SCORING_PATTERN = re.compile(
    r"(reward|scor|evaluat|incentive|challenge|task|validat|verif|miner)", re.I
)

# README headings that describe the task itself, as opposed to install steps.
TASK_HEADERS = re.compile(
    r"^#{1,4}\s*.*(task|challenge|scoring|score|reward|incentive|miner|how it works|evaluation)",
    re.I | re.M,
)

_PLACEHOLDER_OWNERS = {"username", "deprecated", "your-org", "yourorg", "example", "org"}
_PLACEHOLDER_REPOS = {"repo", "deprecated", "your-repo", "subnet", "example"}


class RepoRef:
    """A normalized, classified reference to a subnet's repository."""

    __slots__ = ("raw", "owner", "repo", "url", "status", "reason")

    def __init__(self, raw: str, owner: str = "", repo: str = "",
                 url: str = "", status: str = "unknown", reason: str = ""):
        self.raw, self.owner, self.repo = raw, owner, repo
        self.url, self.status, self.reason = url, status, reason

    @property
    def ok(self) -> bool:
        return self.status == "ok"

    def as_dict(self) -> Dict[str, Any]:
        return {
            "github_url_onchain": self.raw,
            "github_url_resolved": self.url,
            "repo_owner": self.owner,
            "repo_name": self.repo,
            "repo_status": self.status,
            "repo_status_reason": self.reason,
        }


def parse_repo(raw: str) -> RepoRef:
    """Normalize an on-chain repo string. Does not hit the network.

    Returns status: ok | none | placeholder | org_only | unparsable
    """
    s = (raw or "").strip()
    if not s:
        return RepoRef(raw, status="none", reason="no repo URL on chain")

    s = s.rstrip("/")
    if s.endswith(".git"):
        s = s[:-4]
    m = re.search(r"github\.com[/:]+([^/]+)(?:/([^/#?]+))?", s, re.I)
    if not m:
        return RepoRef(raw, status="unparsable", reason=f"not a github URL: {raw!r}")

    owner, repo = m.group(1), m.group(2)
    if not repo:
        return RepoRef(raw, owner=owner, status="org_only",
                       reason=f"points at an org/user, not a repository: {raw!r}")
    if owner.lower() in _PLACEHOLDER_OWNERS and repo.lower() in _PLACEHOLDER_REPOS:
        return RepoRef(raw, owner=owner, repo=repo, status="placeholder",
                       reason=f"unmodified template placeholder: {raw!r}")

    return RepoRef(raw, owner=owner, repo=repo,
                   url=f"https://github.com/{owner}/{repo}", status="ok")


def resolve(ref: RepoRef) -> RepoRef:
    """Follow redirects and record the FINAL url. Sets status to dead/redirected."""
    if not ref.ok:
        return ref
    try:
        r = requests.head(ref.url, headers=UA, timeout=TIMEOUT, allow_redirects=True)
        if r.status_code == 404:
            ref.status, ref.reason = "dead", "HTTP 404 (deleted or private)"
            return ref
        if r.status_code >= 400:
            ref.status, ref.reason = "error", f"HTTP {r.status_code}"
            return ref
        final = r.url.rstrip("/")
        if final.lower() != ref.url.lower():
            m = re.search(r"github\.com/([^/]+)/([^/#?]+)", final, re.I)
            if m:
                ref.owner, ref.repo = m.group(1), m.group(2)
                ref.url = f"https://github.com/{ref.owner}/{ref.repo}"
                ref.status, ref.reason = "redirected", f"{ref.raw} -> {ref.url}"
    except Exception as e:
        ref.status, ref.reason = "error", f"{type(e).__name__}"
    return ref


def _get(url: str) -> Optional[requests.Response]:
    try:
        r = requests.get(url, headers=UA, timeout=TIMEOUT, allow_redirects=True)
        return r if r.status_code == 200 else None
    except Exception:
        return None


def fetch_readme(ref: RepoRef) -> Dict[str, Any]:
    """README text + sha + which branch it came from. main, then master."""
    for branch in ("main", "master"):
        r = _get(f"https://raw.githubusercontent.com/{ref.owner}/{ref.repo}/{branch}/README.md")
        if r is not None and r.text.strip():
            text = r.text
            return {
                "readme_text": text,
                "readme_sha": hashlib.sha256(text.encode("utf-8", "replace")).hexdigest()[:16],
                "readme_branch": branch,
                "readme_bytes": len(text),
                "readme_task_sections": _task_sections(text),
            }
    return {"readme_text": "", "readme_sha": "", "readme_branch": "",
            "readme_bytes": 0, "readme_task_sections": ""}


def _task_sections(text: str) -> str:
    """Hash only the task/scoring-describing headings and their bodies.

    A README changes constantly for reasons that are not a new challenge (badges,
    typos, install notes). Hashing just the task-relevant sections is what makes
    README_TASK_DIFF a signal instead of noise.
    """
    lines, keep, on = text.splitlines(), [], False
    for ln in lines:
        if ln.startswith("#"):
            on = bool(TASK_HEADERS.match(ln))
        if on:
            keep.append(ln.strip())
    body = "\n".join(keep)
    return hashlib.sha256(body.encode("utf-8", "replace")).hexdigest()[:16] if body else ""


def fetch_min_compute(ref: RepoRef) -> Dict[str, Any]:
    """min_compute.yml presence + whether it is an untouched template copy."""
    for branch in ("main", "master"):
        r = _get(f"https://raw.githubusercontent.com/{ref.owner}/{ref.repo}/{branch}/min_compute.yml")
        if r is not None and r.text.strip():
            text = r.text
            # The template ships this exact comment; ~23 of 31 repos never edit it.
            is_template = "update this version key as needed" in text
            has_sections = ("miner:" in text and "validator:" in text)
            return {
                "min_compute_present": True,
                "min_compute_is_template": bool(is_template),
                "min_compute_conforms": bool(has_sections),
                "min_compute_text": text[:4000],
            }
    return {"min_compute_present": False, "min_compute_is_template": False,
            "min_compute_conforms": False, "min_compute_text": ""}


def _atom(url: str) -> List[Dict[str, str]]:
    r = _get(url)
    if r is None:
        return []
    try:
        root = ElementTree.fromstring(r.content)
    except Exception:
        return []
    ns = {"a": "http://www.w3.org/2005/Atom"}
    out = []
    for e in root.findall("a:entry", ns):
        def txt(tag):
            el = e.find(f"a:{tag}", ns)
            return (el.text or "").strip() if el is not None and el.text else ""
        link = e.find("a:link", ns)
        out.append({
            "title": txt("title"),
            "updated": txt("updated"),
            "id": txt("id"),
            "link": link.get("href", "") if link is not None else "",
        })
    return out


def fetch_releases(ref: RepoRef) -> List[Dict[str, str]]:
    return _atom(f"https://github.com/{ref.owner}/{ref.repo}/releases.atom")


def fetch_commits(ref: RepoRef, branch: str = "main") -> List[Dict[str, str]]:
    entries = _atom(f"https://github.com/{ref.owner}/{ref.repo}/commits/{branch}.atom")
    if not entries and branch == "main":
        entries = _atom(f"https://github.com/{ref.owner}/{ref.repo}/commits/master.atom")
    return entries


def scoring_commits(entries: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """Commits whose message suggests the scoring rules moved.

    The commit atom feed carries no file list, so this matches on the message.
    That is a weaker signal than a real path diff and is labelled as such
    downstream — it earns a lower-confidence event class, never a hard claim.
    """
    return [e for e in entries if SCORING_PATTERN.search(e.get("title", ""))]


def probe(ref: RepoRef, *, want_readme: bool = True) -> Dict[str, Any]:
    """One repo's full GitHub-side evidence. Never raises."""
    out: Dict[str, Any] = dict(ref.as_dict())
    if not ref.ok and ref.status != "redirected":
        out.update(readme_sha="", readme_task_sections="", readme_bytes=0,
                   min_compute_present=False, min_compute_is_template=False,
                   latest_release="", latest_release_utc="", last_commit_utc="",
                   scoring_commit_utc="", scoring_commit_title="")
        return out

    releases = fetch_releases(ref)
    commits = fetch_commits(ref)
    scoring = scoring_commits(commits)

    out.update({
        "latest_release": releases[0]["title"] if releases else "",
        "latest_release_utc": releases[0]["updated"] if releases else "",
        "last_commit_utc": commits[0]["updated"] if commits else "",
        "scoring_commit_utc": scoring[0]["updated"] if scoring else "",
        "scoring_commit_title": scoring[0]["title"][:160] if scoring else "",
    })
    if want_readme:
        out.update(fetch_readme(ref))
        out.update(fetch_min_compute(ref))
    return out
