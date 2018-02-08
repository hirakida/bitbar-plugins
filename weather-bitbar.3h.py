#!/usr/bin/env PYTHONIOENCODING=UTF-8 /usr/local/bin/python3
# -*- coding: utf-8 -*-

import configparser
import urllib.request
import json
import os


def show(forecast):
    print(forecast["dateLabel"] + " " + forecast["telop"])
    temperature_max = forecast["temperature"]["max"]
    temperature_min = forecast["temperature"]["min"]
    if temperature_max:
        print("最高気温 " + temperature_max["celsius"] + "°")
    if temperature_min:
        print("最低気温 " + temperature_min["celsius"] + "°")


FILE_NAME = "~/.bitbarrc"
DEFAULT_CITY = 130010

if os.path.exists(os.path.expanduser(FILE_NAME)):
    config = configparser.ConfigParser()
    config.read(os.path.expanduser(FILE_NAME))
    city = config['weather']['city'] if config.has_option("weather", "city") else DEFAULT_CITY
else:
    city = DEFAULT_CITY

URL = "http://weather.livedoor.com/forecast/webservice/json/v1?city=" + str(city)
response = urllib.request.urlopen(URL)
content = json.loads(response.read().decode("utf8"))

title = content["title"]
forecasts = content["forecasts"]
today = forecasts[0]
tomorrow = forecasts[1]

if title:
    print(title)
if today:
    show(today)
if tomorrow:
    show(tomorrow)
