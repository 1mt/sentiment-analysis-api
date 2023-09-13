import unittest
from api.main import app
from flask_testing import TestCase


class AppTest(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Welcome to the Sentiment Analysis API!", response.data)

    def test_analyze_positive_sentiment(self):
        response = self.client.post('/analyze', json={"text": "I love this!"})
        self.assertEqual(response.status_code, 200)
        json_response = response.get_json()
        self.assertEqual(json_response['sentiment'], 'positive')

    def test_analyze_negative_sentiment(self):
        response = self.client.post('/analyze', json={"text": "I hate this!"})
        self.assertEqual(response.status_code, 200)
        json_response = response.get_json()
        self.assertEqual(json_response['sentiment'], 'negative')

    def test_analyze_neutral_sentiment(self):
        response = self.client.post('/analyze', json={"text": "This is an apple."})
        self.assertEqual(response.status_code, 200)
        json_response = response.get_json()
        self.assertEqual(json_response['sentiment'], 'neutral')

    def test_analyze_no_text(self):
        response = self.client.post('/analyze', json={})
        self.assertEqual(response.status_code, 200)
        json_response = response.get_json()
        self.assertIn('error', json_response)


if __name__ == "__main__":
    unittest.main()
