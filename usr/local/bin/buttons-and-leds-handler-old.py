#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BOARD)

ledPin = 12
powerButtonPin = 5
printerTogglePin = 7

GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(powerButtonPin, GPIO.IN)
#GPIO.setup(powerButtonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(printerTogglePin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print("SETTING POWER LED ON")
GPIO.output(ledPin, GPIO.HIGH)

# Define a callback function that will be called by the GPIO
# event system:
def onButton(channel):
    print("Button Channel Is")
    print(channel)
    if channel == powerButtonPin:
        os.system("/usr/local/bin/shutdown-with-printer&")
    if channel == printerTogglePin:
        os.system("/usr/local/bin/toggle-printer-power&")


# Register an edge detection event on FALLING edge. When this event
# fires, the callback onButton() will be executed. Because of
# bouncetime=20 all edges 20 ms after a first falling edge will be ignored: 
GPIO.add_event_detect(powerButtonPin, GPIO.FALLING, callback=onButton, bouncetime=10000)
GPIO.add_event_detect(printerTogglePin, GPIO.FALLING, callback=onButton, bouncetime=10000)

# The script would exit now but we want to wait for the event to occure
# so we block execution by waiting for keyboard input so every key will exit
# this script
#input()

while True:
    time.sleep(1)
