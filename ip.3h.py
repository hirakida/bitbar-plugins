#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import requests
from requests.exceptions import ConnectionError


def main():
    try:
        response = requests.get("http://ip-api.com/json")
    except ConnectionError as e:
        print(e.strerror)
        return
    content = response.json()
    print(content["query"])
    print("---")
    print("as: {0}".format(content["as"]))
    print("isp: {0}".format(content["isp"]))
    print("org: {0}".format(content["org"]))
    print("---")
    print("city: {0}".format(content["city"]))
    print("region: {0}".format(content["regionName"]))
    print("country: {0}".format(content["country"]))
    print("timezone: {0}".format(content["timezone"]))
    print("zip: {0}".format(content["zip"]))
    print("lat: {0}".format(content["lat"]))
    print("lon: {0}".format(content["lon"]))
    print("---")


if __name__ == '__main__':
    main()
