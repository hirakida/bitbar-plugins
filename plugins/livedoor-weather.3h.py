#!/usr/local/bin/python3
# coding=utf-8

import base64
import io
import json
import urllib.error
import urllib.parse
import urllib.request

from PIL import Image

CITY = 400010


def show(forecast, top):
    # image
    icon_file = "/tmp/icon.gif"
    image_url = forecast["image"]["url"]
    if image_url:
        try:
            with urllib.request.urlopen(image_url) as response:
                img = Image.open(io.BytesIO(response.read()))
                resized = img.resize((img.width - 10, img.height - 10))
                resized.save(icon_file)
                with open(icon_file, "rb") as icon:
                    b64_encoded = base64.b64encode(icon.read())
                    print("| image={}".format(b64_encoded.decode("utf-8")))
                    if top:
                        print("---")
        except urllib.error.HTTPError as err:
            print(err.reason)
        except urllib.error.URLError as err:
            print(err.reason)

    # temperature
    temperature_max = forecast["temperature"]["max"]
    temperature_min = forecast["temperature"]["min"]
    if temperature_max:
        print("Max: {}°C | color=#333333".format(temperature_max["celsius"]))
    if temperature_min:
        print("Min: {}°C | color=#333333".format(temperature_min["celsius"]))
    print("---")


def main():
    url = "http://weather.livedoor.com/forecast/webservice/json/v1"
    params = urllib.parse.urlencode({"city": CITY})
    req = urllib.request.Request("{}?{}".format(url, params))
    try:
        with urllib.request.urlopen(req) as response:
            content = json.loads(response.read().decode("utf8"))
            forecasts = content["forecasts"]
            today = forecasts[0]
            tomorrow = forecasts[1]
            if today:
                show(today, True)
            if tomorrow:
                show(tomorrow, False)
            print("Go to the website... | href=http://weather.livedoor.com/area/forecast/{}".format(CITY))
    except urllib.error.HTTPError as err:
        print(err.reason)
    except urllib.error.URLError as err:
        print(err.reason)


if __name__ == '__main__':
    main()
