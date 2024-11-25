from flask import Flask, render_template, request, redirect, session, jsonify
import json
import requests
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from dotenv import load_dotenv
# Load environment variables
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "your_default_secret_key")
bcrypt = Bcrypt(app)

# PostgreSQL Database Configuration
db_user = os.getenv("POSTGRES_USER", "your_postgres_user")
db_password = os.getenv("POSTGRES_PASSWORD", "your_postgres_password")
db_host = os.getenv("POSTGRES_HOST", "localhost")
db_port = os.getenv("POSTGRES_PORT", "5432")
db_name = os.getenv("POSTGRES_DB", "your_database_name")

app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)


# WeatherLog Model
class WeatherLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    city = db.Column(db.String(120), nullable=False)
    temperature = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

# Initialize the database
with app.app_context():
    db.create_all()

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        with open('data/users.json') as f:
            users = json.load(f)['users']
        username = request.form['username']
        password = request.form['password']
        for user in users:
            if user['username'] == username and bcrypt.check_password_hash(user['password'], password):
                session['username'] = username
                return redirect('/dashboard')
        return "Invalid credentials"
    return render_template('login.html')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return render_template('dashboard.html')
    return redirect('/login')

@app.route('/weather/<city>')
def get_weather(city):
    api_key = os.getenv("OPENWEATHER_API_KEY")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&APPID={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Unable to fetch weather data"}

@app.route('/log_weather', methods=['POST'])
def log_weather():
    if 'username' in session:
        data = request.json
        log = WeatherLog(username=session['username'], **data)
        db.session.add(log)
        db.session.commit()
        return {"message": "Logged successfully"}
    return {"error": "Unauthorized"}

@app.route('/weather_logs')
def weather_logs():
    if 'username' in session:
        logs = WeatherLog.query.filter_by(username=session['username']).all()
        return render_template('weather_logs.html', logs=logs)
    return redirect('/login')

@app.route('/delete_log/<int:log_id>', methods=['POST'])
def delete_log(log_id):
    if 'username' in session:
        log = WeatherLog.query.get(log_id)
        if log:
            db.session.delete(log)
            db.session.commit()
            return {"message": "Deleted successfully"}
        else:
            return {"error": "Log not found"}, 404
    return {"error": "Unauthorized"}, 401

@app.route('/log_weather', methods=['POST'])
def log_weather():
    if 'username' in session:
        data = request.json
        log = WeatherLog(username=session['username'], **data)
        db.session.add(log)
        db.session.commit()
        return {"message": "Weather data logged successfully"}
    return {"error": "Unauthorized"}, 401

if __name__ == '__main__':
    app.run(debug=True)
