# Garage Dimension Recommender
This project aims to recommend optimal garage dimensions based on the analysis of historical usage data. It takes into account the average and peak daily demand for cars and motorbikes and suggests a suitable number of levels, cars per level, and motorbikes per level to meet the target occupancy rate.

## Requirements
- Python 3.x
- pandas
- numpy

## Installation
1. Clone this repository:
```
git clone https://github.com/phuonganhniie/venice_parking_garage.git
```
2. Install the required packages:
```
pip install -r requirements.txt
```

## Usage
1. Prepare a CSV file with the historical usage data. The file should have the following columns: `Date`, `Cars in`, `Cars out`, `Motorbikes in`, `Motorbikes out`.

2. Run the `main.py` script with the appropriate command-line arguments:
```
python src/main.py --input_file data.csv --target_occupancy_rate 0.7 --levels 3
```
- Replace `data.csv` with the path to your CSV file, `0.7` with the desired target occupancy rate, and `3` with the desired number of levels.

- The default of target occupancy rate is `0.8` and default levels is `1`.

3. The script will output the recommended garage dimensions in the following format: 
```
Garage dimensions: {'Levels': 3, 'Cars per level': 450, 'Motorbikes per level': 94}
```

## Project Structure
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
- `data_processing.py`: Contains functions to read data from the CSV file and preprocess it.
- `analysis.py`: Contains functions to calculate the average daily demand and peak daily demand for cars and motorbikes.
- `recommendations.py`: Contains functions to calculate the required number of slots for cars and motorbikes and recommend the garage dimensions.
- `main.py`: The main script that ties everything together and provides the command-line interface.

## Testing
Unit tests are provided for `analysis.py` and `recommendations.py`. To run the tests, execute the following commands:
```
python tests/test_analysis.py
python tests/test_recommendations.py
```

## Documentation
For more information on the project and its functions, please refer to the docstrings in the respective Python files.

## License
This project is licensed under the [MIT License](LICENSE).