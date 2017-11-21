# A really basic sprinkler start stop script because Homevision has a scheduler/timer
# and we have a backup in sprinkler-failsafe 

import logging
logging.basicConfig(filename='/tmp/pi-sprinkler.log', level=logging.INFO)

from relay_lib_seeed import *
import sys 

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

zone = sys.argv[1]
zone = int(zone)
state = sys.argv[2]

installedZones = int(5)

def checkAnyZonesRunning():
    zonerunningcount = 0
    for zonenumber in range(1, installedZones):
        if relay_get_port_status(zonenumber):
            zonerunningcount = zonerunningcount + 1
            print zonerunningcount
    if zonerunningcount > 0:
        logging.info('Cannot turn zone' + str(zonenumber) + ' on because there is already a zone running')
        zonerunningcount = 0
        return True
    else:
        return False    
 
if state == "On":
    if not checkAnyZonesRunning():
        relay_on(zone)
        logging.info('Turned Zone ' + str(zone) + ' on')

if state == "Off":
    relay_off(zone)
    logging.info('Turned Zone ' + str(zone) + ' off')
