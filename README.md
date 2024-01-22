# Stock Forecast App

This is a simple stock prediction app built using Streamlit, yfinance, and Facebook Prophet. The app allows users to select a stock (e.g., GOOG, AAPL, MSFT, GME) and predict its closing prices using the Prophet time series forecasting model.

## Features

- **Interactive Interface:** Choose a stock from a predefined list and set the number of years for the forecast using an intuitive interface.
- **Data Visualization:** View raw stock data, including opening and closing prices, in an interactive plot.
- **Prophet Forecast:** Utilizes the Facebook Prophet library to predict future stock prices and visualizes the forecast using Plotly charts.
- **Forecast Components:** Explore different components of the forecast, such as trends and seasonalities.

## Usage

1. Clone the repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the app with `streamlit run app.py`.

## Dependencies

- Streamlit
- yfinance
- fbprophet
- plotly

## How to Run

```bash
streamlit run app.py
