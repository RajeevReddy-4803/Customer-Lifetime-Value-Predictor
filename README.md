# 🛍️ Customer Lifetime Value (CLTV) Predictor

A Streamlit web application that predicts the **future monetary value** of a customer to a business using their past behavior, purchase frequency, and geographic location. This model is trained on real-world RFM data and helps businesses estimate customer worth.

---

## 🚀 Features

- Predicts Customer Lifetime Value (CLTV) based on:
  - 🕒 Recency (days since last purchase)
  - 🔁 Frequency (number of purchases)
  - 🌍 Country of the customer
- Real-time input using **Streamlit**
- Outputs monetary value in both **USD and INR**
- Automatically handles one-hot encoding for country selection
- Scaled features for improved model performance

---

## 🧠 Technologies Used

- Python
- Streamlit
- Scikit-learn
- Pandas, NumPy
- Joblib (for saving and loading models)
- Machine Learning: Linear Regression / Ridge / Lasso (choose what you used)

---

## 📁 Project Structure

Customer-Lifetime-Value-Prediction/
│
├── app.py # Streamlit app
├── model_artifacts/
│ ├── model.pkl # Trained ML model
│ ├── scaler.pkl # Scaler used during training
│ ├── feature_columns.pkl # Feature list (incl. dummy vars)
│
├── data/
│ └── rfm_data.csv # Raw or preprocessed dataset (optional)
├── .gitignore
├── requirements.txt
└── README.md


---

## 🧪 Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/your-username/cltv-predictor.git
cd cltv-predictor```bash

python -m venv venv
source venv/bin/activate     # For Linux/macOS
venv\Scripts\activate        # For Windows

pip install -r requirements.txt
streamlit run app.py

