from django.shortcuts import render
from .utils import get_weather

def index(request):
    city = request.GET.get('city', 'London')  # Default to London if no city provided
    weather_data = get_weather(city)
    return render(request, 'weather/index.html', {'weather_data': weather_data})

