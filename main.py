import face
import camera
import mask
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
    print("Thank you for using")

    while True:
        camera.takePicture(0.5)

        if face.detectFace("p.jpeg") > 0:
            # face detected, check if mask

            if mask.detectMask("/home/pi/Desktop/mask-detector/p.jpeg") == 1:
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