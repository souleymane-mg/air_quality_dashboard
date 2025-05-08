import random
from datetime import datetime
from utils.geo_locations import quartier_coords

def get_simulated_data():
    quartier = random.choice(list(quartier_coords.keys()))
    return {
        "quartier": quartier,
        "temperature": round(random.uniform(28, 42), 1),
        "pm25": round(random.uniform(10, 150), 2),
        "humidite": round(random.uniform(20, 90), 1),
        "timestamp": datetime.now().strftime("%H:%M:%S"),
        "lat": quartier_coords[quartier][0],
        "lon": quartier_coords[quartier][1]
    }
