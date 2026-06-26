# Python DevSecOps Demo

A simple Flask application used for learning DevSecOps tools such as:

- Jenkins
- SonarQube
- Trivy
- Docker

## Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the application:

```bash
python app.py
```

The application will be available at:

```
http://localhost:5000
```

## Build Docker Image

```bash
docker build -t python-devsecops-demo .
```

## Run Docker Container

```bash
docker run -d -p 5000:5000 python-devsecops-demo
```