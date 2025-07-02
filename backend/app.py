from flask import Flask, request, jsonify
from flask_cors import CORS
from main import image_prep, load_model
import os

app = Flask(__name__)
CORS(app)

model = load_model()  # טוען את המודל המאומן

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    os.makedirs("uploads", exist_ok=True)
    file_path = os.path.join("uploads", "image.jpg")
    file.save(file_path)

    image = image_prep(file_path)
    prediction = model.predict(image)

    label = "Drawing" if prediction[0][0] > 0.5 else "Photograph"
    return jsonify({'result': label})
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
