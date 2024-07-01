import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cv2
import tensorflow as tf
from tensorflow.keras.models import load_model

# Load the model
loaded_model = load_model('VGG_model.h5')

# Define the class names
label_to_class_name = {0: 'Cyst', 1: 'Normal', 2: 'Stone', 3: 'Tumor'}

def predict_class(img_path):
    """
    This function takes the path of an image file as input, processes the image,
    and returns the predicted class label.
    """
    # Load and preprocess the image
    img = cv2.imread(img_path)

    # Check if the image was loaded correctly
    if img is None:
        raise ValueError("Image not found or unable to load")

    # Resize and normalize the image
    resize = tf.image.resize(img, (224, 224))
    resize = resize / 255.0  # Normalize to [0, 1]

    # Expand dimensions to match the input shape expected by the model
    input_tensor = np.expand_dims(resize, axis=0)

    # Predict using the loaded model
    yhat = loaded_model.predict(input_tensor)
    max_index = np.argmax(yhat)

    # Return the predicted class label
    return label_to_class_name[max_index]
