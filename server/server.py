from flask import Flask, request, Response
import jsonpickle
import numpy as np
import cv2
import tensorflow.keras
import tensorflow
from tensorflow import keras
from PIL import Image as im, ImageOps




# Initialize the Flask application
app = Flask(__name__)

def detectMask(imagePath):
    # Disable scientific notation for clarity
    np.set_printoptions(suppress=True)

    # Load the model
    model = keras.models.load_model("/home/goon/Desktop/mask-detector/server/keras_model.h5")
    
    # Create the array of the right shape to feed into the keras model
    # The 'length' or number of images you can put into the array is
    # determined by the first position in the shape tuple, in this case 1.
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Replace this with the path to your image
    image = im.open(imagePath)

    # resize the image to a 224x224 with the same strategy as in TM2:
    # resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, im.ANTIALIAS)

    # turn the image into a numpy array
    image_array = np.asarray(image)

    # display the resized image
    image.show()

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # run the inference
    prediction = model.predict_proba(data)
    a = prediction.tolist()
    print(a)
    if (a[0][0] > 0.5):
        return 0
    else:
        return 1

# route http posts to this method
@app.route('/api/test', methods=['POST'])
def test():
    r = request
    # convert string of image data to uint8
    nparr = np.fromstring(r.data, np.uint8)
    # decode image
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    new = im.fromarray(img)
    new.save('goon.jpeg')
    #   
    prediction = detectMask('/home/goon/Desktop/mask-detector/goon.jpeg')
    # build a response dict to send back to client
    response = prediction
    
    # encode response using jsonpickle
    response_pickled = jsonpickle.encode(response)

    return Response(response=response_pickled, status=200, mimetype="application/json")


# start flask app
app.run(host="127.0.0.1", port=25565)
