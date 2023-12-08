
# IoT Device Management Platform

The IoT Device Management Platform is a comprehensive solution designed to facilitate the efficient management of Internet of Things (IoT) devices. This platform empowers users to register and authenticate with JSON Web Token (JWT) authentication, utilizing a role-based access control system that includes levels such as Operator, Engineer, Manager, and Owner.

### Table of Contents

- [IoT Device Management Platform](#iot-device-management-platform)
  - [Key Features](#key-features)
  - [Installation](#installation)


## Key Features

- **User Authentication:** Utilize JWT authentication for secure user registration and authentication.
- **Role-Based Access Control (RBAC):** Implement a flexible RBAC system with distinct roles, including Operator, Engineer, Manager, and Owner, to regulate access and permissions within the platform.
- **Device Information Management:** Store and manage device information in a dedicated database to ensure accurate and organized records.
- **Telemetry Data Storage:** Separate telemetry data into its own database for efficient storage and retrieval, providing a scalable solution for managing large volumes of data.
- **RESTful API Design:** Develop a well-structured and RESTful API to enable seamless communication and interaction with the IoT Device Management Platform.
- **Serializers:** Use serializers to transform complex data types into JSON and simplify data handling in your Django application.
- **Viewsets:** Implement viewsets to organize the logic for processing HTTP requests in a clean and modular way.
- **Routing:** Define URL patterns and routing mechanisms to map HTTP requests to the appropriate viewsets.
- **Swagger Documentation:** Utilize Swagger to automatically generate interactive API documentation, showcasing the available endpoints and their functionalities.

## Installation
Follow these steps to set up and run the project on your system:

```bash
1. Clone the Repository
git clone <repository-url>
cd <project-directory>

2. Make .env file in your repository
cp .env example-env 

3. Build the Project
sudo make build

4. Make Migrations
Open a new terminal window and navigate to the project directory:
cd <project-directory>
# Run the following command to create database migrations:
sudo make makemigrations

5. Apply Migrations
# In the same terminal window, apply the migrations to set up the database:
sudo make migrate
