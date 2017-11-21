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

if state == "On":
    relay_on(zone)
    logging.info('Zone' + str(zonenumber) + ' on')

if state == "Off":
    relay_off(zone)
    logging.info('Zone' + str(zonenumber) + ' off')
