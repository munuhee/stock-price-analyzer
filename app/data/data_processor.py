import requests
from flask import jsonify, current_app
from config import API_KEY
import numpy as np

VANTAGE_API_URL = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY'

def fetch_stock_data(symbol, start_date, end_date):
    params = {
        'symbol': symbol,
        'apikey': API_KEY,
        'outputsize': 'full',
        'datatype': 'json',
    }

    try:
        response = requests.get(VANTAGE_API_URL, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()
        if 'Time Series (Daily)' in data:
            daily_data = data['Time Series (Daily)']
            filtered_data = {
                date: {
                    'Open': float(values['1. open']),
                    'High': float(values['2. high']),
                    'Low': float(values['3. low']),
                    'Close': float(values['4. close']),
                    'Volume': int(values['5. volume'])
                }
                for date, values in daily_data.items()
                if start_date <= date <= end_date
            }
            
            return filtered_data, 200
        return {'error': 'Invalid response from Alpha Vantage'}, 500

    except requests.exceptions.RequestException as e:
        return {'error': 'Failed to fetch stock data: ' + str(e)}, 500

def statistical_calculations(data):
    # Extract OHLCV values
    close_value = {
        'Close': [item['Close'] for item in data.values()],
    }

    # Calculate average, standard deviation, and median
    calculations = {}
    for key, values in close_value.items():
        calculations[key + '_Average'] = np.mean(values)
        calculations[key + '_StdDev'] = np.std(values)
        calculations[key + '_Median'] = np.median(values)

    return calculations
