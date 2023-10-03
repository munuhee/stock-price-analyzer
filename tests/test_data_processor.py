import unittest
import requests
from unittest.mock import Mock, patch
from app.data.data_processor import fetch_stock_data, statistical_calculations

class TestStockDataFunctions(unittest.TestCase):

    @patch('requests.get')
    def test_fetch_stock_data_success(self, mock_requests_get):
        # Mock the response from Alpha Vantage API
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'Time Series (Daily)': {
                '2023-01-01': {
                    '1. open': '100.00',
                    '2. high': '110.00',
                    '3. low': '90.00',
                    '4. close': '105.00',
                    '5. volume': '1000'
                },
                '2023-01-02': {
                    '1. open': '110.00',
                    '2. high': '120.00',
                    '3. low': '100.00',
                    '4. close': '115.00',
                    '5. volume': '1200'
                }
            }
        }
        mock_requests_get.return_value = mock_response

        symbol = 'AAPL'
        start_date = '2023-01-01'
        end_date = '2023-01-02'

        result, status_code = fetch_stock_data(symbol, start_date, end_date)

        expected_result = {
            '2023-01-01': {
                'Open': 100.00,
                'High': 110.00,
                'Low': 90.00,
                'Close': 105.00,
                'Volume': 1000
            },
            '2023-01-02': {
                'Open': 110.00,
                'High': 120.00,
                'Low': 100.00,
                'Close': 115.00,
                'Volume': 1200
            }
        }

        self.assertEqual(result, expected_result)
        self.assertEqual(status_code, 200)

    @patch('requests.get', side_effect=requests.exceptions.RequestException("Test Exception"))
    def test_fetch_stock_data_failure(self, mock_requests_get):
        symbol = 'AAPL'
        start_date = '2023-01-01'
        end_date = '2023-01-02'

        result, status_code = fetch_stock_data(symbol, start_date, end_date)

        expected_result = {'error': 'Failed to fetch stock data: Test Exception'}

        self.assertEqual(result, expected_result)
        self.assertEqual(status_code, 500)

    def test_statistical_calculations(self):
        data = {
            '2023-01-01': {'Close': 105.00},
            '2023-01-02': {'Close': 115.00}
        }

        expected_result = {
            'Close_Average': 110.00,
            'Close_StdDev': 5.00,
            'Close_Median': 110.00
        }

        result = statistical_calculations(data)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()