import tkinter as tk
from tkinter import *
from tkinter import ttk,messagebox
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
from dotenv import load_dotenv
import os
load_dotenv()

root = Tk()
root.title("Weather App")
root.geometry("950x550+300+200")
root.resizable(0,0)



def getWeather():
    try:

        city = textfield.get()

        geolocator = Nominatim(user_agent = "geoapiExercised")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng = location.longitude, lat = location.latitude)
    
        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text = current_time)
        name.config(text = "CURRENT WEATHER")

        #WEATHERAPI
        api_key = os.getenv("OPENWEATHER_API_KEY")
        api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    

        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp']-273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        t.config(text = (temp,"°C"))
        c.config(text = (condition,"|","FEELS","LIKE",temp,"°C"))

        w.config(text = (wind,"mph"))
        h.config(text = (humidity,"%"))
        d.config(text = description)
        p.config(text = (pressure,"hPa"))
    
    except Exception as e:
        messagebox.showerror("Weather App", "Invalid Entry!!")



Search_image = PhotoImage(file = "search.png")
myimage = Label(image = Search_image)
myimage.place(x = 25, y = 25)


textfield = tk.Entry(root,justify = "center",width = 17,font = ("Mono Sans",25,"bold"), bg = "#404040", fg = "white", borderwidth = 0)
textfield.place(x = 80, y = 48)
textfield.focus()


search_icon = PhotoImage(file = "search_icon.png")
myimage_icon = Button(image = search_icon, borderwidth = 0, cursor = "hand2", bg = "#404040", command = getWeather)
myimage_icon.place(x = 395, y = 38)


Logo_image = PhotoImage(file= "logo.png")
logo = Label(image=Logo_image)
logo.place(x = 120, y = 120)


Frame_image = PhotoImage(file="box.png")
frame_myimage  = Label(image = Frame_image)
frame_myimage.pack(padx = 5, pady = 5, side = BOTTOM)


name = Label(root,font = ("Arial", 16, "bold"))
name.place(x = 40, y = 100)
clock = Label(root, font = ("Helventica", 20))
clock.place(x = 40, y = 130)




lable1 = Label(root,text = "WIND", font = ("Helvatica", 16, "bold"), fg = "white", bg = "#1AB5EF")
lable1.place(x = 130, y = 450)


lable2 = Label(root,text = "HUMIDITY", font = ("Helvatica", 16, "bold"), fg = "white", bg = "#1AB5EF")
lable2.place(x = 250, y = 450)


lable3 = Label(root,text = "DESCRIPTION", font = ("Helvatica", 16, "bold"), fg = "white", bg = "#1AB5EF")
lable3.place(x = 435, y = 450)


lable4 = Label(root,text = "PRESSURE", font = ("Helvatica", 16, "bold"), fg = "white", bg = "#1AB5EF")
lable4.place(x = 670, y = 450)


t = Label(font = ("Arial", 70 , "bold"), fg = "#EE666D") 
t.place(x = 400, y = 150)

c = Label(font = ("Arial",16,"bold"))
c.place(x = 400, y =  250)

w = Label(text = "...", font = ("Arial", 20, "bold"), bg = "#1AB5EF")
w.place(x = 135, y = 490)

h = Label(text = "...", font = ("Arial", 20, "bold"), bg = "#1AB5EF")
h.place(x = 280, y = 490)

d = Label(text = "...", font = ("Arial", 20, "bold"), bg = "#1AB5EF")
d.place(x = 480, y = 490)

p = Label(text = "...", font = ("Arial", 20, "bold"), bg = "#1AB5EF")
p.place(x = 700, y = 490)


root,mainloop()