#!/usr/bin/python

"""Run from cron every minute. Checks if any zones are on and if so allows them to run for no
more than 60 minutes before shutting them off automatically
Is a fail safe to ensure that even if the Pi loses WIFI, the water won't run all night. """

import logging
import os
logging.basicConfig(filename='/tmp/pi-sprinkler-failsafe.log', level=logging.INFO)

from relay_lib_seeed import *

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

zone1Button = 24
zone2Button = 18
zone1LEDpin = 3
zone2LEDpin = 23
GPIO.setup(zone1LEDpin,GPIO.OUT)
GPIO.setup(zone2LEDpin,GPIO.OUT)

installedZones = int(5)

def allLEDsOff():
    GPIO.output(zone1LEDpin, GPIO.LOW)
    GPIO.output(zone2LEDpin, GPIO.LOW)

def checkAllZones():
    for zonenumber in range(1, installedZones):
        if relay_get_port_status(zonenumber):
            logging.info('Zone' + str(zonenumber) + ' on')
        else:
            logging.info('No zones running')


def checkLogFile():
    zonecount = 0
    for zonenumber in range(1, installedZones):
        with open("/tmp/pi-sprinkler-failsafe.log", "r") as logfile:
            for line in logfile:
                if "Zone" + str(zonenumber) in line:
                    zonecount = zonecount + 1
                    print zonecount
                    if zonecount > 60:
                        turnOffZone(zonenumber)
                        zonecount = 0

def turnOffZone(zone):
    relay_all_off()
    allLEDsOff()
    print "Turning off all zones"
    with open('/tmp/pi-sprinkler-failsafe.log', 'w'):
        pass

checkLogFile()

checkAllZones()