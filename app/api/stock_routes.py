from flask import Blueprint, jsonify, request
from app.data.data_processor import fetch_stock_data, statistical_calculations

api_bp = Blueprint('api', __name__)

@api_bp.route('/health', methods=['GET'])
def health_check():
    """
    This route returns a 200 OK response if your application is healthy
    """
    return jsonify({'message': 'Application is healthy'}), 200

@api_bp.route('/', methods=['GET'])
def hello():
    """
    welcome route
    """
    return jsonify({'message': 'welcome to stock price analyzer'})

@api_bp.route('/fetch_stock_data', methods=['GET'])
def get_stock_data():
    symbol = request.args.get('symbol')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    if not symbol or not start_date or not end_date:
        return jsonify({'error': 'Please provide symbol, start_date, and end_date parameters.'}), 400

    stock_data, status_code = fetch_stock_data(symbol, start_date, end_date)

    if status_code != 200:
        return jsonify(stock_data), status_code

    calculations = statistical_calculations(stock_data)

    return jsonify(calculations), 200