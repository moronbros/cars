#!/usr/bin/python

import sys
import httplib
import json
from pprint import pprint

target = sys.argv[1]

connection = httplib.HTTPSConnection('www.car2go.com')

headers = {'Content-type:': 'application/json'}

connection.request('GET', '/api/v2.1/vehicles?loc=seattle&oauth_consumer_key=GetMeWheels&format=json')
response = connection.getresponse()
cars = json.loads(response.read().decode())


for car in cars[u'placemarks']:
    if car[u'name'] == target:
        print car
