import streamlit as st
import pandas as pd
import plotly.express as px

def main():
    st.title("Real-time DHT Sensor Readings Dashboard")

    try:
        df = pd.read_csv('dht_readings.csv', parse_dates=['Timestamp'], index_col='Timestamp')
    except FileNotFoundError:
        st.write("No data available yet.")
        return

    st.line_chart(df[['Humidity', 'Temperature']])

    # Create a scatter plot with Plotly
    fig = px.scatter(df, x='Humidity', y='Temperature', labels={'Humidity': 'Humidity (%)', 'Temperature': 'Temperature (°C)'})
    st.plotly_chart(fig)

if __name__ == '__main__':
    main()
