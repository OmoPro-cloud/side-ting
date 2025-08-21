import requests

#NEW: if an HTTP response is 200, then your request has succeeded. If it's response is a 404, then the source couldn't be found, and 500 indicates a server error
#write a function that will take an input(city) from the user and return its current weather

def get_weather(city, api_key):
  try: #if unable to fetch weather, return error
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    data = response.json()
    if response.status_code != 200: #if the request is NOT FOUND
      print('Error fetching weather', data.get('message', 'Unknown error'))
      return
    temp_k = data['main']['temp']
    temp_c = -273.15
    weather_description = data['weather'][0]['description']
    print(f'Weather in {city} right now: {weather_description}')
    print(f'The temperature in {city} right now is: {temp_c:.2f}Celcius')
    return 'Done'
  except Exception as e:
    print('Error fetching weather: ', e)
  
city = input('Enter your city: ')
api_key = 'd445f540e455fccdf27aed42e74a6fd4'
weather = get_weather(city, api_key)
print(weather)