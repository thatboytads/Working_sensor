from gpiozero import MotionSensor
from gpiozero import LED
import time
pir1=MotionSensor(17)
pir2=MotionSensor(27)
buzz=LED(4)
cnt1=False
cnt2=False
parked=0
try:
	while True:
		cnt=pir1.motion_detected
		if cnt==True and parked==0:
			print("Front wheel has been sensed by 1st")
			print("Waiting for front wheel to be sensed by 2nd")
			if pir2.wait_for_motion(2):
				print("front wheel sensed by 2nd")
				print("Wiating for back wheel to be sensed by 1st")
				time.sleep(2)
				if pir1.wait_for_motion(2):
					print("back wheel sensed by 1st")
					print("Car in")
					buzz.on()
					time.sleep(3)
					buzz.off()
					parked=1
					continue
		cnt2=pir1.motion_detected
		if cnt2==True and parked==1:
			print("Back wheel going out by 1st sensor")
			print("Waiting for front wheel to be sensed by 2nd")
			if pir2.wait_for_motion(2):
				print("front wheel been sensed by 2nd")
				print("waiting for front to be sensed by 1st")
				time.sleep(2)
				if pir1.wait_for_motion(2):
					print("front wheel sensed by 2nd")
					print("car out")
					buzz.on()
					time.sleep(3)
					buzz.off()
					parked=0
					continue
except KeyboardInterrupt:
	pass
