import os
from flask import Flask

# Initialize the Flask app
app = Flask(__name__)

# Define the home route
@app.route('/')
def hello_world():
    return "<h1>Hello, World!</h1><p>Welcome to my first web page!</p>"

# Run the app
if __name__ == '__main__':
    # Get the PORT environment variable (default to 5000 if not set)
    port = int(os.getenv("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
