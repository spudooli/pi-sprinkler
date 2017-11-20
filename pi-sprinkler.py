from relay_lib_seeed import *

import logging
logging.basicConfig(filename='/tmp/pi-sprinkler.log',level=logging.INFO)

zone = sys.argv[1]
state = sys.argv[2]

if state = On:
	relay_on(zone)

if state = Off:
	relay_off(state)
	