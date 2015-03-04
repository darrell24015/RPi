#! /usr/bin/python

from PyGlow import PyGlow
from time import sleep

myPiGlow = PyGlow()

colors = ["white","blue","green","yellow","orange","red"]

myPiGlow.all(0)

while True:
   for x in colors:
      myPiGlow.color(x,90)
      sleep(1)
      myPiGlow.color(x,0)
      sleep(1)

myPiGlow.update_leds()
