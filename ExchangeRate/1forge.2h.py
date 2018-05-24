#!/usr/local/bin/python3
# -*- coding: utf-8 -*-


import configparser
import os
import requests
from datetime import datetime
from requests.exceptions import ConnectionError

FILE_NAME = "~/.bitbarrc"
PAIRS = "USDJPY,EURJPY"


def load_api_key():
    if not os.path.exists(os.path.expanduser(FILE_NAME)):
        raise Exception("file not found.")
    config = configparser.ConfigParser()
    config.read(os.path.expanduser(FILE_NAME))

    if not config.has_option("1forge", "api_key"):
        raise Exception("api_key not found.")
    return config["1forge"]["api_key"]


def main():
    api_key = load_api_key()
    try:
        response = requests.get("https://forex.1forge.com/1.0.3/quotes",
                                params={"pairs": PAIRS, "api_key": api_key})
    except ConnectionError as e:
        print(e.strerror)
        return
    rates = response.json()
    for rate in rates:
        print("{0}: {1}".format(rate["symbol"], rate["price"]))
        print("bid: {0}".format(rate["bid"]))
        print("ask: {0}".format(rate["ask"]))
        print("{0}".format(datetime.fromtimestamp(rate["timestamp"])))
        print("---")


if __name__ == '__main__':
    main()
