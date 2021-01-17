# face.py
# Sherwin Chiu, Kyrollous Nassif, George Li, Matthew Hao
# 01/16/2021
# Desc: Gets an image and compares it to a cascade which can classify whether or not something is a face already.
# Detects the face and returns how many faces have been detected
import sys
import cv2



def detectFace(imagePath):
    cv2.setUseOptimized(True)
    # Getting paths for cascade/image
    cascadePath = "haarcascade_frontalface_default.xml"
    # Process image and cascades to classify them
    image = cv2.imread(imagePath)
    cascade = cv2.CascadeClassifier(cascadePath)
    # Compare images to cascade, detect how many faces are there
    faces = cascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5, minSize=(50, 50))
    # Show faces (for testing)
#    for (x, y, w, h) in faces:
#        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 1)
#    cv2.imshow("test", image)
#    cv2.waitKey(0)
    # Return number of faces
    return len(faces)
