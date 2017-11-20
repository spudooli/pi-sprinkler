# pi-sprinkler

Raspberry Pi Sprinkler, 2 zones, with added fail safe

Thanks to the work of John Wargo at https://github.com/johnwargo/Seeed-Studio-Relay-Board

A Seeed Studio relay board is mounted on top of a Raspberry Pi connected to 24VDC Hunter PGV solenoid valves, voice controlled with Google Assistant, which is connected to an IFTT recipe, that calls a webhook on our webserver, which runs a macro in Homevision, which calls an external shell script, which runs a pi-sprinkler.py on the Rapsberry Pi via SSH. 

The Homevision macro will handle turning off the zone after an appropriate amount of time. but in case that fails, there is sprinkler-failsafe.py that is run every minute via cron.

There is also local control via buttons connected to Rapsberry Pi GPIOs, but they will trigger everything via Homevision anyway to maintain control.   
