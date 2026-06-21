# Dockerized Python Version Application

This project demonstrates a simple Dockerized Python application using the official Python 3.12 Slim image.

## Features

- Uses python:3.12-slim as base image
- Displays current Python version
- Displays current date and time
- Runs automatically when container starts

## Project Structure

```text
docker_app_assignement/
├── app.py
├── Dockerfile
├── requirements.txt
└── README.md
```

## Build Docker Image

```bash
docker build -t python-version-app .
```

## Run Docker Container

```bash
docker run --rm python-version-app
```

## Sample Output

```text
==================================================
Python Version : 3.12.11
Current Date & Time : 2026-06-21 14:25:18.456321
==================================================
```

## Screenshot

Place the output screenshot inside:

```text
screenshots/output.png
```

Then add:

```markdown
![Output Screenshot](screenshots/output.png)
```

## Author
Puneet Khandelwal