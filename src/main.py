import argparse
import data_processing as dp
import analysis as an
import recommendations as rec

def main(args):
    # Read and process data
    data = dp.read_data(args.input_file)
    daily_usage = dp.calculate_daily_usage(data)
    
    # Analyze data
    average_daily_demand = an.calculate_average_daily_demand(daily_usage)
    peak_daily_demand = an.calculate_peak_daily_demand(daily_usage)
    
    # Calculate recommendations
    slots = rec.calculate_slots(average_daily_demand, peak_daily_demand, args.target_occupancy_rate)
    garage_dimensions = rec.recommend_garage_dimensions(slots, args.levels)
    
    # Print results
    print("Garage dimensions:", garage_dimensions)
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Garage Dimension Recommender')
    parser.add_argument('--input_file', type=str, default="data/historical_data.csv", help='Path to the input CSV file')
    parser.add_argument('--target_occupancy_rate', type=float, default=0.8, help='Target occupancy rate (0-1)')
    parser.add_argument('--levels', type=int, default=1, help='Number of parking levels')
    args = parser.parse_args()
    
    main(args)