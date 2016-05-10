import serial, time 
from time import sleep 
import time 
import os, json 
import ibmiotf.application
import uuid

ser = serial.Serial('/dev/ttyACM0', 9600)
try:
  options = ibmiotf.application.ParseConfigFile("/home/pi/device.cfg")
  options["deviceId"] = options["id"]
  options["id"] = "aaa" + options["id"]
  client = ibmiotf.application.Client(options)
  client.connect()
  while 1:
      serial_line = ser.readline()
      ts = int(time.time())
      #print serial_line # If using Python 2.x use: print serial_line
      # Do some other work on the data
      myData = {'NO2' :serial_line, 'timestamp' : ts}
      client.publishEvent("raspberry", options["deviceId"], "input", "json", myData)
      print (str(serial_line) + " has been published." + str(ts))

      time.sleep(2) # sleep 5 minutes

      # Loop restarts once the sleep is finished

except ibmiotf.ConnectionException as e:
    print e
ser.close() # Only executes once the loop exits
