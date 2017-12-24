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
    zone1LEDpin.close()
    zone2LEDpin.off()
    zone2LEDpin.close()


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
    while True:
        time.sleep(1)
        with open("/tmp/zone1.txt", "r") as zoneLED1file:
            for line in zoneLED1file:
                if "Zone1" in line:
                    zone1LEDpin.blink()
                else:
                    allLEDsOff()
                    with open('/tmp/zone1.txt', 'w'):
                        pass
        with open("/tmp/zone2.txt", "r") as zoneLED2file:
            for line in zoneLED2file:
                if "Zone2" in line:
                    zone2LEDpin.blink()
                else:
                    allLEDsOff()
                    with open('/tmp/zone2.txt', 'w'):
                        pass
except KeyboardInterrupt:
    logging.info('Stopped Pi Sprinkler Button - Stopped')

