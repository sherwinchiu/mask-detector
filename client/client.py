from __future__ import print_function
import requests
import json
import cv2

ip = '2.tcp.ngrok.io'
port = '18342'
addr = 'http://'+ip+':'+port

test_url = addr + '/api/test'

content_type = "image/jpeg"
headers = {'content-type': content_type}

<<<<<<< HEAD
img = cv2.imread('/home/pi/Desktop/mask-detector/p.jpeg')
_, img_encoded = cv2.imencode('.jpg',img)
=======
img = cv2.imread('p.jpeg')
img_encoded = cv2.imencode('.jpg',img)
>>>>>>> 5cf19acaed80476efd59929190690e211f10aa91
response = requests.post(test_url, data=img_encoded.tostring(),headers=headers)

print(json.loads(response.text))