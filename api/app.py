from flask import Flask, request, jsonify
from textblob import TextBlob

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the Sentiment Analysis API! Use /analyze endpoint to get sentiment."

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        data = request.json
        text = data['text']
        analysis = TextBlob(text)
        sentiment = "positive" if analysis.sentiment.polarity > 0 else "negative" if analysis.sentiment.polarity < 0 else "neutral"
        return jsonify({'sentiment': sentiment, 'polarity': analysis.sentiment.polarity})
    except Exception as e:
        return jsonify({'error': str(e)})