from gpiozero import MotionSensor
pir = MotionSensor(17)
if pir.wait_for_motion(4):
	print("Motion detected!")
else:
	print("no motion")

