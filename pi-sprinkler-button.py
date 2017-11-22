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

button_list = [17,18] 

GPIO.setup(button_list, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def buttonZone1(channel):  
    print "Zone 1 button pressed"

def buttonZone2(channel):  
    print "Zone 2 button pressed"

GPIO.add_event_detect(17, GPIO.FALLING, callback=buttonZone1, bouncetime=300)

GPIO.add_event_detect(18, GPIO.FALLING, callback=buttonZone2, bouncetime=300)


#def DoTheLoop():
#    count = 0
#    while count < 30:
#        print count

#while 1:
#:    DoTheLoop()
