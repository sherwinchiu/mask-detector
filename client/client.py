from __future__ import print_function
import requests
import json
import cv2

ip = '174.119.148.14'
port = '25565'
addr = 'http://'+ip+':'+port

test_url = addr + '/api/test'

content_type = 'image/jpeg'
headers = {'content-type': content_type}

img = cv2.imread('p.jpeg')
img_encoded = cv2.imencode('.jpg',img)
response = requests.post(test_url, data=img_encoded.tostring(),headers=headers)

print(json.loads(response.text))