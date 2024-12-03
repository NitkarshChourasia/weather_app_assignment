from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone

db = SQLAlchemy()

class WeatherData(db.Model):
    __tablename__ = 'weather_data'
    id = db.Column(db.Integer, primary_key=True)  # Primary key for the table
    username=db.Column(db.String(100), nullable=False) #Ensure this column exists in the table
    country_name = db.Column(db.String(100), nullable=False)  # Country name
    city_name = db.Column(db.String(100), nullable=False)  # City name
    weather_condition = db.Column(db.String(100), nullable=False)  # Weather condition (e.g., "Smoke")
    temperature = db.Column(db.Float, nullable=False)  # Temperature in degrees (float for precision)
    pressure = db.Column(db.Integer, nullable=False)  # Atmospheric pressure in hPa
    humidity = db.Column(db.Integer, nullable=False)  # Humidity percentage
    wind_speed = db.Column(db.Float, nullable=False)  # Wind speed in m/s
    wind_degree = db.Column(db.Float, nullable=False)  # Wind direction in degrees
    timestamp = db.Column(db.DateTime(timezone=True), default=datetime.now(timezone.utc))  # UTC timestamp

    def __repr__(self):
        return f"<WeatherData(city_name={self.city_name}, country_name={self.country_name})>"
