# light.py
# Sherwin Chiu, Kyrollous Nassif, George Li, Matthew Hao
# 01/16/2021
# Desc: Quick lighting script to turn on green/red LEDs 

import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(5, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(6, GPIO.OUT, initial=GPIO.LOW)


def turnGreen():
    GPIO.output(2, GPIO.LOW)
    GPIO.output(1, GPIO.HIGH)

def turnRed():
    GPIO.output(1, GPIO.LOW)
    GPIO.output(2, GPIO.HIGH)