from sqlalchemy import create_engine, text
from config import DB_URL

def save_weather(weather):
    if weather is None:
        print("No weather data")
        return
    
    engine = create_engine(DB_URL)
    
    with engine.connect() as conn:
        # Check if this date already exists
        check = text("SELECT COUNT(*) FROM weather_raw WHERE fetched_date = :date")
        result = conn.execute(check, {"date": weather["fetched_date"]})
        count = result.scalar()
        
        if count > 0:
            print(f"Weather for {weather['fetched_date']} already exists. Skipping.")
            return
        
        # Insert only if date is new
        query = text("""
            INSERT INTO weather_raw 
            (city, temperature, humidity, weather_description, wind_speed, fetched_date)
            VALUES (:city, :temperature, :humidity, :description, :wind, :date)
        """)
        
        conn.execute(query, {
            "city": weather["city"],
            "temperature": weather["temperature"],
            "humidity": weather["humidity"],
            "description": weather["weather_description"],
            "wind": weather["wind_speed"],
            "date": weather["fetched_date"]
        })
        
        conn.commit()
        
    print(f"Saved weather for {weather['city']}")

# Test
if __name__ == "__main__":
    from extract import fetch_weather
    save_weather(fetch_weather())