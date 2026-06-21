# Base Image
FROM python:3.12-slim

# Set Working Directory
WORKDIR /app

# Copy Application
COPY app.py .

# Run Application
CMD ["python", "app.py"]