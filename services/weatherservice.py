import requests
import os
from flask import Flask, jsonify, request, make_response
from constants import API_KEY

app = Flask(__name__)
port = int(os.environ.get('PORT', 5000))

@app.route("/")
def home():
    return "Hello, this is a Flask Microservice"
    
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=port)

@app.route('/<city>', methods=['GET'])
def get_weather(city):
    BASE_URL = "http://api.weatherapi.com/v1/current.json"
    params = {
        'key': API_KEY,
        'q': city
    }
    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        return jsonify({'error': response.json()['message']}), response.status_code
    
    weather_data = response.json()
    location = weather_data['location']['name']
    temp_c = weather_data['current']['temp_c']
    localtime = weather_data['location']['localtime']
    message = f"Weather in {location}: {temp_c} °C. (Recorded: {localtime})"

    return jsonify({'data': message}), 200
    