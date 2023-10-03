import unittest
from flask import Flask, jsonify
from app.api.stock_routes import api_bp


class TestAPIBlueprint(unittest.TestCase):
    def setUp(self):
        # Create a test Flask app
        self.app = Flask(__name__)
        self.app.register_blueprint(api_bp)

        # Set Flask app to testing mode
        self.app.testing = True

        # Create a test client to make requests
        self.client = self.app.test_client()

    def test_health_check(self):
        response = self.client.get('/health')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Application is healthy')

    def test_hello(self):
        response = self.client.get('/')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'welcome to stock price analyzer')

    def test_fetch_stock_data(self):
        response = self.client.get('/fetch_stock_data?symbol=AAPL&start_date=2023-01-01&end_date=2023-12-31')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()