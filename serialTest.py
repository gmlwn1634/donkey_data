import serial
import time
import json


port = '/dev/ttyACM0'
baud = 9600
serial = serial.Serial(port,baud)

time.sleep(0.3)



while True:
    if serial.readable():
        res = serial.readline()
        distance = res.decode()[:len(res)-1]
        if int(distance) < 40:
            print("catch ",distance)
