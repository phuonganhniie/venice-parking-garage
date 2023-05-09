import pandas as pd
import src.data_processing as dp
import src.analysis as an
import src.recommendations as rec
from flask import Flask, render_template, request
from io import StringIO

DATA_FOLDER = 'data'
ALLOWED_EXTENSIONS = {'csv'}

app = Flask(__name__)
app.config['DATA_FOLDER'] = DATA_FOLDER

# Check if the uploaded file is a CSV file
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_garage_dimensions(occupancy_rate, parking_levels, preprocess_data):
    # Read and process data
    data = dp.preprocess_data(preprocess_data)
    daily_usage = dp.calculate_daily_usage(data)

    # Analyze data
    average_daily_demand = an.calculate_average_daily_demand(daily_usage)
    peak_daily_demand = an.calculate_peak_daily_demand(daily_usage)

    # Calculate recommendations
    try:
        slots = rec.calculate_slots(average_daily_demand, peak_daily_demand, occupancy_rate)
        garage_dimensions = rec.recommend_garage_dimensions(slots, parking_levels)
    except ValueError as e:
        return str(e)

    return garage_dimensions

@app.route('/', methods=['GET', 'POST'])
def index():
    error_message = None
    dimensions = None
    occupancy_rate = 0.5
    parking_levels = 1
    
    if request.method == 'POST':
        occupancy_rate = float(request.form['occupancy_rate'])
        parking_levels = int(request.form['levels'])
        
        if not (0 < occupancy_rate < 1) or parking_levels < 1:
            default_rate = 0.5
            default_levels = 1
            error_message = "Invalid input values. Please input occupancy rate in range (0, 1) and garage levels at least 1."
            return render_template('index.html', error_message=error_message, dimensions=dimensions, occupancy_rate=default_rate, levels=default_levels)
        
        else:
            uploaded_file = request.files.get('csv_file')
            
            if uploaded_file:
                csv_content = StringIO(uploaded_file.read().decode('utf-8'))
                uploaded_data = pd.read_csv(csv_content)

                required_columns = ['Date', 'Cars in', 'Cars out', 'Motorbikes in', 'Motorbikes out']
                if all(column in uploaded_data.columns for column in required_columns):
                    dimensions = get_garage_dimensions(occupancy_rate, parking_levels, uploaded_data)
                else:
                    error_message = "Invalid CSV file. The file must have the required columns: `Date`, `Cars in`, `Cars out`, `Motorbikes in`, `Motorbikes out`."
        
    return render_template('index.html', error_message=error_message, dimensions=dimensions, occupancy_rate=occupancy_rate, levels=parking_levels)

if __name__ == '__main__':
    app.run(debug=True)