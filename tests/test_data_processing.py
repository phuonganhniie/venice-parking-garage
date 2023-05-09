import unittest
import pandas as pd
import numpy as np
import src.data_processing as dp

class TestDataProcessing(unittest.TestCase):
    def test_preprocess_data(self):
        data = pd.DataFrame({
            "Date": ["2021-01-01", "2021-01-02", np.nan],
            "Cars in": [5, -3, 8],
            "Cars out": [3, 2, -6],
            "Motorbikes in": [-4, 6, 7],
            "Motorbikes out": [1, -2, 4]
        })

        expected_data = pd.DataFrame({
            "Date": ["2021-01-01", "2021-01-02"],
            "Cars in": [5, 3],
            "Cars out": [3, 2],
            "Motorbikes in": [4, 6],
            "Motorbikes out": [1, 2]
        })

        preprocessed_data = dp.preprocess_data(data)
        pd.testing.assert_frame_equal(preprocessed_data.reset_index(drop=True), expected_data.reset_index(drop=True))
        
    def test_calculate_daily_usage(self):
        data = pd.DataFrame({
            "Date": ["2021-01-01", "2021-01-02"],
            "Cars in": [5, 3],
            "Cars out": [3, 2],
            "Motorbikes in": [4, 6],
            "Motorbikes out": [1, 2]
        })

        expected_daily_usage = pd.DataFrame({
            "Date": ["2021-01-01", "2021-01-02"],
            "Cars": [5, 3],
            "Motorbikes": [4, 6]
        })

        daily_usage = dp.calculate_daily_usage(data)
        pd.testing.assert_frame_equal(daily_usage.reset_index(drop=True), expected_daily_usage.reset_index(drop=True))
        
if __name__ == '__main__':
    unittest.main()