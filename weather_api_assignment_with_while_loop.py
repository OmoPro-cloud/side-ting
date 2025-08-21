import requests

def get_weather(city, api_key):
  url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
  response = requests.get(url)
  data = response.json()
  if response.status_code != 200:
    print(f'Error fetching weather: ', data.get('weather', 'Unknown Error'))
    return None
  
  temp_k = data['main']['temp']
  temp_c = temp_c - 273.15
  description = data['weather'][0]['description']
  print(f'Weather in {city}: {description}')
  print(f'Temperature in {city}: {temp_k:.2f}°C')
  return True

def main(api_key):
  while True:
    city = input('Welcome to the Weather App. Enter a city (or type bye to exit).')
    if city.lower() == 'bye':
      print('Goodbye')
      break
    