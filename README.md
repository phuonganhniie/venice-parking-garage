# Garage Dimension Recommender
This project aims to recommend optimal garage dimensions based on the analysis of historical usage data. It takes into account the average and peak daily demand for cars and motorbikes and suggests a suitable number of levels, cars per level, and motorbikes per level to meet the target occupancy rate.

## Features
- Reads and processes historical garage usage data.
- Calculates average daily demand and peak daily demand for cars and motorbikes.
- Recommends garage dimensions based on target occupancy rate and number of levels.
- Simple web interface to input target occupancy rate and number of levels, and displays the recommended garage dimensions.

## Getting Started
### Prerequisites
- Python 3.6 or higher
- pandas
- numpy
- Flask

### Installation
1. Clone this repository:
```
git clone https://github.com/phuonganhniie/venice_parking_garage.git
```
2. Change into the project directory:
```
cd venice_parking_garage
```
3. Install the required packages:
```
pip install -r requirements.txt
```
**Note**: It is recommended to install the required project packages from `requirements.txt` within a Python virtual environment to avoid potential conflicts with other packages on your system.

## Usage
1. Prepare a CSV file with the historical usage data. The file should have the following columns: `Date`, `Cars in`, `Cars out`, `Motorbikes in`, `Motorbikes out`.

2. Run the `app.py` for run the application:
```
python app.py
```

3. Open your web browser and navigate to `http://127.0.0.1:5000`.

4. Upload your CSV file containing the historical data.

5. Enter the desired occupancy rate (between 0 and 1) and the number of garage levels (greater than or equal to 1).

6. Click "Submit" to calculate the recommended garage dimensions.

7. The results will be displayed on the same page.

`Note: If the provided CSV file does not have the required columns, an error message will be displayed. Ensure that your CSV file has the correct format before uploading it.`

### Target Occupancy Rate
The `Target Occupancy Rate` input field is the desired percentage of the garage's total capacity that should be occupied at any given time. It balances the trade-offs between cost, customer satisfaction, and parking availability. A lower occupancy rate results in more available slots but a larger, potentially costlier garage. A higher occupancy rate leads to fewer available slots, a smaller garage, but may cause longer waiting times for parking. Input your desired `Target Occupancy Rate`, and the system will calculate the optimal number of slots for cars and motorbikes.

## Project Structure
The project consists of the following modules:
```
venice_parking_garage/
│
├── data/
│   └── historical_data.csv
│
├── src/
│   ├── __init__.py
│   ├── data_processing.py
│   ├── analysis.py
│   └── recommendations.py
│
├── templates/
│   └── index.html
│
├── tests/
│   ├── __init__.py
│   ├── test_analysis.py
│   ├── test_data_processing.py
│   └── test_recommendations.py
│
├── app.py
├── README.md
└── requirements.txt
```
- `data_processing.py`: This module is responsible for reading the input CSV file and calculating the daily usage data.
- `analysis.py`: This module performs analysis on the daily usage data to determine the average daily demand and peak daily demand for cars and motorbikes.
- `recommendations.py`: This module calculates the number of parking slots required for cars and motorbikes, and recommends garage dimensions based on the demand data and the number of parking levels. 
- `main.py`: This module serves as the entry point for the project. It reads the input data, processes it, performs analysis, calculates recommendations, and displays the results.

## Testing
Unit tests are provided for `analysis.py` , `data_processing.py` and `recommendations.py`. To run the tests, execute the following commands:
```
python -m unittest tests/test_analysis.py
python -m unittest tests/test_data_processing.py
python -m unittest tests/test_recommendations.py
```