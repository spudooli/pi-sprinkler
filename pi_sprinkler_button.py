#!/usr/bin/python

"""Monitors GPIO buttons to allow local control of Sprinklers
Also provides LED status updates
Should be started by systemd"""

import logging
logging.basicConfig(filename='/tmp/pi-sprinkler.log',level=logging.INFO)

from relay_lib_seeed import *

from gpiozero import LED, Button

import time


installedZones = int(5)
zone1Button = Button(24, hold_time=2)
zone2Button = Button(18, hold_time=2)
zone1LEDpin = LED(4)
zone2LEDpin = LED(23)


def allLEDsOff():
    zone1LEDpin.off()
    zone2LEDpin.off()


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
        zone1LEDpin.on()
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
        zone2LEDpin.on()
    else:
        relay_all_off()
        logging.info('Turned Zone 1 off')
        with open('/tmp/pi-sprinkler-failsafe.log', 'w'):
            pass
        allLEDsOff()

logging.info('Started Pi Sprinkler Button')

zone1Button.when_held = buttonZone1
zone2Button.when_held = buttonZone2

try:
    while True:
        time.sleep(0.2)

except KeyboardInterrupt:
    logging.info('Stopped Pi Sprinkler Button - Stopped')
