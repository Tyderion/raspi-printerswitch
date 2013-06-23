#!/usr/bin/python
import os
import time
import RPi.GPIO as GPIO

PIN = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN, GPIO.OUT)



def turn_on_printer():
  global printer_on, PIN
  print "Turning printer on"
  GPIO.output(PIN, GPIO.HIGH)
  printer_on = True

def turn_off_printer():
  global printer_on, PIN
  print "Turning Printer off"
  GPIO.output(PIN, GPIO.LOW)
  printer_on = False


printer_on = GPIO.input(PIN)
while (True):
  response = os.system("ping -c1 -W1 " + "archie")
  if response == 0:
    if not printer_on:
      turn_on_printer()

  else:
    if printer_on:
      turn_off_printer()



