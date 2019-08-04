import tkinter as tk
from tkinter import font
import requests

Height = 500
Wid= 600
root = tk.Tk()
# define functionality

def test_func(entry):
	print(f'entry: {entry}')

# api.openweathermap.org/data/2.5/forecast?q={city name},{country code}

# bd37554dd2cda9259c347506aa77d649
def format_resp(weather):
	try:
		name = weather['name']
		desc =weather['weather'][0]['description']
		temp = weather['main']['temp']
		country = weather['sys']['country']
		final_str = 'City: %s \nCountry: %s \nCondition: %s \nTemprature: %s °' % (name, country, desc, temp)
	except:
		final_str = 'There is a problem retreiving this information'

	return final_str

def get_weather(city):
	weather_key = 'bd37554dd2cda9259c347506aa77d649'
	url = 'https://api.openweathermap.org/data/2.5/weather'
	params = {'APPID':weather_key, 'q':city, 'units':'metric'}
	respone = requests.get(url, params=params)
	weather = respone.json()
	label['text'] = format_resp(weather)
	



canvas= tk.Canvas(root, height = Height, width = Wid)
canvas.pack()

bgImage=tk.PhotoImage(file='landscape.png')
bgLabel=tk.Label(root, image=bgImage)
bgLabel.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg = '#80c1ff', bd = 5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=('Bebas Neue', 28))
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text='Search', font=('Bebas Neue', 18), command=lambda:get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lframe=tk.Frame(root, bg = '#80c1ff', bd = 5)
lframe.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lframe, bg='#FFF', font=('Bebas Neue Book', 22), justify='left', anchor='nw', padx=10, pady=10)
label.place(relwidth=1, relheight=1)


root.mainloop()
