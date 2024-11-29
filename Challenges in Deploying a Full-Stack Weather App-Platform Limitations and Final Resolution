### Hosting and Deployment Challenges for Weather App Project

During the deployment phase of my **Weather Data Management Web Application**, I faced several challenges while trying to host the project on various platforms. Below is a detailed account of the steps I took, the issues I encountered, and the final resolution.

#### 1. **Vercel Deployment**:
I initially attempted to deploy the Flask-based weather app on **Vercel**, a popular platform for hosting web applications. While Vercel supports dynamic deployments, it faced issues due to the database integration.

- **Issue**: The free tier of Vercel does not support the usage of relational databases like **PostgreSQL** for full-stack applications. The PostgreSQL database was a crucial component for storing user-specific weather logs in this project.
- **Result**: The application could not be deployed successfully with a PostgreSQL database, and I was unable to utilize the dynamic server-side features in production. If the application were to run without a database (using in-memory data storage or simpler configurations), it would have worked fine.

#### 2. **AWS Deployment**:
Next, I explored hosting the project on **AWS**. AWS provides various services like **EC2** for backend hosting and **RDS** for database hosting, along with other services for deploying full-stack applications.

- **Issue**: While AWS does support both backend and database hosting, the costs involved were a significant concern. AWS services, particularly for hosting a **PostgreSQL** database along with backend services, require a paid plan, which was beyond the budget for this project.
- **Result**: Due to the costs associated with AWS, I could not proceed with the deployment of the full-stack application on this platform. I needed a more affordable solution that would accommodate both backend and database hosting.

#### 3. **GitHub Pages**:
I also considered using **GitHub Pages**, a free service provided by GitHub for hosting static websites. GitHub Pages is designed for frontend applications and can host HTML, CSS, and JavaScript files.

- **Issue**: GitHub Pages only supports static pages and does not allow for hosting backend services such as Flask applications or managing databases. As my weather app was a **full-stack** project with both frontend and backend components (Flask app and PostgreSQL), this platform could not accommodate the dynamic server-side code and database storage.
- **Result**: Since GitHub Pages only supports static content, it was not a viable option for hosting the full-stack Flask app with dynamic backend processing and database storage.

#### 4. **Final Resolution**: GitHub Repository Hosting
After exploring multiple options, I finally settled on **uploading the project code to GitHub**. While the app could not be hosted live in a production environment, I chose to showcase the project by making the complete source code available on GitHub for review and further development.

- **Reasoning**: By uploading the project to GitHub, I could still share the project with others, provide access to the code for learning purposes, and allow for potential collaboration or improvements. Although the app could not be hosted live due to database restrictions on free hosting platforms, GitHub provided a great alternative for storing and sharing the code.

### Conclusion:
In summary, during the deployment phase of my Flask-based **Weather Data Management Web Application**, I faced multiple challenges regarding platform compatibility, database integration, and budget constraints. The key platforms I explored—Vercel, AWS, and GitHub Pages—each had their limitations:

- **Vercel**: Free tier did not support PostgreSQL database.
- **AWS**: Required paid services for backend and database hosting.
- **GitHub Pages**: Could only host static content, not dynamic Flask applications.

Ultimately, I decided to **upload the project code to GitHub** as a solution, enabling others to access the source code and make use of the project while bypassing the hosting issues encountered.