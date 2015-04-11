from PyGlow import PyGlow
from time import sleep

myPiGlow = PyGlow()

myPiGlow.all(0)

while True:
   myPiGlow.color("white",90)
   sleep(1)
   myPiGlow.color("white",0)
   sleep(1)
   myPiGlow.color("blue",90)
   sleep(1)
   myPiGlow.color("blue",0)
   sleep(1)
   myPiGlow.color("green",90)
   sleep(1)
   myPiGlow.color("green",0)
   sleep(1)
   myPiGlow.color("yellow",90)
   sleep(1)
   myPiGlow.color("yellow",0)
   sleep(1)
   myPiGlow.color("orange",90)
   sleep(1)
   myPiGlow.color("orange",0)
   sleep(1)
   myPiGlow.color("red",90)
   sleep(1)
   myPiGlow.color("red",0)
   sleep(1)

myPiGlow.update_leds()
