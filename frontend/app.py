# frontend/app.py
import streamlit as st
import requests

st.title("Eczema Climate Care Analyzer")

st.header("📷 Upload a skin image")
img_file = st.file_uploader("Choose an image...", type=["jpg", "png"])

st.header("🌍 Enter your city")
city = st.text_input("City")

if st.button("Analyze"):
    if img_file and city:
        files = {'image': img_file}
        pred_res = requests.post("http://localhost:5000/predict", files=files).json()
        eczema = pred_res['eczema_detected']

        climate_res = requests.post("http://localhost:5000/climate_analysis", json={"city": city}).json()

        st.subheader("🧪 Eczema Detection Result:")
        st.write("Eczema Detected" if eczema else "No Eczema Detected")

        st.subheader("🌡️ Climate Info")
        st.write(f"Temperature: {climate_res['temperature']}°C")
        st.write(f"Humidity: {climate_res['humidity']}%")

        st.subheader("💡 Care Tips")
        for tip in climate_res['advice']:
            st.markdown(f"- {tip}")
    else:
        st.warning("Please upload an image and enter a city.")
