from django.shortcuts import render
import requests
import json
import urllib.request 
import datetime

def index(request):
    x = datetime.datetime.now()
    y = x.strftime('%A')


    if request.method == "POST":
        city = str(request.POST.get('city'))
        url = urllib.request.urlopen("http://api.openweathermap.org/data/2.5/weather?appid=c2b5120a826c5ba4f2467a1e74eb44a8&units=metric&q=" + city).read()


        # this variable contains the json data which api returns
        json_data = json.loads(url)
        context = {'x':x,
                    'y':y,
                    'city':city,
                   'weather':json_data["weather"][0]["main"],
                   'temprature':json_data["main"]["temp"],
                   'temp_min':json_data["main"]["temp_min"],
                   'temp_max':json_data["main"]["temp_max"],
                   'pressure': json_data["main"]["pressure"],
                   'humidity' : json_data["main"]["humidity"],
                   'weather_icon' : json_data["weather"][0]["icon"],
                   'wind' : json_data["wind"]["speed"] }
    else:
        context={}
    return render(request,"index.html",context)