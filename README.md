Car Price Predictor

A machine learning regression model served via Flask API to predict car prices.

How to run:-

1. Install dependencies:

   pip install -r requirements.txt


2. Run Flask app:

   python app.py

3. Send POST request to http://127.0.0.1:5000/predict with JSON input.

4. Example curl command to test the API:
 
   curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d @sample_input.json


Project files
app.py - Flask app
car_price_model.pkl - saved ML model
requirements.txt - dependencies
sample_input.json - example input
