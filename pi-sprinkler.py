from relay_lib_seeed import *

import logging
logging.basicConfig(filename='/tmp/pi-sprinkler.log',level=logging.INFO)

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)


zone = sys.argv[1]
state = sys.argv[2]

if state = On:
	relay_on(zone)

if state = Off:
	relay_off(zone)

