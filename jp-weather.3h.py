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
    return config['weather']['city'] if config.has_option("jp-weather", "city") else DEFAULT_CITY


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
    url = "http://weather.livedoor.com/forecast/webservice/json/v1"
    params = urllib.parse.urlencode({"city": get_city()})
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
