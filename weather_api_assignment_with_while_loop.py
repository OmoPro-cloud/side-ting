import requests

def get_weather(city, api_key):
  while True:
    try:
      url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
      response = requests.get(url)
      data = response.json()
      if response.status_code != 200:
        print('Error fetching weather', data.get('message', 'Unknown error'))
        return
      temp_k = data['main']['temp']
      temp_c = temp_k - 273.15
      weather_description = data['weather'][0]['description']
      print(f'Weather in {city}: {weather_description}')
      print(f'Temperature in {city}: {temp_c:.2f}')
      return 'Done'
    except Exception as e:
      print('Erorr fetching weather: ', e)

    city = input('Welcome to the Weather App. Please enter a city to view its weather' \
    'or type "bye" to leave.')
    if city == {'bye'}:
      break
    weather = get_weather(city, api_key)
    print(weather)
    
print(get_weather)