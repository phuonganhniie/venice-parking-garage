import math 

def calculate_slots(daily_demand, peak_demand, occupancy_rate):
    """
    Calculate the number of slots required for cars and motorbikes.

    :param daily_demand: dict, the average daily demand for cars and motorbikes
    :param peak_demand: dict, the peak daily demand for cars and motorbikes
    :param occupancy_rate: float, the target occupancy rate
    :return: dict, the number of slots required for cars and motorbikes
    """
    if occupancy_rate <= 0 or occupancy_rate >= 1:
        raise ValueError("The occupancy rate must be greater than 0 and less than 1.")
    
    # cars_slots = int(max(daily_demand["Cars"], peak_demand["Cars"]) / occupancy_rate)
    # motorbikes_slots = int(max(daily_demand["Motorbikes"], peak_demand["Motorbikes"]) / occupancy_rate)
    cars_slots = int(max(daily_demand["Cars"], peak_demand["Cars"]) / (1-occupancy_rate))
    motorbikes_slots = int(max(daily_demand["Motorbikes"], peak_demand["Motorbikes"]) / (1-occupancy_rate))
    
    return {"Cars": cars_slots, "Motorbikes": motorbikes_slots}

def recommend_garage_dimensions(slots, levels):
    """
    Recommend garage dimensions based on the number of slots and levels.

    :param slots: dict, the number of slots required for cars and motorbikes
    :param levels: int, the number of levels
    :return: dict, the garage dimensions
    """
    cars_per_level = int(math.ceil(slots["Cars"] / levels))
    motorbikes_per_level = int(math.ceil(slots["Motorbikes"] / levels)) 
    return {"Levels": levels, "Cars per level": cars_per_level, "Motorbikes per level":motorbikes_per_level}