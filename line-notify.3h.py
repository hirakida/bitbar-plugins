#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import configparser
import json
import os
import time
import urllib.request
import urllib.parse
import urllib.error

FILE_NAME = "~/.bitbarrc"


def load_access_token():
    if not os.path.exists(os.path.expanduser(FILE_NAME)):
        raise Exception("file not found.")
    config = configparser.ConfigParser()
    config.read(os.path.expanduser(FILE_NAME))
    if not config.has_option("line-notify", "access-token"):
        raise Exception("access-token not found.")
    return config['line-notify']['access-token']


def main():
    access_token = load_access_token()
    url = "https://notify-api.line.me/api/status"
    headers = {"Authorization": "Bearer " + access_token}
    req = urllib.request.Request(url=url, headers=headers)
    try:
        with urllib.request.urlopen(req) as response:
            content = json.loads(response.read().decode("utf8"))
            print("{0}".format(content["target"]))
            print("targetType: {0}".format(content["targetType"]))
            print("---")
            print("Limit: {0}".format(response.headers["x-ratelimit-limit"]))
            print("Remaining: {0}".format(response.headers["x-ratelimit-remaining"]))
            print("ImageLimit: {0}".format(response.headers["x-ratelimit-imagelimit"]))
            print("ImageRemaining: {0}".format(response.headers["x-ratelimit-imageremaining"]))
            reset = response.headers["x-ratelimit-reset"]
            str_reset = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(int(reset)))
            print("Reset: {0}".format(str_reset))
            print("---")
    except urllib.error.HTTPError as err:
        print(err.reason)
    except urllib.error.URLError as err:
        print(err.reason)


if __name__ == '__main__':
    main()
