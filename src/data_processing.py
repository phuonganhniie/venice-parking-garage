import pandas as pd

def read_data(file_path):
    return pd.read_csv(file_path, parse_dates=['Date'])

def calculate_daily_usage(data):
    data['Cars'] = data['Cars in'] 
    data['Motorbikes'] = data['Motorbikes in'] 
    
    return data[["Date", "Cars", "Motorbikes"]]