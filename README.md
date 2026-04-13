# 🌱 Crop Recommendation System using Machine Learning

A Machine Learning-based web application that recommends the best crop based on soil nutrients and environmental conditions such as Nitrogen (N), Phosphorus (P), Potassium (K), temperature, humidity, pH, and rainfall.

This project helps farmers make **data-driven decisions** instead of relying on guesswork.

---

## 🚀 Features

* 🌾 Predicts best crop using Machine Learning
* 📊 Multiple model comparison
* 🏆 Best model selection (Random Forest - 99.55% accuracy)
* 🌐 Interactive Streamlit web app
* 📈 Data visualization (Heatmap, Bar chart, Histogram)
* ⚡ Fast prediction system
* 🧠 Smart farming support

---

## 🧠 Machine Learning Workflow

1. Data Collection
2. Data Preprocessing
3. Feature Selection
4. Train-Test Split
5. Feature Scaling (StandardScaler)
6. Model Training:

   * Logistic Regression
   * Decision Tree
   * Random Forest
   * KNN
7. Model Evaluation (Accuracy, Precision, Recall, F1 Score)
8. Best Model Selection
9. Model Saving using Joblib

---

## 📊 Model Performance

| Model               | Accuracy   |
| ------------------- | ---------- |
| Logistic Regression | 96.36%     |
| Decision Tree       | 98.41%     |
| Random Forest       | **99.55%** |
| KNN                 | 95.68%     |

🏆 **Best Model: Random Forest Classifier**

---

## 📁 Project Structure

```
crop-recommendation-ml-project
│
├── app
│   └── app.py
│
├── data
│   └── Crop_recommendation_dataset.csv
│
├── models
│   ├── model_training.py
│   ├── predict.py
│   ├── crop_model.pkl
│   └── scaler.pkl
│
├── eda.py
├── requirements.txt
└── README.md
```

---

## 🖥️ How to Run the Project

### 1️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 2️⃣ Train the Model

```
python models/model_training.py
```

### 3️⃣ Run the Web App

```
streamlit run app/app.py
```

---

## 📊 Input Features

* Nitrogen (N)
* Phosphorus (P)
* Potassium (K)
* Temperature
* Humidity
* pH level
* Rainfall

---

## 🎯 Output

* Recommended Crop 🌾

---

## 📸 App Preview

👉 Enter soil & weather data
👉 Click "Predict"
👉 Get best crop recommendation

---

## 🌟 Future Improvements

* 📱 Mobile App Integration
* 🌦️ Real-time Weather API
* 🌱 Fertilizer Recommendation System
* ☁️ Cloud Deployment

---

## 🧑‍💻 Author

**Himanshu Pandey**

---

## 📌 Conclusion

This project demonstrates how Machine Learning can improve agricultural productivity by recommending the most suitable crops based on environmental conditions.

---

⭐ If you like this project, give it a star!
