#Run from cron every minute. Checks if any zones are on and if so allows them to run for no 
# more than 60 minutes before shutting them off automatically
#Is a fail safe to ensure that even if the Pi loses WIFI, the water won't run all night.

from relay_lib_seeed import *

import logging
logging.basicConfig(filename='/tmp/pi-sprinkler.log',level=logging.INFO)

installedZones = int(5)

def checkAllZones():
	for x in range(1, installedZones):
		if relay_get_port_status(x):
			print "yep"
			logging.info('Zone' + str(x) + ' on')

def checkLogFile():
	zonecount = 0
	for x in range(1, installedZones):	
		file = open("/tmp/pi-sprinkler.log", "r")
		for line in file:
			if "Zone" + str(x) in line:
				zonecount = zonecount + 1
		if zonecount > 60:
				turnOffZone(x)

def turnOffZone(zone):
	#something
	print "Turning off zone " + zone

checkAllZones()

checkLogFile()
