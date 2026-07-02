from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[2]
IA_ROOT = ROOT / "02_IA"
OUT_ROOT = ROOT / "99_ChatGPT_Project_Sources"
CATALOGUE = OUT_ROOT / "02_CATALOGUE_IA.md"
ALLOWED_STATUS = {"Validé", "Partiel", "À surveiller", "Obsolète"}


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def audit_catalogue(errors: list[str]) -> None:
    if not CATALOGUE.exists():
        fail(errors, "Catalogue manquant : 99_ChatGPT_Project_Sources/02_CATALOGUE_IA.md")
        return
    catalogue = read_text(CATALOGUE)
    for fiche in sorted(IA_ROOT.glob("*/fiche_permanente.md")):
        source = rel(fiche)
        if source not in catalogue:
            fail(errors, f"Fiche permanente non référencée dans le catalogue : {source}")


def audit_no_watch_or_daily_files(errors: list[str]) -> None:
    if not OUT_ROOT.exists():
        fail(errors, "Dossier Project Sources manquant : 99_ChatGPT_Project_Sources")
        return
    for path in OUT_ROOT.rglob("*"):
        if not path.is_file():
            continue
        normalized = rel(path).lower()
        if "/veille/" in normalized or "\\veille\\" in normalized or "veille" in path.parts:
            fail(errors, f"Fichier de veille inclus dans Project Sources : {rel(path)}")
        if "/audits/daily/" in normalized or "\\audits\\daily\\" in normalized:
            fail(errors, f"Audit quotidien inclus dans Project Sources : {rel(path)}")


def audit_statuses(errors: list[str]) -> None:
    status_pattern = re.compile(r"(?:Statut(?: normalisé)?\s*:\s*`?)([^`\n|]+)")
    for path in OUT_ROOT.rglob("*.md"):
        text = read_text(path)
        if re.search(r"Statut dans la base\s*:", text, flags=re.IGNORECASE):
            fail(errors, f"Statut source brut non normalisé dans {rel(path)}")
        for match in status_pattern.finditer(text):
            raw = match.group(1).strip().strip("`").strip()
            status = raw.split("|", 1)[0].strip()
            if status and status not in ALLOWED_STATUS:
                fail(errors, f"Statut non normalisé dans {rel(path)} : {status}")
        if path.name == "02_CATALOGUE_IA.md":
            for line in text.splitlines():
                if not line.startswith("| ["):
                    continue
                cells = [cell.strip().strip("`") for cell in line.strip("|").split("|")]
                if len(cells) >= 2 and cells[1] not in ALLOWED_STATUS:
                    fail(errors, f"Statut catalogue non normalisé dans {rel(path)} : {cells[1]}")


def markdown_links(text: str) -> list[str]:
    links = []
    for match in re.finditer(r"(?<!!)\[[^\]]+\]\(([^)]+)\)", text):
        target = match.group(1).strip()
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        links.append(target)
    return links


def audit_internal_links(errors: list[str]) -> None:
    for path in OUT_ROOT.rglob("*.md"):
        text = read_text(path)
        for target in markdown_links(text):
            target_path = unquote(target.split("#", 1)[0]).strip()
            if not target_path:
                continue
            resolved = (path.parent / target_path).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                fail(errors, f"Lien sortant non autorisé dans {rel(path)} : {target}")
                continue
            if not resolved.exists():
                fail(errors, f"Lien interne invalide dans {rel(path)} : {target}")


def main() -> int:
    errors: list[str] = []
    audit_catalogue(errors)
    audit_no_watch_or_daily_files(errors)
    audit_statuses(errors)
    audit_internal_links(errors)

    if errors:
        print("Audit Project Sources : ÉCHEC")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Audit Project Sources : OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
