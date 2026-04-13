import joblib
import numpy as np

model = joblib.load("crop_model.pkl")
scaler = joblib.load("scaler.pkl")

def predict_crop(N, P, K, temp, humidity, ph, rainfall):
    data = np.array([[N, P, K, temp, humidity, ph, rainfall]])
    data = scaler.transform(data)
    prediction = model.predict(data)
    return prediction[0]