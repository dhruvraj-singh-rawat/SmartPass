import serial
import os
import requests
import json                                                  #import serial module
from gpiozero import Buzzer
from time import sleep

buzzer = Buzzer(17)

def not_authenticated_buzzer():
	a=2
	while a:
		buzzer.on()
		sleep(.4)
		buzzer.off()
		sleep(.7)

def authenticated_buzzer():

	buzzer.on()
	sleep(2)
	buzzer.off()
	sleep(.1)

def read_rfid ():
   ser = serial.Serial ("/dev/ttyAMA0")                           #Open named port 
   ser.baudrate = 9600                                            #Set baud rate to 9600
   data = ser.read(12)                                            #Read 12 characters from serial port to data
   ser.close ()                                                   #Close port
   return data                                                    #Return data


while (1):
	print 'Please TAP Your RFID \n\n'

	rfid_no=read_rfid()
	if (rfid_no):
		#payload = {'rfid_no': '76008BC4FFC6'}
		payload = {'rfid_no': rfid_no}

		r = requests.post('http://192.168.43.174:5000/api_responce', params=payload)
		data1 = json.loads(r.text)

		if data1['status']==1:
			print ('Allowed to enter')
			authenticated_buzzer()
		else:
			print 'NOT Allowed\n\n'
			not_authenticated_buzzer()