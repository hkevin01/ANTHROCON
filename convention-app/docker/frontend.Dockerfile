# Use a base image with Python
FROM python:3.11

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY frontend/requirements.txt ./requirements.txt

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire frontend folder into the container
COPY frontend/ ./frontend/

# Set the environment variable for display
ENV DISPLAY=:0

# Command to run the Kivy application
CMD ["python", "frontend/kivy_app/main.py"]