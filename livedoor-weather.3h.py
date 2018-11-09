#!/usr/local/bin/python3

import configparser
import json
import os
import urllib.request
import urllib.parse
import urllib.error

CONFIG_FILE = "~/.bitbarrc"
DEFAULT_CITY = 130010


def get_city():
    config = configparser.ConfigParser()
    config.read(os.path.expanduser(CONFIG_FILE))
    return config["livedoor-weather"]["city"] if config.has_option("livedoor-weather", "city") else DEFAULT_CITY


def show(forecast):
    print("{0} {1} | color=#333333".format(forecast["dateLabel"], forecast["telop"]))
    print("---")
    temperature_max = forecast["temperature"]["max"]
    temperature_min = forecast["temperature"]["min"]
    if temperature_max and temperature_min:
        print("Max:{0}° Min:{1}° | color=#333333".format(temperature_max["celsius"], temperature_min["celsius"]))
    print("---")


def main():
    city = get_city()
    url = "http://weather.livedoor.com/forecast/webservice/json/v1"
    params = urllib.parse.urlencode({"city": city})
    req = urllib.request.Request("{}?{}".format(url, params))
    try:
        with urllib.request.urlopen(req) as response:
            content = json.loads(response.read().decode("utf8"))
            forecasts = content["forecasts"]
            today = forecasts[0]
            tomorrow = forecasts[1]
            if today:
                show(today)
            if tomorrow:
                show(tomorrow)
            print("Go to the website... | href=http://weather.livedoor.com/area/forecast/{0}".format(city))
    except urllib.error.HTTPError as err:
        print(err.reason)
    except urllib.error.URLError as err:
        print(err.reason)


if __name__ == '__main__':
    main()
