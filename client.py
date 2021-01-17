# client.py
# George Li, Sherwin Chiu, Kyrollous Nassif, Matthew Hao
# 01/16/2021
# Desc: Client-side that sends requests with pictures. Server can respond with a 0 or 1.
# 0 is used to say no-mask, 1 is used to say mask
from __future__ import print_function
import requests
import json
import cv2

def sendRequest():
    ip = '2.tcp.ngrok.io'
    port = '18342'
    addr = 'http://'+ip+':'+port

    test_url = addr + '/api/test'

    content_type = "image/jpeg"
    headers = {'content-type': content_type}

    img = cv2.imread('/home/pi/Desktop/mask-detector/p.jpeg')
    _, img_encoded = cv2.imencode('.jpg',img)
    response = requests.post(test_url, data=img_encoded.tobytes(),headers=headers)

    return json.loads(response.text)
    