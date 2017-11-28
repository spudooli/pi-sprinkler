#!/usr/bin/python

"""Monitors GPIO buttons to allow local control of Sprinklers
Also provides LED status updates
Should be started by systemd"""

import logging
logging.basicConfig(filename='/tmp/pi-sprinkler.log',level=logging.INFO)

from relay_lib_seeed import *

import time

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

Led_status = 1

button_list = 18
zone1LEDpin = 23


GPIO.setup(button_list, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.output(zone1LEDpin, GPIO.HIGH) # Set LedPin high(+3.3V) to off led

def buttonZone1(channel):
    print "Zone 1 button pressed"
    GPIO.output(zone1LEDpin, status)


GPIO.add_event_detect(18, GPIO.FALLING, callback=buttonZone2, bouncetime=300)


def DoTheLoop():
    count = 0
    while count < 30:
        count = count + 1
        time.sleep(.2)

while 1:
    DoTheLoop()
