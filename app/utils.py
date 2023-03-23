from PIL import Image
from keras.models import load_model
import numpy as np
from app.config import *

model = load_model('Model.h5',compile=False)

def image_preprocess(image):
    image = image.resize(SIZE).convert('L')
    return image

def predict(image):
    image = image_preprocess(image)
    predimg = np.array(image)  # Convert to numpy array
    predimg = np.expand_dims(predimg, axis=0)  # Expand dimensions
    result = model.predict(predimg, steps=1)
    if result[0][0].astype('int') == 0:
        label = 'dog'
    elif result[0][0].astype('int') == 1:
        label = 'cat'
    print(label)
    return label