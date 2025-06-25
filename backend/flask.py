from flask import Flask, request
from main import image_prep, model
import os

app = Flask(__name__)
os.makedirs("uploads", exist_ok=True)

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['file'] 
    file_path = "uploads/image.jpg"
    file.save(file_path)

    image = image_prep(file_path)
    prediction = model.predict(image)

    return "Drawing" if prediction[0][0] > 0.5 else "Photograph"

if __name__ == "__main__":
    app.run(debug=True)