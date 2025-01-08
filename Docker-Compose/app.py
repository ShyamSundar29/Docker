# Import the Flask class from the flask module
from flask import Flask
# Import the Redis module to interact with the Redis database
import redis

# Create an instance of the Flask class to initialize the web application
app = Flask(__name__)

# Create a connection to the Redis service running on the "redis" host at port 6379
# This assumes you have a Redis service running with the name "redis"
cache = redis.Redis(host='redis', port=6379)

# Define a route for the root URL ('/')
# The decorator tells Flask to associate the following function with the root URL
@app.route('/')
def home():
    # Use Redis to increment the "hits" counter and retrieve the new count
    # The "hits" key is used to track the number of visits to this page
    count = cache.incr('hits')
    
    # Return a message that displays the number of times the page has been viewed
    return f"Hello World! This page has been viewed {count} times."

# The entry point for the Flask application
# If this script is run directly (not imported), the Flask app will start
if __name__ == "__main__":
    # Run the Flask app on host '0.0.0.0' (accessible externally) and port 5000
    # This is useful for when running the app inside a Docker container
    app.run(host="0.0.0.0", port=5000)
