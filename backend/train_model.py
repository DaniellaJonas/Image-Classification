import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.applications import MobileNetV2
import os

BATCH_SIZE = 10
IMG_SIZE = (180, 120)  # height, width
EPOCHS_INITIAL = 10
EPOCHS_FINETUNE = 10
FINE_TUNE_AT = 100 

print("Loading dataset...")

train_dataset = tf.keras.utils.image_dataset_from_directory(
    "dataset",
    validation_split=0.2,
    subset="training",
    seed=123,
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    label_mode="binary"
)

val_dataset = tf.keras.utils.image_dataset_from_directory(
    "dataset",
    validation_split=0.2,
    subset="validation",
    seed=123,
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    label_mode="binary"
)

print("Dataset loaded! Classes:", train_dataset.class_names)

normalization_layer = layers.Rescaling(1./255)

data_augmentation = tf.keras.Sequential([
    layers.RandomFlip("horizontal"),
    layers.RandomRotation(0.1),
    layers.RandomZoom(0.1),
])

base_model = MobileNetV2(input_shape=(*IMG_SIZE, 3),
                         include_top=False,
                         weights='imagenet')
base_model.trainable = False

model = models.Sequential([
    normalization_layer,
    data_augmentation,
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.Dense(64, activation='relu'),
    layers.Dropout(0.2),
    layers.Dense(1, activation='sigmoid')
])

model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

print("Starting initial training...")
history_initial = model.fit(
    train_dataset,
    epochs=EPOCHS_INITIAL,
    validation_data=val_dataset
)

base_model.trainable = True

for layer in base_model.layers[:FINE_TUNE_AT]:
    layer.trainable = False

model.compile(
    optimizer=tf.keras.optimizers.Adam(1e-5),
    loss='binary_crossentropy',
    metrics=['accuracy']
)

print("Starting fine-tuning...")
history_finetune = model.fit(
    train_dataset,
    epochs=EPOCHS_FINETUNE,
    validation_data=val_dataset
)

print("Saving model...")
model.save("model.keras")
print("Model saved as model.keras")
