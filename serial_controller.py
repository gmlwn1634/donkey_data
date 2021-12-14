#!/usr/bin/env python3

import serial
import time

class SerialController:
    def __init__(self):
        self.ser = ""
        self.temp = ""
        self.data = 9999
        self.distance = 30
        self.on = True
        self.wave_throttle = 0

    def update(self):
        while self.on:
            self.poll()

    def poll(self):
        self.ser = serial.Serial('/dev/ttyACM0', 9600)
        try:
            self.data = self.ser.readline().decode('utf-8').strip('/r').strip('/t')
            self.data = int(self.data)
            #print("recive:", self.data)
 
        except:
            #print("Wrong Data..!", self.data)
            

    def run_threaded(self, throttle):
        if throttle is None:
            return throttle

        if 0 < self.data < self.distance:
            self.wave_throttle = 0
            #print("stop!!", self.data)
            return self.wave_throttle


    def run(self, throttle):
        result = self.run_threaded(throttle)
        return result

    def shutdown(self):
        self.ser.close()
        self.on = False
        print("shutdown wave sensor..!")
