# Making a basic API request
import requests
import json

# Set up our request
weather_api_url = "https://api.openweathermap.org/data/2.5/weather"

# Parameters for our request
parameters = {
    "q": "london",         # The city we want weather for
    "appid": "eaf68ffb413d707283399af330d02c3f",    # API key (we'll discuss this)
    "units": "metric"           # Get temperature in Celsius
}

# Make the request
response = requests.get(weather_api_url, params=parameters)

# Check if request was successful
if response.status_code == 200:
    # Parse the JSON response
    weather_data = response.json()
    
    # Extract and display some data
    city = weather_data["name"]
    temperature = weather_data["main"]["temp"]
    weather = weather_data["weather"][0]["description"]
    
    print(f"Current weather in {city}:")
    print(f"Temperature: {temperature}°C")
    print(f"Conditions: {weather}")
else:
    print(f"Error: {response.status_code}")
    print(response.text)

print(json.dumps(weather_data, indent = 4))

# for key, value in weather_data.items():
#     if isinstance(value, dict):
#         print(f"{key}:")
#         for sub_key, sub_value in value.items():
#             print(f"    {sub_key}: {sub_value}")
#     elif isinstance(value, list):
#         print(f"{key}:")
#         for item in value:
#             if isinstance(item, dict):
#                 for sub_key, sub_value in item.items():
#                     print(f"    {sub_key}: {sub_value}")
#             else:
#                 print(f"    {item}")
#     else:
#         print(f"{key}: {value}")

# import json
# # JSON data as a multi-line string
# json_data = '''
# {
#   "coord": {
#     "lon": -0.1257,
#     "lat": 51.5085
#   },
#   "weather": [
#     {
#       "id": 801,
#       "main": "Clouds",
#       "description": "few clouds",
#       "icon": "02n"
#     }
#   ],
#   "base": "stations",
#   "main": {
#     "temp": 282.85,
#     "feels_like": 281.94,
#     "temp_min": 281.51,
#     "temp_max": 284.01,
#     "pressure": 1019,
#     "humidity": 85,
#     "sea_level": 1019,
#     "grnd_level": 1015
#   },
#   "visibility": 10000,
#   "wind": {
#     "speed": 2.06,
#     "deg": 0
#   },
#   "clouds": {
#     "all": 13
#   },
#   "dt": 1745455725,
#   "sys": {
#     "type": 1,
#     "id": 1414,
#     "country": "GB",
#     "sunrise": 1745469938,
#     "sunset": 1745521877
#   },
#   "timezone": 3600,
#   "id": 2643743,
#   "name": "London",
#   "cod": 200
# }
# '''
# weather_data = json.loads(json_data)
# print(weather_data["wind"]["speed"])