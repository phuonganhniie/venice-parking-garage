# Garage Dimension Recommender
This project aims to recommend optimal garage dimensions based on the analysis of historical usage data. It takes into account the average and peak daily demand for cars and motorbikes and suggests a suitable number of levels, cars per level, and motorbikes per level to meet the target occupancy rate.

## Getting Started
### Prerequisites
- Python 3.6 or higher
- pandas
- numpy

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

## Usage
1. Prepare a CSV file with the historical usage data. The file should have the following columns: `Date`, `Cars in`, `Cars out`, `Motorbikes in`, `Motorbikes out`.

2. Run the `main.py` script with the appropriate command-line arguments:
```
python src/main.py --input_file data.csv --target_occupancy_rate 0.7 --levels 3
```
- `--input_file`: Path to the input CSV file containing the historical parking data.
- `--target_occupancy_rate`: Target occupancy rate (between 0 and 1). Default is 0.8.
- `--levels`: Number of parking levels. Default is 1.

3. The script will output the recommended garage dimensions in the following format: 
```
Garage dimensions: {'Levels': 3, 'Cars per level': 450, 'Motorbikes per level': 94}
```

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
│   ├── recommendations.py
│   └── main.py
│
├── tests/
│   ├── __init__.py
│   ├── test_analysis.py
│   └── test_recommendations.py
│
├── README.md
└── requirements.txt
```
- `data_processing.py`: This module is responsible for reading the input CSV file and calculating the daily usage data.
- `analysis.py`: This module performs analysis on the daily usage data to determine the average daily demand and peak daily demand for cars and motorbikes.
- `recommendations.py`: This module calculates the number of parking slots required for cars and motorbikes, and recommends garage dimensions based on the demand data and the number of parking levels. 
- `main.py`: This module serves as the entry point for the project. It reads the input data, processes it, performs analysis, calculates recommendations, and displays the results.

## Testing
Unit tests are provided for `analysis.py` and `recommendations.py`. To run the tests, execute the following commands:
```
python -m unittest tests/test_analysis.py
python -m unittest tests/test_recommendations.py
```

## License
This project is licensed under the [MIT License](LICENSE).