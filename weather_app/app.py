"""
This module initializes the Flask application and sets up routes for the weather app.
"""

import json
import re  # to use regex for password validation
import os
import logging
import random
from datetime import timedelta
from logging.handlers import RotatingFileHandler

from datetime import datetime, timezone
import requests
from flask import Flask, render_template, request, redirect, session, jsonify, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from dotenv import load_dotenv
from flask_bcrypt import Bcrypt
from flask_wtf.csrf import CSRFProtect
from secret_key_generator import generate_secret_key
from models import db, WeatherLog
from flask_migrate import Migrate


# Load environment variables from .env
load_dotenv()

# Initialize the Flask app
app = Flask(__name__)


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
# Initialize the logger
print("logger initialised")
app.logger = loggers

# PostgreSQL Database Configuration
db_user = os.getenv("POSTGRES_USER")
db_password = os.getenv("POSTGRES_PASSWORD")
db_host = os.getenv("POSTGRES_HOST")
db_port = os.getenv("POSTGRES_PORT")
db_name = os.getenv("POSTGRES_DB")


app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
)
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=99)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)

migrate = Migrate(app, db)
with app.app_context():
    try:
        db.create_all()
        # WeatherLog.__table__.create(db.engine)
        app.logger.info("Tables created successfully.")
    except Exception as e:
        WeatherLog.__table__.create(db.engine)
        app.logger.error(f"Error creating tables: {e}")
        app.logger.info("Tables created successfully by Engine.")


csrf = CSRFProtect(app)
app.secret_key = generate_secret_key() or os.getenv(
    "FLASK_SECRET_KEY", "default_fallback_key"
)
if app.secret_key == "default_fallback_key":
    print(
        "WARNING: Using default secret key. Please set the FLASK_SECRET_KEY environment variable."
    )
bcrypt = Bcrypt(app)
# Initialize SQLAlchemy


# Initialize the database


# @app.route("/")
# def dashboard_icons():
#     weather_icons = {
#         "Clouds": url_for("static", filename="images/clouds.png"),
#         "Clear": url_for("static", filename="images/clear.png"),
#         "Rain": url_for("static", filename="images/rain.png"),
#         "Drizzle": url_for("static", filename="images/drizzle.png"),
#         "Mist": url_for("static", filename="images/mist.png"),
#         "Snow": url_for("static", filename="images/snow.png"),
#         "Thunderstorm": url_for("static", filename="images/thunder.png"),
#         "default": url_for("static", filename="images/search.png"),
#     }
#     return render_template("dashboard.html", weather_icons=weather_icons)


# Function to read users from the JSON file
def read_users_from_json():
    with open("data/users.json") as f:
        return json.load(f)["users"]


# Function to write users to the JSON file
def write_users_to_json(users):
    with open("data/users.json", "w") as f:
        json.dump({"users": users}, f, indent=4)


# Login route
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        users = read_users_from_json()
        username = request.form["username"]
        password = request.form["password"]

        # Log login attempt
        app.logger.info(f"Login attempt for user: {username}")

        for user in users:
            if user["username"] == username and bcrypt.check_password_hash(
                user["password"], password
            ):
                session["username"] = username
                print(f"session username: {session["username"]}")
                return redirect("/dashboard")  # Redirect after successful login

        # Log failed login attempt
        app.logger.warning(f"Failed login attempt for user: {username}")
        return "Invalid credentials", 401  # Return an error message if login fails

    return render_template("login.html")  # Render the login form on GET request


# !to build a strong password check isn't there a library?
def is_password_strong(password):
    """
    Validates whether a password is strong.
    A strong password should:
    - Be at least 8 characters long
    - Contain at least one uppercase letter
    - Contain at least one lowercase letter
    - Contain at least one number
    - Contain at least one special character
    """
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):  # Check for at least one uppercase letter
        return False
    if not re.search(r"[a-z]", password):  # Check for at least one lowercase letter
        return False
    if not re.search(r"[0-9]", password):  # Check for at least one digit
        return False
    if not re.search(
        r'[!@#$%^&*(),.?":{}|<>]', password
    ):  # Check for a special character
        return False
    return True


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]

        # Log the registration attempt
        app.logger.info(f"Registration attempt for user: {username}")

        # Check if passwords match
        if password != confirm_password:
            app.logger.warning(f"Passwords do not match for user: {username}")
            return "Passwords do not match. Please try again.", 400

        # Check if password is strong
        if not is_password_strong(password):
            app.logger.warning(
                f"Weak password attempt during registration for user: {username}"
            )
            return (
                "Password must be at least 8 characters long, contain uppercase, lowercase, a digit, and a special character.",
                400,
            )

        # Hash the password
        hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")

        # Load existing users
        users = read_users_from_json()

        # Check if the username already exists
        if any(user["username"] == username for user in users):
            app.logger.warning(f"Username already exists: {username}")
            return "Username already exists", 400

        # Add new user to the users list
        users.append({"username": username, "password": hashed_password})

        # Save updated users list to JSON file
        write_users_to_json(users)
        app.logger.info(f"User registered successfully: {username}")
        return redirect("/login")

    return render_template("register.html")


def login_required_check(func):
    def login_required_wrapper(*args, **kwargs):
        if "username" not in session:
            return redirect("/login")
        return func(*args, **kwargs)

    login_required_wrapper.__name__ = func.__name__
    return login_required_wrapper


@app.route("/home")
@app.route("/dashboard")
@app.route("/")
@login_required_check
def home():
    return render_template("dashboard.html")


# Utility function to fetch weather data from OpenWeather API
@app.route("/weather", methods=["GET"])
def fetch_weather_data():
    city = request.args.get("city")
    app.logger.info(f"Fetching weather data for city: {city}")
    
    # Handle missing city parameter
    if not city:
        app.logger.warning("City parameter is missing in weather fetch request")
        return jsonify({"error": "City parameter is required"}), 400

    api_key1 = os.getenv("OPENWEATHER_API_KEY")
    api_key2 = os.getenv("OPENWEATHER_API_KEY1")
    api_key = random.choice([api_key1, api_key2])

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&APPID={api_key}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()

        weather_condition = data["weather"][0]["main"]
        weather_description = data["weather"][0]["description"]
        weather_icon = data["weather"][0]["icon"]
        city_name = data["name"]
        temp = round(data["main"]["temp"])
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        # Mapping OpenWeather icons to your own images
        icon_map = {
            "Clouds": "clouds.png",
            "Clear": "clear.png",
            "Rain": "rain.png",
            "Drizzle": "drizzle.png",
            "Mist": "mist.png",
            "Snow": "snow.png",
            "Thunderstorm": "thunder.png",
            "Smoke": "smoke.png",  # Add new icon for "smoke"
            "Haze": "haze.png",    # Example: Haze condition
            # Add more mappings if needed
        }

        # Default icon if no match found
        weather_icon_path = icon_map.get(weather_condition, "search.png")

        # Pass weather data to the template
        return render_template("weather.html", 
                               city_name=city_name, 
                               weather_condition=weather_condition, 
                               weather_description=weather_description,
                               temp=temp, 
                               humidity=humidity, 
                               wind_speed=wind_speed)
    
    else:
        return jsonify({"error": "City not found"}), response.status_code
    

logs = []

# Log weather data route
@app.route("/add_log_weather", methods=["POST", "GET"])
def add_log_weather():
    # data = fetch_weather_data()
    data = request.json
    app.logger.info(f"Recieved data: {data}")
    # if not data.get("city"): 
    #     app.logger.warning(f"Missing city or temperature data in log request by user: {session['username']}")
    #     return jsonify({"error": "Missing city"}), 400
# Extract data
    username = session.get("username")
    print(username)
    city = data.get("city")
    temperature = data.get("temperature")
    pressure = data.get("pressure")
    humidity = data.get("humidity")
    wind_speed = data.get("wind_speed")
    wind_degree = data.get("wind_degree")

    # Create a new WeatherLog object
    new_log = WeatherLog(
        username=username,
        city=city,
        temperature=temperature,
        pressure=pressure,
        humidity=humidity,
        wind_speed=wind_speed,
        wind_degree=wind_degree
    )

    # Add the new log to the session and commit it to the database
    try:
        db.session.add(new_log)
        db.session.commit()
        return jsonify({"message": "Weather log added successfully!"}), 201
    except Exception as e:
        app.logger.error(f"Error saving data to database: {str(e)}")
        return jsonify({"error": "An error occurred while saving the weather log"}), 500



# View weather logs route
@app.route("/weather_logs_list")
@login_required_check
def weather_logs_list():
    logs = WeatherLog.query.filter_by(username=session["username"]).all()
    return render_template("weather_logs.html", logs=logs, username=session["username"])


@app.route("/clear-logs", methods=["POST"])
def clear_logs():
    if "user_id" not in session:
        return jsonify({"success": False, "error": "User not authenticated"}), 401

    user_id = session["user_id"]

    try:
        # Delete logs for the logged-in user only
        WeatherLog.query.filter_by(user_id=user_id).delete()
        db.session.commit()
        return jsonify({"success": True, "message": "All logs cleared for user"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"success": False, "error": str(e)}), 500


# Delete weather log route (integrated with both DB and in-memory logs)
@app.route("/delete_log/<log_id>", methods=["POST"])
def delete_log(log_id):
    # If using a database
    log = weather_db.query.get_or_404(log_id)
    if log.username != session.get("username"):
        app.logger.warning(
            f"Unauthorized deletion attempt for log id: {log_id} by user: {session.get('username')}"
        )
        return jsonify({"status": "error", "message": "Forbidden"}), 403

    db.session.delete(log)
    db.session.commit()
    app.logger.info(
        f"User {session.get('username')} deleted weather log with id: {log_id}"
    )
    return jsonify({"status": "success", "message": "Log deleted successfully"}), 200


# Logout route
@app.route("/logout")
@login_required_check
def logout():
    app.logger.info(f"User {session['username']} logged out.")
    session.clear()  # Clear the session data
    return redirect("/login")  # Redirect to the login page


# @app.errorhandler(500)
# def internal_error(error):
#     app.logger.error(f"Server Error: {error}")
#     return jsonify({"error": "Internal server error"}), 500

# @app.errorhandler(404)
# def not_found_error(error):
#     app.logger.warning(f"404 Error: {error}")
#     return jsonify({"error": "Not found"}), 404

@login_required_check
@app.route("/debug_session")
def debug_session():
    session_id = request.cookies.get("session")
    print(f"Session ID: {session_id}")
    app.logger.info(f"Session data {session}" )
    print(f"Session data: {session}")
    print(f"Session username: {session.get('username')}")
    print(WeatherLog.__table__)
    print(app.secret_key) 
    return "Check the console for session data"



if __name__ == "__main__":
    app.run(debug=True)
