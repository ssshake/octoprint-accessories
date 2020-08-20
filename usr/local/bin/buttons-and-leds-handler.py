#!/usr/bin/env python
from gpiozero import Button #import button from the Pi GPIO library
from gpiozero import LED

from time import sleep # import time functions
import os #imports OS library for Shutdown control

led = LED(18) 
stopButton = Button(3) # defines the button as an object and chooses GPIO 26
printerButton = Button(4)

led.on()

def blink():
    led.off()
    sleep(0.1)
    led.on()
    sleep(0.1)


while True: #infinite loop
     if printerButton.is_pressed: #Check to see if button is pressed
        for x in range(10):            
            if printerButton.is_pressed:
                blink();
        if printerButton.is_pressed:
            print("this would have shut toggled the printer down.....")
            os.system("/usr/local/bin/toggle-printer-power")
     if stopButton.is_pressed: #Check to see if button is pressed
        for x in range(10):            
            if stopButton.is_pressed:
                blink();
        if stopButton.is_pressed:
            print("this would have shut down.....")
            #os.system("/usr/local/bin/shutdown-with-printer")
            while True:
                blink()
     sleep(1) # wait for the hold time we want. 
