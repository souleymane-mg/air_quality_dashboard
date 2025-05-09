import requests
from utils.geo_locations import region_coords
import os
from datetime import datetime
import time
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

# Récupérer la clé API depuis les variables d'environnement
API_KEY = os.getenv('OPENWEATHER_API_KEY')

def get_weather_data(lat, lon):
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={API_KEY}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        print(f"Erreur API météo: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Erreur requête météo: {str(e)}")
    return None

def get_air_quality_data(lat, lon):
    url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_KEY}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        print(f"Erreur API pollution: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Erreur requête pollution: {str(e)}")
    return None

def get_live_weather_data():
    data = []

    for region, (lat, lon) in region_coords.items():
        print(f"\nRécupération des données pour {region}...")

        weather_data = get_weather_data(lat, lon)
        air_data = get_air_quality_data(lat, lon)

        if weather_data and air_data:
            try:
                entry = {
                    "region": region,  # ✅ Nom de la région ici
                    "temperature": weather_data["main"]["temp"],
                    "humidite": weather_data["main"]["humidity"],
                    "pm25": air_data["list"][0]["components"].get("pm2_5", 0),
                    "lat": lat,
                    "lon": lon,
                    "timestamp": weather_data["dt"]
                }
                data.append(entry)
                print(f"✅ Données ajoutées pour {region} : {entry}")
            except Exception as e:
                print(f"⛔ Erreur traitement pour {region}: {e}")
        else:
            print(f"❌ API indisponible pour {region}")

        time.sleep(1)

    return data
