#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import *
dis = UltrasonicSensor('in1')
touch = TouchSensor('in2')
angle = GyroSensor('in3')
cs = ColorSensor('in4'); 
cs.mode = 'COL-COLOR';
#for motor
m1 = Motor('outA')
m2 = Motor('outB')
m3 = Motor('outC')
#for gyro
sp = 900
angle.mode='GYRO-ANG' # Put the gyro sensor into ANGLE mode.
units = angle.units
path = 1
d = 20
b = 2 # time for grabBall and realseBall
#funcations
def stopMoving():
	m1.stop()
	m2.stop()
def moveForward():
	m1.run_forever(speed_sp = sp)
	m2.run_forever(speed_sp = sp)
	sleep(.1)	
	
def turnRight(turnAngle):
	degree = angle.value()
	Sound.beep().wait();
	while(degree-angle.value() > -turnAngle):
		m1.run_forever(speed_sp=100);
		m2.run_forever(speed_sp=-100);
	stopMoving();
	
def turnLeft(turnAngle):
	degree = angle.value()
	Sound.beep().wait();
	while(degree-angle.value() < turnAngle):
		m1.run_forever(speed_sp=-100);
		m2.run_forever(speed_sp=100);
	stopMoving();
def grabBall():
	m3.run_forever(speed_sp = -900)
	sleep(b)#b varbile is for time
	m3.stop()
def releaseBall():
	m3.run_forever(speed_sp = 900)
	sleep(b)
	m3.stop()
def moveBackward(t):
	m1.run_forever(speed_sp=-900);
	m2.run_forever(speed_sp=-900);
	sleep(t)
while (touch.value() == 0):
	sleep(.05)
	Sound.speak("Please press my buttons").wait()
	print("no code running")
n = 1
Sound.beep().wait()
while (n == 1):
	if (path == 1):	#straight
		moveForward()
		sleep(.8)
		path = path + 1
		
	if (path == 2):	#right
		turnRight(75)
		sleep(.1)
		path =  path + 1
		
	if (path == 3):	#straight
		m1.run_forever(speed_sp=500);
		m2.run_forever(speed_sp=500);
		sleep(.1)
		while (path == 3):
			if (cs.value() == 1):
				print("path 3 is working")
				stopMoving()
				grabBall()
				if (dis.value == 2550):
					print("I see ball")
					Sound.speak("I see ball, i will grab").wait()
				path = path + 1
				break
				
	if (path == 4):	#backward
		moveBackward(.8)
		path =  path + 1
		stopMoving()
		
	if (path == 5): #left
		turnLeft(80)
		sleep(.1)
		path = path + 1
		
	if (path == 6):	#straight
		m1.run_forever(speed_sp=300); #300
		m2.run_forever(speed_sp=300);
		sleep(.1)
		while (path == 6):
			if (cs.value() == 1):
				print("path 6 is working")
				stopMoving()
				releaseBall()
				if (dis.value == 2550):
					Sound.speak("Dropping ball now").wait()
				path = path + 1
				break
	n = 0
Sound.speak("I am done. Please give me treat now").wait()