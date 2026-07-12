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
import unicodedata
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
CORRECTION_TERMS = (
    "tighten",
    "consolidate",
    "safeguard",
    "rename",
    "correction",
    "audit",
    "rules",
    "fix",
)
STRONG_SECTION_TERMS = (
    "role principal",
    "forces",
    "cas d'usage valides",
    "cas d'usage validés",
    "decisions strategiques",
    "décisions stratégiques",
)
METADATA_UPDATE_RE = re.compile(r"^(?:[-*]\s*)?derni[eè]re mise [aà] jour\s*:", re.IGNORECASE)
UNCERTAINTY_ALLOWED_SECTION_TERMS = (
    "evolutions",
    "Ã©volutions",
    "évolutions",
    "points a surveiller",
    "limites",
    "faiblesses",
    "points Ã  surveiller",
    "points à surveiller",
)

RISK_ORDER = {
    "faible": 1,
    "moyen": 2,
    "eleve": 3,
    "bloquant": 4,
}

COMMIT_CLASSES = {
    "knowledge": "Knowledge batch",
    "protocol": "Protocol / system",
    "maintenance": "Maintenance",
    "audit": "Audit",
}

QUALITY_ALERT_CATEGORY_ORDER = {
    "creation abusive de fiche permanente": 1,
    "modification abusive des fiches transversales": 2,
    "sur-enrichissement": 3,
    "speculation": 4,
    "marketing integre": 5,
}


@dataclass
class ChangedFile:
    status: str
    path: str
    old_path: str | None = None


@dataclass
class CommitInfo:
    full_hash: str
    short_hash: str
    date: str
    subject: str
    classification: str
    files: list[ChangedFile]


@dataclass
class Alert:
    level: str
    category: str
    path: str
    observation: str
    recommendation: str


@dataclass(frozen=True)
class ExactDuplicateEvidence:
    original_source_path: str
    existing_watch_path: str


@dataclass(frozen=True)
class LexicalMatch:
    term: str
    line_number: int
    passage: str
    section: str


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
        for item in changed_files_for_commit(commit):
            key = (item.path, item.old_path, item.status)
            by_key[key] = item
    return list(by_key.values())


def changed_files_for_commit(commit: str) -> list[ChangedFile]:
    raw = run_git(["diff-tree", "--no-commit-id", "--name-status", "-r", commit])
    return parse_name_status(raw)


def dedupe_changed_files(files: list[ChangedFile]) -> list[ChangedFile]:
    by_key: dict[tuple[str, str | None, str], ChangedFile] = {}
    for item in files:
        by_key[(item.path, item.old_path, item.status)] = item
    return list(by_key.values())


def diff_changed_content_lines(commit: str, path: str) -> list[str]:
    raw = run_git(["show", "--format=", "--unified=0", commit, "--", path], check=False)
    lines: list[str] = []
    for line in raw.splitlines():
        if not line.startswith(("+", "-")):
            continue
        if line.startswith(("+++", "---")):
            continue
        lines.append(line[1:].strip())
    return lines


def is_metadata_update_line(line: str) -> bool:
    return bool(METADATA_UPDATE_RE.match(line.strip()))


def metadata_only_change(commit: str, path: str) -> bool:
    changed_lines = [line for line in diff_changed_content_lines(commit, path) if line]
    return bool(changed_lines) and all(is_metadata_update_line(line) for line in changed_lines)


def metadata_only_across_commits(commits: list[str], path: str) -> bool:
    touched = False
    for commit in commits:
        changed_lines = [line for line in diff_changed_content_lines(commit, path) if line]
        if not changed_lines:
            continue
        touched = True
        if not all(is_metadata_update_line(line) for line in changed_lines):
            return False
    return touched


def commit_is_metadata_maintenance(commit: str, files: list[ChangedFile]) -> bool:
    changed = [item for item in files if item.status.startswith("M")]
    if not changed:
        return False
    if not all(PERMANENT_RE.match(item.path) for item in changed):
        return False
    return all(metadata_only_change(commit, item.path) for item in changed)


def classify_commit(subject: str, files: list[ChangedFile], commit: str | None = None) -> str:
    subject_lower = subject.lower()
    paths = [item.path for item in files]
    all_paths = paths + [item.old_path for item in files if item.old_path]

    touches_audit = any(path and path.startswith("00_System/audits/") for path in all_paths)
    touches_permanent = any(path and PERMANENT_RE.match(path) for path in all_paths)
    touches_knowledge = any(
        path
        and (
            path.startswith("02_IA/")
            or (path.startswith("01_Collecte/sources_brutes/") and "/traitees/" in path)
        )
        for path in all_paths
    )
    touches_protocol = any(
        path
        and (
            path.startswith("00_System/")
            or path.startswith("03_Frameworks/")
            or path.startswith("04_Templates/")
        )
        for path in all_paths
    )

    if touches_audit or "audit" in subject_lower:
        return COMMIT_CLASSES["audit"]
    if commit and commit_is_metadata_maintenance(commit, files):
        return COMMIT_CLASSES["maintenance"]
    if not touches_permanent and (
        "rename processed" in subject_lower
        or "move processed" in subject_lower
        or "source renaming" in subject_lower
    ):
        return COMMIT_CLASSES["maintenance"]
    if touches_knowledge or touches_permanent:
        return COMMIT_CLASSES["knowledge"]
    if touches_protocol or "protocol" in subject_lower or "system" in subject_lower or "aos" in subject_lower:
        return COMMIT_CLASSES["protocol"]
    return COMMIT_CLASSES["maintenance"]


def commit_infos(commit_lines: list[str]) -> list[CommitInfo]:
    infos: list[CommitInfo] = []
    for line in commit_lines:
        parts = line.split("\t", 3)
        if len(parts) != 4:
            continue
        full_hash, short_hash, date, subject = parts
        files = changed_files_for_commit(full_hash)
        infos.append(
            CommitInfo(
                full_hash=full_hash,
                short_hash=short_hash,
                date=date,
                subject=subject,
                classification=classify_commit(subject, files, full_hash),
                files=files,
            )
        )
    return infos


def read_text(path: str) -> str:
    file_path = Path(path)
    if not file_path.exists() or not file_path.is_file():
        return ""
    return file_path.read_text(encoding="utf-8", errors="replace")


def normalize_for_matching(text: str) -> str:
    """Normalize case and accents without losing word or line boundaries."""
    decomposed = unicodedata.normalize("NFKD", text)
    return "".join(char for char in decomposed if not unicodedata.combining(char)).lower()


def whole_term_pattern(term: str) -> re.Pattern[str]:
    parts = [re.escape(part) for part in normalize_for_matching(term).strip().split()]
    expression = r"\s+".join(parts)
    return re.compile(rf"(?<!\w){expression}(?!\w)", re.IGNORECASE)


def lexical_matches(
    path: str, terms: tuple[str, ...], *, section_mode: str = "all"
) -> list[LexicalMatch]:
    """Find complete terms and retain the triggering section and passage."""
    patterns = [(term, whole_term_pattern(term)) for term in terms]
    matches: list[LexicalMatch] = []
    section = "Hors section"
    normalized_section = ""
    allowed_sections = tuple(normalize_for_matching(term) for term in UNCERTAINTY_ALLOWED_SECTION_TERMS)
    strong_sections = tuple(normalize_for_matching(term) for term in STRONG_SECTION_TERMS)

    for line_number, line in enumerate(read_text(path).splitlines(), start=1):
        stripped = line.strip()
        normalized_line = normalize_for_matching(stripped)
        if stripped.startswith("#"):
            section = stripped.lstrip("#").strip() or "Hors section"
            normalized_section = normalize_for_matching(section)
            continue

        in_allowed = any(term in normalized_section for term in allowed_sections)
        in_strong = any(term in normalized_section for term in strong_sections)
        if section_mode == "outside_allowed" and in_allowed:
            continue
        if section_mode == "strong" and not in_strong:
            continue
        for term, pattern in patterns:
            if pattern.search(normalized_line):
                matches.append(LexicalMatch(term, line_number, stripped, section))
    return matches


def lexical_observation(prefix: str, match: LexicalMatch) -> str:
    passage = match.passage if len(match.passage) <= 180 else f"{match.passage[:177]}..."
    return (
        f'{prefix} Terme : "{match.term}" ; section : "{match.section}" ; '
        f'ligne {match.line_number} : "{passage}".'
    )


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


def files_for_knowledge_audit(infos: list[CommitInfo]) -> list[ChangedFile]:
    files: list[ChangedFile] = []
    for info in infos:
        if info.classification == COMMIT_CLASSES["knowledge"]:
            files.extend(info.files)
            continue
        files.extend([item for item in info.files if PERMANENT_RE.match(item.path)])
    return dedupe_changed_files(files)


def commits_for_knowledge_audit(infos: list[CommitInfo]) -> list[str]:
    commits: list[str] = []
    for info in infos:
        if info.classification == COMMIT_CLASSES["knowledge"] or any(
            PERMANENT_RE.match(item.path) for item in info.files
        ):
            commits.append(info.full_hash)
    return commits


def commit_message(commit: str) -> str:
    return run_git(["show", "-s", "--format=%s%n%b", commit], check=False)


def commit_declares_duplicate(commit: str) -> bool:
    """Require an explicit duplicate trace; topic similarity is never evidence."""
    message = normalize_for_matching(commit_message(commit))
    return "doublon" in message or "duplicate" in message


def source_blob_at_commit(commit: str, path: str) -> str:
    return run_git(["rev-parse", f"{commit}:{path}"], check=False)


def exact_duplicate_evidence(commit: str, path: str) -> ExactDuplicateEvidence | None:
    """Return provenance only for a declared, byte-identical, already-watched source.

    A matching Git blob is the exact-duplicate proof.  A prior processed source and
    a watch note created in that same earlier treatment identify the capitalisation
    that is being reused.  No lexical or topical comparison is used.
    """
    if not commit_declares_duplicate(commit):
        return None
    blob = source_blob_at_commit(commit, path)
    if not blob:
        return None

    # Search only the history preceding the archiving commit: the current source
    # cannot validate itself.
    previous_commits = run_git(
        ["log", f"{commit}^", "--find-object", blob, "--format=%H"], check=False
    ).splitlines()
    for previous_commit in previous_commits:
        previous_files = changed_files_for_commit(previous_commit)
        previous_sources = [
            item.path
            for item in previous_files
            if "/traitees/" in item.path
            and item.path.startswith("01_Collecte/sources_brutes/")
            and source_blob_at_commit(previous_commit, item.path) == blob
        ]
        existing_watches = [
            item.path for item in previous_files if item.status.startswith("A") and WATCH_RE.match(item.path)
        ]
        if previous_sources and existing_watches:
            return ExactDuplicateEvidence(previous_sources[0], existing_watches[0])
    return None


def recognized_exact_duplicates(
    files: list[ChangedFile], commits: list[str]
) -> dict[str, ExactDuplicateEvidence]:
    recognized: dict[str, ExactDuplicateEvidence] = {}
    for item in classify_files(files)["processed_sources"]:
        for commit in commits:
            if not any(changed.path == item.path for changed in changed_files_for_commit(commit)):
                continue
            evidence = exact_duplicate_evidence(commit, item.path)
            if evidence:
                recognized[item.path] = evidence
                break
    return recognized


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
        is_metadata_only = metadata_only_across_commits(commits, item.path)
        if is_metadata_only:
            alerts.append(
                Alert(
                    level="faible",
                    category="maintenance metadata",
                    path=item.path,
                    observation="Modification limitee a la ligne de derniere mise a jour.",
                    recommendation="Aucune action Aion prioritaire requise.",
                )
            )
            continue
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
        speculation_matches = speculation_matches_requiring_review(item.path)
        if speculation_matches:
            match = speculation_matches[0]
            alerts.append(
                Alert(
                    level="moyen",
                    category="speculation",
                    path=item.path,
                    observation=lexical_observation(
                        "Formulation speculative detectee dans une section forte.", match
                    ),
                    recommendation="Verifier que ces elements restent en points a surveiller et ne sont pas presentes comme faits valides.",
                )
            )
        marketing_matches = lexical_matches(item.path, MARKETING_TERMS)
        if marketing_matches:
            match = marketing_matches[0]
            alerts.append(
                Alert(
                    level="moyen",
                    category="marketing integre",
                    path=item.path,
                    observation=lexical_observation(
                        "Terme marketing ou sponsorise detecte dans une fiche permanente.", match
                    ),
                    recommendation="Verifier que le marketing est exclu des connaissances durables.",
                )
            )

    for item in classes["transversal_modified"]:
        if metadata_only_across_commits(commits, item.path):
            continue
        alerts.append(
            Alert(
                level="eleve",
                category="modification abusive des fiches transversales",
                path=item.path,
                observation="Fiche transversale modifiee dans la periode auditee.",
                recommendation="Verifier que la source apporte une regle generale durable, pas une mention secondaire.",
            )
        )

    exact_duplicates = recognized_exact_duplicates(files, commits)
    for item in classes["processed_sources"]:
        source_topic = Path(item.path).stem.replace("_transcript", "")
        has_watch = any(WATCH_RE.match(f.path) for f in files)
        if not has_watch and item.path not in exact_duplicates:
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


def audit_decision(priority_alerts: list[Alert]) -> str:
    if any(alert.level == "bloquant" for alert in priority_alerts):
        return "Blocage"
    if any(alert.level == "eleve" for alert in priority_alerts):
        return "Audit Aion recommande"
    if any(alert.level == "moyen" for alert in priority_alerts):
        return "GO partiel"
    return "GO"


def priority_risk(priority_alerts: list[Alert]) -> str:
    if not priority_alerts:
        return "faible"
    return highest_risk(priority_alerts)


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


def format_commits(infos: list[CommitInfo]) -> str:
    rows = []
    for info in infos:
        rows.append(f"- `{info.short_hash}` - {info.date} - {info.classification} - {info.subject}")
    return "\n".join(rows) if rows else "- Aucun commit analyse."


def format_git_analysis_method(infos: list[CommitInfo]) -> str:
    return "\n".join(
        [
            f"- Nombre de commits analyses : {len(infos)}",
            "- Methode fichiers : git diff-tree --no-commit-id --name-status -r <commit>",
            "- Base de comparaison : parent direct de chaque commit analyse.",
            "- Aggregation : union dedupliquee des fichiers retournes par chaque commit analyse.",
        ]
    )


def format_commits_by_class(infos: list[CommitInfo], classification: str) -> str:
    selected = [info for info in infos if info.classification == classification]
    if not selected:
        return "- Aucun commit."
    return "\n".join(f"- `{info.short_hash}` - {info.date} - {info.subject}" for info in selected)


def format_ignored_commits(infos: list[CommitInfo]) -> str:
    ignored = [
        info
        for info in infos
        if info.classification
        in {
            COMMIT_CLASSES["protocol"],
            COMMIT_CLASSES["maintenance"],
            COMMIT_CLASSES["audit"],
        }
    ]
    if not ignored:
        return "- Aucun commit ignore pour audit connaissance."
    return "\n".join(
        f"- `{info.short_hash}` - {info.date} - {info.classification} - {info.subject}"
        for info in ignored
    )


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


def format_exact_duplicates(duplicates: dict[str, ExactDuplicateEvidence]) -> str:
    if not duplicates:
        return "- Aucun doublon exact accepte detecte."
    return "\n".join(
        f"- Source : `{source}` - Statut : doublon exact accepte - "
        f"Source deja capitalisee : `{evidence.original_source_path}` - "
        f"Fiche de veille existante : `{evidence.existing_watch_path}`."
        for source, evidence in sorted(duplicates.items())
    )


def subject_tokens(path: str) -> set[str]:
    parts = re.split(r"[/_.\-\s]+", path.lower())
    return {part for part in parts if len(part) >= 4 and part not in {"fiche", "permanente", "veille"}}


def touches_alert_subject(info: CommitInfo, alert: Alert) -> bool:
    alert_tokens = subject_tokens(alert.path)
    paths = [item.path for item in info.files] + [item.old_path for item in info.files if item.old_path]
    if alert.path in paths:
        return True
    haystack = " ".join([info.subject.lower(), *(path.lower() for path in paths if path)])
    return any(token in haystack for token in alert_tokens)


def correction_touches_alert(info: CommitInfo, alert: Alert) -> bool:
    subject = info.subject.lower()
    return any(term in subject for term in CORRECTION_TERMS) and touches_alert_subject(info, alert)


def alert_treated_or_attenuated(alert: Alert, infos: list[CommitInfo]) -> bool:
    if alert.level == "bloquant":
        return False
    matching_indexes = [index for index, info in enumerate(infos) if touches_alert_subject(info, alert)]
    if len(matching_indexes) < 2:
        return False
    newest_matching_index = min(matching_indexes)
    return correction_touches_alert(infos[newest_matching_index], alert)


def text_in_strong_section(path: str, terms: tuple[str, ...]) -> bool:
    return bool(lexical_matches(path, terms, section_mode="strong"))


def speculation_terms_outside_allowed_sections(path: str) -> bool:
    return bool(lexical_matches(path, SPECULATION_TERMS, section_mode="outside_allowed"))


def speculation_matches_requiring_review(path: str) -> list[LexicalMatch]:
    """Weak/monitoring sections are contextual; strong knowledge sections are reviewable."""
    return lexical_matches(path, SPECULATION_TERMS, section_mode="strong")


def is_priority_candidate(alert: Alert) -> bool:
    if alert.level == "bloquant":
        return True
    if alert.category == "creation abusive de fiche permanente":
        return True
    if alert.category == "modification abusive des fiches transversales":
        return True
    if alert.category == "sur-enrichissement" and alert.path.startswith(MAJOR_PREFIXES):
        return True
    if alert.category == "speculation":
        return text_in_strong_section(alert.path, SPECULATION_TERMS)
    return False


def split_aion_alerts(alerts: list[Alert], infos: list[CommitInfo]) -> tuple[list[Alert], list[Alert]]:
    priority: list[Alert] = []
    treated: list[Alert] = []
    for alert in alerts:
        if alert_treated_or_attenuated(alert, infos):
            treated.append(alert)
        elif is_priority_candidate(alert):
            priority.append(alert)

    priority.sort(
        key=lambda alert: (
            -RISK_ORDER[alert.level],
            QUALITY_ALERT_CATEGORY_ORDER.get(alert.category, 99),
            alert.path,
        )
    )
    treated.sort(
        key=lambda alert: (
            -RISK_ORDER[alert.level],
            QUALITY_ALERT_CATEGORY_ORDER.get(alert.category, 99),
            alert.path,
        )
    )
    return priority[:7], treated


def priority_alerts(alerts: list[Alert], infos: list[CommitInfo]) -> list[Alert]:
    priority, _ = split_aion_alerts(alerts, infos)
    return priority


def format_aion_alerts(alerts: list[Alert], empty: str) -> str:
    if not alerts:
        return f"- {empty}"
    return "\n".join(
        f"- {alert.level} - `{alert.path}` - {alert.category} : {alert.observation} "
        f"Recommandation : {alert.recommendation}"
        for alert in alerts
    )


def format_treated_alerts(alerts: list[Alert]) -> str:
    if not alerts:
        return "- Aucune alerte traitee ou attenuee detectee."
    return "\n".join(
        f"- Traite / a verifier - {alert.level} - `{alert.path}` - {alert.category} : {alert.observation}"
        for alert in alerts
    )


def legacy_priority_alerts(alerts: list[Alert], minimum: int = 3, maximum: int = 7) -> list[Alert]:
    actionable = [alert for alert in alerts if alert.level != "faible"]
    actionable.sort(
        key=lambda alert: (
            -RISK_ORDER[alert.level],
            QUALITY_ALERT_CATEGORY_ORDER.get(alert.category, 99),
            alert.path,
        )
    )
    if len(actionable) <= maximum:
        return actionable
    return actionable[: max(minimum, maximum)]


def format_priority_alerts(alerts: list[Alert]) -> str:
    selected = legacy_priority_alerts(alerts)
    if not selected:
        return "- Aucune alerte prioritaire."
    return "\n".join(
        f"- {alert.level} - `{alert.path}` - {alert.category} : {alert.observation} "
        f"Recommandation : {alert.recommendation}"
        for alert in selected
    )


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
    infos = commit_infos(commits_lines)
    commits = commit_hashes(commits_lines)
    files = changed_files_for_commits(commits)
    knowledge_files = files_for_knowledge_audit(infos)
    knowledge_commits = commits_for_knowledge_audit(infos)
    exact_duplicates = recognized_exact_duplicates(knowledge_files, knowledge_commits)
    classes = classify_files(files)
    alerts = detect_alerts(knowledge_files, knowledge_commits)
    aion_priority_alerts, treated_alerts = split_aion_alerts(alerts, infos)
    risk = highest_risk(alerts)
    decision = audit_decision(aion_priority_alerts)
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
        "{{a_traiter_par_aion}}": format_aion_alerts(aion_priority_alerts, "Aucune alerte prioritaire."),
        "{{alertes_traitees_ou_attenuees}}": format_treated_alerts(treated_alerts),
        "{{nombre_alertes_prioritaires}}": str(len(aion_priority_alerts)),
        "{{nombre_alertes_traitees_ou_attenuees}}": str(len(treated_alerts)),
        "{{nombre_alertes_total}}": str(len(alerts)),
        "{{commits_analyses}}": format_commits(infos),
        "{{commits_knowledge_batch}}": format_commits_by_class(infos, COMMIT_CLASSES["knowledge"]),
        "{{commits_protocol_system}}": format_commits_by_class(infos, COMMIT_CLASSES["protocol"]),
        "{{commits_maintenance}}": format_commits_by_class(infos, COMMIT_CLASSES["maintenance"]),
        "{{commits_audit}}": format_commits_by_class(infos, COMMIT_CLASSES["audit"]),
        "{{commits_ignores_audit_connaissance}}": format_ignored_commits(infos),
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
    method_section = f"\n## Méthode d’analyse Git\n\n{format_git_analysis_method(infos)}\n"
    report = report.replace("\n## Fichiers crees\n", f"{method_section}\n## Fichiers crees\n")
    duplicate_section = f"\n## Doublons exacts acceptes\n\n{format_exact_duplicates(exact_duplicates)}\n"
    report = report.replace("\n## Fichiers crees\n", f"{duplicate_section}\n## Fichiers crees\n")
    return report


def write_report(report: str, date: dt.date | None = None, suffix: str = "") -> Path:
    report_date = date or dt.date.today()
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    normalized_suffix = suffix if not suffix or suffix.startswith("-") else f"-{suffix}"
    output = REPORT_DIR / f"{report_date:%Y-%m-%d}_audit-journalier-aos{normalized_suffix}.md"
    output.write_text(report, encoding="utf-8", newline="\n")
    return output


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a passive AOS daily audit report.")
    parser.add_argument("--since-hours", type=int, default=24, help="Git commit lookback window.")
    parser.add_argument("--fallback-count", type=int, default=10, help="Recent commits to inspect if 24h is empty.")
    parser.add_argument("--suffix", default="", help="Optional suffix added before the .md extension.")
    parser.add_argument("--print-path", action="store_true", help="Print generated report path.")
    args = parser.parse_args()

    report = render_report(args.since_hours, args.fallback_count)
    output = write_report(report, suffix=args.suffix)
    if args.print_path:
        print(output.as_posix())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
