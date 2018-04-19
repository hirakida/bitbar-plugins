#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import requests
from requests.exceptions import ConnectionError

TOP = "JPY"
BASE = "USD"

try:
    response = requests.get("https://api.fixer.io/latest", params={"base": BASE})
except ConnectionError as e:
    print(e.strerror)
else:
    content = response.json()
    rates = content["rates"]
    print("{0}: {1}".format(TOP, rates[TOP]))
    print("---")
    print("base: {0}".format(content["base"]))
    print("---")
    for key in rates.keys():
        print("{0}: {1}".format(key, rates[key]))
