import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cv2
import tensorflow as tf
from tensorflow.keras.models import load_model

loaded_model = load_model('VGG_model.h5')

label_to_class_name = {0: 'Cyst', 1: 'Normal', 2: 'Stone', 3: 'Tumor'}

def predict_class(img):
    """
    This function takes the path of an image file as input, processes the image,
    and returns the predicted class label.
    """

    if img is None:
        raise ValueError("Image not found or unable to load")

    resize = tf.image.resize(img, (224, 224))
    resize = resize / 255.0 

    input_tensor = np.expand_dims(resize, axis=0)

    yhat = loaded_model.predict(input_tensor)
    max_index = np.argmax(yhat)

    return label_to_class_name[max_index]
