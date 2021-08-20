import streamlit as st 

import yfinance as yf
from datetime import date

from fbprophet import Prophet
from fbprophet.plot import plot_plotly
from plotly import graph_objs as go

START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

st.title("Stock Forecast App")

# Needs to be a tuple
stocks = ("GOOG", "AAPL", "MSFT", "GME")
selected_stock = st.selectbox("Select stock for prediction", stocks)

n_years = st.slider("Years of prediction:", 1, 20)
period = n_years * 365

# Function to load the stock data
# Cache the data for a stock so that we don't need to run this function again
# if the user recently chose this stock
@st.cache
def load_data(stock_name):
    data = yf.download(stock_name, START, TODAY)
    # Put the date in the first column
    data.reset_index(inplace=True)
    # Returns a pandas data frame
    return data

data_load_state = st.text("Loading data...")
data = load_data(selected_stock)
data_load_state.text("Loading data... done!")

st.subheader("Raw data")
# Streamlit can handle pandas data frame
st.write(data.tail())

# Plot raw data
def plot_raw_data():
    # Create a figure
    fig = go.Figure()
    # Plot a trace for the opening and closing prices
    fig.add_trace(go.Scatter(x=data['Date'], y=data["Open"], name="stock opening price"))
    fig.add_trace(go.Scatter(x=data['Date'], y=data["Close"], name="stock closing price"))

    fig.layout.update(title_text="Time Series data with Rangeslider", xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

plot_raw_data()

# Predict forecast with Prophet.
df_train = data[['Date','Close']]
df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

m = Prophet()
m.fit(df_train)
future = m.make_future_dataframe(periods=period)
forecast = m.predict(future)

# Show and plot forecast
st.subheader('Forecast data')
st.write(forecast.head())
    
st.write(f'Forecast plot for {n_years} years')
fig1 = plot_plotly(m, forecast)
st.plotly_chart(fig1)

st.write("Forecast components")
fig2 = m.plot_components(forecast)
st.write(fig2)

