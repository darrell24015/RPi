# single_led_blink.py
# Author: Darrell Little
# Version: 0.1
# Date: 02/28/2015
# This simple program sets up GPIO pin 11 as OUT 3.3V
# Then inside a loop, turns on GPIO pin 11 (True)
# Waits 1 second and turns off GPIO pin 11 (False)
# Since the GPIO requires Admin permission, you have to use sudo
# To run the program, type sudo python single_led_blink.py
# To stop the program, type Control-C
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

while True:
    GPIO.output(11, True)
    time.sleep(1)
    GPIO.output(11, False)
    time.sleep(1)
