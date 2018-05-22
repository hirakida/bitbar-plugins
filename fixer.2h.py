#!/usr/local/bin/python3
# -*- coding: utf-8 -*-


import configparser
import os
import requests
from requests.exceptions import ConnectionError

TOP = "JPY"
FILE_NAME = "~/.bitbarrc"


def load_access_key():
    if not os.path.exists(os.path.expanduser(FILE_NAME)):
        raise Exception("file not found.")
    config = configparser.ConfigParser()
    config.read(os.path.expanduser(FILE_NAME))

    if not config.has_option("fixer", "access_key"):
        raise Exception("access_key not found.")
    return config["fixer"]["access_key"]


def main():
    access_key = load_access_key()
    try:
        response = requests.get("http://data.fixer.io/api/latest", params={"access_key": access_key})
    except ConnectionError as e:
        print(e.strerror)
        return
    content = response.json()
    rates = content["rates"]
    print("{0}: {1}".format(TOP, rates[TOP]))
    print("---")
    print("base: {0}".format(content["base"]))
    print("---")
    for key in rates.keys():
        print("{0}: {1}".format(key, rates[key]))


if __name__ == '__main__':
    main()
