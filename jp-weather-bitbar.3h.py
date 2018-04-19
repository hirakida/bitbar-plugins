#!/usr/bin/env PYTHONIOENCODING=UTF-8 /usr/local/bin/python3
# -*- coding: utf-8 -*-

import configparser
import os
import requests
from requests.exceptions import ConnectionError

FILE_NAME = "~/.bitbarrc"
DEFAULT_CITY = 130010


def show(forecast):
    print("{0} {1}".format(forecast["dateLabel"], forecast["telop"]))
    temperature_max = forecast["temperature"]["max"]
    temperature_min = forecast["temperature"]["min"]
    if temperature_max:
        print("Highest {0}°".format(temperature_max["celsius"]))
    if temperature_min:
        print("Lowest {0}°".format(temperature_min["celsius"]))


def city():
    if os.path.exists(os.path.expanduser(FILE_NAME)):
        config = configparser.ConfigParser()
        config.read(os.path.expanduser(FILE_NAME))
        return config['weather']['city'] if config.has_option("weather", "city") else DEFAULT_CITY
    else:
        return DEFAULT_CITY


def main():
    try:
        response = requests.get("http://weather.livedoor.com/forecast/webservice/json/v1",
                                params={"city": city()})
    except ConnectionError as e:
        print(e.strerror)
        return
    content = response.json()
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


if __name__ == '__main__':
    main()
