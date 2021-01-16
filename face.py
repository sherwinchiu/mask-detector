# face.py
# Sherwin Chiu, Kyrollous Nassif, George Li, Matthew Hao 
# 01/16/2021
# Desc: Gets an image and compares it to a cascade which can classify whether or not something is a face already.
# Detects the face and returns how many faces have been detected
import sys
import cv2
import numpy as np

# Getting paths for cascade/image
imagePath = "index.jpeg"
cascadePath = "haarcascade_frontalface_default.xml"
# Process image and cascades to classify them
image = cv2.imread(imagePath)
cascade = cv2.CascadeClassifier(cascadePath)
# Compare images to cascade, detect how many faces are there
faces = cascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5,minSize=(50,50))
# Print number of faces 
print(len(faces))

