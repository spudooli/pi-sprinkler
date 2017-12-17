#!/usr/bin/python3

""" A really basic sprinkler start stop script because Homevision has a scheduler/timer
and we have a backup in sprinkler-failsafe """

import logging
logging.basicConfig(filename='/tmp/pi-sprinkler.log', level=logging.INFO)

from relay_lib_seeed import *

import sys

from gpiozero import LED

zone1LEDpin = LED(4)
zone2LEDpin = LED(23)

zone = sys.argv[1]
zone = int(zone)
state = sys.argv[2]

installedZones = int(5)

def allLEDsOff():
    zone1LEDpin.off()
    zone2LEDpin.off()

def checkAnyZonesRunning():
    zonerunningcount = 0
    for zonenumber in range(1, installedZones):
        if relay_get_port_status(zonenumber):
            zonerunningcount = zonerunningcount + 1
            print(zonerunningcount)
    if zonerunningcount > 0:
        logging.info('Cannot turn zone' + str(zonenumber) + ' on there is already a zone running')
        zonerunningcount = 0
        return True
    else:
        return False

if zone == 0:
    relay_all_off()
    with open('/tmp/zone1.txt', 'w'):
        pass
    with open('/tmp/zone2.txt', 'w'):
        pass

if zone == 1:
    if state == "On":
        if not checkAnyZonesRunning():
            file = open('/tmp/zone1.txt','w')
            file.write(“zone1”)
            file.close
            relay_on(1)
            logging.info('Turned Zone 1 on')
            zone1LEDpin.blink(background=True)
    if state == "Off":
        with open('/tmp/zone1.txt', 'w'):
            pass
        relay_off(1)
        logging.info('Turned Zone 1 off')

if zone == 2:
    if state == "On":
        if not checkAnyZonesRunning():
            file = open('/tmp/zone2.txt','w')
            file.write(“zone2”)
            file.close
            relay_on(2)
            logging.info('Turned Zone 2 on')
            zone2LEDpin.blink(background=True)
    if state == "Off":
        with open('/tmp/zone2.txt', 'w'):
            pass
        relay_off(2)
        logging.info('Turned Zone 2 off')
