import unittest
from bioactivity_analysis.core import fetch_pubchem_bioactivity, fetch_chembl_bioactivity

class TestCoreFunctions(unittest.TestCase):
    def test_pubchem_fetch(self):
        data = fetch_pubchem_bioactivity("P00734")
        self.assertIsInstance(data, list)

    def test_chembl_fetch(self):
        data = fetch_chembl_bioactivity("P00734")
        self.assertIsInstance(data, list)

if __name__ == "__main__":
    unittest.main()
