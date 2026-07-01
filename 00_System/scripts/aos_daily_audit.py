#!/usr/bin/env python3
"""Generate a passive daily AOS audit report.

The script is intentionally non destructive. It reads Git metadata and files,
then writes a Markdown report under 00_System/audits/daily/.
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path


REPORT_DIR = Path("00_System/audits/daily")
TEMPLATE_PATH = Path("00_System/audits/templates/TEMPLATE_DAILY_AUDIT.md")

PERMANENT_RE = re.compile(r"^02_IA/.+/fiche_permanente\.md$")
WATCH_RE = re.compile(r"^02_IA/.+/veille/.+\.md$")
TRANSVERSAL_PREFIXES = (
    "02_IA/Agents IA/",
    "02_IA/Orchestration IA/",
    "02_IA/MCP/",
    "02_IA/Standards IA/",
)
MAJOR_PREFIXES = (
    "02_IA/ChatGPT/",
    "02_IA/Claude/",
    "02_IA/Gemini/",
    "02_IA/Codex/",
    "02_IA/Claude Code/",
)
SPECULATION_TERMS = (
    "a confirmer",
    "a surveiller",
    "hypothese",
    "speculatif",
    "semble",
    "pourrait",
    "devrait",
    "peut-etre",
    "non officiel",
    "benchmark",
    "prix",
    "disponibilite",
    "capacites futures",
)
MARKETING_TERMS = (
    "marketing",
    "sponsor",
    "sponsorise",
    "promesse",
    "hype",
    "landing page",
    "abonnement",
    "formation",
)

RISK_ORDER = {
    "faible": 1,
    "moyen": 2,
    "eleve": 3,
    "bloquant": 4,
}


@dataclass
class ChangedFile:
    status: str
    path: str
    old_path: str | None = None


@dataclass
class Alert:
    level: str
    category: str
    path: str
    observation: str
    recommendation: str


def run_git(args: list[str], check: bool = True) -> str:
    result = subprocess.run(
        ["git", *args],
        check=check,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    return result.stdout.strip()


def normalize_path(path: str) -> str:
    return path.replace("\\", "/").strip()


def parse_name_status(raw: str) -> list[ChangedFile]:
    files: list[ChangedFile] = []
    for line in raw.splitlines():
        if not line.strip():
            continue
        parts = line.split("\t")
        status = parts[0]
        if status.startswith("R") and len(parts) >= 3:
            files.append(
                ChangedFile(
                    status=status,
                    old_path=normalize_path(parts[1]),
                    path=normalize_path(parts[2]),
                )
            )
        elif len(parts) >= 2:
            files.append(ChangedFile(status=status, path=normalize_path(parts[1])))
    return files


def recent_commits(since_hours: int, fallback_count: int) -> list[str]:
    since = f"{since_hours} hours ago"
    raw = run_git(["log", f"--since={since}", "--pretty=format:%H%x09%h%x09%ci%x09%s"])
    commits = raw.splitlines() if raw else []
    if commits:
        return commits
    raw = run_git(["log", f"-{fallback_count}", "--pretty=format:%H%x09%h%x09%ci%x09%s"])
    return raw.splitlines() if raw else []


def commit_hashes(commit_lines: list[str]) -> list[str]:
    hashes: list[str] = []
    for line in commit_lines:
        parts = line.split("\t", 3)
        if parts and parts[0]:
            hashes.append(parts[0])
    return hashes


def changed_files_for_commits(commits: list[str]) -> list[ChangedFile]:
    by_key: dict[tuple[str, str | None, str], ChangedFile] = {}
    for commit in commits:
        raw = run_git(["show", "--name-status", "--format=", "--find-renames=40%", commit])
        for item in parse_name_status(raw):
            key = (item.path, item.old_path, item.status)
            by_key[key] = item
    return list(by_key.values())


def read_text(path: str) -> str:
    file_path = Path(path)
    if not file_path.exists() or not file_path.is_file():
        return ""
    return file_path.read_text(encoding="utf-8", errors="replace")


def added_line_count(commit: str, path: str) -> int:
    raw = run_git(["show", "--numstat", "--format=", commit, "--", path], check=False)
    total = 0
    for line in raw.splitlines():
        parts = line.split("\t")
        if len(parts) >= 3 and parts[0].isdigit():
            total += int(parts[0])
    return total


def classify_files(files: list[ChangedFile]) -> dict[str, list[ChangedFile]]:
    created = [f for f in files if f.status.startswith("A")]
    modified = [f for f in files if f.status.startswith("M")]
    renamed = [f for f in files if f.status.startswith("R")]
    permanent_modified = [f for f in files if PERMANENT_RE.match(f.path) and not f.status.startswith("A")]
    permanent_created = [f for f in files if PERMANENT_RE.match(f.path) and f.status.startswith("A")]
    watch_created = [f for f in files if WATCH_RE.match(f.path) and f.status.startswith("A")]
    transversal_modified = [
        f for f in files if f.path.startswith(TRANSVERSAL_PREFIXES) and not f.status.startswith("A")
    ]
    processed_sources = [
        f for f in files if "/traitees/" in f.path and f.path.startswith("01_Collecte/sources_brutes/")
    ]
    return {
        "created": created,
        "modified": modified,
        "renamed": renamed,
        "permanent_modified": permanent_modified,
        "permanent_created": permanent_created,
        "watch_created": watch_created,
        "transversal_modified": transversal_modified,
        "processed_sources": processed_sources,
    }


def detect_alerts(files: list[ChangedFile], commits: list[str]) -> list[Alert]:
    classes = classify_files(files)
    alerts: list[Alert] = []

    for item in classes["permanent_created"]:
        text = read_text(item.path).lower()
        if "a surveiller" in text or "non officiel" in text or "source youtube" in text:
            level = "eleve"
            observation = "Nouvelle fiche permanente creee avec signaux d'incertitude ou source faible."
        else:
            level = "moyen"
            observation = "Nouvelle fiche permanente creee dans la periode auditee."
        alerts.append(
            Alert(
                level=level,
                category="creation abusive de fiche permanente",
                path=item.path,
                observation=observation,
                recommendation="Verifier que le sujet est principal ou durable avant conservation.",
            )
        )

    for item in classes["permanent_modified"]:
        text = read_text(item.path).lower()
        added = max((added_line_count(commit, item.path) for commit in commits), default=0)
        if item.path.startswith(MAJOR_PREFIXES) and added >= 50:
            alerts.append(
                Alert(
                    level="eleve",
                    category="sur-enrichissement",
                    path=item.path,
                    observation=f"Fiche permanente majeure modifiee largement ({added} lignes ajoutees detectees).",
                    recommendation="Faire relire par Aion si la source est non officielle ou speculative.",
                )
            )
        elif added >= 25:
            alerts.append(
                Alert(
                    level="moyen",
                    category="sur-enrichissement",
                    path=item.path,
                    observation=f"Modification importante d'une fiche permanente ({added} lignes ajoutees detectees).",
                    recommendation="Verifier que les ajouts restent synthetiques et consolides.",
                )
            )
        if any(term in text for term in SPECULATION_TERMS):
            alerts.append(
                Alert(
                    level="moyen",
                    category="speculation",
                    path=item.path,
                    observation="Termes d'incertitude detectes dans une fiche permanente.",
                    recommendation="Verifier que ces elements restent en points a surveiller et ne sont pas presentes comme faits valides.",
                )
            )
        if any(term in text for term in MARKETING_TERMS):
            alerts.append(
                Alert(
                    level="moyen",
                    category="marketing integre",
                    path=item.path,
                    observation="Termes marketing ou sponsorises detectes dans une fiche permanente.",
                    recommendation="Verifier que le marketing est exclu des connaissances durables.",
                )
            )

    for item in classes["transversal_modified"]:
        alerts.append(
            Alert(
                level="eleve",
                category="modification abusive des fiches transversales",
                path=item.path,
                observation="Fiche transversale modifiee dans la periode auditee.",
                recommendation="Verifier que la source apporte une regle generale durable, pas une mention secondaire.",
            )
        )

    for item in classes["processed_sources"]:
        source_topic = Path(item.path).stem.replace("_transcript", "")
        has_watch = any(WATCH_RE.match(f.path) for f in files)
        if not has_watch:
            alerts.append(
                Alert(
                    level="bloquant",
                    category="source traitee sans veille",
                    path=item.path,
                    observation=f"Source traitee detectee sans fiche de veille creee dans les commits analyses ({source_topic}).",
                    recommendation="Verifier manuellement le traitement avant nouvelle automatisation.",
                )
            )

    if not alerts:
        alerts.append(
            Alert(
                level="faible",
                category="hygiene",
                path="repository",
                observation="Aucune anomalie V1 detectee par les heuristiques locales.",
                recommendation="Lecture humaine optionnelle du rapport.",
            )
        )

    return alerts


def highest_risk(alerts: list[Alert]) -> str:
    return max(alerts, key=lambda alert: RISK_ORDER[alert.level]).level


def audit_decision(risk: str) -> str:
    if risk == "bloquant":
        return "Blocage"
    if risk == "eleve":
        return "Audit Aion recommande"
    if risk == "moyen":
        return "GO partiel"
    return "GO"


def bullet_list(items: list[str], empty: str = "Aucun element detecte.") -> str:
    if not items:
        return f"- {empty}"
    return "\n".join(f"- {item}" for item in items)


def format_files(files: list[ChangedFile]) -> list[str]:
    formatted: list[str] = []
    for item in sorted(files, key=lambda f: f.path):
        if item.old_path:
            formatted.append(f"{item.status} {item.old_path} -> {item.path}")
        else:
            formatted.append(f"{item.status} {item.path}")
    return formatted


def format_commits(commit_lines: list[str]) -> str:
    rows = []
    for line in commit_lines:
        parts = line.split("\t", 3)
        if len(parts) == 4:
            _, short_hash, date, subject = parts
            rows.append(f"- `{short_hash}` - {date} - {subject}")
    return "\n".join(rows) if rows else "- Aucun commit analyse."


def format_alerts(alerts: list[Alert]) -> str:
    lines: list[str] = []
    today = dt.datetime.now().strftime("%Y%m%d")
    for index, alert in enumerate(alerts, start=1):
        lines.extend(
            [
                f"### AUDIT-{today}-{index:03d} - {alert.category}",
                "",
                f"- Risque : {alert.level}",
                f"- Fichier concerne : `{alert.path}`",
                f"- Observation : {alert.observation}",
                f"- Recommandation : {alert.recommendation}",
                "- Decision attendue : Aion / utilisateur / Codex sur demande",
                "",
            ]
        )
    return "\n".join(lines).strip()


def format_alerts_by_level(alerts: list[Alert], level: str) -> str:
    selected = [a for a in alerts if a.level == level]
    if not selected:
        return "- Aucun risque detecte."
    return "\n".join(f"- `{a.path}` - {a.category} : {a.observation}" for a in selected)


def recommendations(alerts: list[Alert]) -> str:
    seen: set[str] = set()
    items: list[str] = []
    for alert in alerts:
        if alert.recommendation not in seen:
            seen.add(alert.recommendation)
            items.append(alert.recommendation)
    return bullet_list(items)


def render_report(since_hours: int, fallback_count: int) -> str:
    now = dt.datetime.now()
    commits_lines = recent_commits(since_hours, fallback_count)
    commits = commit_hashes(commits_lines)
    files = changed_files_for_commits(commits)
    classes = classify_files(files)
    alerts = detect_alerts(files, commits)
    risk = highest_risk(alerts)
    decision = audit_decision(risk)
    status = run_git(["status", "--short"], check=False)
    head = run_git(["rev-parse", "--short", "HEAD"], check=False)
    period = f"Dernieres {since_hours}h ou fallback {fallback_count} commits recents"

    template = TEMPLATE_PATH.read_text(encoding="utf-8")
    replacements = {
        "{{date}}": now.strftime("%Y-%m-%d"),
        "{{GO / GO partiel / Audit Aion recommande / Blocage}}": decision,
        "{{faible / moyen / eleve / bloquant}}": risk,
        "{{commit}}": head,
        "{{periode}}": period,
        "{{datetime}}": now.strftime("%Y-%m-%d %H:%M:%S"),
        "{{periode_detail}}": period,
        "{{commits_analyses}}": format_commits(commits_lines),
        "{{fichiers_crees}}": bullet_list(format_files(classes["created"])),
        "{{fichiers_modifies}}": bullet_list(format_files(classes["modified"] + classes["renamed"])),
        "{{fiches_permanentes_impactees}}": bullet_list(
            format_files(classes["permanent_modified"] + classes["permanent_created"])
        ),
        "{{nouvelles_fiches_permanentes}}": bullet_list(format_files(classes["permanent_created"])),
        "{{fiches_transversales_modifiees}}": bullet_list(format_files(classes["transversal_modified"])),
        "{{fiches_veille_creees}}": bullet_list(format_files(classes["watch_created"])),
        "{{sources_traitees}}": bullet_list(format_files(classes["processed_sources"])),
        "{{alertes_detectees}}": format_alerts(alerts),
        "{{risques_faibles}}": format_alerts_by_level(alerts, "faible"),
        "{{risques_moyens}}": format_alerts_by_level(alerts, "moyen"),
        "{{risques_eleves}}": format_alerts_by_level(alerts, "eleve"),
        "{{risques_bloquants}}": format_alerts_by_level(alerts, "bloquant"),
        "{{recommandations}}": recommendations(alerts),
        "{{git_status_short}}": status or "(propre)",
    }
    report = template
    for placeholder, value in replacements.items():
        report = report.replace(placeholder, value)
    return report


def write_report(report: str, date: dt.date | None = None) -> Path:
    report_date = date or dt.date.today()
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    output = REPORT_DIR / f"{report_date:%Y-%m-%d}_audit-journalier-aos.md"
    output.write_text(report, encoding="utf-8", newline="\n")
    return output


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a passive AOS daily audit report.")
    parser.add_argument("--since-hours", type=int, default=24, help="Git commit lookback window.")
    parser.add_argument("--fallback-count", type=int, default=10, help="Recent commits to inspect if 24h is empty.")
    parser.add_argument("--print-path", action="store_true", help="Print generated report path.")
    args = parser.parse_args()

    report = render_report(args.since_hours, args.fallback_count)
    output = write_report(report)
    if args.print_path:
        print(output.as_posix())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
