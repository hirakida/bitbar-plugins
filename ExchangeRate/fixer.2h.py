#!/usr/local/bin/python3
# -*- coding: utf-8 -*-


import configparser
import os
import json
import urllib.request
import urllib.parse
import urllib.error

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
    url = "http://data.fixer.io/api/latest"
    params = urllib.parse.urlencode({"access_key": access_key})
    req = urllib.request.Request("{}?{}".format(url, params))
    try:
        with urllib.request.urlopen(req) as response:
            body = response.read().decode("utf8")
            content = json.loads(body)
            rates = content["rates"]
            print("{0}: {1}".format(TOP, rates[TOP]))
            print("---")
            print("base: {0}".format(content["base"]))
            print("---")
            for key in rates.keys():
                print("{0}: {1}".format(key, rates[key]))
    except urllib.error.HTTPError as err:
        print(err.reason)
    except urllib.error.URLError as err:
        print(err.reason)


if __name__ == '__main__':
    main()
