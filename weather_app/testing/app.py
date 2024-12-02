from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
import logging
from logging.handlers import RotatingFileHandler
import secrets
import random
import requests
import os
from flask_cors import CORS

load_dotenv()
app = Flask(__name__)
CORS(app)

app.secret_key = secrets.token_hex(2048)


def setup_logging():
    # Create a logger
    logger = logging.getLogger("FlaskAppLogger")
    logger.setLevel(logging.DEBUG)  # Log all levels (DEBUG and above)

    # Define the log format
    log_formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # File Handler (for saving logs to a file)
    file_handler = RotatingFileHandler("app.log", maxBytes=100000, backupCount=10)
    file_handler.setLevel(logging.INFO)  # Log at INFO level or higher in the file
    file_handler.setFormatter(log_formatter)

    # Console Handler (for printing to CMD)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(
        logging.INFO
    )  # You can change this to DEBUG or ERROR based on needs
    console_handler.setFormatter(log_formatter)

    # Add the handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    # Add the logger to the Flask app's logger
    app.logger.addHandler(file_handler)
    app.logger.addHandler(console_handler)

    return logger


loggers = setup_logging()
app.logger = loggers


@app.route("/weather", methods=["GET", "POST"])
def fetch_weather_data():
    city = request.args.get("city")
    app.logger.info(f"Fetching weather data for city: {city}")

    # Handle missing city parameter
    if not city:
        app.logger.warning("City parameter is missing in weather fetch request")
        return jsonify({"error": "City parameter is required"}), 400

    # Fetch API keys from environment variables
    api_keys = [os.getenv("OPENWEATHER_API_KEY"), os.getenv("OPENWEATHER_API_KEY1")]
    api_keys = [key for key in api_keys if key]  # Filter out None values

    # Can add an alternator to switch between keys using true and false values
    if not api_keys:
        app.logger.error("No API keys found in environment variables")
        return (
            jsonify({"error": "Server configuration error: API keys are missing"}),
            500,
        )

    api_key = random.choice(api_keys)
    # TODO: This is good but what if the api requests sent gives error for the whole request?
    # It should try again then with individual keys two times more
    # Implement this logic too, here

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&APPID={api_key}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return jsonify({
            "country_name" : data["sys"]["country"],
            "city_name": data["name"],
            "weather_condition": data["weather"][0]["main"],
            "temp": round(data["main"]["temp"], 2),
            "pressure": data["main"]["pressure"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
            "wind_degree": data["wind"]["deg"]
        })
        

    else:
        return jsonify({"error": "City not found"}), response.status_code



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)