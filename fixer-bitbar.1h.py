#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import requests

TOP = "JPY"

response = requests.get("https://api.fixer.io/latest", params={"base": "USD"})
content = response.json()
rates = content["rates"]

print(TOP + ":" + str(rates[TOP]))
print("---")
print("base:" + content["base"])
print("---")

for key in rates.keys():
    print(key + ":" + str(rates[key]))
