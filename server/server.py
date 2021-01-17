from flask import Flask, request, Response
import jsonpickle
import numpy as np
import cv2
import tensorflow.keras
import tensorflow
from tensorflow import keras
from PIL import Image, ImageOps



# Initialize the Flask application
app = Flask(__name__)

def detectMask(image):
    # Disable scientific notation for clarity
    np.set_printoptions(suppress=True)

    # Load the model
    model = tensorflow.keras.models.load_model("/home/goon/Desktop/mask-detector/server/keras_model.h5")
    
    # Create the array of the right shape to feed into the keras model
    # The 'length' or number of images you can put into the array is
    # determined by the first position in the shape tuple, in this case 1.
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Replace this with the path to your image
    

    # resize the image to a 224x224 with the same strategy as in TM2:
    # resizing the image to be at least 224x224 and then cropping from the center
    w,h = 512,512
    data=np.zeros((h,w,3),dtype=np.uint8)
    data[0:256,0:256]=[255,0,0]
    image=Image.fromarray(data,'RGB')
    image.save('my.png')
    
    

    # turn the image into a numpy array
    image_array = np.asarray(image)

    # display the resized image
    image.show()

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # run the inference
    prediction = model.predict(data)
    print (model.predict(data))
    print(prediction)
    return prediction

# route http posts to this method
@app.route('/api/test', methods=['POST'])
def test():
    r = request
    # convert string of image data to uint8
    nparr = np.fromstring(r.data, np.uint8)
    # decode image
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    # 
    prediction = detectMask(img)
    # build a response dict to send back to client
    response = {'message': 0
            }
    
    # encode response using jsonpickle
    response_pickled = jsonpickle.encode(response)

    return Response(response=response_pickled, status=200, mimetype="application/json")


# start flask app
app.run(host="127.0.0.1", port=25565)
