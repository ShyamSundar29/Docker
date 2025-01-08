# This specifies the base image to be used for your Docker container. We use Python 3.9-slim for a lighter version of Python.
FROM python:3.9-slim

# These environment variables configure Flask:
# - FLASK_APP tells Flask which file to run as the application
# - FLASK_RUN_HOST=0.0.0.0 makes the app accessible on all IP addresses within the container (required for Docker)
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# This sets the current directory in the container where all commands will be executed. It's where your app files will reside.
WORKDIR /app

# This copies the 'requirements.txt' file from the local machine to the '/app' directory inside the container.
COPY requirements.txt .

# This installs the dependencies listed in the 'requirements.txt' file, without using the pip cache.
RUN pip install -r requirements.txt

# This copies all the files in your current directory (including the app code and configuration files) into the '/app' directory inside the container.
COPY . .

# Exposing this port allows the Docker container to listen for incoming connections on port 5000.
EXPOSE 5000

# This tells Docker to run the Flask development server with the specified command when the container starts.
# It will automatically start the Flask app from the 'app.py' file, using the environment variables defined earlier.
CMD ["flask", "run"]