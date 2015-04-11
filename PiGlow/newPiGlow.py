#! /usr/bin/python

# newPiGlow.py
# Author: Darrell Little
# Version: 0.2
# Date: 03/04/2015

from PyGlow import PyGlow
from time import sleep

myPiGlow = PyGlow()

colors = ["white","blue","green","yellow","orange","red"]

c = 0

myPiGlow.all(0)

print "Beginning Colors"

while c < 5:
   for x in colors:
      print "Color: ",x
      myPiGlow.color(x,90)
      sleep(1)
      myPiGlow.color(x,0)
      sleep(1)
      c += 1

print "End Colors"

myPiGlow.all(0)

myPiGlow.update_leds()
