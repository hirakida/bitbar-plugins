#!/usr/local/bin/python3

import configparser
import json
import os
import urllib.request
import urllib.parse
import urllib.error
from builtins import ValueError
from datetime import datetime

CONFIG_FILE = "~/bitbar/.bitbarrc"
PAIRS = "USDJPY,EURJPY"


def get_api_key():
    config = configparser.ConfigParser()
    config.read(os.path.expanduser(CONFIG_FILE))
    if not config.has_option("exchange-rate-1forge", "api_key"):
        raise ValueError("api_key not found.")
    return config["exchange-rate-1forge"]["api_key"]


def main():
    api_key = get_api_key()
    api_url = "http://forex.1forge.com/1.0.3/quotes"
    params = urllib.parse.urlencode({"pairs": PAIRS, "api_key": api_key})
    req = urllib.request.Request("{}?{}".format(api_url, params))
    try:
        with urllib.request.urlopen(req) as response:
            content = response.read().decode("utf8")
            rates = json.loads(content)
            print(":currency_exchange:")
            print("---")
            for rate in rates:
                print("{0}: {1} | color=#333333".format(rate["symbol"], rate["price"]))
                print("bid:{0} | color=#333333".format(rate["bid"]))
                print("ask:{0} | color=#333333".format(rate["ask"]))
                print("{0} | color=#333333 size=10".format(datetime.fromtimestamp(rate["timestamp"])))
                print("---")
            print("Go to the website... | href=https://1forge.com/forex-data-api")
    except urllib.error.HTTPError as err:
        print(err.reason)
    except urllib.error.URLError as err:
        print(err.reason)


if __name__ == '__main__':
    main()
