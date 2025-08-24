# CI/CD Pipeline for Flask API with Docker & GitHub Actions

This project is a simple Flask REST API with an automated CI/CD pipeline using GitHub Actions, Docker, and pytest.

## Project Structure

```
flask-ci-cd-project/
│── app/
│   ├── __init__.py
│   ├── main.py           # Flask API
│   └── routes.py         # API routes
│
│── tests/
│   └── test_routes.py    # pytest unit tests
│
│── requirements.txt      # dependencies
│── Dockerfile            # Docker container setup
│── .flake8               # linting config
│── .github/
│   └── workflows/
│       └── ci-cd.yml     # GitHub Actions pipeline
└── README.md             # documentation
```

## Getting Started

### Prerequisites

*   Python 3.9+
*   Docker

### Installation and Running Locally

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/<your-username>/flask-ci-cd-project.git
    cd flask-ci-cd-project
    ```

2.  **Create a virtual environment and install dependencies:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3.  **Run the application:**
    ```bash
    gunicorn --bind 127.0.0.1:5000 "app.main:create_app()"
    ```
    The application will be available at `http://127.0.0.1:5000/hello`.

### Running with Docker

1.  **Build the Docker image:**
    ```bash
    docker build -t flask-api .
    ```

2.  **Run the Docker container:**
    ```bash
    docker run -p 5000:5000 flask-api
    ```
    The application will be available at `http://localhost:5000/hello`.

## Testing

To run the unit tests, use pytest:
```bash
pytest
```

## CI/CD Pipeline

The project uses GitHub Actions for CI/CD. The pipeline is defined in `.github/workflows/ci-cd.yml` and includes the following jobs:

*   **Linting:** Checks the code for style issues using `flake8`.
*   **Testing:** Runs the unit tests using `pytest`.
*   **Docker Build:** Builds the Docker image for the application.

The pipeline is triggered on every push and pull request to the `main` branch.
