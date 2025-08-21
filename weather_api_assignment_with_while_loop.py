import requests

'''Current VSCode theme is "One Dark" extension, "Coldy Python Theme" extension is pretty dope too'''
def get_weather(city, api_key):
  url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
  response = requests.get(url)
  data = response.json()
  if response.status_code != 200:
    print(f'Error fetching weather: ', data.get('weather', 'Unknown Error'))
    return None
  
  temp_k = data['main']['temp']
  temp_c = temp_k - 273.15
  description = data['weather'][0]['description']
  print(f'Weather in {city}: {description}')
  print(f'Temperature in {city}: {temp_c:.2f}°C')
  return True

def main(api_key):
  while True:
    city = input('Welcome to the Weather App. Enter a city (or type bye to exit).')
    if city.lower() == 'bye':
      print('Goodbye')
      break
    success = get_weather(city, api_key)
    if success is None:
      print('Unable to proceed with request. Please try again.')

if __name__ == '__main__':
  api_key = '6162d674c0d3ce291204035f9a8ce1e7'
  main(api_key)
  print()
