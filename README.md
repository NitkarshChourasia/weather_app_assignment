Objective
Your assignment is to create a weather data management application using Python. The application should enable users to:

Securely log in using a predefined JSON file for authentication.
Retrieve real-time weather data for specific cities.
Log and manage the retrieved weather data in a structured format.
Features and Requirements
1. Retrieve Weather Data:

Implement a feature that retrieves weather data using the OpenWeather API for any city.
API Format: https://api.openweathermap.org/data/2.5/weather?q=<your_city>&APPID=<your_API>
More Info on API: OpenWeather Current Weather Data
Retrieve and display the following weather details:
Temperature (in Celsius or Fahrenheit)
Pressure
Humidity
Wind Speed
Wind Degree
Auto-retrieve weather data for a user-specified city every 2 seconds.
2. Log Weather Data:

Add a button labeled "Log Weather" to store the currently displayed weather data.
Store logged data in a list, displaying it in a table or card view for the user.
3. User Authentication:

Create a Login Page that authenticates users based on credentials stored in a JSON file.
Format of the JSON file can be as per your choice:
Ensure only authenticated users can access the weather retrieval and logging functionalities.
4. Weather Log Management:

Allow users to perform the following actions on their weather logs:
View logged weather data in a table.
Delete individual logs.
5. Persistence:

Store user-specific weather logs in a relational database (e.g., SQLite or PostgreSQL).
6. Error Handling and Security:

Handle API errors (e.g., invalid city names or connection issues).
Securely manage API keys and avoid exposing them in the code.
Optional AWS Task
As an optional challenge, you may integrate the following AWS-related feature:

AWS Lambda & API Gateway:
Build a serverless backend that logs weather data into an AWS DynamoDB database.
Replace the local database with this cloud-based solution for enhanced persistence and scalability.
Technologies to Use
Required:

Backend: Python (Django, Flask, or FastAPI).
Frontend: HTML, CSS, and optionally JavaScript (or Bootstrap for styling).
Database: SQLite (for simplicity) or PostgreSQL.
Weather API: OpenWeather API.
Authentication: JSON file-based user authentication.
Optional:

AWS SDK for integrating AWS services like Lambda and DynamoDB.
Docker for containerization of the application.
