from datetime import datetime
import requests



response_json = ''
articles = []
API_key = "api_key"



def set_API_key(apikey):
	global api_key
	
	api_key = apikey
	
def get_current_weather(lat, lon):
	global API_key
	global response_json
	global articles
	response = requests.get(f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&appid={API_key}')
	response_json = response.json()
	current = response_json["current"]
	dt = current['dt']
	dt = datetime.fromtimestamp(dt)
	dt = dt.strftime("%I:%M %p")
	temp = current['temp']
	temp = str(int(temp - 273.5))
	weather = current['weather']
	current_weather = weather[0]
	main = current_weather['main']
	icon = current_weather['icon']
	icon = f"https://res.cloudinary.com/di539zorg/image/upload/c_scale,w_400/v1604022492/Weather%20App/{icon}.png"
	wind = current['wind_speed']
	uvi = current['uvi']
	humidity = current['humidity']
	if uvi <= 2:
		uvi = 'Low'
	elif uvi <= 5:
		uvi = 'Moderate'
	elif uvi <= 7:
		uvi = 'High'
	elif uvi <= 10:
		uvi = 'Very High'
	elif uvi >= 11:
		uvi = 'Extreme'
	
	return dt, temp, main, icon, wind, uvi, humidity


def get_hourly_weather(lat, lon):
	global API_key
	global response_json
	global articles
	response = requests.get(f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&appid={API_key}')
	response_json = response.json()
	hourly = response_json["hourly"]
	hourly_weather = []
	for weather in hourly:
		dt = weather["dt"]
		dt = datetime.fromtimestamp(dt)
		time = dt.strftime("%I:%M %p")
		time_now = datetime.now()
		time_now = time_now.strftime("%I:%M %p")
		temp = weather['temp']
		temp = str(int(temp - 273.5))
		if time >= time_now:
			hourly_weather.append([time, temp])
	
	return hourly_weather
	
