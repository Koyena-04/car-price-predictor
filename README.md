Car Price Predictor

A machine learning regression model served via Flask API to predict car prices.

How to run:-

1. Install dependencies:

   pip install -r requirements.txt


2. Run Flask app:
   python app.py

3. Send POST request to http://127.0.0.1:5000/predict with JSON input.


Project files
app.py - Flask app
car_price_model.pkl - saved ML model
requirements.txt - dependencies
sample_input.json - example input
