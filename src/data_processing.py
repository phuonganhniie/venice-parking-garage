import pandas as pd

def read_data(file_path):
    return pd.read_csv(file_path, parse_dates=['Date'])

def preprocess_data(data):
    # Remove rows with missing values
    data = data.dropna()
    
    # Handle negative values by taking their absolute values
    data['Cars in'] = data['Cars in'].abs()
    data['Cars out'] = data['Cars out'].abs()
    data['Motorbikes in'] = data['Motorbikes in'].abs()
    data['Motorbikes out'] = data['Motorbikes out'].abs()

    return data

def calculate_daily_usage(data):
    # data['Cars'] = data['Cars in'] - data['Cars out']
    # data['Cars'] = data['Cars'].clip(lower=0)
    
    # data['Motorbikes'] = data['Motorbikes in'] - data['Motorbikes out']
    # data['Motorbikes'] = data['Motorbikes'].clip(lower=0)
    
    data['Cars'] = data['Cars in']
    data['Cars'] = data['Cars'].clip(lower=0)
    
    data['Motorbikes'] = data['Motorbikes in']
    data['Motorbikes'] = data['Motorbikes'].clip(lower=0)
    
    return data[["Date", "Cars", "Motorbikes"]]