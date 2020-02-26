import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

p = GPIO.PWM(12, 50)
p.start(10)
time.sleep(10)
p.ChangeDutyCycle(5)
p.stop()
GPIO.cleanup()
