
from tensorflow.keras.models import load_model
import cv2
import numpy as np

# Load the pretrained model
model = load_model("models/fire_detection_cnn.h5")

def preprocess_frame(frame):
    resized = cv2.resize(frame, (64, 64))
    normalized = resized.astype("float32") / 255.0
    return np.expand_dims(normalized, axis=0)

def predict_fire(frame):
    processed = preprocess_frame(frame)
    prediction = model.predict(processed)
    return prediction[0][0] > 0.5  # Adjust threshold
