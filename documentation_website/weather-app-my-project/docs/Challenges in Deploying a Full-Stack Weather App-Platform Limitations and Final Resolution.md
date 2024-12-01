### Hosting and Deployment Challenges for Weather App Project

During the deployment phase of my **Weather Data Management Web Application**, I encountered several challenges while attempting to host the project across various platforms. Here is a detailed breakdown of the steps taken, the issues faced, and the final outcomes.

---

#### **1. Vercel Deployment**
I initially tried to deploy the Flask-based weather app on **Vercel**, known for its seamless support for frontend frameworks and serverless functions. However, integrating the backend and database encountered obstacles.

- **Issue**: The free tier of Vercel does not support relational databases like **PostgreSQL**, which was essential for storing user-specific weather logs. Although the app could run with in-memory storage or simpler configurations, it could not support the database-dependent functionality in production.
- **Outcome**: The deployment failed due to the lack of support for PostgreSQL databases in Vercel's free tier.

---

#### **2. AWS Deployment**
Next, I explored **AWS**, leveraging its robust suite of services like **EC2** for backend hosting and **RDS** for database management.

- **Issue**: While AWS offers comprehensive solutions for full-stack applications, including backend and database hosting, the associated costs were beyond the budget of this project. Particularly, hosting a **PostgreSQL** database and backend services required a paid plan.
- **Outcome**: I couldn't proceed with AWS due to the costs involved.

---

#### **3. Azure Deployment**
I also considered deploying the project on **Microsoft Azure**, a cloud platform with similar offerings to AWS.

- **Issue**: Hosting the Flask app and PostgreSQL database on Azure incurred costs, which were a significant constraint for this project. As a result, I was unable to deploy the application on Azure.
- **Outcome**: The deployment on Azure was not feasible due to budget limitations.

---

#### **4. GitHub Pages**
Since GitHub Pages provides free hosting for static websites, I explored hosting the frontend or documentation site there.

- **Issue**: GitHub Pages does not support backend services or dynamic content, making it unsuitable for the full-stack Flask application.
- **Outcome**: GitHub Pages was used to host the **static documentation** of the project successfully.

---

#### **Final Resolution**
Given the challenges of hosting the full-stack app, I decided to:

1. **Upload the source code to GitHub**:  
   - This allows others to review, learn from, and collaborate on the project.  
   - The app itself couldn't be hosted live due to database restrictions and platform constraints.

2. **Host the project documentation on GitHub Pages**:  
   - The static documentation was successfully hosted on **GitHub Pages** and linked to a custom domain I purchased:  
     **[nitkarshchourasia.me](https://nitkarshchourasia.me)**.

---

### **Conclusion**
In summary, deploying the Flask-based **Weather Data Management Web Application** involved navigating platform limitations, database integration issues, and budget constraints. Key observations include:

- **Vercel**: Free tier lacked support for PostgreSQL.  
- **AWS and Azure**: Reliable but costly for backend and database hosting.  
- **GitHub Pages**: Ideal for static content but unsuitable for the dynamic app.

Ultimately, I hosted the **documentation site** successfully on GitHub Pages, linked to my custom domain, while making the project’s **source code available on GitHub** for accessibility and collaboration.