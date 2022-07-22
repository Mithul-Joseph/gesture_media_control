from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import cv2
import keyboard as k
import time

# Load the model
model = load_model('<Enter location of model>')

# Create the array of the right shape to feed into the keras model
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
#resize the image to a 224x224 with the same strategy as in TM2:
size = (224, 224)

#dummy image so that it is easier to quit the program rather than force quitting.
img = cv2.imread('<Enter location for dummy png image>')

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    color = cv2.cvtColor(frame, cv2.COLOR_RGBA2RGB)
    image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    
    #displaying the dummy image
    cv2.imshow('img',img)

    #resizing the image to be at least 224x224 and then cropping from the center
    image = ImageOps.fit(image, size, Image.ANTIALIAS)
    image_array = np.asarray(image)
    
    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    
    # Load the image into the array
    data[0] = normalized_image_array

    # run the inference
    prediction = model.predict(data)
    pred = np.argmax(prediction)

    if cv2.waitKey(1) & 0xFF == ord('q'):  
        break

    d = {0:'shift+n', 1:'k'}

    if pred in [0,1]:
        k.press_and_release(d[pred])
        time.sleep(2)

cap.release()
cv2.destroyAllWindows()