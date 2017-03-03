#!/usr/bin/python

# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

###########################################
# This file is for the upstairs RPi-APlus #
###########################################


#############################
# Setting up Python Modules #
#############################
from time import sleep
import Adafruit_DHT
import sys
from ubidots import ApiClient

##################################
# Method for displaying the      #
# countdown between measurements #
# Pass the method the number     #
# of minutes into variable 't'   #
##################################
def countdown(t):
    for i in range(t,0,-1):
        print 'Waiting for %d minutes\r' % i,
        sys.stdout.flush()
        sleep(60)
try:
	# Create an Ubidots object using API key
	api = ApiClient("f4a44b0bbbfdc25207c5841ba91ada2c2bc9235c")
	# Instantiate Variable objects - Humidity and Temperature
	# Create new variables in Ubidots for each room
	# Edit these variables according to the room being measured
	humidity_value = api.get_variable("555a4777762542487814e5a6")
	temperature_value = api.get_variable("555a47c07625424af45b924e")
	print '\r\nSuccessfully connected to Ubidots.'
	print '\r\nNow ready to take measurements:'
except:
	print '\r\nFailed to connect to Ubidots!'
	print '\r\nIs there an Internet connection? Stopping program.'
	sys.exit(0)

# Sensor should be set to Adafruit_DHT.DHT11,
# Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
# 10/09/15 Changing the upstairs sensor to DHT11, since DHT22 went bad on Humidity
sensor = Adafruit_DHT.DHT11

# Example using a Beaglebone Black with DHT sensor
# connected to pin P8_11.
# pin = 'P8_11'

# Using a Raspberry Pi with DHT sensor
# connected to pin 23.
pin = 23

# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

# Note that sometimes you won't get a reading and
# the results will be null (because Linux can't
# guarantee the timing of calls to read the sensor).  
# If this happens try again!

# Put measurements in a loop, wait 900 seconds (15 minutes) between sending data
while humidity is not None:
	humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
	if humidity is not None and temperature is not None:
		convertCtoF = (9.0/5.0 * temperature + 32)
		print '\r\nTemp= {0:0.1f}*C  Humidity= {1:0.1f}%'.format(temperature, humidity)
		print 'Converted Temp= {0:0.1f}*F'.format(convertCtoF)
		send_temp = round(convertCtoF,1)
		send_humi = round(humidity,1)
		print 'Sending temperature to Ubidots: ',send_temp
		print 'Sending humidity to Ubidots: ',send_humi
		# Send the values to Ubidots
		# Using try : except to handle errors sending to Ubidots
		try: 
		   humidity_value.save_value({'value':send_humi})
		   temperature_value.save_value({'value':send_temp})
		except:
		   print '\r\nFailed to send to Ubidots! Will try again.'
	else:
		print '\r\nFailed to get both readings! Will try again.'
	# Call the countdown() method
	# 03/02/2017 Changed wait time to 30 minutes
	countdown(30)
else:
	print '\r\nSensor malfunction. Stopping program!'
