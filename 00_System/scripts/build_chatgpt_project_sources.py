from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
IA_ROOT = ROOT / "02_IA"
OUT_ROOT = ROOT / "99_ChatGPT_Project_Sources"
OUT_FICHES = OUT_ROOT / "fiches_permanentes"

ALLOWED_STATUS = ("Validé", "Partiel", "À surveiller", "Obsolète")


@dataclass
class PermanentFiche:
    name: str
    source_path: Path
    rel_source: str
    slug: str
    status: str
    title: str
    sections: dict[str, str]

    @property
    def generated_file(self) -> str:
        return f"fiches_permanentes/{self.slug}.md"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8", newline="\n")


def slugify(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    normalized = normalized.lower()
    normalized = re.sub(r"[^a-z0-9]+", "-", normalized).strip("-")
    return normalized or "fiche"


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def parse_sections(text: str) -> tuple[str, dict[str, str]]:
    lines = text.splitlines()
    title = lines[0].lstrip("# ").strip() if lines else "Fiche permanente"
    sections: dict[str, list[str]] = {}
    current: str | None = None
    for line in lines[1:]:
        match = re.match(r"^##\s+(.+?)\s*$", line)
        if match:
            current = match.group(1).strip()
            sections[current] = []
            continue
        if current:
            sections[current].append(line)
    return title, {key: "\n".join(value).strip() for key, value in sections.items()}


def find_section(sections: dict[str, str], needle: str) -> str:
    needle = needle.lower()
    for key, value in sections.items():
        if needle in key.lower():
            return value
    return ""


def first_signal(text: str, fallback: str = "Information non renseignée dans la fiche permanente.") -> str:
    clean = text.strip()
    if not clean:
        return fallback
    for paragraph in re.split(r"\n\s*\n", clean):
        stripped = paragraph.strip()
        if stripped and not stripped.startswith("#"):
            return " ".join(stripped.split())
    return fallback


def status_for(sections: dict[str, str]) -> str:
    combined = "\n".join(sections.values()).lower()
    use_cases = find_section(sections, "cas d'usage valides").lower()
    identity = find_section(sections, "fiche d'identite").lower()
    if "obsol" in combined:
        return "Obsolète"
    if "aucun cas d'usage" in use_cases or "en veille" in identity or "a evaluer" in combined or "à evaluer" in combined:
        return "À surveiller"
    if any(not value.strip() for value in sections.values()):
        return "Partiel"
    return "Validé"


def load_fiches() -> list[PermanentFiche]:
    fiches: list[PermanentFiche] = []
    for path in sorted(IA_ROOT.glob("*/fiche_permanente.md")):
        text = read_text(path)
        title, sections = parse_sections(text)
        name = title.replace("- Fiche permanente", "").strip()
        fiches.append(
            PermanentFiche(
                name=name,
                source_path=path,
                rel_source=rel(path),
                slug=slugify(name),
                status=status_for(sections),
                title=title,
                sections=sections,
            )
        )
    return fiches


def md_link(fiche: PermanentFiche) -> str:
    return f"[{fiche.name}]({fiche.generated_file})"


def sanitize_section(content: str, fiche: PermanentFiche, label: str) -> str:
    if "fiche d'identite" not in label.lower():
        return content
    lines = []
    replaced = False
    for line in content.splitlines():
        if re.match(r"^\s*-\s*Statut dans la base\s*:", line, flags=re.IGNORECASE):
            lines.append(f"- Statut normalisé Aion : {fiche.status}")
            replaced = True
        else:
            lines.append(line)
    if not replaced:
        lines.append(f"- Statut normalisé Aion : {fiche.status}")
    return "\n".join(lines).strip()


def section_block(fiche: PermanentFiche, label: str) -> str:
    content = find_section(fiche.sections, label)
    if not content:
        content = "Information non renseignée dans la fiche permanente."
    else:
        content = sanitize_section(content, fiche, label)
    return f"## {label}\n\nSource permanente : `{fiche.rel_source}`.\n\n{content}"


def build_mode_emploi(fiches: list[PermanentFiche]) -> str:
    return f"""# AION - Mode d'emploi des sources projet

## Objectif

Ce dossier est une projection synthétique de la BDD IA AOS pour upload manuel dans les Sources du projet ChatGPT "AI Operating System - BDD IA".

Il permet à Aion d'interroger les connaissances IA validées ou explicitement marquées à surveiller, sans accès direct GitHub.

## Règles d'utilisation

- Prioriser `02_CATALOGUE_IA.md` pour identifier une IA, son statut et sa fiche permanente source.
- Utiliser `03_INDEX_CAS_USAGE.md` pour choisir un outil par besoin.
- Utiliser `04_INDEX_ORCHESTRATION.md` pour raisonner sur les rôles multi-IA et les garde-fous.
- Utiliser `05_STANDARDS_STRATEGIQUES.md` pour appliquer les règles AOS de qualité, validation et décision.
- Ne pas traiter une fiche de veille comme vérité. Les veilles ne sont pas incluses dans ce dossier.
- En cas d'incertitude, répondre avec le statut `À surveiller` et citer la fiche permanente source.

## Statuts normalisés

- `Validé` : connaissance consolidée et exploitable.
- `Partiel` : connaissance utile mais incomplète.
- `À surveiller` : connaissance présente dans une fiche permanente mais dépendante de validation, test, recoupement ou suivi.
- `Obsolète` : connaissance conservée pour mémoire mais à ne pas utiliser comme recommandation active.

## Périmètre

- Nombre de fiches permanentes IA projetées : {len(fiches)}.
- Source primaire : `02_IA/*/fiche_permanente.md`.
- Exclusions : `veille/`, `00_System/audits/daily/`, sources brutes, transcriptions, audits quotidiens.

## Fichiers principaux

- [Index global AOS](01_INDEX_GLOBAL_AOS.md)
- [Catalogue IA](02_CATALOGUE_IA.md)
- [Index cas d'usage](03_INDEX_CAS_USAGE.md)
- [Index orchestration](04_INDEX_ORCHESTRATION.md)
- [Standards stratégiques](05_STANDARDS_STRATEGIQUES.md)
"""


def build_global_index(fiches: list[PermanentFiche]) -> str:
    rows = "\n".join(
        f"- {md_link(fiche)} - Statut : `{fiche.status}` - Source : `{fiche.rel_source}`"
        for fiche in fiches
    )
    return f"""# Index global AOS pour projet ChatGPT

## Périmètre

Projection synthétique générée depuis les fiches permanentes IA. Les fiches de veille et les audits quotidiens sont exclus.

## Navigation

- [Mode d'emploi](00_AION_MODE_EMPLOI.md)
- [Catalogue IA](02_CATALOGUE_IA.md)
- [Index cas d'usage](03_INDEX_CAS_USAGE.md)
- [Index orchestration](04_INDEX_ORCHESTRATION.md)
- [Standards stratégiques](05_STANDARDS_STRATEGIQUES.md)

## Fiches permanentes projetées

{rows}
"""


def build_catalogue(fiches: list[PermanentFiche]) -> str:
    rows = []
    for fiche in fiches:
        role = first_signal(find_section(fiche.sections, "role principal"))
        usage = first_signal(find_section(fiche.sections, "cas d'usage valides"))
        rows.append(f"| {md_link(fiche)} | {fiche.status} | {role} | {usage} | `{fiche.rel_source}` |")
    return """# Catalogue IA

## Règle de lecture

Le catalogue référence chaque fiche permanente IA disponible dans `02_IA`. Le statut est normalisé pour usage Aion.

| IA | Statut | Rôle principal | Cas d'usage validés ou position actuelle | Fiche permanente source |
| --- | --- | --- | --- | --- |
""" + "\n".join(rows) + "\n"


def build_usage_index(fiches: list[PermanentFiche]) -> str:
    blocks = ["# Index des cas d'usage\n"]
    for fiche in fiches:
        blocks.append(f"## {fiche.name}\n")
        blocks.append(f"- Statut : `{fiche.status}`")
        blocks.append(f"- Fiche projet : {md_link(fiche)}")
        blocks.append(f"- Fiche permanente source : `{fiche.rel_source}`\n")
        for label in ("Cas d'usage valides", "Cas d'usage a eviter", "Workflows recommandes", "Prompts & methodes"):
            content = find_section(fiche.sections, label)
            blocks.append(f"### {label}\n\n{content or 'Information non renseignée dans la fiche permanente.'}\n")
    return "\n".join(blocks)


def build_orchestration_index(fiches: list[PermanentFiche]) -> str:
    blocks = ["# Index orchestration IA\n"]
    for fiche in fiches:
        orch = find_section(fiche.sections, "orchestration ia")
        integration = find_section(fiche.sections, "integration dans mon ecosysteme")
        if not orch and not integration:
            continue
        blocks.append(f"## {fiche.name}\n")
        blocks.append(f"- Statut : `{fiche.status}`")
        blocks.append(f"- Fiche projet : {md_link(fiche)}")
        blocks.append(f"- Fiche permanente source : `{fiche.rel_source}`\n")
        blocks.append(f"### Orchestration IA\n\n{orch or 'Information non renseignée dans la fiche permanente.'}\n")
        blocks.append(f"### Intégration AOS\n\n{integration or 'Information non renseignée dans la fiche permanente.'}\n")
    return "\n".join(blocks)


def build_standards() -> str:
    sources = [
        ("Qualité de connaissance", "07_Standards/knowledge_quality_standard.md", [
            "Distinguer fait vérifié, retour d'expérience, hypothèse et contenu marketing.",
            "Conserver les informations non validées dans les fiches de veille.",
            "Intégrer dans les fiches permanentes uniquement les différences validées.",
            "Préférer une synthèse exploitable à une accumulation de notes.",
        ]),
        ("Processing", "03_Frameworks/knowledge_processing/README.md", [
            "Une source passe par collecte, qualification, extraction, analyse, validation et capitalisation.",
            "Les informations urgentes mais non validées restent marquées à surveiller.",
        ]),
        ("Organisation", "03_Frameworks/knowledge_organization/README.md", [
            "Les fiches permanentes sont la couche de vérité consolidée.",
            "Les doublons, contradictions et éléments obsolètes doivent être traités explicitement.",
        ]),
        ("Décision", "03_Frameworks/knowledge_decision/README.md", [
            "Les décisions IA doivent tracer le besoin, les critères, les risques et l'arbitrage.",
            "Les statuts opérationnels doivent permettre GO, NO GO ou À surveiller.",
        ]),
        ("Instructions agents", "99_System/agents/instructions_agents.md", [
            "Les agents exécutent le workflow AOS et ne redéfinissent pas l'architecture.",
            "Le chemin de référence est Source -> Collecte -> Qualification -> Fiche de veille -> Validation -> Fiche permanente -> Archivage.",
        ]),
    ]
    blocks = ["# Standards stratégiques AOS\n"]
    for title, source, points in sources:
        blocks.append(f"## {title}\n")
        blocks.append(f"Source : `{source}`.\n")
        blocks.extend(f"- {point}" for point in points)
        blocks.append("")
    blocks.append("## Règle spécifique aux Sources projet ChatGPT\n")
    blocks.append("- Les fiches de veille ne sont jamais importées comme vérité dans `99_ChatGPT_Project_Sources`.")
    blocks.append("- Toute information issue d'une fiche permanente garde un pointeur vers sa fiche permanente source.")
    blocks.append("- Les statuts utilisables par Aion sont strictement : `Validé`, `Partiel`, `À surveiller`, `Obsolète`.")
    return "\n".join(blocks)


def build_projection(fiche: PermanentFiche) -> str:
    blocks = [
        f"# {fiche.name} - Source projet ChatGPT",
        "",
        "## Traçabilité",
        "",
        f"- Statut normalisé : `{fiche.status}`",
        f"- Fiche permanente source : `{fiche.rel_source}`",
        "- Type : projection synthétique depuis fiche permanente AOS",
        "- Exclusion : aucune fiche de veille n'est copiée dans ce fichier",
        "",
    ]
    for label in (
        "Fiche d'identite",
        "Role principal",
        "Architecture",
        "Forces",
        "Faiblesses",
        "Cas d'usage valides",
        "Cas d'usage a eviter",
        "Workflows recommandes",
        "Prompts & methodes",
        "Integration dans mon ecosysteme",
        "Orchestration IA",
        "Evolutions",
        "Decisions strategiques",
    ):
        blocks.append(section_block(fiche, label))
        blocks.append("")
    return "\n".join(blocks)


def main() -> None:
    fiches = load_fiches()
    OUT_FICHES.mkdir(parents=True, exist_ok=True)

    write_text(OUT_ROOT / "00_AION_MODE_EMPLOI.md", build_mode_emploi(fiches))
    write_text(OUT_ROOT / "01_INDEX_GLOBAL_AOS.md", build_global_index(fiches))
    write_text(OUT_ROOT / "02_CATALOGUE_IA.md", build_catalogue(fiches))
    write_text(OUT_ROOT / "03_INDEX_CAS_USAGE.md", build_usage_index(fiches))
    write_text(OUT_ROOT / "04_INDEX_ORCHESTRATION.md", build_orchestration_index(fiches))
    write_text(OUT_ROOT / "05_STANDARDS_STRATEGIQUES.md", build_standards())
    for fiche in fiches:
        write_text(OUT_FICHES / f"{fiche.slug}.md", build_projection(fiche))

    print(f"Generated {OUT_ROOT.relative_to(ROOT)} with {len(fiches)} permanent IA fiches.")


if __name__ == "__main__":
    main()
