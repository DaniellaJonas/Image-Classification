import tensorflow as tf
import os

print("🔄 Loading dataset...")
dataset = tf.keras.utils.image_dataset_from_directory(
    "dataset",
    image_size=(180, 120),  # height=180, width=120
    batch_size=10,
    label_mode="binary",
    shuffle=True,
    seed=123
)

print("✅ Dataset loaded! Classes:", dataset.class_names)

model = tf.keras.models.Sequential([
    tf.keras.layers.Rescaling(1./255, input_shape=(180, 120, 3)),
    tf.keras.layers.Conv2D(32, (3, 3), activation="relu"),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(32, activation="relu"),
    tf.keras.layers.Dense(1, activation="sigmoid")
])

model.compile(
    loss="binary_crossentropy",
    optimizer="adam",
    metrics=["accuracy"]
)

print("🚀 Starting model training...")
history = model.fit(dataset, epochs=5)

print("💾 Saving the model...")
model.save("model.keras")

print("✅ Model saved successfully as 'model.keras'")
