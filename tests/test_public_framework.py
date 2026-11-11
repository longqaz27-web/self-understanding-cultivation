"""No external dependencies; editorial rather than clinical validity checks."""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCENARIOS = json.loads((ROOT/'scenarios/scenarios_v0.1.json').read_text(encoding='utf-8'))
SCHEMA = json.loads((ROOT/'schemas/episode.schema.json').read_text(encoding='utf-8'))
EXAMPLE = json.loads((ROOT/'examples/fictional_episode.json').read_text(encoding='utf-8'))

class OpenFrameworkTests(unittest.TestCase):
    def test_all_twelve_scenarios(self):
        self.assertEqual(len(SCENARIOS['items']), 12)
        self.assertEqual(len({x['id'] for x in SCENARIOS['items']}), 12)

    def test_every_choice_has_reasons_and_context(self):
        for item in SCENARIOS['items']:
            with self.subTest(item=item['id']):
                self.assertGreaterEqual(len(item['choices']), 3)
                self.assertEqual(item['scoring'], 'none')
                self.assertGreaterEqual(len(item['reflection_questions']), 3)
                self.assertTrue(item['context']['time_pressure'])
                for choice in item['choices']:
                    self.assertTrue(all(choice[k] for k in ['action','possible_benefit','possible_cost','fit_if']))

    def test_non_diagnostic_status_is_explicit(self):
        self.assertEqual(SCENARIOS['validation_status'],'not_psychometrically_validated')
        for name in ['README.md','docs/EVIDENCE_AND_PROFILE.md','docs/VALIDATION_PLAN.md']:
            self.assertTrue((ROOT/name).exists())
        self.assertIn('不能', (ROOT/'docs/EVIDENCE_AND_PROFILE.md').read_text(encoding='utf-8'))

    def test_example_declares_all_required_fields(self):
        self.assertTrue(set(SCHEMA['required']).issubset(EXAMPLE.keys()))
        self.assertTrue(set(SCHEMA['properties']['context']['required']).issubset(EXAMPLE['context'].keys()))
        self.assertEqual(EXAMPLE['evidence_sources'],['self_report'])
        self.assertEqual(len(EXAMPLE['alternative_explanations']),2)

    def test_static_demo_no_network_or_browser_storage(self):
        html=(ROOT/'docs/index.html').read_text(encoding='utf-8')
        for forbidden in ['localStorage','sessionStorage','fetch(', 'XMLHttpRequest', 'sendBeacon(', '<script src=', 'https://cdn']:
            self.assertNotIn(forbidden,html)
        self.assertIn('createObjectURL',html)
        self.assertIn('role="status"',html)

    def test_license_and_privacy_documents(self):
        self.assertIn('CC BY 4.0',(ROOT/'LICENSE').read_text(encoding='utf-8'))
        self.assertIn('MIT License',(ROOT/'LICENSE-CODE').read_text(encoding='utf-8'))
        self.assertIn('Issue/PR',(ROOT/'docs/PRIVACY_AND_SAFETY.md').read_text(encoding='utf-8'))

    def test_embedded_twelve_scenarios_match_canonical_bank(self):
        html = (ROOT/'docs/index.html').read_text(encoding='utf-8')
        match = re.search(r'<script id="scenario-data" type="application/json">(.*?)</script>', html, re.S)
        self.assertIsNotNone(match)
        embedded = json.loads(match.group(1))
        self.assertEqual(embedded, SCENARIOS)
        self.assertEqual(len(embedded['items']), 12)
        self.assertIn('scenarioSelect', html)

    def test_site_event_export_and_import_contract(self):
        html = (ROOT/'docs/index.html').read_text(encoding='utf-8')
        for token in ['observed_facts','action_taken','outcome_observed','alternative_explanations',
                      'evidence_sources','if_then_plan','review_status','importJson','counterexample',
                      'createObjectURL']:
            with self.subTest(token=token):
                self.assertIn(token, html)

    def test_site_javascript_parses_with_node(self):
        import shutil
        import subprocess
        if not shutil.which('node'):
            self.skipTest('Node.js not installed')
        html = (ROOT/'docs/index.html').read_text(encoding='utf-8')
        scripts = re.findall(r'<script(?:\s+[^>]*)?>(.*?)</script>',html,re.S)
        self.assertEqual(len(scripts),2)
        result = subprocess.run(['node','--check','-'],input=scripts[-1],capture_output=True,text=True)
        self.assertEqual(result.returncode,0,result.stderr)

if __name__ == '__main__':
    unittest.main()
