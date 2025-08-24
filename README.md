# Flask CI/CD Pipeline

## Overview
This project demonstrates a complete **CI/CD pipeline for a Python-based Flask REST API**.  
The pipeline automates code testing, linting, containerization with Docker, and deployment through GitHub Actions.  
It serves as a practical example of how modern development teams streamline software delivery using CI/CD practices.

---

## Features
- REST API built with **Flask**  
- Unit testing with **pytest**  
- Code linting with **flake8**  
- Containerized using **Docker**  
- Automated CI/CD pipeline with **GitHub Actions**  
- Deployment to cloud platforms (Heroku or Render)  

---

## Project Structure

flask-ci-cd-project/
│── app/
│ ├── init.py
│ ├── main.py
│ ├── routes.py
│
│── tests/
│ ├── test_routes.py
│
│── requirements.txt
│── Dockerfile
│── docker-compose.yml
│── .flake8
│── .github/
│ └── workflows/
│ └── ci-cd.yml
│── README.md


---

## Tech Stack
- **Programming Language:** Python 3.10  
- **Framework:** Flask  
- **Testing:** Pytest  
- **Linting:** Flake8  
- **CI/CD Tool:** GitHub Actions  
- **Containerization:** Docker  
- **Deployment:** Heroku / Render  

---

## CI/CD Workflow
1. **Code Quality Check** – Flake8 runs on every push to ensure code follows PEP8 standards.  
2. **Automated Testing** – Pytest runs unit tests to validate API functionality.  
3. **Docker Build** – Application is containerized with Docker.  
4. **Docker Push** – Docker image is pushed to DockerHub.  
5. **Deployment** – Application is deployed to Heroku/Render automatically after tests pass.  

---

## How to Run Locally

### Prerequisites
- Python 3.10+  
- Docker (optional, for containerized execution)  

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/flask-ci-cd-pipeline.git
   cd flask-ci-cd-pipeline

python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows
pip install -r requirements.txt

python app/main.py

pytest

docker build -t flask-ci-cd .
docker run -p 5000:5000 flask-ci-cd

## **Deployment**
### This project can be deployed to:

- Heroku: Using a Procfile and GitHub integration.
- Render: Connect GitHub repo for auto-deployments.
- AWS/GCP/Azure: Deploy Docker image using ECS, Cloud Run, or App Service.

# Use Case in Industry
- Automating testing and deployment ensures code reliability.
- Docker makes the application portable and scalable.
- CI/CD with GitHub Actions reduces manual effort and speeds up release cycles.
- Useful for web development, data engineering, and machine learning deployment scenarios.

## **License**
**This project is licensed under the MIT License.**

yaml
Copy
Edit
