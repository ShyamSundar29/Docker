# Import the Flask class from the flask module
from flask import Flask

# Create an instance of the Flask class for your web application
# The argument __name__ helps Flask determine the root path for the application
app = Flask(__name__)

# Define a route for the root URL ('/')
# This decorator tells Flask which URL should trigger the associated function
@app.route('/', methods=['GET'])  # The route responds to HTTP GET requests
def home():
    # Define the function that will run when the root URL is accessed
    # This function returns the response "Hello World" to the client
    return "Hello World From Docker!"

# Check if this script is being run directly (not imported as a module)
if __name__ == "__main__":
    # Run the Flask development server
    # host="0.0.0.0" allows access from any IP address (useful for testing on a network)
    # port=5000 sets the port number for the server
    app.run(host="0.0.0.0", port=5000)
