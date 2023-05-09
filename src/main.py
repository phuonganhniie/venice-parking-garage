import data_processing as dp
import analysis as an
import recommendations as rec

CSV_FILE_PATH = "data/historical_data.csv"
TARGET_OCCUPANCY_RATE = 0.8
PARKING_LEVELS = 1

def main():
    # Read and process data
    data = dp.read_data(CSV_FILE_PATH)
    daily_usage = dp.calculate_daily_usage(data)
    
    # Analyze data
    average_daily_demand = an.calculate_average_daily_demand(daily_usage)
    peak_daily_demand = an.calculate_peak_daily_demand(daily_usage)
    
    # Calculate recommendations
    slots = rec.calculate_slots(average_daily_demand, peak_daily_demand, TARGET_OCCUPANCY_RATE)
    garage_dimensions = rec.recommend_garage_dimensions(slots, PARKING_LEVELS)
    
    # Print results
    print("Garage dimensions:", garage_dimensions)
    
if __name__ == "__main__":
    main()