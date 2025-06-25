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


def image_prep(img_path):
    img = Image.open(img_path).resize((1800, 1200)) #מעלה תמונה ומסדר את הגודל
    img = np.array(img) / 255.0 #הופכים את התמונה למערך מספרים
    img = np.expand_dims(img, axis=0) #מגדיר שיש קבוצה אחת עם תמונה אחת בפנים
    return img


image = image_prep("my_image.jpg")
prediction = model.predict(image)

if prediction[0][0] > 0.5:
    print("It's a drawing")
else:
    print("It's a painting!")
