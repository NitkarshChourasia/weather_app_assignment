import json
import re  # to use regex for password validation
from datetime import datetime
import os
import logging
from datetime import timedelta
import requests
from flask import Flask, render_template, request, redirect, session, jsonify
from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_bcrypt import Bcrypt
from sqlalchemy import func
import random
from flask_wtf.csrf import CSRFProtect
from secret_key_generator import generate_secret_key
from logging.handlers import RotatingFileHandler
from flask.sessions import SecureCookieSessionInterface

# Load environment variables from .env
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
# Set up the logger for both CMD and file output
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask

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


# Initialize the logger
logger = setup_logging()
print("logger initialised")
app.logger = logger

# PostgreSQL Database Configuration
db_user = os.getenv("POSTGRES_USER")
db_password = os.getenv("POSTGRES_PASSWORD")
db_host = os.getenv("POSTGRES_HOST")
db_port = os.getenv("POSTGRES_PORT")
db_name = os.getenv("POSTGRES_DB")

app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

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
db = SQLAlchemy(app)


# WeatherLog Model
#! Have to update this also
#! Have to update this also
#! Have to update this also
#! Have to update this also
#! Have to update this also
class WeatherLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    city = db.Column(db.String(120), nullable=False)
    temperature = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=func.current_timestamp())
#! Have to update this also
#! Have to update this also
#! Have to update this also
#! Have to update this also
#! Have to update this also


# Initialize the database
with app.app_context():
    db.create_all()


@app.route("/")
def dashboard_icons():
    weather_icons = {
        "Clouds": url_for("static", filename="images/clouds.png"),
        "Clear": url_for("static", filename="images/clear.png"),
        "Rain": url_for("static", filename="images/rain.png"),
        "Drizzle": url_for("static", filename="images/drizzle.png"),
        "Mist": url_for("static", filename="images/mist.png"),
        "Snow": url_for("static", filename="images/snow.png"),
        "Thunderstorm": url_for("static", filename="images/thunder.png"),
        "default": url_for("static", filename="images/search.png"),
    }
    return render_template("dashboard.html", weather_icons=weather_icons)


# Utility function to fetch weather data from OpenWeather API
@app.route("/weather", methods=["GET"])
def fetch_weather_data():
    city = request.args.get("city")
    app.logger.info(f"Fetching weather data for city: {city}")
    print(city)
    if not city:
        app.logger.warning("City parameter is missing in weather fetch request")
        return jsonify({"error": "City parameter is required"}), 400

    api_key1 = os.getenv("OPENWEATHER_API_KEY")
    api_key2 = os.getenv("OPENWEATHER_API_KEY1")
    api_key = random.choice([api_key1, api_key2])
    print(api_key)

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&APPID={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        app.logger.info(f"Successfully fetched weather data for city: {city}")
        return jsonify(response.json())  # Return the weather data as JSON
    else:
        app.logger.error(f"Failed to fetch weather data for city: {city} (Status code: {response.status_code})")
        return jsonify({"error": "City not found"}), response.status_code


# Define logs globally
logs = []


# Decorator for authentication check
def login_required_check(func):
    def login_required_wrapper(*args, **kwargs):
        if "username" not in session:
            return redirect("/login")
        return func(*args, **kwargs)

    login_required_wrapper.__name__ = func.__name__
    return login_required_wrapper


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
            if user["username"] == username and bcrypt.check_password_hash(user["password"], password):
                session["username"] = username
                return redirect("/dashboard")  # Redirect after successful login

        # Log failed login attempt
        app.logger.warning(f"Failed login attempt for user: {username}")
        return "Invalid credentials", 401  # Return an error message if login fails

    return render_template("login.html")  # Render the login form on GET request

# For registration purposes

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
            app.logger.warning(f"Weak password attempt during registration for user: {username}")
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


# Home route
@app.route("/home")
@app.route("/")
@login_required_check
def home():
    return render_template("dashboard.html")


# Dashboard route
@app.route("/dashboard")
@login_required_check
def dashboard():
    return render_template("dashboard.html")


# Fetch weather data route
@app.route("/weather/<city>")
def get_weather(city):
    data = fetch_weather_data(city)
    if data:
        return jsonify(data)
    return jsonify({"error": "Unable to fetch weather data"}), 500


# Log weather data route
@app.route("/log_weather", methods=["POST"])
@login_required_check
def log_weather_data():
    data = request.json
    if not data.get("city") or not data.get("temperature"):
        app.logger.warning(f"Missing city or temperature data in log request by user: {session['username']}")
        return jsonify({"error": "Missing city or temperature data"}), 400

    log = WeatherLog(
        username=session["username"], city=data["city"], temperature=data["temperature"]
    )
    db.session.add(log)
    db.session.commit()
    app.logger.info(f"User {session['username']} logged weather data for city: {data['city']} with temperature: {data['temperature']}")
    return jsonify({"message": "Weather data logged successfully"}), 201


# View weather logs route
@app.route("/weather_logs")
@login_required_check
def weather_logs():
    logs = WeatherLog.query.filter_by(username=session["username"]).all()
    return render_template("weather_logs.html", logs=logs)


# Delete weather log route (integrated with both DB and in-memory logs)
@app.route("/delete_log/<int:log_id>", methods=["POST"])
@login_required_check
def delete_log(log_id):
    # If using in-memory logs:
    global logs
    if "logs" in globals() and any(log["id"] == log_id for log in logs):
        logs = [log for log in logs if log["id"] != log_id]
        return jsonify({"message": "Log deleted successfully"}), 200

    # If using the database:
    log = WeatherLog.query.get_or_404(log_id)
    if log.username != session["username"]:
        app.logger.warning(f"Unauthorized deletion attempt for log id: {log_id} by user: {session['username']}")
        return jsonify({"error": "Forbidden"}), 403

    db.session.delete(log)
    db.session.commit()
    app.logger.info(f"User {session['username']} deleted weather log with id: {log_id}")
    return jsonify({"message": "Log deleted successfully"}), 200


# Logout route
@app.route("/logout")
@login_required_check
def logout():
    app.logger.info(f"User {session['username']} logged out.")
    session.clear()  # Clear the session data
    return redirect("/login")  # Redirect to the login page


@app.route("/clear-logs", methods=[""])
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

@app.errorhandler(500)
def internal_error(error):
    app.logger.error(f"Server Error: {error}")
    return jsonify({"error": "Internal server error"}), 500

@app.errorhandler(404)
def not_found_error(error):
    app.logger.warning(f"404 Error: {error}")
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
