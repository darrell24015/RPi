# This simple program sets up GPIO pins 11,13,15, 16, 18 and 22 as OUT 3.3V
# Then inside a loop, turns on each GPIO pin (True)
# Waits and turns off each GPIO pin (False)
# To run the program, type sudo python six_loop_blink.py
# Since the GPIO requires Admin permission, you have to use sudo
# To stop the program, type Control-C

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

# Turn on the pins in order to make a loop then flash all six LED lights
while True:
    GPIO.output(11, True)
    time.sleep(.1)
    GPIO.output(13, True)
    GPIO.output(11, True)
    time.sleep(.1)
    GPIO.output(15, True)
    GPIO.output(11, False)
    time.sleep(.1)
    GPIO.output(22, True)
    GPIO.output(13, False)
    time.sleep(.1)
    GPIO.output(18, True)
    GPIO.output(15, False)
    time.sleep(.1)
    GPIO.output(16, True)
    GPIO.output(18, False)
    time.sleep(.1)
    GPIO.output(22, False)
    time.sleep(.1)
    GPIO.output(16, False)
    time.sleep(.5)

# Flash All the LEDs
    GPIO.output(11, True)
    GPIO.output(13, True)
    GPIO.output(22, True)
    GPIO.output(15, True)
    GPIO.output(18, True)
    GPIO.output(16, True)
    time.sleep(.5)
    GPIO.output(11, False)
    GPIO.output(13, False)
    GPIO.output(22, False)
    GPIO.output(15, False)
    GPIO.output(18, False)
    GPIO.output(16, False)
    time.sleep(1)
   
