#!/usr/bin/python
import RPi.GPIO as GPIO

PIN = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN, GPIO.OUT)

GPIO.output(PIN,GPIO.HIGH)
