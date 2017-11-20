#Run from cron every minute. Checks if any zones are on and if so allows them to run for no 
# more than 90 minutes before shutting them off automatically
#Is a fail safe to ensure that even if the Pi loses WIFI, the water won't run all night.

from relay_lib_seeed import *

import logging
logging.basicConfig(filename='/tmp/pi-sprinkler.log',level=logging.INFO)

installedZones = 2

def checkAllZones()

def turnOffZone(zone)
	relay_off(zone)

checkAllZones()
