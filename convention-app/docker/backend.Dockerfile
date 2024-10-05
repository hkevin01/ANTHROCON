# Use a base image with Python
FROM python:3.11

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY backend/requirements.txt ./requirements.txt

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire backend folder into the container
COPY backend/ ./backend/

# Set the environment variable for Flask
ENV FLASK_APP=backend.main

# Command to run the Flask application
CMD ["flask", "run", "--host=0.0.0.0"]