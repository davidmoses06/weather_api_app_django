import requests
import requests

def get_weather(city):
    """
    Fetches weather data for a given city from an external API.

    Args:
        city (str): The name of the city.

    Returns:
        dict: Weather data for the city.
    """
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=23a7ab0dbfeeede33ce6b3805c5d3c10'
    response = requests.get(url.format(city)).json()
    if response.get('cod') == 200:  # Check if the API call was successful
        weather_data = {
            'city': city,
            'temperature': response['main']['temp'],
            'description': response['weather'][0]['description'],
            'icon': response['weather'][0]['icon']
        }
        return weather_data
    else:
        # Handle API call errors
        error_message = response.get('message', 'Unknown error occurred.')
        print(f"Error fetching weather for {city}: {error_message}")
        return None
