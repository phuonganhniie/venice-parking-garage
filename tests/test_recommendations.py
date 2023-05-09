import unittest
from src.recommendations import calculate_slots, recommend_garage_dimensions

class TestRecommendations(unittest.TestCase):
    
    def test_calculate_slots(self):
        daily_demand = {"Cars": 500, "Motorbikes": 150}
        peak_demand = {"Cars": 700, "Motorbikes": 180}
        occupancy_rate = 0.8
        expected_slots = {"Cars": 3500, "Motorbikes": 900}
        
        slots = calculate_slots(daily_demand, peak_demand, occupancy_rate)
        self.assertEqual(slots, expected_slots)
        
    def test_recommend_garage_dimensions(self):
        slots = {"Cars": 875, "Motorbikes": 225}
        levels = 3
        expected_dimensions = {
            "Levels": 3,
            "Cars per level": 292,
            "Motorbikes per level": 75,
        }

        dimensions = recommend_garage_dimensions(slots, levels)
        self.assertEqual(dimensions, expected_dimensions)

if __name__ == '__main__':
    unittest.main()