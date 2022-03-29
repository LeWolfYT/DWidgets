#create a simple thermometer using tkinter, tkinter.ttk, and openweathermap
#the openweathermap API key is:
#429f9fac553fdb5c97dc4231ab98024f
import tkinter as tk
import tkinter.ttk as ttk
import time
import requests
import json
import os
import math
#we will use ipwhois to get the current location (the website ipgeolocation.io is used)
#we need the lat and lon coordinates to get the weather


#create the main window (the title is "WThermometer" and the window is 300x200)
thermometerrt = tk.Tk()
thermometerrt.title("WThermometer")
thermometerrt.geometry("300x200")
thermometerrt.wm_attributes("-topmost", 1)


#the thermometer will be displayed in a label that fills almost the entire window
#the label is created with the text "0 degrees" (with the word degrees being replaced with the degree symbol) and the font size is the value of the variable "font_size"


#create label
font_size = 90
label = tk.Label(thermometerrt, text="0°", font=("Helvetica", font_size), bg="white", fg="black", borderwidth=0, relief="flat")
label.place(relx=0.5, rely=0.5, anchor="center")


#create the function that draws the label with the temperature (it has a forever loop that refreshes the temperature every minute)
def draw_label():
    #get the current temperature
    temp = get_temp()
    #set the label's text to the temperature
    label.config(text=str(round(temp,1))+"°F")
    #wait one minute
    thermometerrt.after(60000, draw_label)


#create the function that gets the temperature
def get_temp():
    #get the current latitude
    lat = get_lat()
    #get the current longitude
    lon = get_lon()
    #get the temperature from openweathermap using the lat and lon coordinates
    temp = get_weather(lat, lon)
    #return the temperature
    return temp


#create the function that gets the latitude
def get_lat():
    #get the current location
    location = get_location()
    #get the latitude from the location
    lat = location["latitude"]
    #return the latitude
    return lat


#create the function that gets the longitude
def get_lon():
    #get the current location
    location = get_location()
    #get the longitude from the location
    lon = location["longitude"]
    #return the longitude
    return lon


#create the function that gets the location
def get_location():
    #get the ip address from ipinfo.io (this is embedded in this function)
    ip = requests.get("https://ipinfo.io/ip").text
    #get the location from ipwhois (ipwhois.app/json/(ip))
    #this is formatted as json
    location = requests.get("https://ipwhois.app/json/"+ip).json()
    #return the location
    return location


#create the function that gets the temperature from openweathermap
def get_weather(lat, lon):
    #get the current weather from openweathermap using the lat and lon coordinates
    weather = requests.get("https://api.openweathermap.org/data/2.5/onecall?lat="+str(lat)+"&lon="+str(lon)+"&exclude=minutely,hourly&units=imperial&appid=429f9fac553fdb5c97dc4231ab98024f").json()
    #get the current temperature from the weather
    temp = weather["current"]["temp"]
    #return the temperature
    return temp

#start the main loop
def mainloop():
    #call the function that draws the label
    draw_label()


mainloop()
thermometerrt.mainloop()