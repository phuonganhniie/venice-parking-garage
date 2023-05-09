import pandas as pd
import src.data_processing as dp
import src.analysis as an
import src.recommendations as rec
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from io import StringIO

DATA_FOLDER = 'data'
ALLOWED_EXTENSIONS = {'csv'}

app = Flask(__name__)
app.config['DATA_FOLDER'] = DATA_FOLDER

# Check if the uploaded file is a CSV file
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def calculate_garage_dimensions(occupancy_rate, parking_levels, data):
    # Read and process data
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
    error_message = None
    if request.method == 'POST':
        try:
            occupancy_rate = float(request.form['occupancy_rate'])
            if occupancy_rate <= 0 or occupancy_rate > 1:
                error_message = "Invalid input values. Please input occupancy rate in range greater than 0 and less than 1."
                return render_template('index.html', error_message=error_message, occupancy_rate=0.8, levels=1)
            
            parking_levels = int(request.form['levels'])
            if parking_levels <= 1:
                error_message = "Invalid input values. Please input garage levels at least 1."
                return render_template('index.html', error_message=error_message, occupancy_rate=0.8, levels=1)
                
        except ValueError:
            error_message = "Invalid input values. Please provide valid numbers."
            
        else:
            # Check if a file is uploaded
            if 'csv_file' not in request.files:
                error_message = "No file part. Please upload a CSV file."
            else:
                uploaded_file = request.files['csv_file']
        
                if uploaded_file.filename == '':
                    error_message = "No selected file. Please upload a CSV file."
                else:
                    # Read the uploaded CSV file
                    csv_content = StringIO(uploaded_file.read().decode('utf-8'))
                    uploaded_data = pd.read_csv(csv_content) 
                    
                    # Check if the required columns are present in the uploaded file
                    required_columns = ['Date', 'Cars in', 'Cars out', 'Motorbikes in', 'Motorbikes out']
                    if not all(column in uploaded_data.columns for column in required_columns):
                        error_message = "Invalid CSV file. The file must have the required columns: `Date`, `Cars in`, `Cars out`, `Motorbikes in`, `Motorbikes out`."
                    else:  
                        # if uploaded_file and allowed_file(uploaded_file.filename):
                        #     filename = secure_filename(uploaded_file.filename)
                        #     file_path = os.path.join(app.config['DATA_FOLDER'], filename)
                        #     uploaded_file.save(file_path)

                        garage_dimensions = calculate_garage_dimensions(occupancy_rate, parking_levels, uploaded_data)
                        return render_template('index.html', dimensions=garage_dimensions, occupancy_rate=occupancy_rate, levels=parking_levels)
    
    return render_template('index.html', error_message=error_message, occupancy_rate=0.8, levels=1)

if __name__ == '__main__':
    app.run(debug=True)