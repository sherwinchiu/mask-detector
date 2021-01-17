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
    print(json.loads(response.text))
    return json.loads(response.text)
    

# test
sendRequest()