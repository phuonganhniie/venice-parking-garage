import unittest
import pandas as pd
import src.analysis as ana

class TestAnalysis(unittest.TestCase):
    def setUp(self):
        self.sample_data = pd.DataFrame({
            'Cars': [10, 20, 30, 25],
            'Motorbikes': [5, 8, 10, 7]
        })

    def test_calculate_average_daily_demand(self):
        result = ana.calculate_average_daily_demand(self.sample_data)
        self.assertAlmostEqual(result["Cars"], 21.25)
        self.assertAlmostEqual(result["Motorbikes"], 7.5)

    def test_calculate_peak_daily_demand(self):
        result = ana.calculate_peak_daily_demand(self.sample_data)
        self.assertEqual(result["Cars"], 30)
        self.assertEqual(result["Motorbikes"], 10)

if __name__ == '__main__':
    unittest.main()
