# models.py
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone

db = SQLAlchemy()
class WeatherLog(db.Model):
    __tablename__ = 'weather_logs'  # Make sure the table name is correct
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)  # Ensure this column exists
    city = db.Column(db.String(100), nullable=False)
    temperature = db.Column(db.Float, nullable=False)
    pressure = db.Column(db.Integer, nullable=False)
    humidity = db.Column(db.Integer, nullable=False)
    wind_speed = db.Column(db.Float, nullable=False)
    wind_degree = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime(timezone=True), default=datetime.now(timezone.utc))