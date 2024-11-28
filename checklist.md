---

### **Weather Data Management Application - Detailed Checklist**

---

#### **1. Retrieve Weather Data**
- **[ ] API Integration:**
  - [X] Register and get an API key from OpenWeather API.
  - [X] Set up environment variable or configuration file to securely store the API key.
  - [X] Implement a function to fetch data from the OpenWeather API:
    - [X] Create a function to send GET requests to the OpenWeather API.
    - [X] Implement error handling for invalid API requests.
  - [X] Define the API URL format (`https://api.openweathermap.org/data/2.5/weather?q=<city>&appid=<API_KEY>`).
  
- **[ ] Fetch Required Weather Details:**
  - [ ] Retrieve **temperature** (in Celsius or Fahrenheit).
  - [ ] Retrieve **humidity**.
  - [ ] Retrieve **pressure**.
  - [ ] Retrieve **wind speed**.
  - [ ] Retrieve **wind degree**.

- **[ ] Auto-Retrieve Weather Data:**
  - [X] Implement auto-refresh every 2 seconds with updated weather data.
  - [X] Display weather data in real-time on the frontend.

- **[ ] Display Weather Data:**
  - [ ] Create frontend elements to display the retrieved data (e.g., temperature, humidity, etc.).
  - [X] Ensure the UI dynamically updates with new data every 2 seconds.

- **[ ] Error Handling:**
  - [ ] Handle errors such as invalid city names, API request failures, or network issues.
  - [ ] Display error messages to the user if the data cannot be fetched.

---

#### **2. Log Weather Data**
- **[ ] Button to Log Weather:**
  - [X] Create a "Log Weather" button that allows users to log the current weather data.
  - [X] Implement a click event that captures and stores the current weather information.

- **[ ] Store Weather Logs:**
  - [X] Create a data structure (e.g., list or array) to store logged weather data.
  - [ ] Ensure the data is properly formatted (e.g., storing the date, city, temperature, etc.).

- **[ ] Display Logged Weather Data:**
  - [ ] Create a table or card layout to display the logged weather data on the frontend.
  - [X] Show the timestamp for each logged weather entry.

- **[ ] Clear Weather Logs:**
  - [ ] Add a "Clear All Logs" button to allow users to clear all weather logs.
  - [ ] Implement a confirmation prompt to prevent accidental deletion.

---

#### **3. User Authentication**
- **[ ] JSON Authentication File:**
  - [ ] Create a JSON file to store user credentials (e.g., `{"username": "user", "password": "password123"}`).
  - [ ] Securely store the authentication JSON file, ensuring it is not exposed in the frontend code.
  
- **[ ] Login Page:**
  - [ ] Create a login form where users can enter their credentials.
  - [ ] Add form validation to check if the username and password are provided.
  - [ ] Compare the user input with the stored credentials in the JSON file.

- **[ ] Session Management:**
  - [ ] Implement a session to maintain the user's login state after authentication.
  - [ ] Ensure users cannot access the weather features unless logged in.
  
- **[ ] Access Control:**
  - [ ] Block non-authenticated users from accessing weather retrieval and logging functionalities.
  - [ ] Redirect non-authenticated users to the login page.

---

#### **4. Weather Log Management**
- **[ ] View Weather Logs:**
  - [ ] Create a table that displays all logged weather data (city, temperature, timestamp, etc.).
  - [ ] Sort the logs by timestamp, city, or temperature as needed.

- **[ ] Delete Weather Logs:**
  - [ ] Add a "Delete" button for each individual log entry.
  - [ ] Implement a function to remove a specific weather log from the list.
  - [ ] Ensure deleted logs are removed from the backend storage (database).

- **[ ] Edit Weather Logs (Optional):**
  - [ ] Add functionality to allow users to edit a specific weather log.
  - [ ] Provide an interface to update weather details (e.g., temperature, city).

---

#### **5. Persistence (Database)**
- **[ ] Database Setup:**
  - [ ] Choose and set up the database (SQLite or PostgreSQL).
  - [ ] Create database tables to store user information and weather logs.
    - **Users Table:** (username, password, email, etc.)
    - **Weather Logs Table:** (log_id, user_id, city, temperature, humidity, pressure, wind_speed, timestamp, etc.)

- **[ ] User-Specific Weather Logs:**
  - [ ] Implement user-specific storage for weather logs.
  - [ ] Link weather logs to the specific authenticated user in the database.

- **[ ] CRUD Operations for Logs:**
  - [ ] Implement **Create** operation to store new weather logs.
  - [ ] Implement **Read** operation to fetch and display logs.
  - [ ] Implement **Update** operation (if editing logs).
  - [ ] Implement **Delete** operation to remove specific logs.

- **[ ] Ensure Data Integrity:**
  - [ ] Implement transaction management to ensure logs are stored and deleted correctly.
  - [ ] Handle database errors gracefully (e.g., connection issues, constraint violations).

---

#### **6. Error Handling and Security**
- **[ ] Handle API Errors:**
  - [ ] Handle errors such as invalid city names or API connection issues.
  - [ ] Provide meaningful error messages on the frontend if data cannot be fetched.

- **[ ] Secure API Key:**
  - [ ] Ensure that the OpenWeather API key is not exposed in the frontend code.
  - [ ] Store the API key securely in environment variables or configuration files.

- **[ ] User Input Validation:**
  - [ ] Validate user input during login and weather retrieval (e.g., ensure valid city name format).
  - [ ] Sanitize inputs to avoid security vulnerabilities (e.g., SQL injection).

- **[ ] Secure Login Authentication:**
  - [ ] Use secure hashing (e.g., bcrypt) for storing user passwords (instead of plain text).
  - [ ] Implement HTTPS for secure communication between the frontend and backend.

---

#### **7. Optional AWS Task (Advanced)**
- **[ ] AWS Lambda & API Gateway Setup:**
  - [ ] Set up an AWS Lambda function to handle logging weather data into DynamoDB.
  - [ ] Create an API Gateway to interface with the Lambda function.

- **[ ] AWS DynamoDB Integration:**
  - [ ] Replace the local database (SQLite/PostgreSQL) with DynamoDB for storing weather logs.
  - [ ] Implement the necessary read/write operations for interacting with DynamoDB.

- **[ ] Ensure Scalability:**
  - [ ] Test the cloud-based solution with large data sets to ensure scalability.
  - [ ] Implement proper logging and error handling in AWS Lambda functions.

- **[ ] AWS IAM Roles:**
  - [ ] Set up appropriate IAM roles and permissions to allow Lambda functions to interact with DynamoDB securely.

---

#### **8. Technologies and Tools**
- **[ ] Backend Framework:**
  - [ ] Choose a Python backend framework (Flask, Django, or FastAPI).
  - [ ] Set up the backend environment with necessary dependencies (e.g., requests, flask, SQLAlchemy, etc.).

- **[ ] Frontend Development:**
  - [ ] Implement the frontend using HTML, CSS, and optionally JavaScript (or Bootstrap for styling).
  - [ ] Ensure the frontend is responsive and user-friendly.
  - [ ] Implement AJAX calls to fetch weather data and submit logged weather entries.

- **[ ] Database Setup:**
  - [ ] Choose a database system (SQLite or PostgreSQL).
  - [ ] Set up ORM (Object Relational Mapping) if using a framework like Flask/Django.
  - [ ] Implement database migrations for easy schema management.

- **[ ] Authentication Implementation:**
  - [ ] Use JSON file for initial authentication or consider a more secure option like JWT or OAuth if needed.
  - [ ] Ensure login credentials are encrypted and stored securely.

- **[ ] Optional: Dockerize Application:**
  - [ ] Create Dockerfiles for both frontend and backend components.
  - [ ] Use Docker Compose to orchestrate multi-container applications.
  - [ ] Test the containerized application locally before deployment.

---

#### **9. Final Submission**
- **[ ] Test Full Application:**
  - [ ] Test the weather data retrieval, logging, and management functionalities.
  - [ ] Test user authentication and ensure proper session management.
  - [ ] Test the database interactions (CRUD operations for weather logs).
  - [ ] Test error handling (e.g., API failures, invalid city names, etc.).

- **[ ] Documentation (README):**
  - [ ] Write clear instructions for setting up and running the application.
  - [ ] Include details about the required API keys, installation steps, and how to authenticate users.

- **[ ] Code Quality:**
  - [ ] Ensure code is well-documented, organized, and follows best practices.
  - [ ] Use version control (Git) and ensure code is properly committed and pushed to a repository.

- **[ ] Final Submission:**
  - [ ] Submit the solution (link to GitHub repository, Docker images, or AWS setup if applicable).
  - [ ] Submit by the deadline (29th November).