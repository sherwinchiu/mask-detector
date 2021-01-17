# camera.py
# Sherwin Chiu, Kyrollous Nassif, George Li, Matthew Hao
# 01/16/2021 
# Desc: Takes a picture with integrated camera from PiCamera, then saves to desktop
# Also comes with feature to delete picture

from picamera import PiCamera
from time import sleep
import os

def takePicture(shutterSpeed):
    camera = PiCamera()
#    camera.start_preview()
    sleep(shutterSpeed)
    camera.capture('/home/pi/Desktop/mask-detector/p.jpeg')
#    camera.stop_preview()
    camera.close()

def deletePicture():
    os.remove('/home/pi/Desktop/mask-detector/p.jpeg')
