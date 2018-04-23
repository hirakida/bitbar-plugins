#!/usr/bin/env PYTHONIOENCODING=UTF-8 /usr/local/bin/python3
# -*- coding: utf-8 -*-

import arrow
import configparser
import os
import requests
from requests.exceptions import ConnectionError

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
    try:
        response = requests.get("https://notify-api.line.me/api/status",
                                headers={"Authorization": "Bearer " + access_token})
    except ConnectionError as e:
        print(e.strerror)
        return
    content = response.json()
    reset = arrow.get(response.headers["x-ratelimit-reset"]).replace(tzinfo="Asia/Tokyo")
    print("{0}".format(content["target"]))
    print("targetType: {0}".format(content["targetType"]))
    print("---")
    print("Limit: {0}".format(response.headers["x-ratelimit-limit"]))
    print("Remaining: {0}".format(response.headers["x-ratelimit-remaining"]))
    print("ImageLimit: {0}".format(response.headers["x-ratelimit-imagelimit"]))
    print("ImageRemaining: {0}".format(response.headers["x-ratelimit-imageremaining"]))
    print("reset: {0}".format(reset))
    print("---")


if __name__ == '__main__':
    main()
