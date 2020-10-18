# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 17:35:10 2020

@author: amanb
"""

import serial
import time
import schedule
from bs4 import BeautifulSoup


def main_func():
    arduino = serial.Serial('com1', 9600)
    print('Established serial connection to Arduino')
    arduino_data = arduino.readline()

    decoded_values = str(arduino_data[0:len(arduino_data)].decode("utf-8"))
    list_values = decoded_values.split('x')

    for item in list_values:
        list_in_floats.append(float(item))

    print(f'Collected readings from Arduino: {list_in_floats}')   
    
    arduino_data = 0
    list_in_floats.clear()
    list_values.clear()
    arduino.close()
    print('Connection closed')
    print('<----------------------------->')


# ----------------------------------------Main Code------------------------------------
# Declare variables to be used
list_values = []
list_in_floats = []

print('Program started')

# Setting up the Arduino
schedule.every(3).seconds.do(main_func)

while True:
    schedule.run_pending()
    time.sleep(1)