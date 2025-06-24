#ספריות
import tensorflow as tf
import tensorflow_datasets as tfds
from tensorflow.keras.utils import image_dataset_from_directory
import numpy as np
import matplotlib.pyplot as plt 
from PIL import Image 
from sklearn.metrics import confusion_matrix, classification_report

#הגדרת מודל
model = tf.keras.models.Sequential([
    tf.keras.layers.Rescaling(1./255, input_shape=(1200, 1800, 3)),
    tf.keras.layers.Conv2D(32, (3,3), activation="relu"),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')

])

#הכנת המודל ללמידה
#loss - טועה או צודק
#אופטימייזר יודע לומר בכמה הוא טועה
model.compile(
    loss="binary_crossentropy",
    optimizer="adam",
    metrics=["accuracy"]
)

#העלאת דאטה סט
dataset = image_dataset_from_directory(
    "dataset",
    image_size = (1200, 1800),
    batch_size=10,
    label_mode="binary",
    shuffle=True,
    seed=123,
)
