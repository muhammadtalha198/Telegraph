"""catalog.py: the Intent Catalog is the authority for what each intent means and whether it is verifiable."""
from __future__ import annotations

import unittest

from tests.helpers import registry

from minercheck.catalog import Catalog, audit_spec, build_index, description_clauses


class CatalogIndex(unittest.TestCase):
    entries = build_index()

    def test_every_catalog_intent_has_a_tier(self):
        self.assertEqual(len(self.entries), 119)
        tiers = {e.tier for e in self.entries.values()}
        self.assertEqual(tiers, {"required", "judgment", "unverifiable"})

    def test_tiers_follow_the_columns(self):
        e = self.entries
        self.assertEqual(e["LIVE_PORT_CONGESTION"].tier, "unverifiable")   # Verifiable=No
        self.assertEqual(e["TEXT_SUMMARIZATION"].tier, "judgment")          # NON-DETERMINISTIC
        self.assertEqual(e["CRYPTO_PRICE_LOOKUP"].tier, "required")         # DETERMINISTIC
        self.assertEqual(e["LIQUIDITY_DEPTH_VERIFY"].tier, "required")      # HYBRID comparator+adapter
        # unverifiable carries the catalog's own reason
        self.assertIn("derived metric", e["LIVE_PORT_CONGESTION"].tier_reason)

    def test_descriptions_are_verbatim_from_the_workbook(self):
        self.assertTrue(self.entries["FX_NOW"].description.startswith("Provides real-time institutional"))

    def test_build_sheet_descriptions_agree(self):
        mism = [e.intent for e in self.entries.values()
                if e.build_sheet_description and e.build_sheet_description != e.description]
        self.assertEqual(mism, [])


class Aliases(unittest.TestCase):
    cat = Catalog()

    def test_onchain_name_maps_to_catalog_row(self):
        self.assertEqual(self.cat.entry("CRYPTO_PRICE").intent, "CRYPTO_PRICE_LOOKUP")
        self.assertEqual(self.cat.entry("WEATHER_CHECK").intent, "WEATHER_CURRENT")
        self.assertIsNone(self.cat.entry("NOT_A_REAL_INTENT"))


class Alignment(unittest.TestCase):
    cat = Catalog()
    reg = registry()

    def test_every_catalog_spec_is_aligned(self):
        for name, spec in self.reg.specs.items():
            if (spec.catalog or {}).get("local_only"):
                continue
            with self.subTest(intent=name):
                self.assertEqual(audit_spec(spec, self.cat), [], f"{name} drifted from the catalog")

    def test_clause_splitter(self):
        cl = description_clauses("Provides real-time ambient temperature, humidity, and wind vectors by coordinates.")
        self.assertTrue(any("temperature" in c for c in cl))
        self.assertTrue(any("wind vectors" in c for c in cl))
        # one-word fragments (e.g. "humidity") are intentionally not treated as standalone clauses
        self.assertNotIn("humidity", cl)


if __name__ == "__main__":
    unittest.main()
