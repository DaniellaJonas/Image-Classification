import numpy as np
from tensorflow.keras.models import load_model as keras_load_model
from PIL import Image

def load_model():
    return keras_load_model("model.keras")

def image_prep(img_path):
    img = Image.open(img_path).resize((120, 180))  # width=120, height=180
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0)
    return img