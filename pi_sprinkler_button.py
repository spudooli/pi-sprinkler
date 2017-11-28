#!/usr/bin/python

"""Monitors GPIO buttons to allow local control of Sprinklers
Also provides LED status updates
Should be started by systemd"""

import logging
logging.basicConfig(filename='/tmp/pi-sprinkler.log',level=logging.INFO)

from relay_lib_seeed import *
from pi_sprinkler import checkAnyZonesRunning

import time

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

Led_status = 1

zone1Button = 18
zone1LEDpin = 23


GPIO.setup(button_list, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(zone1LEDpin,GPIO.OUT)


GPIO.output(zone1LEDpin, GPIO.LOW) # Set LedPin high(+3.3V) to off led

def buttonZone1():
    print "Zone 1 button pressed"
    if not checkAnyZonesRunning():
        relay_on(1)
        logging.info('Turned Zone ' + str(zone) + ' on')
        GPIO.output(zone1LEDpin, GPIO.HIGH)

    else:
        relay_off(1)
        logging.info('Turned Zone ' + str(zone) + ' on')
        GPIO.output(zone1LEDpin, GPIO.LOW)



GPIO.add_event_detect(zone1Button, GPIO.FALLING, callback=buttonZone1, bouncetime=300)


try:
    while True:
        time.sleep(0.2)

except KeyboardInterrupt:
    GPIO.cleanup()
