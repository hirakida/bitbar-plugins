#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import configparser
import json
import os
import urllib.request
import urllib.parse
import urllib.error

FILE_NAME = "~/.bitbarrc"
DEFAULT_CITY = 130010


def load_city():
    if os.path.exists(os.path.expanduser(FILE_NAME)):
        config = configparser.ConfigParser()
        config.read(os.path.expanduser(FILE_NAME))
        return config['weather']['city'] if config.has_option("weather", "city") else DEFAULT_CITY
    else:
        return DEFAULT_CITY


def show(forecast):
    print("{0} {1}".format(forecast["dateLabel"], forecast["telop"]))
    temperature_max = forecast["temperature"]["max"]
    temperature_min = forecast["temperature"]["min"]
    if temperature_max:
        print("Highest {0}°".format(temperature_max["celsius"]))
    if temperature_min:
        print("Lowest {0}°".format(temperature_min["celsius"]))
    print("---")


def main():
    city = load_city()
    url = "http://weather.livedoor.com/forecast/webservice/json/v1"
    params = urllib.parse.urlencode({"city": city})
    req = urllib.request.Request("{}?{}".format(url, params))
    try:
        with urllib.request.urlopen(req) as response:
            content = json.loads(response.read().decode("utf8"))
            title = content["title"]
            forecasts = content["forecasts"]
            today = forecasts[0]
            tomorrow = forecasts[1]
            if title:
                print(title)
                print("---")
            if today:
                show(today)
            if tomorrow:
                show(tomorrow)
    except urllib.error.HTTPError as err:
        print(err.reason)
    except urllib.error.URLError as err:
        print(err.reason)


if __name__ == '__main__':
    main()
