import requests

def get_weather(api_key, city=None, latitude=None, longitude=None):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    params = {
        'appid': api_key,
        'units': 'metric'  # You can change this to 'imperial' for Fahrenheit
    }
    
    if city:
        params['q'] = city
    elif latitude and longitude:
        params['lat'] = latitude
        params['lon'] = longitude
    else:
        print("Please provide either city name or latitude/longitude.")
        return
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        print(f"Error: {response.status_code}")
        return None

def display_weather(weather_data):
    if weather_data:
        print("\nWeather Information:")
        print(f"City: {weather_data['name']}")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Weather: {weather_data['weather'][0]['description']}")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Wind Speed: {weather_data['wind']['speed']} m/s")
    else:
        print("Unable to fetch weather data.")

def main():
    api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
    
    city = input("Enter the city name: ")
    
    weather_data = get_weather(api_key, city=city)
    display_weather(weather_data)

if __name__ == "__main__":
    main()
