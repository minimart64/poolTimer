#! /etc/lib python

import RPi.GPIO as GPIO
from time import sleep

# global variables
pumpPin = 4
heaterPin = 17
lightPin = 27
fillPin = 22

# set up the pins
# GPIO.setwarnings(False) # add in when ready to go to prod
GPIO.setmode(GPIO.BCM)
GPIO.setup(pumpPin, GPIO.OUT)
GPIO.setup(heaterPin, GPIO.OUT)
GPIO.setup(lightPin, GPIO.OUT)
GPIO.setup(fillPin, GPIO.OUT)

#set them all LOW
GPIO.output(pumpPin, GPIO.LOW)
GPIO.output(heaterPin, GPIO.LOW)
GPIO.output(lightPin, GPIO.LOW)
GPIO.output(fillPin, GPIO.LOW)



# cycle some stuff
GPIO.output(heaterPin, GPIO.HIGH)
sleep(10)
GPIO.output(heaterPin, GPIO.LOW)

def heaterOn():
	pumpOn()
	GPIO.output(heaterPin, GPIO.HIGH)
	
def pumpOn():
	
