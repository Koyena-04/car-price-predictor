# 🚗 Car Price Predictor

A machine learning regression project that predicts car prices based on various features such as brand, model, engine type, transmission, fuel economy, and more.  
The trained model is served via a Flask API that accepts JSON input and returns the predicted MSRP.

---

## 🔍 Features

- End-to-end pipeline with data cleaning, preprocessing, and feature engineering
- Trained regression model (Linear Regression)
- Deployment-ready Flask API
- Testable via JSON input and curl command
- Includes sample input and prediction demo

---

## 🧠 Tech Stack

- Python (Pandas, NumPy, Scikit-learn)
- Jupyter Notebook for EDA & modeling
- Flask for API deployment
- Git & GitHub for version control

---

## 📁 Project Structure
   car-price-predictor/
   ├── app.py # Flask API to serve the model
   ├── car_price_model.pkl # Trained model saved using joblib
   ├── sample_input.json # Example input to test the API
   ├── requirements.txt # Python dependencies
   ├── notebooks/ # Contains Jupyter notebooks for EDA & model training
   │ └── car_price_model.ipynb
   ├── .gitignore
   └── README.md


---

## 🧪 How to Run the Project Locally

### 1️⃣ Clone the repository:

    git clone https://github.com/Koyena-04/car-price-predictor.git
    cd car-price-predictor

### 2️⃣ Create a virtual environment and activate it:

    python -m venv venv
    venv\Scripts\activate    # For Windows
    # OR
    source venv/bin/activate # For Mac/Linux

### 3️⃣ Install dependencies:

    pip install -r requirements.txt

### 4️⃣ Run the Flask app:

    python app.py


# 🚀 Test the API
  You can use the included sample input to test the API:

### 🔹 Sample curl command:

    curl -X POST http://127.0.0.1:5000/predict \
    -H "Content-Type: application/json" \
    -d @sample_input.json

📊 Model Performance (on test data)
- Model Used: Linear Regression (or specify if different)

- R² Score: 0.9057

- RMSE: $3,400



