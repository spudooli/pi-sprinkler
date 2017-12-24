#!/usr/bin/python3

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

button1pressed = False
button2pressed = False


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

def buttonZone1(status):
    print("Zone 1 button pressed")
    if not checkAnyZonesRunning():
        relay_on(1)
        logging.info('Turned Zone 1 on')
        button1pressed = True
        zone1LEDpin.on()
    else:
        relay_all_off()
        logging.info('Turned Zone 1 off')
        with open('/tmp/pi-sprinkler-failsafe.log', 'w'):
            pass
        button1pressed = False
        allLEDsOff()

def buttonZone2(status):
    print("Zone 2 button pressed")
    if not checkAnyZonesRunning():
        relay_on(2)
        logging.info('Turned Zone 1 on')
        button2pressed = True
        zone2LEDpin.on()
    else:
        relay_all_off()
        logging.info('Turned Zone 1 off')
        with open('/tmp/pi-sprinkler-failsafe.log', 'w'):
            pass
        button2pressed = False
        allLEDsOff()

logging.info('Started Pi Sprinkler Button')

zone1Button.when_held = buttonZone1
zone2Button.when_held = buttonZone2

try:
    zone1blinkingcount = 0
    zone2blinkingcount = 0
    while True:
        time.sleep(1)
        if relay_get_port_status(1):
            print("Looks like zone 1 is on")
            if not button1pressed:
                print("And not pressed")
                if (zone1blinkingcount > 10):
                    print(zone1blinkingcount)
                    zone1LEDpin.blink()
                    zone1blinkingcount = 0
            zone1blinkingcount = zone1blinkingcount + 1
        else:
            if not button1pressed:
                zone1LEDpin.off()
                zone1blinkingcount = 0

        if relay_get_port_status(2):
            if not button2pressed:
                zone2LEDpin.blink()
except KeyboardInterrupt:
    logging.info('Stopped Pi Sprinkler Button - Stopped')

