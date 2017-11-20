#Monitors GPIO buttons to allow local control of Sprinklers

import logging
logging.basicConfig(filename='/tmp/pi-sprinkler.log',level=logging.INFO)

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def Loop():
	count = 0
	while (count < 30):
		input_state = GPIO.input(18)
			if input_state == False:
            	print('Button Pushed')
            	relay_on(zone)
            	time.sleep(0.2)

