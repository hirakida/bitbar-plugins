#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import requests

response = requests.get("http://ip-api.com/json")
content = response.json()

print(content["query"])
print("---")
print("as: " + content["as"])
print("isp: " + content["isp"])
print("org: " + content["org"])
print("---")
print("city: " + content["city"])
print("region: " + content["regionName"])
print("country: " + content["country"])
print("timezone: " + content["timezone"])
print("zip: " + content["zip"])
print("lat: " + str(content["lat"]))
print("lon: " + str(content["lon"]))
print("---")
