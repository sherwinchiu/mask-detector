from __future__ import print_function
import requestsimport json
import json
import cv2

addr = 'http:ip:5000'
test_url = addr + '/api/test'

content_type = 'image/jpeg'
headers = {'content-type': content_type}

img = cv2.imread('lena.jpg')
_, img_encoded = cv2.imencode('.jpg',img)
response = requests.post(test_url, data=img_encoded.tostring(),headers=headers)
print(json.loads(response.text))