import numpy as np
import pandas as pd
import yfinance as yf
from flask import Flask, jsonify

# Initialize Flask app
app = Flask(__name__)

# Load stock data (example: SPY S&P 500 ETF)
def get_market_data():
    ticker = "SPY"
    data = yf.download(ticker, period="1y", interval="1d")
    data['Return'] = data['Adj Close'].pct_change()
    data['Volatility'] = data['Return'].rolling(window=5).std()
    data['Momentum'] = data['Adj Close'] - data['Adj Close'].shift(5)
    data.dropna(inplace=True)
    return data

# Simple AI Model (Random Market Prediction)
def predict_market_movement():
    data = get_market_data()
    last_row = data.iloc[-1]
    
    # Dummy AI logic: If momentum is positive, predict "Up", else "Down"
    prediction = "Up" if last_row['Momentum'] > 0 else "Down"
    return prediction

# Flask API Endpoint
@app.route('/predict', methods=['GET'])
def predict():
    prediction = predict_market_movement()
    return jsonify({"Market Prediction": prediction})

# Run Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
