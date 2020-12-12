from apis.weather_api import get_current_weather, get_hourly_weather
from texture.gradient_color import gradient
from datetime import datetime
from kivymd.app import MDApp
from plyer import gps
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.clock import Clock




kv ='''
ScreenManager:
	MainUI:

<MainUI>:
	name: 'MainUI'
	
	
	RelativeLayout:
		canvas:
			Color:
				rgba: .95,.95,1,1
			Rectangle:
				size: self.size
				pos: self.pos
			
		RelativeLayout:
			size_hint: 1, 1
			canvas.before:
				Color:
					rgba: 1,1,1,1
				RoundedRectangle:
					radius:[15,15,15,15]
					size: self.size
			
			MDLabel:
				text: "Today"
				font_name: 'fonts/Gilroy-light.otf'
				font_size: '23dp'
				pos_hint: {'center_x' : .9, 'center_y' : .8}
			
			AsyncImage:
				source: app.current_weather()[3]
				pos_hint: {'center_x' : .3, 'center_y' : .64}
			
			MDLabel:
				text: str(app.current_weather()[1])
				font_size: '44dp'
				font_name: 'fonts/Gilroy-ExtraBold.otf'
				pos_hint: {'center_x' : .97, 'center_y' : .65}
				
			MDLabel:
				text: '°c'
				font_size: '22dp'
				font_name: 'fonts/Gilroy-ExtraBold.otf'
				color: .8,.8,.8,1
				pos_hint: {'x' : .6, 'center_y' : .668}
				
			
			MDLabel:
				text: app.current_weather()[2]
				font_name: 'fonts/Gilroy-light.otf'
				font_size: '18dp'
				pos_hint: {'center_x' : .97, 'center_y' : .6}		
				
			AsyncImage:
				source: 'https://res.cloudinary.com/di539zorg/image/upload/c_scale,w_64/v1604029712/Weather%20App/wind.png'
				pos_hint: {'center_x' : .5, 'center_y' : .45}
			
			MDLabel:
				text: str(app.current_weather()[4])+'[color=#cccccc][size=10sp]m/s[/size][/color]'
				markup: True
				font_name: 'fonts/Gilroy-light.otf'
				font_size: '18dp'
				pos_hint: {'center_x' : .95, 'center_y' : .4}
			
			AsyncImage:
				source: 'https://res.cloudinary.com/di539zorg/image/upload/c_scale,w_64/v1604029712/Weather%20App/uv.png'
				pos_hint: {'center_x' : .8, 'center_y' : .45}
			
			MDLabel:
				text: app.current_weather()[5]
				markup: True
				font_name: 'fonts/Gilroy-light.otf'
				font_size: '15dp'
				pos_hint: {'x': .72, 'center_y' : .4}
			
			AsyncImage:
				source: 'https://res.cloudinary.com/di539zorg/image/upload/c_scale,w_64/v1604029712/Weather%20App/humidity.png'
				pos_hint: {'center_x' : .2, 'center_y' : .45}
			
			MDLabel:
				text: str(app.current_weather()[6])+'[color=#cccccc][size=10sp]%[/size][/color]'
				markup: True
				font_name: 'fonts/Gilroy-light.otf'
				font_size: '18dp'
				pos_hint: {'x': .15, 'center_y' : .4}
			
			
			
			
			
								
'''

class MainUI(Screen):
	pass
	
sm = ScreenManager()
sm.add_widget(MainUI(name = 'MainUI'))

class Weatherapp(MDApp):
	
	def build(self):
		self.screen = Screen()
		main = Builder.load_string(kv)
		self.screen.add_widget(main)
		
		
		
		return self.screen
	
	
	
	def theme_color(self):
		return 0.6, 0.8, 1, 1
		
		
	def time_now(self):
		now = datetime.now()
		return str(now.strftime("%I:%M %p"))	
	
	def current_weather(self):
		lat = 23.76
		lon = 86
		return get_current_weather(lat, lon)
	
	def texture(self):
		return gradient().create([[255, 204, 204, 255], [255, 204, 204, 255], [179, 179, 255, 255], [179, 179, 255, 255]], 'Top-Bottom')
				
Weatherapp().run()
