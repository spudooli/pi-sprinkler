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

button_list = [17,18] 
zone1LEDpin = 11
zone2LEDpin = 12

GPIO.setup(button_list, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.output(zone1LEDpin, GPIO.HIGH) # Set LedPin high(+3.3V) to off led
GPIO.output(zone2LEDpin, GPIO.HIGH) # Set LedPin high(+3.3V) to off led

def zone1LED(status):
    GPIO.output(zone1LEDpin, status)  # switch led status(on-->off; off-->on)
    if status == 1:
        print 'led off...'
    else:
        print '...led on'

def zone2LED(status):
    GPIO.output(zone2LEDpin, status)  # switch led status(on-->off; off-->on)
    if status == 1:
        print 'led off...'
    else:
        print '...led on'

def buttonZone1(channel):  
    print "Zone 1 button pressed"

def buttonZone2(channel):  
    print "Zone 2 button pressed"

GPIO.add_event_detect(17, GPIO.FALLING, callback=buttonZone1, bouncetime=300)

GPIO.add_event_detect(18, GPIO.FALLING, callback=buttonZone2, bouncetime=300)


def DoTheLoop():
    count = 0
    while count < 30:
        count = count + 1
        time.sleep(.2)

while 1:
    DoTheLoop()
