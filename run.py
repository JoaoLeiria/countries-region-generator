#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from pprint import pprint

import requests
import json

f = open('generated_data.json', 'w')

with open('data.json') as data_file:
    countries = json.load(data_file)
for country in countries:
	# country = countries[0]
	auxInfo = json.loads(requests.get("https://restcountries.eu/rest/v2/alpha/" + country['countryShortCode']).content)
	country['timezones'] = auxInfo['timezones']
	country['translations'] = auxInfo['translations']
	country['latlng'] = auxInfo['latlng']
	country['flag'] = "./flags/" + country['countryShortCode'] + ".svg"

f.write(json.dumps(countries))
f.close()
# print json.dumps(country, sort_keys=True, indent=4, separators=(',', ': '))