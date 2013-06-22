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

hostname = "archie"


printer_on = False
while (True):
  response = os.system("ping -c1 -W1 " + hostname)
  if response == 0:
    print "got response"
    if not printer_on:
      turn_on_printer()

  else:
    print "got no response"
    if printer_on:
      turn_off_printer()
  time.sleep(10)



