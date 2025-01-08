# Use an official Python runtime as the base image
# This image comes with Python 3.7 installed and provides a suitable environment to run Python apps
FROM python:3.7

# Copy the content of the current directory (.) on the host machine to the /app directory in the container
# This will copy all your application files, including app.py, requirements.txt, etc.
COPY . /app

# Set the working directory inside the container to /app
# This ensures that all subsequent commands will be executed from the /app directory
WORKDIR /app

# Install the required Python packages listed in requirements.txt
# This installs all dependencies that your application needs to run, such as Flask, numpy, etc.
RUN pip install -r requirements.txt

# Define the default command to run the application when the container starts
# This command runs the Python script 'app.py' to start your Flask application
CMD ["python", "app.py"]
