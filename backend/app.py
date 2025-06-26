from flask import Flask, request
from flask_cors import CORS
from main import image_prep, model 
import os

app = Flask(__name__)
CORS(app)  

# יצירת תיקיית העלאות אם לא קיימת
os.makedirs("uploads", exist_ok=True)

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return "No file part", 400

    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400

    file_path = "uploads/image.jpg"
    file.save(file_path)

    image = image_prep(file_path)
    prediction = model.predict(image)

    return "Drawing" if prediction[0][0] > 0.5 else "Photograph"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)