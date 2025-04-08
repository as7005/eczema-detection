# 🧴 Eczema Climate Care Analyzer


![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-darkgreen)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-brightgreen)
![Status](https://img.shields.io/badge/Status-Prototype-orange)


This is a full-stack web app that detects eczema from images and provides personalized care tips based on current climate conditions (like temperature and humidity).

## 🧠 Features

- 📷 **Eczema Detection** — Upload a skin image for basic (dummy) analysis  
- 🌦️ **Climate-Based Care Advice** — Enter your city to receive weather-based skin care tips  
- 🧪 Built with:
  - **Python + Flask** for backend
  - **Streamlit** for frontend
  - **OpenWeather API** for climate data

---

## 🚀 How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/as7005/eczema-detection.git
cd eczema-detection
````

### 2. Set Up Virtual Environment (Windows)

```bash
py -m venv venv
.\venv\Scripts\Activate.ps1  # Use PowerShell
````

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash
Open two terminal tabs or windows:
```

🧠 Backend (Flask API)
```bash
cd backend
python app.py
```

### 🎨 Frontend (Streamlit)
```bash
cd frontend
streamlit run app.py
```

# Notes
The app currently uses a dummy model for eczema detection — you can plug in your own trained model easily.

The weather feature uses the OpenWeatherMap API. You can add your own API key in climate_logic.py.

### 📂 Project Structure
eczema_climate_care/
│
├── backend/
│   ├── app.py
│   ├── climate_logic.py
│   ├── dummy_model.py
│   └── utils.py
│
├── frontend/
│   └── app.py
│
├── requirements.txt
├── .gitignore
└── README.md

