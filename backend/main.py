import numpy as np
from tensorflow.keras.models import load_model as keras_load_model
from tensorflow.keras.utils import image_dataset_from_directory
from PIL import Image

def load_model():
    return keras_load_model("model.keras")

def image_prep(img_path):
    img = Image.open(img_path).resize((1800, 1200))
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0)
    return img