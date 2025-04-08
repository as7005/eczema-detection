# backend/app.py
from flask import Flask, request, jsonify
from climate_logic import analyze_climate
from dummy_model import predict
import requests

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict_eczema():
    image = request.files['image']
    # Save image and run model
    eczema = predict(image)
    return jsonify({'eczema_detected': eczema})

@app.route('/climate_analysis', methods=['POST'])
def climate_analysis():
    data = request.json
    city = data['city']
    response = analyze_climate(city)
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
