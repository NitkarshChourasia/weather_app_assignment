# **Weather App Assignment 🌦️**

[![License: GPL-3.0](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](LICENSE)

This is a Python-based web application that allows users to retrieve, log, and manage weather data. It features secure user authentication, real-time weather data retrieval using the OpenWeather API, and persistent logging with a PostgreSQL database.

<!-- ### **Live Demo**
🌐 [Weather App Assignment](https://weather-app-assignment-green.vercel.app/) -->

### **Extensive Documentation**

📖 [Weather App Documentation](https://nitkarshchourasia.me/)

---

## **Key Features** 🚀

1. **Real-Time Weather Data Retrieval**

   - Fetches weather data using the [OpenWeather API](https://openweathermap.org/current) for any city.
   - Displays key details:
     - **Temperature** (Celsius or Fahrenheit)
     - **Pressure**
     - **Humidity**
     - **Wind Speed and Direction**
   - Auto-refreshes weather data every 2 seconds.

2. **User Authentication**

   - Secure login based on credentials stored in a JSON file.
   - Passwords hashed for secure storage and validation.
   - Only authenticated users can access the app's features.

3. **Weather Logging**

   - Log the displayed weather data with a single click.
   - Persistent storage using PostgreSQL, ensuring user-specific logs are saved.
   - View logged data in a structured table or card view.
   - Ability to delete individual logs.

4. **Enhanced Security**

   - CSRF protection and secure cookie management.
   - API keys securely managed to prevent exposure.

5. **User Experience Enhancements**

   - Night mode for better readability in low-light conditions.
   - Auto-logout after inactivity for enhanced security.
   - Auto-refresh feature every 10 minutes for selected locations.

6. **Optional AWS Integration** (Challenge)
   - Serverless backend using AWS Lambda and API Gateway for storing weather logs in DynamoDB.

---

## **Technologies Used** 🛠️

### **Backend**

- **Python**: Flask for server-side development.
- **PostgreSQL**: For persistent and scalable database storage.
- **SQLAlchemy**: ORM for seamless database integration.

### **Frontend**

- **HTML**, **CSS**, and **JavaScript**: Core frontend technologies.
- **Bootstrap**: For responsive and modern design.

### **Third-Party Services**

- **OpenWeather API**: For fetching real-time weather data.
- **AWS Lambda & DynamoDB** _(optional)_: For cloud-based data storage.

### **Tools**

- **Docker**: Containerization for ease of deployment.
- **Vercel**: Hosting and deployment.

---

## **Setup and Installation** 🛠️

1. **Clone the Repository**

   ```bash
   git clone https://github.com/NitkarshChourasia/weather_app_assignment.git
   cd weather_app_assignment
   ```

2. **Set Up the Environment**

   - Create a `.env` file for sensitive credentials (refer to `.env.example`):
     ```plaintext
     API_KEY=your_openweather_api_key
     DATABASE_URL=your_postgresql_database_url
     SECRET_KEY=your_flask_secret_key
     ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**

   ```bash
   flask run
   ```

5. **Access the App**  
   Navigate to [http://localhost:5000](http://localhost:5000) in your browser.

---

## **Project Structure** 📂

```plaintext
weather_app/
│
├── __pycache__/                  # Compiled Python cache files
│   ├── app.cpython-312.pyc
│   ├── models.cpython-312.pyc
│   └── secret_key_generator.cpython-312.pyc
│
├── app.log                       # Application logs
├── app.py                        # Main application entry point
├── data/                         # Directory for data files
│   └── users.json                # Stores user credentials
│
├── models.py                     # Database models and ORM definitions
├── secret_key_generator.py       # Utility to generate secret keys
├── static/                       # Static files (images, styles, scripts)
│   ├── images/                   # Images used in the application
│   │   ├── background.jpg
│   │   ├── clear.png
│   │   ├── clouds.png
│   │   └── ... (more weather-related icons)
│   │
│   ├── scripts/                  # JavaScript files
│   │   └── dashboard.js
│   │
│   └── styles/                   # CSS stylesheets
│       ├── dashboard.css
│       ├── login_register.css
│       └── weather_logs.css
│
├── templates/                    # HTML templates for Flask rendering
│   ├── dashboard.html
│   ├── login.html
│   ├── register.html
│   └── weather_logs.html
│
├── README.md                     # Project documentation
├── requirements.txt              # Python dependencies
└── utils.py                      # Helper functions and utilities
```

---

## **Challenges Faced & Resolutions** ⚡

1. **Hosting Issues**

   - Resolved by refining Vercel configuration and Docker setup.

2. **API Key Security**

   - Secured by using `.env` files and environment variables.

3. **Database Scalability**
   - Moved from SQLite to PostgreSQL for better handling of concurrent requests.

---

## **Future Enhancements** 🛠️

- Full AWS integration for backend and database.
- Improved user analytics for weather data trends.
- Real-time push notifications for severe weather alerts.

---

## **Contributing** 🤝

Contributions are welcome! Feel free to submit issues and pull requests.

---

## **License** 📜

This project is licensed under the GPL-3.0 License. See the [LICENSE](LICENSE) file for details.

---

## **Contact Me** 📞

💼 **Nitkarsh Chourasia**

- 📧 Email: [playnitkarsh@gmail.com](mailto:playnitkarsh@gmail.com)
- 🌐 [GitHub](https://github.com/NitkarshChourasia) | [LinkedIn](https://www.linkedin.com/) | [LeetCode](https://leetcode.com/)

<!--

weather_app/
│
├── app/                       # Application core
│   ├── __init__.py            # App factory and initialization
│   ├── models.py              # Database models
│   ├── routes/                # Blueprint routes
│   │   ├── __init__.py        # Blueprint initialization
│   │   ├── auth.py            # Authentication routes (login/register)
│   │   ├── dashboard.py       # Dashboard-related routes
│   │   └── weather_logs.py    # Weather logging routes
│   ├── services/              # Service layer (e.g., API integrations)
│   │   ├── __init__.py        # Service initialization
│   │   └── weather_api.py     # OpenWeather API interactions
│   ├── utils/                 # Helper functions
│   │   ├── __init__.py        # Utility initialization
│   │   ├── logger.py          # Logging utilities
│   │   └── data_handler.py    # User and data manipulation utilities
│   ├── static/                # Static files (CSS, JS, Images)
│   │   ├── images/            # Images used in the app
│   │   ├── scripts/           # JavaScript files
│   │   └── styles/            # CSS stylesheets
│   └── templates/             # HTML templates
│       ├── layout.html        # Base template for consistent layout
│       ├── dashboard.html     # Dashboard page
│       ├── login.html         # Login page
│       ├── register.html      # Registration page
│       └── weather_logs.html  # Weather logs page
│
├── data/                      # Data-related files
│   └── users.json             # Mock user data for authentication
│
├── logs/                      # Log files
│   └── app.log                # Application log file
│
├── tests/                     # Unit and integration tests
│   ├── __init__.py            # Test suite initialization
│   ├── test_auth.py           # Tests for authentication
│   ├── test_weather_api.py    # Tests for weather API integration
│   └── test_weather_logs.py   # Tests for weather logging
│
├── migrations/                # Database migration scripts
│   └── (Auto-generated files by Flask-Migrate)
│
├── .env                       # Environment variables (ignored in Git)
├── .gitignore                 # Files and directories to be ignored by Git
├── LICENSE                    # License file
├── README.md                  # Project documentation
├── requirements.txt           # Python dependencies
├── secret_key_generator.py    # Script to generate Flask secret keys
└── wsgi.py                    # WSGI entry point for deployment -->
