import numpy as np

def calculate_average_daily_demand(daily_usage):
    """
    Calculate the average daily demand for cars and motorbikes.

    :param daily_usage: pd.DataFrame, the daily usage data
    :return: dict, the average daily demand for cars and motorbikes
    """
    cars_average = np.mean(daily_usage['Cars'])
    motorbikes_average = np.mean(daily_usage['Motorbikes'])
    return {"Cars": cars_average, "Motorbikes": motorbikes_average}

def calculate_peak_daily_demand(daily_usage):
    """
    Calculate the peak daily demand for cars and motorbikes.

    :param daily_usage: pd.DataFrame, the daily usage data
    :return: dict, the peak daily demand for cars and motorbikes
    """
    car_peak = np.max(daily_usage['Cars'])
    motorbikes_peak = np.max(daily_usage['Motorbikes'])
    print("cars peak: ", car_peak)
    print("moto peak: ", motorbikes_peak)
    return {"Cars": car_peak, "Motorbikes": motorbikes_peak}