from django.shortcuts import render
import requests


def index(req): #request
    API_KEY = "Here should be your API key (from openweathermap.org)"
    current_weather_url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

    if req.method == 'POST':
        city1 = req.POST['city1']
        city2 = req.POST.get('city2', None)

        weather_data1 = fetch_weather(city1, API_KEY, current_weather_url)
        weather_data2 = None
        if city2:
            weather_data2 = fetch_weather(city2, API_KEY, current_weather_url)

        context = {
            'weather_data1': weather_data1,
            'weather_data2': weather_data2,
        }

        return render(req, 'weather_app/index.html', context)
    else:
        return render(req, 'weather_app/index.html',)


def fetch_weather(city, api_key, current_weather_url):
    response = requests.get(current_weather_url.format(city, api_key)).json()
    weather_data = {
        'city': city,
        'temperature': round(response['main']['temp'] - 273.15, 2),
        'description': response['weather'][0]['description'],
        'icon': response['weather'][0]['icon'],
    }
    return weather_data
