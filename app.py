import streamlit as st
from getrequest import get_weather_data

st.title("APi Calling")

city = st.text_input("Enter city")

weather_data = get_weather_data(city=city)

if(weather_data):
    st.subheader("Weather description")
    st.write(weather_data['weather'][0]['description'])
    st.write(weather_data['main']['temp'])
