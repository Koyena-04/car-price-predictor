from flask import Flask, request, jsonify
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load your trained pipeline
model = joblib.load("car_price_model.pkl")

@app.route("/")
def home():
    return "Car Price Prediction API is running."

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Load JSON input into a DataFrame
        input_data = request.get_json(force=True)
        input_df = pd.DataFrame([input_data])

        # Predict log(MSRP), then convert back
        log_pred = model.predict(input_df)[0]
        predicted_price = np.expm1(log_pred)

        return jsonify({
            "predicted_msrp": round(predicted_price, 2)
        })

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
