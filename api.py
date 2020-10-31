# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 18:56:50 2020

@author: Aman
"""
import flask
from flask import jsonify
import json
import re
import urllib
from urllib import request
from bs4 import BeautifulSoup
data1=urllib.request.urlopen("https://api.thingspeak.com/channels/1183417/feeds.json?results=150");
my_json=data1.read().decode('utf-8').replace("'",'"')
data=json.loads(my_json);
final_data=json.dumps(data,indent=9,sort_keys=True)
app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
   return data

app.run()