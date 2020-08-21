#!/usr/bin/env python
from gpiozero import Button #import button from the Pi GPIO library
from gpiozero import PWMLED

from time import sleep # import time functions
import os #imports OS library for Shutdown control

led = PWMLED(18) 
stopButton = Button(3) # defines the button as an object and chooses GPIO 26
printerButton = Button(4)

led.value = 1

def blink():
    led.off()
    sleep(0.1)
    led.on()
    sleep(0.1)


while True: #infinite loop
     if printerButton.is_pressed: #Check to see if button is pressed
        led.pulse()
        sleep(2)
        if printerButton.is_pressed:
            blink()
            blink()
            blink()
            os.system("/usr/local/bin/toggle-printer-power")
            sleep(1)
            for x in range(10):
                if printerButton.is_pressed:
                    blink();
            if printerButton.is_pressed:
                print("YOU should check if printer is on, and if so send command to preheat")
        led.value = 1
     if stopButton.is_pressed: #Check to see if button is pressed
        for x in range(10):            
            if stopButton.is_pressed:
                blink();
        if stopButton.is_pressed:
            os.system("/usr/local/bin/shutdown-with-printer")
     sleep(1) # wait for the hold time we want. 
