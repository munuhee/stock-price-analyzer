
<div align="center">
  <img src="https://res.cloudinary.com/murste/image/upload/v1698907632/stevolve_x8ioeu.png" alt="Stephen Murichu's Logo" width="100" />
</div>

# Stock Price Analyzer
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python Version](https://img.shields.io/badge/Python-3.10-green)](https://www.python.org/downloads/)

This is a microservice designed to deliver comprehensive stock price analysis effortlessly. You can retrieve stock data by sending HTTP requests with your desired company's stock symbol and date range. Here's how you can use it:

## Installation

Before you can run the application, ensure you have the following prerequisites and dependencies:

- Docker
- Kubernetes (optional, for deployment)

To install the application, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/munuhee/stock-price-analyzer.git
   cd stock-price-analyzer
   
2. Run the setup.sh file (Builds the Docker container):

    ```bash
    chmod +x bin/setup.sh
    ./bin/setup.sh

Now, the Crypto Price Checker application is running locally on port 8080.

## Usage

### HTTP Request

Send a GET request to the following endpoint:

```text
   http://localhost:8080/api/fetch_stock_data?symbol=<COMPANY_SYMBOL>&start_date=<START_DATE>&end_date=<END_DATE>
```
Replace `<COMPANY_SYMBOL>` with the stock symbol of the company you want to analyze, `<START_DATE>` with the starting date of the analysis period (e.g., "2022-01-01"),  `<END_DATE>` with the date of the analysis period (e.g., "2022-12-31").

###  Example using cURL
```bash
    curl -X GET "http://localhost:8080/api/fetch_stock_data?symbol=AAPL&start_date=2022-01-01&end_date=2022-12-31"
```
## API Routes
* `/api/health (GET)`: Returns a 200 OK response if the application is healthy.

* `/api/ (GET)`: Welcome route that returns a simple welcome message.

* `/api/fetch_stock_data (GET)`: Fetches stock data for the specified company and date range. Requires the symbol, start_date, and end_date parameters in the query string.

## API Implementation Details
**`stock_routes.py`**
This file contains the API routes and their respective handlers. It also includes a health check route and a welcome route for basic functionality testing.

**`data_processor.py`**
This module handles data retrieval from the Alpha Vantage API and performs statistical calculations on the retrieved data. It includes two main functions:

**`fetch_stock_data(symbol, start_date, end_date)`**: Fetches daily stock data for the specified symbol and date range using the Alpha Vantage API. It filters and processes the data and returns it in a structured format.

**`statistical_calculations(data)`**: Performs statistical calculations on the stock data, including calculating the average, standard deviation, and median of the closing prices.

**`run.py`**
This script is used to run the Flask application. It creates the Flask app and starts the server on port 8080 in debug mode.
