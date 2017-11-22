#!/usr/bin/python

"""Run from cron every minute. Checks if any zones are on and if so allows them to run for no
more than 60 minutes before shutting them off automatically
Is a fail safe to ensure that even if the Pi loses WIFI, the water won't run all night. """

import logging
import os
logging.basicConfig(filename='/tmp/pi-sprinkler-failsafe.log', level=logging.INFO)

from relay_lib_seeed import *

installedZones = int(5)

def checkAllZones():
    for zonenumber in range(1, installedZones):
        if relay_get_port_status(zonenumber):
            logging.info('Zone' + str(zonenumber) + ' on')
        else:
            logging.info('No zones running')


def checkLogFile():
    zonecount = 0
    for zonenumber in range(1, installedZones):
        with open("/tmp/pi-sprinkler-failsafe.log", "r") as logfile:
            for line in logfile:
                if "Zone" + str(zonenumber) in line:
                    zonecount = zonecount + 1
                    print zonecount
                    if zonecount > 60:
                        turnOffZone(zonenumber)
                        zonecount = 0

def turnOffZone(zone):
    relay_off(zone)
    print "Turning off zone "
    os.remove("/tmp/pi-sprinkler-failsafe.log")

checkAllZones()

checkLogFile()
