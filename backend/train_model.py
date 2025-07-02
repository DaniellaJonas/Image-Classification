import tensorflow as tf

# טעינת הדאטהסט מהתיקיות
dataset = tf.keras.utils.image_dataset_from_directory(
    "dataset",
    image_size=(1200, 1800),
    batch_size=10,
    label_mode="binary",
    shuffle=True,
    seed=123
)

# בניית המודל
model = tf.keras.models.Sequential([
    tf.keras.layers.Rescaling(1./255, input_shape=(1200, 1800, 3)),
    tf.keras.layers.Conv2D(32, (3, 3), activation="relu"),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(32, activation="relu"),
    tf.keras.layers.Dense(1, activation="sigmoid")
])

# קומפילציה
model.compile(
    loss="binary_crossentropy",
    optimizer="adam",
    metrics=["accuracy"]
)

# אימון המודל
model.fit(dataset, epochs=5)

# שמירת המודל לשימוש עתידי
model.save("model.keras")
