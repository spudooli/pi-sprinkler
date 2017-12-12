import serial

arduino = serial.Serial(
    port='/dev/ttyAMA0',
    baudrate=19200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)

def checkZoneRunning(command):
    print command
    arduino.write(command)
    line = ""
    line = arduino.readline()   #read a '\n' terminated lin
    print line
    if line == "1":
        return True
    else:
        return False

def relay_on(command):
    print command
    arduino.write(command)

def relay_all_off():
    arduino.write('B')
    arduino.write('D')
    arduino.write('F')
    arduino.write('H')

