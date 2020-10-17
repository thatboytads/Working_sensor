#!/usr/bin/env python
"""
	Detects motion and outputs a sound via a piezo buzzer. 
"""

import RPi.GPIO as GPIO
import time

__author__ = "gus-pimylifeup"
__version__ = "1.0"
__maintainer__ = "pimylifeup.com"
pir_sensor2 = 13
pir_sensor = 11
piezo = 7

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pir_sensor2, GPIO.IN)
GPIO.setup(piezo,GPIO.OUT)

GPIO.setup(pir_sensor, GPIO.IN)

current_state = 0
current = 0
parked = 0
try:
    while True:
        current_state = GPIO.input(pir_sensor)
        if current_state == 1 and parked == 0:
            time.sleep(1)
            print("are we parking")
            current_state=GPIO.input(pir_sensor)
            current_state2= GPIO.input(pir_sensor2)
            current = current_state + current_state2
            if current == 2:
                print("welcome car")
                GPIO.output(piezo,True)
                print("ring")
                time.sleep(1)
                print("stop")
                GPIO.output(piezo,False)
                print("waiting for you to park")
                time.sleep(3)
                print("we done hey!!!!!!")
                parked = 1
                continue
        current_state2= GPIO.input(pir_sensor2)
        if current_state2 == 1 and parked == 1:
            print("are you going?")
            time.sleep(1)
            current_state= GPIO.input(pir_sensor)
            current = current_state + current_state2
            if current == 2:
                print("don't go")
                GPIO.output(piezo,True)
                print("ring")
                time.sleep(1)
                print("stop")
                GPIO.output(piezo,False)
                print("waiting for you to go")
                time.sleep(3)
                print("see you next time")
                parked = 0
                continue
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
