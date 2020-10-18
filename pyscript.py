# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 17:35:10 2020

@author: amanb
"""

import serial
import time
import schedule
import urllib
from urllib.request import urlopen

def update_data(i, n):
    data=urlopen('https://api.thingspeak.com/update?api_key=82E96JJMSTJI6JMW&field'+str(i)+'='+str(n))
    print(data)
    
def main_func():
    arduino = serial.Serial('com1', 9600)
    print('Established serial connection to Arduino')
    arduino_data = arduino.readline()

    decoded_values = str(arduino_data[0:len(arduino_data)].decode("utf-8"))
    list_values = decoded_values.split('x')

    for item in list_values:
        list_in_floats.append(float(item))
    a=list_in_floats[0];
    b=list_in_floats[1];
    c=list_in_floats[2];
    update_data(1,a);
    update_data(2,b);
    update_data(3,c);
    print(f'Collected readings from Arduino: {list_in_floats}')
      
    arduino_data = 0
    list_in_floats.clear()
    list_values.clear()
    arduino.close()
   
    
def main_func_1():
    arduino_1=serial.Serial('com2',9600)
    arduino_data_1=arduino_1.readline()
    decoded_values_1 = str(arduino_data_1[0:len(arduino_data_1)].decode("utf-8"))
    list_values_1 = decoded_values_1.split('x')
    for item_1 in list_values_1:
        list_in_floats_1.append(float(item_1))
    d=list_in_floats_1[0];
    e=list_in_floats_1[1];
    update_data(4,d);
    update_data(5,e);
    print(f'Collected readings from Arduino: {list_in_floats_1}')    
    arduino_data_1 = 0
    list_in_floats_1.clear()
    list_values_1.clear()
    arduino_1.close()
    print('Connection closed')
    print('<--------------------------------------------->')
    
# ----------------------------------------Main Code------------------------------------
# Declare variables to be used
list_values = []
list_in_floats = []
list_values_1= []
list_in_floats_1 = []


print('Program started')

# Setting up the Arduino
schedule.every(2).seconds.do(main_func)
schedule.every(5).seconds.do(main_func_1)

while True:
    schedule.run_pending()
    time.sleep(1)