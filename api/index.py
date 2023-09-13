from flask import Flask, request, jsonify
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

app = Flask(__name__)

# Load dataset and split into train and test sets
boston = datasets.load_boston()
X_train, X_test, y_train, y_test = train_test_split(boston.data, boston.target, test_size=0.2, random_state=42)

# Train a linear regression model
model = LinearRegression().fit(X_train, y_train)

@app.route('/')
def index():
    return "Welcome to the House Price Prediction API! Use /predict endpoint to get price predictions."

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        prediction = model.predict(np.array([data['features']]))
        return jsonify({'prediction': prediction[0]})
    except Exception as e:
        return jsonify({'error': str(e)})