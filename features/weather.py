import os
from dotenv import load_dotenv
from security import safe_requests

load_dotenv()


def get_weather(city):
    api_key = os.getenv("WEATHER_API_KEY")

    url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=yes"
    try:
        res = safe_requests.get(url)
        data = res.json()

        if "error" in data:
            return f"Error: {data['error']['message']}"

        # Basic weather details
        location = data['location']['name']
        condition = data['current']['condition']['text']
        temp_c = data['current']['temp_c']
        feels_like = data['current']['feelslike_c']

        # Air Quality data
        epa_index = data['current']['air_quality'].get('us-epa-index')
        defra_index = data['current']['air_quality'].get('gb-defra-index')

        # EPA Interpretation
        epa_status = {
            1: "Good",
            2: "Moderate",
            3: "Unhealthy for sensitive groups",
            4: "Unhealthy",
            5: "Very Unhealthy",
            6: "Hazardous"
        }.get(epa_index, "Unknown")

        # DEFRA µgm-3 range based on index
        defra_info = {
            1: "0-11",
            2: "12-23",
            3: "24-35",
            4: "36-41",
            5: "42-47",
            6: "48-53",
            7: "54-58",
            8: "59-64",
            9: "65-70",
            10: "71+ "
        }

        defra_range = defra_info.get(defra_index)

        return (
            f"The current weather in {location} is {condition}. "
            f"The temperature is {temp_c}°C (Feels like {feels_like}°C). "
            f"Air quality is in the range of {defra_range} and is {epa_status}"
        )

    except Exception as e:
        return f"Error getting weather: {e}"

print(get_weather("Pune"))
