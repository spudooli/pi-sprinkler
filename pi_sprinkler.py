#!/usr/bin/python

""" A really basic sprinkler start stop script because Homevision has a scheduler/timer
and we have a backup in sprinkler-failsafe """

import logging
logging.basicConfig(filename='/tmp/pi-sprinkler.log', level=logging.INFO)

from relay_lib_seeed import *
import sys

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
zone1Button = 24
zone2Button = 18
zone1LEDpin = 3
zone2LEDpin = 23
GPIO.setup(zone1LEDpin,GPIO.OUT)
GPIO.setup(zone2LEDpin,GPIO.OUT)

zone = sys.argv[1]
zone = int(zone)
state = sys.argv[2]

installedZones = int(5)

def allLEDsOff():
    GPIO.output(zone1LEDpin, GPIO.LOW)
    GPIO.output(zone2LEDpin, GPIO.LOW)

def checkAnyZonesRunning():
    zonerunningcount = 0
    for zonenumber in range(1, installedZones):
        if relay_get_port_status(zonenumber):
            zonerunningcount = zonerunningcount + 1
            print zonerunningcount
    if zonerunningcount > 0:
        logging.info('Cannot turn zone' + str(zonenumber) + ' on there is already a zone running')
        zonerunningcount = 0
        return True
    else:
        return False

if zone == "1":
    if state == "On":
        if not checkAnyZonesRunning():
            relay_on(1)
            logging.info('Turned Zone 1 on')
            GPIO.output(zone1LEDpin, GPIO.HIGH)
    if state == "Off":
        relay_off(1)
        logging.info('Turned Zone 1 off')
        allLEDsOff()

if zone == "2":
    if state == "On":
        if not checkAnyZonesRunning():
            relay_on(2)
            logging.info('Turned Zone 2 on')
            GPIO.output(zone2LEDpin, GPIO.HIGH)
    if state == "Off":
        relay_off(2)
        logging.info('Turned Zone 2 off')
        allLEDsOff()
