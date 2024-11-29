### Objective of the Project

The goal of this project is to build a **weather data management web application** with the following key features:

1. **User Authentication**:  
   - Implement a **secure login system** where users are authenticated based on a predefined **JSON file** containing their credentials.
   - Only authenticated users will be allowed to access the weather data retrieval and logging functionalities.

2. **Weather Data Retrieval**:  
   - Use the **OpenWeather API** to fetch real-time weather data for a specific city.
   - Retrieve and display the following details for the selected city:
     - Temperature (in Celsius or Fahrenheit)
     - Pressure
     - Humidity
     - Wind Speed
     - Wind Degree
   - The weather data should be **auto-retrieved** every 2 seconds for the specified city.

3. **Log Weather Data**:  
   - Provide a feature to **log weather data** by clicking a "Log Weather" button.
   - Store the logged data in a **list** and display it in a **table** or **card view** for users to manage.

4. **Manage Weather Logs**:  
   - Allow users to:
     - View their logged weather data.
     - **Delete individual logs** when needed.

5. **Database Persistence**:  
   - Store user-specific weather logs in a **relational database** (SQLite or PostgreSQL).
   - This ensures data persistence and allows easy access to the logged information.

6. **Error Handling and Security**:  
   - Implement error handling for common issues such as **invalid city names** or **connection issues** when fetching data from the API.
   - **Securely manage API keys**, ensuring they are not exposed in the code.

### Optional Challenge:  
- **AWS Lambda & API Gateway**:
   - For enhanced scalability, replace the local database with **AWS DynamoDB** and integrate **AWS Lambda** for serverless backend functionality.
   - Use **API Gateway** to expose the Lambda function as an API for logging weather data in the cloud.

### Technologies:
- **Backend**: Python (using Django, Flask, or FastAPI)
- **Frontend**: HTML, CSS (and optionally JavaScript or Bootstrap)
- **Database**: SQLite (or PostgreSQL)
- **Weather API**: OpenWeather API
- **Authentication**: JSON file-based user authentication

This project will demonstrate your ability to create a secure, functional web application with weather data management features, integrating both frontend and backend technologies, while ensuring proper error handling and data persistence.