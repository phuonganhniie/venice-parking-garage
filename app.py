# import argparse
# import data_processing as dp
# import analysis as an
# import recommendations as rec

# def main(args):
#     # Read and process data
#     data = dp.read_data(args.input_file)
#     daily_usage = dp.calculate_daily_usage(data)
    
#     # Analyze data
#     average_daily_demand = an.calculate_average_daily_demand(daily_usage)
#     peak_daily_demand = an.calculate_peak_daily_demand(daily_usage)
    
#     # Calculate recommendations
#     slots = rec.calculate_slots(average_daily_demand, peak_daily_demand, args.target_occupancy_rate)
#     garage_dimensions = rec.recommend_garage_dimensions(slots, args.levels)
    
#     # Print results
#     print("Garage dimensions:", garage_dimensions)
    
# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description='Garage Dimension Recommender')
#     parser.add_argument('--input_file', type=str, default="data/historical_data.csv", help='Path to the input CSV file')
#     parser.add_argument('--target_occupancy_rate', type=float, default=0.8, help='Target occupancy rate (0-1)')
#     parser.add_argument('--levels', type=int, default=1, help='Number of parking levels')
#     args = parser.parse_args()
    
#     main(args)

import os
import pandas as pd
import src.data_processing as dp
import src.analysis as an
import src.recommendations as rec
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from io import StringIO

# Add this after the CSV_FILE_PATH variable
DATA_FOLDER = 'data'
ALLOWED_EXTENSIONS = {'csv'}

# CSV_FILE_PATH = "data/historical_data.csv"

app = Flask(__name__)
app.config['DATA_FOLDER'] = DATA_FOLDER

# Add this function to check if the uploaded file is a CSV file
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def calculate_garage_dimensions(occupancy_rate, parking_levels, csv_file_path):
    # Read and process data
    data = dp.read_data(csv_file_path)
    daily_usage = dp.calculate_daily_usage(data)

    # Analyze data
    average_daily_demand = an.calculate_average_daily_demand(daily_usage)
    peak_daily_demand = an.calculate_peak_daily_demand(daily_usage)

    # Calculate recommendations
    slots = rec.calculate_slots(average_daily_demand, peak_daily_demand, occupancy_rate)
    garage_dimensions = rec.recommend_garage_dimensions(slots, parking_levels)

    return garage_dimensions

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Read target occupancy rate and number of levels
        try:
            occupancy_rate = float(request.form['occupancy_rate'])
            parking_levels = int(request.form['levels'])
        except ValueError:
            return "Invalid input values. Please provide valid numbers."
        
        # Check if a file is uploaded
        if 'csv_file' not in request.files:
            return "No file part. Please upload a CSV file."
        
        uploaded_file = request.files['csv_file']
        
        if uploaded_file.filename == '':
            return "No selected file. Please upload a CSV file."
        
        # Read the uploaded CSV file
        csv_content = StringIO(uploaded_file.read().decode('utf-8'))
        uploaded_data = pd.read_csv(csv_content)
        
        # Check if the required columns are present in the uploaded file
        required_columns = ['Date', 'Cars in', 'Cars out', 'Motorbikes in', 'Motorbikes out']
        if not all(column in uploaded_data.columns for column in required_columns):
            return "Invalid CSV file. The file must have the following columns: `Date`, `Cars in`, `Cars out`, `Motorbikes in`, `Motorbikes out`."
        
        if uploaded_file and allowed_file(uploaded_file.filename):
            filename = secure_filename(uploaded_file.filename)
            file_path = os.path.join(app.config['DATA_FOLDER'], filename)
            uploaded_file.save(file_path)

        garage_dimensions = calculate_garage_dimensions(occupancy_rate, parking_levels, file_path)
        return render_template('index.html', dimensions=garage_dimensions, occupancy_rate=occupancy_rate, levels=parking_levels)
    else:
        return render_template('index.html', occupancy_rate=0.8, levels=1)

if __name__ == '__main__':
    app.run(debug=True)
