# backend/climate_logic.py
import requests

def analyze_climate(city):
    API_KEY = 'YOUR_API_KEY'
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    r = requests.get(url).json()
    
    humidity = r['main']['humidity']
    temp = r['main']['temp']

    advice = []
    if humidity < 40:
        advice.append("Use a humidifier and thick moisturizer.")
    if temp > 30:
        advice.append("Avoid sweating; stay in cool environments.")
    if temp < 10:
        advice.append("Protect skin from cold wind and dryness.")

    return {
        'temperature': temp,
        'humidity': humidity,
        'advice': advice
    }
