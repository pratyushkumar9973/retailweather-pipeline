from extract import fetch_weather
from load import save_weather

print("Starting pipeline...")

weather = fetch_weather()
save_weather(weather)

print("Done!")