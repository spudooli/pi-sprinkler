#!/usr/bin/python

# Monitors GPIO buttons to allow local control of Sprinklers
# Also provides LED status updates
#Should be started by systemd

import logging
logging.basicConfig(filename='/tmp/pi-sprinkler.log',level=logging.INFO)

from relay_lib_seeed import *

import time

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def Loop():
    count = 0
    while count < 30:
        input_state = GPIO.input(18)
        if input_state == False:
            print "Button Pushed"
            #relay_on(zone)
            time.sleep(0.2)

while 1:
    Loop()
