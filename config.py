import os
from dotenv import load_dotenv

load_dotenv()


OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY", "")
CITY = "Delhi"
COUNTRY_CODE = "IN"
WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"


DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_URL = f"postgresql://postgres:{DB_PASSWORD}@localhost:5432/retailweather"
