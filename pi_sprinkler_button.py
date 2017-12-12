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
GPIO.setwarnings(False)

installedZones = int(5)
zone1Button = 24
zone2Button = 18
zone1LEDpin = 4
zone2LEDpin = 23
GPIO.setup(zone1LEDpin,GPIO.OUT)
GPIO.setup(zone2LEDpin,GPIO.OUT)
GPIO.output(zone1LEDpin, GPIO.LOW)
GPIO.output(zone2LEDpin, GPIO.LOW)

GPIO.setup(zone1Button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(zone2Button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

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

def buttonZone1(status):
    print "Zone 1 button pressed"
    if not checkAnyZonesRunning():
        relay_on(1)
        logging.info('Turned Zone 1 on')
        GPIO.output(zone1LEDpin, GPIO.HIGH)
    else:
        relay_all_off()
        logging.info('Turned Zone 1 off')
        with open('/tmp/pi-sprinkler-failsafe.log', 'w'):
            pass
        allLEDsOff()

def buttonZone2(status):
    print "Zone 2 button pressed"
    if not checkAnyZonesRunning():
        relay_on(2)
        logging.info('Turned Zone 1 on')
        GPIO.output(zone2LEDpin, GPIO.HIGH)
    else:
        relay_all_off()
        logging.info('Turned Zone 1 off')
        with open('/tmp/pi-sprinkler-failsafe.log', 'w'):
            pass
        allLEDsOff()

logging.info('Started Pi Sprinkler Button')

GPIO.add_event_detect(zone1Button, GPIO.FALLING, callback=buttonZone1, bouncetime=300)
GPIO.add_event_detect(zone2Button, GPIO.FALLING, callback=buttonZone2, bouncetime=300)

try:
    while True:
        time.sleep(0.2)

except KeyboardInterrupt:
    GPIO.cleanup()
    logging.info('Stopped Pi Sprinkler Button - Stopped')