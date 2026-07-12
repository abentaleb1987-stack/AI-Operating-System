import importlib.util
import sys
import unittest
from pathlib import Path
from unittest.mock import patch


SCRIPT_PATH = Path(__file__).parents[1] / "aos_daily_audit.py"
SPEC = importlib.util.spec_from_file_location("aos_daily_audit", SCRIPT_PATH)
audit = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class LexicalDetectionTests(unittest.TestCase):
    def matches(self, text, terms=audit.MARKETING_TERMS, section_mode="all"):
        with patch.object(audit, "read_text", return_value=text):
            return audit.lexical_matches("ignored.md", terms, section_mode=section_mode)

    def test_formation_is_detected_as_a_complete_marketing_term(self):
        matches = self.matches("## Offre\nUne formation pratique.")
        self.assertEqual([match.term for match in matches], ["formation"])

    def test_transformation_does_not_match_formation(self):
        self.assertEqual(self.matches("## Forces\nUne transformation fiable."), [])

    def test_multiword_term_is_case_insensitive(self):
        matches = self.matches("## Offre\nLANDING   PAGE documentee.")
        self.assertEqual([match.term for match in matches], ["landing page"])

    def test_uncertainty_in_points_to_watch_is_not_priority(self):
        text = "## 12. Évolutions\n### Points à surveiller\nCette capacité pourrait évoluer."
        matches = self.matches(text, audit.SPECULATION_TERMS, section_mode="strong")
        self.assertEqual(matches, [])

    def test_speculative_statement_in_strong_section_is_detected(self):
        text = "## 4. Forces\nLes capacités futures sont garanties."
        matches = self.matches(text, audit.SPECULATION_TERMS, section_mode="strong")
        self.assertEqual([match.term for match in matches], ["capacites futures"])
        self.assertEqual(matches[0].section, "4. Forces")


class RiskSummaryTests(unittest.TestCase):
    @staticmethod
    def alert(level):
        return audit.Alert(level, "test", "file.md", "observation", "recommendation")

    def test_non_priority_medium_alert_still_sets_medium_maximum_risk(self):
        alerts = [self.alert("moyen")]
        priority, _ = audit.split_aion_alerts(alerts, [])
        self.assertEqual(priority, [])
        self.assertEqual(audit.highest_risk(alerts), "moyen")

    def test_no_anomaly_alert_sets_low_maximum_risk(self):
        self.assertEqual(audit.highest_risk([self.alert("faible")]), "faible")


class ProcessedSourceDuplicateTests(unittest.TestCase):
    SOURCE = "01_Collecte/sources_brutes/videos/traitees/2026-07-10_youtube_codex_workflow_aos_01.txt"
    WATCH = "02_IA/ChatGPT/veille/2026-07-10_youtube_melvynx_gpt-5-6-codex-comparatif-coding.md"
    ORIGINAL = (
        "01_Collecte/sources_brutes/videos/traitees/"
        "2026-07-10_youtube_melvynx_gpt-5-6-codex-comparatif-coding_transcript.txt"
    )

    def processed_source(self):
        return [audit.ChangedFile("A", self.SOURCE)]

    def blocking_alerts(self, files):
        return [
            alert
            for alert in audit.detect_alerts(files, ["archive-commit"])
            if alert.category == "source traitee sans veille" and alert.level == "bloquant"
        ]

    @patch.object(audit, "recognized_exact_duplicates", return_value={})
    def test_new_processed_source_without_watch_blocks(self, _duplicates):
        self.assertEqual(len(self.blocking_alerts(self.processed_source())), 1)

    @patch.object(audit, "recognized_exact_duplicates")
    def test_exact_duplicate_with_identifiable_existing_watch_does_not_block(self, duplicates):
        evidence = audit.ExactDuplicateEvidence(self.ORIGINAL, self.WATCH)
        duplicates.return_value = {self.SOURCE: evidence}
        self.assertEqual(self.blocking_alerts(self.processed_source()), [])
        trace = audit.format_exact_duplicates({self.SOURCE: evidence})
        self.assertIn("doublon exact accepte", trace)
        self.assertIn(self.WATCH, trace)

    @patch.object(audit, "recognized_exact_duplicates", return_value={})
    def test_declared_duplicate_without_existing_watch_proof_still_blocks(self, _duplicates):
        self.assertEqual(len(self.blocking_alerts(self.processed_source())), 1)

    @patch.object(audit, "recognized_exact_duplicates", return_value={})
    def test_similar_topic_is_not_an_exact_duplicate(self, _duplicates):
        similar = [
            audit.ChangedFile(
                "A",
                "01_Collecte/sources_brutes/videos/traitees/2026-07-10_youtube_melvynx_gpt-5-6-codex-similaire.txt",
            )
        ]
        self.assertEqual(len(self.blocking_alerts(similar)), 1)

    @patch.object(audit, "recognized_exact_duplicates")
    def test_reported_2026_07_10_duplicate_is_accepted(self, duplicates):
        duplicates.return_value = {
            self.SOURCE: audit.ExactDuplicateEvidence(self.ORIGINAL, self.WATCH)
        }
        self.assertEqual(self.blocking_alerts(self.processed_source()), [])


if __name__ == "__main__":
    unittest.main()
