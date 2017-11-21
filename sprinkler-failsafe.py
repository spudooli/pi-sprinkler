#Run from cron every minute. Checks if any zones are on and if so allows them to run for no 
# more than 60 minutes before shutting them off automatically
#Is a fail safe to ensure that even if the Pi loses WIFI, the water won't run all night.

from relay_lib_seeed import *

import logging
logging.basicConfig(filename='/tmp/pi-sprinkler.log',level=logging.INFO)

installedZones = int(5)

def checkAllZones():
    for zonenumber in range(1, installedZones):
        if relay_get_port_status(zonenumber):
            print "yep"
            logging.info('Zone' + str(zonenumber) + ' on')

def checkLogFile():
    zonecount = 0
    for zonenumber in range(1, installedZones):
        with open("/tmp/pi-sprinkler.log", "r") as logfile:
            for line in logfile:
                if "Zone" + str(zonenumber) in line:
                    print "found " + line
                    zonecount = zonecount + 1
                    print zonecount
                    if zonecount > 60:
                        turnOffZone(zonenumber)
                        zonecount = 0

def turnOffZone(zone):
    #something
    print "Turning off zone " + zone

checkAllZones()

checkLogFile()
