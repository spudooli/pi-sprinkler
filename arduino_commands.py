import serial

arduino = serial.Serial(
    port='/dev/ttyAMA0',
    baudrate=19200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)

def checkZoneRunning(command):
    arduino.write(command)
    line = ""
    line = arduino.readline()   #read a '\n' terminated lin
    if line == "1":
        return True

def ardiuino_zone(command):
    arduino.write(command)
