#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import urllib.request
import json

base = "USD"
top = "JPY"

URL = "https://api.fixer.io/latest?base=" + base

response = urllib.request.urlopen(URL)
content = json.loads(response.read().decode("utf8"))
rates = content["rates"]

print(top + ":" + str(rates[top]))
print("---")
print("base:" + content["base"])
print("---")

for key in rates.keys():
    print(key + ":" + str(rates[key]))
