import time

import RPi.GPIO as GPIO


#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(12, GPIO.OUT)
#LOW = 100*1/21
#HIGH= 100*2/22
#print(LOW)
#print(HIGH)
#p = GPIO.PWM(12, 50)
#print("starting...")
#p.start(HIGH)
#print("HIGH")
#time.sleep(1)
#p.ChangeDutyCycle(LOW)
#print("LOW")
#time.sleep(1)
#print("stopping")
#p.stop()
#GPIO.cleanup()

def take_pic():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12, GPIO.OUT)
    LOW = 100 * 1 / 21
    HIGH = 100 * 2 / 22
    p = GPIO.PWM(12, 50)
    print("starting...")
    p.start(HIGH)
    print("HIGH")
    time.sleep(1)
    p.ChangeDutyCycle(LOW)
    print("LOW")
    time.sleep(1)
    print("stopping")
    p.stop()
    GPIO.cleanup()
