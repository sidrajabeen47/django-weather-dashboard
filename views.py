import requests
from django.shortcuts import render

def weather_api(req):
    # 1. Get the city name from the search input manually typed by user.
    # If no city is searched yet, it defaults to 'Hyderabad'.
    city = req.GET.get('city', 'Hyderabad')
    
    # 2. Inject the dynamic city variable into the API URL string
    api_key = "PASTE_YOUR_WEATHERAPI_KEY_HERE" 
    url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no'
    
    response = requests.get(url)
    weather_data = response.json()
    
    # 3. If the API returns an error (e.g., city typed incorrectly), handle it gracefully
    if 'error' in weather_data:
        context = {'error': weather_data['error']['message']}
    else:
        context = {'weather': weather_data}
        
    return render(req, 'home.html', context)