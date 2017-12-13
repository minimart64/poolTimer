#!/usr/bin/env python3

import sys, logging, logging.handlers, smtplib, configparser
import RPi.GPIO as GPIO
from time import sleep

# set up the logger
log = logging.getLogger('poolTimer')
hdlr = logging.handlers.RotatingFileHandler('/home/pi/Documents/logs/poolTimer.log',\
                                            'a',500000,7)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
log.addHandler(hdlr)
log.setLevel(logging.INFO)
log.info("__________Blank Space_________")
log.info("##### Starting poolTimer #####")

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
	
