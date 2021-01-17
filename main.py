# main.py
# Matthew Hao, George Li, Sherwin Chiu, Kyrollous Nassif, 
# 01/16/2021
# Desc: Program to have Raspberry Pi to continously check if wearing masks

import face
import camera
import client

# Camera.py Libraries
from picamera import PiCamera
from time import sleep
import os

# Face.py Libraries
import sys
import cv2
import tensorflow.keras
import light

def main():
    print("Face Mask Detection System V1.0")
    print("Thank you for contributing to a safer experience for everyone!")

    while True:
        camera.takePicture(10)

        if face.detectFace("p.jpeg") > 0:
            # face detected, check if mask

            if client.sendRequest() == 1:
                print("Mask Detected, thank you")
                light.turnGreen()
            else:
                print("Mask not found, please put a mask on before entering")
                light.turnRed()

        else:
            print("No face")
        camera.deletePicture()


if __name__ == "__main__":
    main()