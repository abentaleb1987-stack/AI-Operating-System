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


if __name__ == "__main__":
    unittest.main()
