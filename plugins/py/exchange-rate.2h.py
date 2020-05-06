#!/usr/local/bin/python3

import configparser
import json
import os
import urllib.error
import urllib.parse
import urllib.request

CONFIG_FILE = "~/bitbar/.bitbarrc"


def get_access_key():
    config = configparser.ConfigParser()
    config.read(os.path.expanduser(CONFIG_FILE))
    if not config.has_option("exchange-rate", "access_key"):
        raise Exception("access_key not found.")
    return config["exchange-rate"]["access_key"]


def print_rate(rates, currency):
    print("{0}: {1}".format(currency, rates[currency]))


def main():
    access_key = get_access_key()
    url = "http://data.fixer.io/api/latest"
    params = urllib.parse.urlencode({"access_key": access_key})
    req = urllib.request.Request("{}?{}".format(url, params))
    try:
        with urllib.request.urlopen(req) as response:
            body = response.read().decode("utf8")
            content = json.loads(body)
            rates = content["rates"]
            print_rate(rates, "JPY")
            print("---")
            print("base: {0} | size=11".format(content["base"]))
            print("---")
            print_rate(rates, "USD")
            print_rate(rates, "AUD")
            print_rate(rates, "CAD")
            print_rate(rates, "SGD")
            print_rate(rates, "KRW")
            print_rate(rates, "CNY")
            # for key in rates.keys():
            #     print("{0}: {1} | size=11".format(key, rates[key]))
    except urllib.error.URLError:
        pass


if __name__ == '__main__':
    main()
