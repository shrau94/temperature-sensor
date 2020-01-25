import os
import glob
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(22,GPIO.OUT)


#initialize the device 
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm’)

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'
i=0

loop_count = 0

def morsecode ():

	#Dot Dot Dot
	GPIO.output(22,GPIO.HIGH)
	time.sleep(.1)
	GPIO.output(22,GPIO.LOW)
	time.sleep(.1)
	GPIO.output(22,GPIO.HIGH)
	time.sleep(.1)
	GPIO.output(22,GPIO.LOW)
	time.sleep(.1)
	GPIO.output(22,GPIO.HIGH)
	time.sleep(.1)

	#Dash Dash Dah
	GPIO.output(22,GPIO.LOW)
	time.sleep(.2)
	GPIO.output(22,GPIO.HIGH)
	time.sleep(.2)
	GPIO.output(22,GPIO.LOW)
	time.sleep(.2)
	GPIO.output(22,GPIO.HIGH)
	time.sleep(.2)
	GPIO.output(22,GPIO.LOW)
	time.sleep(.2)
	GPIO.output(22,GPIO.HIGH)
	time.sleep(.2)
	GPIO.output(22,GPIO.LOW)
	time.sleep(.2)

	#Dot Dot Dot
	GPIO.output(22,GPIO.HIGH)
	time.sleep(.1)
	GPIO.output(22,GPIO.LOW)
	time.sleep(.1)
	GPIO.output(22,GPIO.HIGH)
	time.sleep(.1)
	GPIO.output(22,GPIO.LOW)
	time.sleep(.1)
	GPIO.output(22,GPIO.HIGH)
	time.sleep(.1)
	GPIO.output(22,GPIO.LOW)



def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    #!/usr/bin/python
    GPIO.setmode(GPIO.BCM)
    GPIO.cleanup()
    GPIO.setwarnings(False)
    GPIO.setup(17,GPIO.OUT)
    GPIO.setup(27,GPIO.OUT)
    print "Lights on"
    GPIO.output(17,GPIO.HIGH)
    GPIO.output(27,GPIO.HIGH)
    GPIO.setmode(GPIO.BCM)
    GPIO.cleanup()
    GPIO.setwarnings(False)
    GPIO.setup(17,GPIO.OUT)
    GPIO.setup(27,GPIO.OUT)
    print "Lights on"
    GPIO.output(17,GPIO.LOW)
    GPIO.output(27,GPIO.LOW)
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c, temp_f
	
while i<3:
	print(read_temp())	
	morsecode()
	time.sleep(1)
        i=i+1
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
print "Lights on"
GPIO.output(17,GPIO.LOW)
GPIO.output(27,GPIO.LOW)


