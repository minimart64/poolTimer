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

def setUp():
    # set up the pins
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pumpPin, GPIO.OUT)
    GPIO.setup(heaterPin, GPIO.OUT)
    GPIO.setup(lightPin, GPIO.OUT)
    GPIO.setup(fillPin, GPIO.OUT)

def allOff():
    #set them all LOW
    GPIO.output(pumpPin, GPIO.LOW)
    GPIO.output(heaterPin, GPIO.LOW)
    GPIO.output(lightPin, GPIO.LOW)
    GPIO.output(fillPin, GPIO.LOW)

def heaterOn():
    pumpOn() # can't run heater without pump
    GPIO.output(heaterPin, GPIO.HIGH)
    log.info("Heater On")

def heaterOff():
    GPIO.output(heaterPin, GPIO.LOW)
    log.info("Heater Off")
    
def pumpOn():
    GPIO.output(pumpPin, GPIO.HIGH)
    log.info("Pump On")

def pumpOff():
    heaterOff() # can't run heater without pump
    GPIO.output(pumpPin, GPIO.LOW)
    log.info("Pump Off")

def lightOn():
    GPIO.output(lightPin, GPIO.HIGH)
    log.info("Light On")

def lightOff():
    GPIO.output(lightPin, GPIO.LOW)
    log.info("Light Off")

def fillOn():
    GPIO.output(fillPin, GPIO.HIGH)
    log.info("Fill On")
    sleep(3600)
    fillOff()

def fillOff():
    GPIO.output(fillPin, GPIO.LOW)
    log.info("Fill Off")

# actual code starts here
setUp()
heaterOff()
fillOn()
