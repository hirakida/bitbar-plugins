#!/usr/local/bin/python3

import configparser
import json
import os
import urllib.request
import urllib.parse
import urllib.error

CONFIG_FILE = "~/bitbar/.bitbarrc"
TOP = "JPY"


def get_access_key():
    config = configparser.ConfigParser()
    config.read(os.path.expanduser(CONFIG_FILE))
    if not config.has_option("exchange-fixer", "access_key"):
        raise Exception("access_key not found.")
    return config["exchange-fixer"]["access_key"]


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
            print("{0}: {1}".format(TOP, rates[TOP]))
            print("---")
            print("base: {0} | size=11".format(content["base"]))
            print("---")
            for key in rates.keys():
                print("{0}: {1} | size=11".format(key, rates[key]))
    except urllib.error.HTTPError as err:
        print(err.reason)
    except urllib.error.URLError as err:
        print(err.reason)


if __name__ == '__main__':
    main()
