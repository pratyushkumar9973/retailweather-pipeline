import requests
from datetime import datetime
from config import OPENWEATHER_API_KEY, CITY, COUNTRY_CODE, WEATHER_URL


def fetch_weather():

    params = {
        "q": f"{CITY},{COUNTRY_CODE}",
        "appid": OPENWEATHER_API_KEY,
        "units": "metric"  
    }
    
    try:
        print("Fetching weather data...")
        response = requests.get(WEATHER_URL, params=params, timeout=10)
        response.raise_for_status()  
        
        
        data = response.json()
        
        weather_data = {
            "city": CITY,
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "weather_description": data["weather"][0]["description"],
            "wind_speed": data["wind"]["speed"],
            "recorded_at": datetime.now(),
            "fetched_date": datetime.now().date()
        }
        
        print(f"Success! Temperature: {weather_data['temperature']}°C")
        return weather_data
        
    except requests.exceptions.RequestException as e:
        print(f"API Error: {e}")
        return None
    except KeyError as e:
        print(f"Data parsing error: {e}")
        return None



if __name__ == "__main__":
    result = fetch_weather()
    print(result)
