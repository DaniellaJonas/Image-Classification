import tensorflow as tf
import tensorflow_datasets as tfds
import numpy as np
import matplotlib.pyplot as plt 
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to our first Flask website!"

if __name__ == "__main__":
    app.run(debug=True)
