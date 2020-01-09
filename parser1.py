#!/usr/bin/env python3

import csv
import requests
import json

ro = []
with open('prilogeniya.csv') as csvfile:
    reader = csv.DictReader(csvfile, doublequote='True')
    for row in reader:
        ro.append(row)

url = 'http://172.16.8.8:1515'
for now in ro:
	data = now
	answer = requests.post(url, data=json.dumps(data))


#answer = requests.post(url, data=json.dumps(ro[2]))
#print(answer)
